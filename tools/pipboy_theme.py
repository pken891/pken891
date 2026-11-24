"""Shared Fallout Pip-Boy CRT theme primitives for GitHub profile SVGs."""

from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
W = 860

# Pip-Boy Phosphor & Vault-Tec Accent Palette
BG_DARK = "#060B07"
BG_PANEL = "#0A140D"
BG_BOX = "#0D1C11"
GREEN = "#18FF62"
GREEN_MID = "#12B849"
GREEN_DIM = "#1E4D2B"
GREEN_SOFT = "#0F2917"
GREEN_TEXT = "#B8E6C1"
TEXT_DIM = "#6FA67D"
GOLD = "#F6D04D"
RED = "#FF4D4D"
FONT = "'Courier New', Consolas, 'Liberation Mono', monospace"


def shared_defs(prefix: str, height: int) -> str:
    return f"""  <defs>
    <linearGradient id="{prefix}-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0B160E"/>
      <stop offset="100%" stop-color="{BG_DARK}"/>
    </linearGradient>
    <pattern id="{prefix}-scan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="2" fill="#000000" fill-opacity="0.24"/>
    </pattern>
    <filter id="{prefix}-glow" x="-15%" y="-15%" width="130%" height="130%">
      <feGaussianBlur stdDeviation="2.0" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="{prefix}-clip">
      <rect x="2" y="2" width="{W - 4}" height="{height - 4}" rx="12"/>
    </clipPath>
  </defs>
  <style>
    .mono {{ font-family: {FONT}; }}
    .title {{ font-family: {FONT}; font-weight: 700; fill: {GREEN}; letter-spacing: 1.2px; }}
    .sub {{ font-family: {FONT}; fill: {GREEN_TEXT}; }}
    .dim {{ font-family: {FONT}; fill: {TEXT_DIM}; }}
    .gold {{ font-family: {FONT}; font-weight: 700; fill: {GOLD}; }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.32; }} }}
    @keyframes sweep {{
      0% {{ transform: translateY(-20px); opacity: 0; }}
      15% {{ opacity: 0.12; }}
      85% {{ opacity: 0.12; }}
      100% {{ transform: translateY({height}px); opacity: 0; }}
    }}
    .blink {{ animation: blink 1.1s steps(1) infinite; }}
    .pulse {{ animation: pulse 2.2s ease-in-out infinite; }}
    .sweep {{ animation: sweep 5.8s linear infinite; }}
  </style>"""


def pipboy_frame(
    prefix: str,
    height: int,
    active_tab: str,
    right_tag: str,
    footer_blocks: tuple[str, str, str] | None = None,
) -> str:
    """Render the Pip-Boy CRT bezel, notched tab header, and optional 3-segment footer."""
    tabs = ["SKILLS", "PROJECTS", "ARCH", "AI", "CAREER"]
    tab_svg = []
    tx = 28
    tw = 82
    gap = 10
    active_x = None

    for tab in tabs:
        if tab == active_tab:
            active_x = tx
            tab_svg.append(
                f'<rect x="{tx}" y="12" width="{tw}" height="24" rx="2" fill="{GREEN}" fill-opacity="0.14"/>'
                f'<path d="M {tx} 36 L {tx} 12 L {tx + tw} 12 L {tx + tw} 36" fill="none" stroke="{GREEN}" stroke-width="1.5"/>'
                f'<text x="{tx + tw / 2}" y="28" text-anchor="middle" font-size="11.5" font-weight="700" class="mono" fill="{GREEN}">{tab}</text>'
            )
        else:
            tab_svg.append(
                f'<text x="{tx + tw / 2}" y="28" text-anchor="middle" font-size="11.5" class="mono" fill="#4E8A5E">{tab}</text>'
            )
        tx += tw + gap

    # Classic Pip-Boy header line broken cleanly around the active tab
    if active_x is not None:
        header_line = (
            f'<line x1="22" y1="36" x2="{active_x}" y2="36" stroke="{GREEN}" stroke-opacity="0.7" stroke-width="1.5"/>'
            f'<line x1="{active_x + tw}" y1="36" x2="{W - 22}" y2="36" stroke="{GREEN}" stroke-opacity="0.7" stroke-width="1.5"/>'
        )
    else:
        header_line = f'<line x1="22" y1="36" x2="{W - 22}" y2="36" stroke="{GREEN}" stroke-opacity="0.7" stroke-width="1.5"/>'

    # Optional 3-segment Pip-Boy HUD footer bar
    footer_svg = ""
    if footer_blocks:
        fy = height - 34
        left_txt, mid_txt, right_txt = footer_blocks
        footer_svg = f"""  <!-- Pip-Boy 3-segment HUD footer -->
  <rect x="26" y="{fy}" width="236" height="20" rx="2" fill="{GREEN_SOFT}" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="36" y="{fy + 14}" font-size="10.5" font-weight="700" class="mono" fill="{GREEN}">{left_txt}</text>
  <rect x="270" y="{fy}" width="320" height="20" rx="2" fill="{GREEN_SOFT}" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="430" y="{fy + 14}" text-anchor="middle" font-size="10.5" class="sub">{mid_txt}</text>
  <rect x="598" y="{fy}" width="236" height="20" rx="2" fill="{GREEN_SOFT}" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="824" y="{fy + 14}" text-anchor="end" font-size="10.5" font-weight="700" class="mono" fill="{GOLD}">{right_txt}</text>"""

    return f"""  <rect x="2" y="2" width="{W - 4}" height="{height - 4}" rx="12" fill="url(#{prefix}-bg)" stroke="{GREEN_DIM}" stroke-width="2"/>
  <rect x="6" y="6" width="{W - 12}" height="{height - 12}" rx="9" fill="none" stroke="{GREEN}" stroke-opacity="0.25" stroke-width="1"/>
  <g clip-path="url(#{prefix}-clip)">
    <rect x="0" y="0" width="{W}" height="18" fill="{GREEN}" class="sweep"/>
  </g>
  <rect x="2" y="2" width="{W - 4}" height="{height - 4}" rx="12" fill="url(#{prefix}-scan)" pointer-events="none"/>
  <!-- Corner ticks -->
  <path d="M 14 26 L 14 14 L 26 14" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} 14 L {W - 14} 14 L {W - 14} 26" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M 14 {height - 26} L 14 {height - 14} L 26 {height - 14}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} {height - 14} L {W - 14} {height - 14} L {W - 14} {height - 26}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <!-- Top Pip-Boy Tab Bar -->
  {"".join(tab_svg)}
  <text x="{W - 28}" y="27" text-anchor="end" font-size="11" class="dim">{right_tag}</text>
  {header_line}
{footer_svg}"""


def vault_boy_vector(x: float, y: float, scale: float = 0.85, prefix: str = "vb") -> str:
    """Monochrome phosphor-green Pip-Boy style Vault Boy giving a thumbs-up."""
    return f"""  <g transform="translate({x}, {y}) scale({scale})" filter="url(#{prefix}-glow)">
    <circle cx="52" cy="54" r="46" fill="{BG_BOX}" stroke="{GREEN}" stroke-opacity="0.45" stroke-width="1.5" stroke-dasharray="4 3"/>
    <path d="M 26 94 L 30 62 Q 46 56 62 62 L 66 94 Z" fill="{BG_DARK}" stroke="{GREEN}" stroke-width="2.4" stroke-linejoin="round"/>
    <path d="M 38 60 L 46 72 L 54 60" fill="none" stroke="{GOLD}" stroke-width="2.2" stroke-linejoin="round"/>
    <line x1="46" y1="72" x2="46" y2="93" stroke="{GOLD}" stroke-width="2"/>
    <path d="M 60 68 L 76 62 L 78 52" fill="none" stroke="{GREEN}" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M 60 68 L 76 62 L 78 52" fill="none" stroke="{BG_DARK}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    <rect x="74" y="47" width="13" height="14" rx="3" fill="{BG_DARK}" stroke="{GREEN}" stroke-width="2.2"/>
    <path d="M 78 47 L 78 36 Q 78 32 82 32 Q 85 32 85 36 L 85 47" fill="{BG_DARK}" stroke="{GREEN}" stroke-width="2.2"/>
    <line x1="82" y1="51" x2="87" y2="51" stroke="{GREEN}" stroke-width="1.5"/>
    <line x1="82" y1="55" x2="87" y2="55" stroke="{GREEN}" stroke-width="1.5"/>
    <ellipse cx="46" cy="36" rx="17" ry="19" fill="{BG_DARK}" stroke="{GREEN}" stroke-width="2.4"/>
    <path d="M 29 34 Q 24 36 29 41" fill="{BG_DARK}" stroke="{GREEN}" stroke-width="2"/>
    <path d="M 29 30 C 27 12, 50 7, 63 16 C 69 20, 68 27, 61 27 C 53 21, 38 22, 31 32 Z" fill="{GREEN}"/>
    <path d="M 37 30 Q 41 28 44 30" fill="none" stroke="{GREEN}" stroke-width="1.6" stroke-linecap="round"/>
    <path d="M 49 30 Q 53 28 56 30" fill="none" stroke="{GREEN}" stroke-width="1.6" stroke-linecap="round"/>
    <circle cx="41" cy="35" r="2.2" fill="{GREEN}"/>
    <circle cx="53" cy="35" r="2.2" fill="{GREEN}"/>
    <path d="M 36 42 Q 47 52 57 41 Q 47 46 36 42 Z" fill="{GREEN}"/>
  </g>"""


def write_svg(filename: str, content: str) -> Path:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    path = ASSETS_DIR / filename
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Generated {path}")
    return path