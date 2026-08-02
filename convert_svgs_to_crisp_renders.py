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
        "03_skinmatch_ai_camera_scanner.svg",
        "04_devicelink_accessory_compatibility.svg",
        "05_petcare_profile_nutrition_matcher.svg",
        "06_darkstore_quality_cctv_audit.svg",
        "07_doorstep_instant_try_and_swap.svg",
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
