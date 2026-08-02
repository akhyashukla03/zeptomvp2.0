import os
import json
import sys
import random

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def generate_10k_dataset():
    print("Generating 10,000 Multi-Platform Mixed Feedback Records...")
    
    sources = [
        "Play Store", "App Store", "Reddit (r/bangalore)", "Reddit (r/india)", 
        "Twitter", "Quora", "MouthShut", "LinkedIn", "ProductHunt", "Trustpilot"
    ]
    
    categories = [
        "Beauty & Grooming", "Pet Supplies", "Electronics", "Baby Care", 
        "Household Essentials", "Groceries", "Snacks"
    ]
    
    usernames = [
        "rahul_m", "sneha_k", "vikram_d", "meera_p", "ananya_dev", "rohan_pm", "pooja_tech",
        "divya_qa", "srinivas_k", "fit_fine", "coffee_lover", "frugal_shopper", "wfh_dev",
        "foodie_delhi", "mumbai_guy", "tech_dude", "mom_of_two", "sharma_ji", "kumar_p", "neha_b"
    ]

    # 40% Positive (Delights & Success Stories)
    positive_templates = [
        ("Got Cetaphil sunscreen delivered in 8 mins right before heading to the airport! Complete lifesaver!", "Beauty & Grooming", "Trial & Convenience Delight"),
        ("Loved finding the free 15ml cleanser sample inside my grocery bag. Tested it and bought full size product!", "Beauty & Grooming", "B2B Free Sample Delight"),
        ("Super fast delivery for phone charger cable when mine died during a remote work call. Super handy!", "Electronics", "Emergency Utility Delight"),
        ("Pedigree dog treats on Zepto are fresh and delivered instantly when we ran low on kibble.", "Pet Supplies", "Pet Care Fast Refill"),
        ("Great experience ordering MamyPoko diapers when we ran out at 11 PM. Extremely reliable night delivery.", "Baby Care", "Emergency Parent Convenience"),
        ("Ordered Surf Excel liquid and dishwashing scrubs along with daily milk. Saved me a supermarket trip!", "Household Essentials", "Grocery Basket Extension"),
        ("Zepto's sub-10 min delivery for party snacks and Coca-Cola saved our midnight get-together!", "Snacks", "Impulse & Snack Convenience"),
        ("Surprised to get authentic Lakme lipstick with fresh batch code. Packaging was crisp and clean.", "Beauty & Grooming", "Product Quality Praise"),
        ("The 2x points streak on daily milk when buying pet food is an awesome loyalty perk. Keep it up!", "Pet Supplies", "Loyalty Rewards Adoption"),
        ("Received a Portronics fast charging cable in 7 minutes. Packaging was neat and device worked perfectly.", "Electronics", "Quality & Speed Praise")
    ]

    # 30% Neutral (Feature Requests & Exploration Curiosity)
    neutral_templates = [
        ("Wish Zepto had an AI shade matcher camera tool for buying lipsticks and foundations without guessing.", "Beauty & Grooming", "Feature Request: AI Shade Matcher"),
        ("Would order high-value gadgets like wireless earphones if there was a 10-minute doorstep try-and-inspect option.", "Electronics", "Feature Request: Doorstep Try & Inspect"),
        ("Didn't realize cat food and pet toys were sold on Zepto until a coworker mentioned it. Banner discovery is low.", "Pet Supplies", "Unaware of Category"),
        ("Would love a category streak board on daily staples (Milk/Bread) that unlocks points when trying new sections.", "Groceries", "Feature Request: Category Streaks"),
        ("Need dark store storage temperature badges so customers know skincare active ingredients are kept cool.", "Beauty & Grooming", "Feature Request: Storage Audit Telemetry"),
        ("I only use search bar for grocery staples. App should suggest small ₹0 trial sample add-ons right inside cart.", "Groceries", "Feature Request: Cart Sampler Nudge"),
        ("Would buy baby wipes regularly if bundled into my weekly milk and egg subscription order.", "Baby Care", "Feature Request: Bundle Subscription"),
        ("I browse pet accessories occasionally, but I want to verify expiry dates before completing checkout.", "Pet Supplies", "Feature Request: Expiry Transparency"),
        ("Would buy travel-size grooming kits if Zepto offered a risk-free ₹100 discount voucher post-trial.", "Beauty & Grooming", "Feature Request: Trial Voucher"),
        ("Nice selection of household batteries and extensions, but needs clearer compatibility filters.", "Electronics", "Feature Request: Device Compatibility UI")
    ]

    # 30% Negative (Friction & Barriers)
    negative_templates = [
        ("Terrified of buying face serums on quick commerce. High heat in dark store warehouses degrades active ingredients.", "Beauty & Grooming", "Trust in Quality / Expiry Fear"),
        ("Laundry detergent and pet kibble are planned bulk buys. I buy 10kg packs on DMart / Amazon for bulk discount.", "Household Essentials", "Planned vs Emergency Mismatch"),
        ("Ordering a single lipstick or charger wrapped in plastic packaging gives me ecological guilt around rider trips.", "Electronics", "Ecological Guilt"),
        ("Checkout dark patterns, rain fees, and tip popups make me speed through checkout in <30s without looking at banners.", "Groceries", "Checkout Dark Pattern Fatigue"),
        ("Chatbot refund loops make me hesitant to buy non-grocery items. Returns are too stressful if item is dangled.", "Beauty & Grooming", "Return & Refund Anxiety"),
        ("Delivered near-expiry curd pack and getting replacement took 4 calls to customer support loops. Painful app bugs.", "Groceries", "Operational & Refund Bot Loop"),
        ("Order delayed by 45 minutes and dark store rider delivered wrong item. Customer support was unreachable.", "Groceries", "Operational & Delivery Delay"),
        ("Pet kibble bag looked dusty and crumpled, like it was stored in an unventilated dark store corner.", "Pet Supplies", "Dark Store Warehouse Skepticism"),
        ("Quick commerce stocks small emergency diaper packs at high prices. Not economically viable for monthly refill.", "Baby Care", "Bulk Pricing Mismatch"),
        ("App crashed during checkout and transaction failed twice, money deducted without order confirmation.", "Groceries", "App Bug / Payment Failure")
    ]

    all_reviews = []

    for i in range(1, 10001):
        source = sources[(i - 1) % len(sources)]
        username = f"{usernames[(i - 1) % len(usernames)]}_{random.randint(100, 999)}"
        
        # Split: 40% Positive (1..4000), 30% Neutral (4001..7000), 30% Negative (7001..10000)
        rand_val = i % 100
        if rand_val < 40:
            sentiment = "Positive"
            rating = random.choice([4, 5])
            content, cat, barrier = positive_templates[i % len(positive_templates)]
        elif rand_val < 70:
            sentiment = "Neutral"
            rating = 3
            content, cat, barrier = neutral_templates[i % len(neutral_templates)]
        else:
            sentiment = "Negative"
            rating = random.choice([1, 2])
            content, cat, barrier = negative_templates[i % len(negative_templates)]
            
        all_reviews.append({
            "id": i,
            "source": source,
            "username": username,
            "rating": rating,
            "sentiment": sentiment,
            "category_mentioned": cat,
            "barrier_identified": barrier,
            "content": content
        })

    os.makedirs("data", exist_ok=True)
    out_file = "data/reviews_dataset.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_reviews, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully generated {len(all_reviews)} reviews in {out_file}")

if __name__ == "__main__":
    generate_10k_dataset()
