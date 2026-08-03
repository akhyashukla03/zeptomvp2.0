import os
import sys
import resvg_py

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def render_crisp_svgs():
    os.makedirs("images/crisp_vector_renders", exist_ok=True)
    svg_dir = "figma_design_assets"
    
    files = [
        "01_b2b_free_sampler_cart.svg",
        "02_category_streak_quest_board.svg",
        "03_restock_cadence_interception.svg",
        "04_post_trial_outcome_loop.svg",
        "05_lifecycle_moment_interceptor.svg",
        "06_freshness_guaranteed_audit.svg",
        "07_neighbourhood_trend_feed.svg",
        "08_discovery100_voucher_conversion.svg"
    ]
    
    for fname in files:
        fpath = os.path.join(svg_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                svg_data = f.read()
            
            # Render SVG to PNG bytes with 4x crisp resolution scale
            png_bytes = resvg_py.svg_to_bytes(svg_data, zoom=4.0)
            
            out_png = os.path.join("images/crisp_vector_renders", fname.replace(".svg", ".png"))
            with open(out_png, "wb") as f:
                f.write(png_bytes)
            print(f"✅ Rendered ultra-crisp vector image: {out_png}")

if __name__ == "__main__":
    render_crisp_svgs()
