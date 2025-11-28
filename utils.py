def generate_logo_prompt(brand, desc):
    return f"""
You are an SVG logo generator AI.
Generate a minimal, clean SVG logo (SVG code only, no explanation).
Brand: {brand}
Description: {desc}
Rules:
- SVG only
- No HTML or CSS
- Professional and unique
Return ONLY the SVG code.
"""
