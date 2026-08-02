import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def generate_all_screens():
    os.makedirs("figma_design_assets", exist_ok=True)

    # 1. Use Case 1: B2B ₹0 Trial Sampler Carousel
    svg_1 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="45" width="360" height="55" rx="12" fill="#1E1430" stroke="#7C3AED"/>
  <text x="35" y="70" fill="#F59E0B" font-family="Arial" font-size="14" font-weight="bold">⚡ Delivery in 10 Mins</text>
  <text x="35" y="88" fill="#E2E8F0" font-family="Arial" font-size="11">Home - Sector 56, Gurgaon 📍</text>
  
  <rect x="20" y="110" width="360" height="35" rx="8" fill="#7C3AED"/>
  <text x="35" y="133" fill="#FFFFFF" font-family="Arial" font-size="12" font-weight="bold">💎 Zepto Discovery Pass Active (✓ ₹0 Sample Unlocked)</text>
  
  <rect x="20" y="155" width="360" height="130" rx="12" fill="#1E293B"/>
  <text x="35" y="180" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">Routine Grocery Staples 🥛</text>
  <rect x="35" y="195" width="330" height="35" rx="6" fill="#0F172A"/>
  <text x="45" y="217" fill="#FFFFFF" font-family="Arial" font-size="12">Amul Taaza Toned Milk (1L)</text><text x="300" y="217" fill="#F59E0B" font-family="Arial" font-size="12" font-weight="bold">Rs. 54</text>
  <rect x="35" y="238" width="330" height="35" rx="6" fill="#0F172A"/>
  <text x="45" y="260" fill="#FFFFFF" font-family="Arial" font-size="12">Brown Bread (400g)</text><text x="300" y="260" fill="#F59E0B" font-family="Arial" font-size="12" font-weight="bold">Rs. 45</text>
  
  <rect x="20" y="295" width="360" height="195" rx="12" fill="#281545" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="35" y="320" fill="#F59E0B" font-family="Arial" font-size="13" font-weight="bold">🎁 Claim ₹0 In-Bag Trial Sample (Brand Sponsored)</text>
  <text x="35" y="338" fill="#94A3B8" font-family="Arial" font-size="10">Rides inside your regular grocery bag at zero extra delivery CAC.</text>
  
  <rect x="35" y="350" width="155" height="125" rx="8" fill="#1E293B" stroke="#7C3AED"/>
  <text x="45" y="372" fill="#FFFFFF" font-family="Arial" font-size="11" font-weight="bold">Cetaphil Gentle Cleanser</text>
  <text x="45" y="388" fill="#10B981" font-family="Arial" font-size="10" font-weight="bold">15ml Trial Pack · ₹0</text>
  <rect x="45" y="435" width="135" height="28" rx="6" fill="#7C3AED"/>
  <text x="75" y="453" fill="#FFFFFF" font-family="Arial" font-size="11" font-weight="bold">+ Add Sample</text>
  
  <rect x="200" y="350" width="155" height="125" rx="8" fill="#1E293B"/>
  <text x="210" y="372" fill="#FFFFFF" font-family="Arial" font-size="11" font-weight="bold">Pedigree Dentastix</text>
  <text x="210" y="388" fill="#10B981" font-family="Arial" font-size="10" font-weight="bold">Single Stick · ₹0</text>
  <rect x="210" y="435" width="135" height="28" rx="6" fill="#334155"/>
  <text x="240" y="453" fill="#FFFFFF" font-family="Arial" font-size="11" font-weight="bold">+ Add Sample</text>
  
  <rect x="20" y="700" width="360" height="50" rx="12" fill="#10B981"/>
  <text x="120" y="730" fill="#FFFFFF" font-family="Arial" font-size="15" font-weight="bold">Proceed to Checkout · Rs. 108</text>
</svg>'''

    # 2. Use Case 2: Category Streak Quest Board
    svg_2 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="50" width="360" height="40" rx="8" fill="#1E293B"/>
  <text x="35" y="75" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">🏆 Zepto Routine Quests · Category Streaks</text>
  
  <rect x="20" y="105" width="360" height="210" rx="14" fill="#1E293B" stroke="#7C3AED" stroke-width="2"/>
  <text x="35" y="135" fill="#F59E0B" font-family="Arial" font-size="13" font-weight="bold">5-Sticker Monthly Exploration Quest</text>
  <text x="35" y="153" fill="#E2E8F0" font-family="Arial" font-size="11">Unlock 2x Grocery Points on Daily Milk/Bread when trying new sections!</text>
  
  <circle cx="55" cy="205" r="22" fill="#10B981"/><text x="45" y="211" fill="#FFFFFF" font-family="Arial" font-size="16">🥛</text>
  <circle cx="125" cy="205" r="22" fill="#10B981"/><text x="115" y="211" fill="#FFFFFF" font-family="Arial" font-size="16">🍿</text>
  <circle cx="195" cy="205" r="22" fill="#7C3AED" stroke="#F59E0B" stroke-width="2"/><text x="185" y="211" fill="#FFFFFF" font-family="Arial" font-size="16">💄</text>
  <circle cx="265" cy="205" r="22" fill="#334155"/><text x="255" y="211" fill="#FFFFFF" font-family="Arial" font-size="16">🐾</text>
  <circle cx="335" cy="205" r="22" fill="#334155"/><text x="325" y="211" fill="#FFFFFF" font-family="Arial" font-size="16">🔌</text>
  
  <rect x="35" y="245" width="330" height="50" rx="8" fill="#0F172A" stroke="#10B981"/>
  <text x="45" y="267" fill="#10B981" font-family="Arial" font-size="12" font-weight="bold">✓ 3/5 Category Stickers Unlocked!</text>
  <text x="45" y="284" fill="#E2E8F0" font-family="Arial" font-size="10">Active Reward: 2x Points on Milk &amp; Bread (+120 points/mo)</text>
</svg>'''

    # 3. Use Case 3: SkinMatch AI Camera Scanner
    svg_3 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="50" width="360" height="40" rx="8" fill="#1E293B"/>
  <text x="35" y="75" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">💄 SkinMatch AI · Camera Undertone Scanner</text>
  
  <rect x="20" y="105" width="360" height="390" rx="16" fill="#1E293B" stroke="#7C3AED" stroke-width="2"/>
  <rect x="40" y="125" width="320" height="240" rx="12" fill="#281545"/>
  <ellipse cx="200" cy="225" rx="65" ry="85" stroke="#F59E0B" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="135" y="230" fill="#E2E8F0" font-family="Arial" font-size="12">Position Face in Oval</text>
  <text x="120" y="348" fill="#F59E0B" font-family="Arial" font-size="11" font-weight="bold">Analyzing Undertones...</text>
  
  <rect x="40" y="380" width="320" height="95" rx="10" fill="#0F172A" stroke="#10B981"/>
  <text x="55" y="405" fill="#10B981" font-family="Arial" font-size="12" font-weight="bold">✓ 98.4% Shade Match Detected</text>
  <text x="55" y="425" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">Maybelline Fit Me #128 Warm Nude</text>
  <text x="55" y="445" fill="#94A3B8" font-family="Arial" font-size="10">Includes 15-Min Rider Doorstep Shade Refund Guarantee!</text>
  
  <rect x="20" y="515" width="360" height="50" rx="12" fill="#7C3AED"/>
  <text x="105" y="545" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">Add Shade #128 to Cart (₹549)</text>
</svg>'''

    # 4. Use Case 4: DeviceLink Auto-Detect Compatibility
    svg_4 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="50" width="360" height="40" rx="8" fill="#1E293B"/>
  <text x="35" y="75" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">🔌 DeviceLink · Phone Model Auto-Detect</text>
  
  <rect x="20" y="105" width="360" height="200" rx="14" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
  <rect x="35" y="125" width="330" height="45" rx="8" fill="#0F172A" stroke="#38BDF8"/>
  <text x="50" y="152" fill="#38BDF8" font-family="Arial" font-size="13" font-weight="bold">📱 iPhone 15 Pro Detected (USB-C 20W)</text>
  
  <text x="35" y="195" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">Portronics Braided USB-C Cable (1m)</text>
  <text x="35" y="215" fill="#10B981" font-family="Arial" font-size="11" font-weight="bold">✓ 100% Verified Compatible · 10-Min Speed</text>
  <rect x="35" y="235" width="330" height="45" rx="8" fill="#7C3AED"/>
  <text x="120" y="262" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">Add Cable to Cart (₹299)</text>
</svg>'''

    # 5. Use Case 5: PetCare Profile & Nutrition Matcher
    svg_5 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="50" width="360" height="40" rx="8" fill="#1E293B"/>
  <text x="35" y="75" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">🐾 PetCare Profile · Age &amp; Breed Matcher</text>
  
  <rect x="20" y="105" width="360" height="220" rx="14" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
  <rect x="35" y="125" width="330" height="45" rx="8" fill="#0F172A" stroke="#F59E0B"/>
  <text x="50" y="152" fill="#F59E0B" font-family="Arial" font-size="13" font-weight="bold">🐕 Bruno · Golden Retriever (2 Yrs)</text>
  
  <text x="35" y="195" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">Pedigree Adult Chicken &amp; Rice (3kg)</text>
  <text x="35" y="215" fill="#10B981" font-family="Arial" font-size="11" font-weight="bold">✓ High Protein Match + ₹0 Free Dentastix Sample</text>
  <rect x="35" y="235" width="330" height="45" rx="8" fill="#10B981"/>
  <text x="110" y="262" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">Add Food + ₹0 Treat Sample</text>
</svg>'''

    # 6. Use Case 6: Model B Dark Store Quality Vault Audit
    svg_6 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="50" width="360" height="40" rx="8" fill="#1E293B"/>
  <text x="35" y="75" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">📦 Model B Dark Store Quality Audit</text>
  
  <rect x="20" y="105" width="360" height="340" rx="16" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="35" y="135" fill="#F59E0B" font-family="Arial" font-size="13" font-weight="bold">🌡️ IoT Storage Telemetry &amp; CCTV Snapshot</text>
  <rect x="35" y="150" width="330" height="40" rx="8" fill="#10B981"/>
  <text x="50" y="175" fill="#FFFFFF" font-family="Arial" font-size="12" font-weight="bold">✓ Storage Temp: 18.2°C (Optimal Cool Climate)</text>
  
  <rect x="35" y="200" width="330" height="180" rx="8" fill="#000000" stroke="#334155"/>
  <text x="45" y="220" fill="#00FF00" font-family="Courier" font-size="10">LIVE CCTV STREAM · DARK STORE #104 (GURGAON SECTOR 56)</text>
  <text x="45" y="235" fill="#00FF00" font-family="Courier" font-size="10">RACK B4: BEAUTY &amp; SKINCARE VAULT · 2026-08-01 14:30:00</text>
  <rect x="120" y="260" width="160" height="90" rx="4" fill="#0F172A" stroke="#F59E0B"/>
  <text x="135" y="310" fill="#E2E8F0" font-family="Arial" font-size="11">[ Overhead CCTV Rack Snapshot ]</text>
  
  <text x="35" y="410" fill="#94A3B8" font-family="Arial" font-size="10">AWS S3 Lifecycle Storage Cost: ~$15/month total (7-day TTL auto-expire).</text>
</svg>'''

    # 7. Use Case 7: QC-Native Doorstep Try & Swap
    svg_7 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="50" width="360" height="40" rx="8" fill="#1E293B"/>
  <text x="35" y="75" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">⚡ QC Doorstep Try &amp; Inspection Window</text>
  
  <rect x="20" y="105" width="360" height="220" rx="14" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
  <text x="35" y="135" fill="#10B981" font-family="Arial" font-size="13" font-weight="bold">⏱️ Rider Doorstep Inspection Active (60s Window)</text>
  <text x="35" y="158" fill="#FFFFFF" font-family="Arial" font-size="12">Inspect box seal &amp; shade with delivery rider present.</text>
  
  <rect x="35" y="180" width="330" height="45" rx="8" fill="#10B981"/>
  <text x="100" y="207" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">✓ Item Perfect · Keep Order</text>
  
  <rect x="35" y="235" width="330" height="45" rx="8" fill="#EF4444"/>
  <text x="90" y="262" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">🔁 Wrong Shade · 1-Click Instant Swap</text>
</svg>'''

    # 8. Use Case 8: Post-Trial DISCOVERY100 Conversion Voucher
    svg_8 = '''<svg width="400" height="850" viewBox="0 0 400 850" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="850" rx="40" fill="#130D1E"/>
  <rect x="140" y="10" width="120" height="25" rx="12" fill="#000000"/>
  <rect x="20" y="50" width="360" height="40" rx="8" fill="#1E293B"/>
  <text x="35" y="75" fill="#FFFFFF" font-family="Arial" font-size="14" font-weight="bold">🏷️ Post-Trial Conversion Voucher</text>
  
  <rect x="20" y="105" width="360" height="200" rx="14" fill="#1E293B" stroke="#F59E0B" stroke-width="2"/>
  <text x="35" y="135" fill="#F59E0B" font-family="Arial" font-size="14" font-weight="bold">🎉 Enjoyed Your Cetaphil Cleanser Sample?</text>
  <text x="35" y="155" fill="#E2E8F0" font-family="Arial" font-size="11">Unlock ₹100 Off Full-Sized Cetaphil Cleanser (250ml)!</text>
  
  <rect x="35" y="175" width="330" height="45" rx="8" fill="#0F172A" stroke="#F59E0B" stroke-dasharray="6 4"/>
  <text x="85" y="202" fill="#F59E0B" font-family="Arial" font-size="14" font-weight="bold">VOUCHER: DISCOVERY100</text>
  
  <rect x="35" y="235" width="330" height="45" rx="8" fill="#7C3AED"/>
  <text x="80" y="262" fill="#FFFFFF" font-family="Arial" font-size="13" font-weight="bold">Order Full Size for ₹449 (Save ₹100)</text>
</svg>'''

    screens = [
        ("01_b2b_free_sampler_cart.svg", svg_1),
        ("02_category_streak_quest_board.svg", svg_2),
        ("03_skinmatch_ai_camera_scanner.svg", svg_3),
        ("04_devicelink_accessory_compatibility.svg", svg_4),
        ("05_petcare_profile_nutrition_matcher.svg", svg_5),
        ("06_darkstore_quality_cctv_audit.svg", svg_6),
        ("07_doorstep_instant_try_and_swap.svg", svg_7),
        ("08_discovery100_voucher_conversion.svg", svg_8)
    ]

    for fname, content in screens:
        fpath = os.path.join("figma_design_assets", fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Generated Figma Vector Screen: {fname}")

    print("\n🎉 Successfully generated ALL 8 use-case Figma vector SVG screens in figma_design_assets/")

if __name__ == "__main__":
    generate_all_screens()
