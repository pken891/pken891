#!/usr/bin/env python3
"""Generate skills-banner.svg and github-stats-banner.svg."""

from pipboy_theme import (
    BG_BOX,
    GOLD,
    GREEN,
    GREEN_DIM,
    GREEN_SOFT,
    W,
    shared_defs,
    vault_boy_vector,
    write_svg,
)


def build_skills_banner() -> str:
    h = 166
    # Segmented Pip-Boy style bars (out of 10 blocks)
    stats = [("INFOSEC", 9), ("NET ENG", 8), ("SYSTEMS", 9), ("LOCAL AI", 8)]
    bars = []
    by = 52
    for label, level in stats:
        segs = []
        for i in range(10):
            sx = 710 + i * 12
            fill = GREEN if i < level else BG_BOX
            opacity = "1" if i < level else "0.5"
            segs.append(
                f'<rect x="{sx}" y="{by}" width="9" height="10" rx="1" '
                f'fill="{fill}" fill-opacity="{opacity}" stroke="{GREEN_DIM}" stroke-width="0.9"/>'
            )
        bars.append(
            f'<text x="646" y="{by + 9}" font-size="10.5" class="mono" fill="{GREEN}">{label}</text>'
            + "".join(segs)
        )
        by += 20

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">
{shared_defs("sk", h)}
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="12" fill="url(#sk-bg)" stroke="{GREEN_DIM}" stroke-width="2"/>
  <rect x="6" y="6" width="{W - 12}" height="{h - 12}" rx="9" fill="none" stroke="{GREEN}" stroke-opacity="0.25" stroke-width="1"/>
  <g clip-path="url(#sk-clip)">
    <rect x="0" y="0" width="{W}" height="18" fill="{GREEN}" class="sweep"/>
  </g>
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="12" fill="url(#sk-scan)" pointer-events="none"/>
  <!-- Corner ticks -->
  <path d="M 14 26 L 14 14 L 26 14" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} 14 L {W - 14} 14 L {W - 14} 26" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M 14 {h - 26} L 14 {h - 14} L 26 {h - 14}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} {h - 14} L {W - 14} {h - 14} L {W - 14} {h - 26}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <!-- Top Pip-Boy Tab Bar (SKILLS only) -->
  <rect x="28" y="12" width="82" height="24" rx="2" fill="{GREEN}" fill-opacity="0.14"/>
  <path d="M 28 36 L 28 12 L 110 12 L 110 36" fill="none" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="69" y="28" text-anchor="middle" font-size="11.5" font-weight="700" class="mono" fill="{GREEN}">SKILLS</text>
  <text x="{W - 28}" y="27" text-anchor="end" font-size="11" class="dim">PROFILE // TECH STACK</text>
  <line x1="22" y1="36" x2="28" y2="36" stroke="{GREEN}" stroke-opacity="0.7" stroke-width="1.5"/>
  <line x1="110" y1="36" x2="{W - 22}" y2="36" stroke="{GREEN}" stroke-opacity="0.7" stroke-width="1.5"/>
  <!-- Pip-Boy 2-segment HUD footer -->
  <rect x="26" y="{h - 34}" width="400" height="20" rx="2" fill="{GREEN_SOFT}" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="38" y="{h - 20}" font-size="10.5" font-weight="700" class="mono" fill="{GREEN}">COLORADO STATE UNIVERSITY</text>
  <rect x="434" y="{h - 34}" width="400" height="20" rx="2" fill="{GREEN_SOFT}" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="822" y="{h - 20}" text-anchor="end" font-size="10.5" font-weight="700" class="mono" fill="{GOLD}">SYSTEMS: ONLINE</text>
{vault_boy_vector(28, 43, 0.80, "sk")}
  <text x="134" y="75" font-size="23" class="title" filter="url(#sk-glow)">TECHNICAL SKILLS &amp; TOOLS<tspan class="blink">_</tspan></text>
  <text x="134" y="97" font-size="11.5" class="sub">IT SUPPORT | HARDWARE TROUBLESHOOTING | NETWORKING</text>
  <text x="134" y="117" font-size="10.5" class="dim">PETER KENOIAN // B.S. COMPUTER SCIENCE W/ FOCUS IN CYBERSECURITY</text>
  <line x1="632" y1="48" x2="632" y2="124" stroke="{GREEN_DIM}" stroke-width="1"/>
  {"".join(bars)}
</svg>"""


def build_stats_banner() -> str:
    h = 84
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">
{shared_defs("st", h)}
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="10" fill="url(#st-bg)" stroke="{GREEN_DIM}" stroke-width="2"/>
  <g clip-path="url(#st-clip)">
    <rect x="0" y="0" width="{W}" height="16" fill="{GREEN}" class="sweep"/>
  </g>
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="10" fill="url(#st-scan)"/>
  <path d="M 14 24 L 14 14 L 24 14" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 24} 14 L {W - 14} 14 L {W - 14} 24" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M 14 {h - 24} L 14 {h - 14} L 24 {h - 14}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 24} {h - 14} L {W - 14} {h - 14} L {W - 14} {h - 24}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <text x="430" y="39" text-anchor="middle" font-size="19" class="title" filter="url(#st-glow)">GITHUB ACTIVITY &amp; STATS<tspan class="blink">_</tspan></text>
  <text x="430" y="61" text-anchor="middle" font-size="11" class="dim">REPOSITORIES  //  COMMIT HISTORY  //  ACTIVE STREAK</text>
</svg>"""


def generate() -> None:
    write_svg("skills-banner.svg", build_skills_banner())
    write_svg("github-stats-banner.svg", build_stats_banner())


if __name__ == "__main__":
    generate()