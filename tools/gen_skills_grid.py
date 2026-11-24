#!/usr/bin/env python3
"""Generate skills-grid.svg (companion CRT panel below skills-banner.svg)."""

from html import escape

from pipboy_theme import (
    BG_BOX,
    GOLD,
    GREEN,
    GREEN_DIM,
    GREEN_TEXT,
    RED,
    W,
    shared_defs,
    write_svg,
)


def render_pills(
    items: list[str],
    start_x: float,
    start_y: float,
    max_width: float,
    accent: str,
    fill_bg: str,
) -> str:
    """Wrap monospace skill tags cleanly inside a card without overflow."""
    cx = start_x
    cy = start_y
    out = []
    for label in items:
        pw = len(label) * 6.8 + 18
        if cx > start_x and (cx - start_x) + pw > max_width:
            cx = start_x
            cy += 27
        out.append(
            f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{pw:.1f}" height="21" rx="3" '
            f'fill="{fill_bg}" stroke="{accent}" stroke-opacity="0.75" stroke-width="1"/>'
            f'<text x="{cx + pw / 2:.1f}" y="{cy + 14.5:.1f}" text-anchor="middle" '
            f'font-size="10.8" class="mono" fill="{GREEN_TEXT}">{escape(label)}</text>'
        )
        cx += pw + 8
    return "\n  ".join(out)


def build_skills_grid() -> str:
    h = 342
    # (x, y, card_height, title, subtitle, accent, pill_bg, items)
    categories = [
        (
            26,
            50,
            116,
            "IT SUPPORT & OPERATIONS",
            "Campus tech support, access control & hardware ops",
            GREEN,
            "#0D2214",
            [
                "Active Directory",
                "Freshservice",
                "Windows 11",
                "Hardware Setup",
                "Troubleshooting",
                "Documentation",
            ],
        ),
        (
            438,
            50,
            116,
            "SECURITY & RESILIENCE",
            "Fault-tolerant architecture, integrity & key hygiene",
            RED,
            "#1F0D0D",
            [
                "HMAC-SHA256",
                "PID Fencing",
                "Crash Recovery",
                "Fault & Tamper Testing",
                "Key Scrubbing",
            ],
        ),
        (
            26,
            180,
            144,
            "NETWORKING & SOFTWARE",
            "Custom TCP protocols, packet analysis & system tooling",
            GOLD,
            "#1B190B",
            [
                "Python",
                "TCP Sockets",
                "Multi-Threading",
                "Git",
                "Wireshark",
                "PCAP Analysis",
                "DNS Resolution",
                "JSON / FSM Logic",
                "Linux",
            ],
        ),
        (
            438,
            180,
            144,
            "LOCAL & CLOUD AI",
            "Portable USB inference & hybrid LLM gateway",
            GREEN,
            "#0D2214",
            [
                "llama.cpp (GGUF)",
                "LiteLLM",
                "Streamlit",
                "Windows Batch",
                "RAM-Tier Routing",
                "Portable USB",
            ],
        ),
    ]

    cards = []
    for x, y, ch, title, subtitle, accent, pill_bg, items in categories:
        pills_svg = render_pills(items, x + 14, y + 58, 368, accent, pill_bg)
        cards.append(
            f"""  <rect x="{x}" y="{y}" width="396" height="{ch}" rx="6" fill="{BG_BOX}" stroke="{GREEN_DIM}" stroke-width="1.3"/>
  <rect x="{x + 14}" y="{y + 13}" width="6" height="13" rx="1" fill="{accent}"/>
  <text x="{x + 28}" y="{y + 24}" font-size="12" font-weight="700" class="mono" fill="{accent}">{escape(title)}</text>
  <text x="{x + 14}" y="{y + 41}" font-size="10.2" class="dim">{escape(subtitle)}</text>
  <line x1="{x + 14}" y1="{y + 48}" x2="{x + 382}" y2="{y + 48}" stroke="{GREEN_DIM}" stroke-width="1"/>
  {pills_svg}"""
        )

    total_tools = sum(len(c[7]) for c in categories)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">
{shared_defs("sg", h)}
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="12" fill="url(#sg-bg)" stroke="{GREEN_DIM}" stroke-width="2"/>
  <rect x="6" y="6" width="{W - 12}" height="{h - 12}" rx="9" fill="none" stroke="{GREEN}" stroke-opacity="0.22" stroke-width="1"/>
  <g clip-path="url(#sg-clip)">
    <rect x="0" y="0" width="{W}" height="18" fill="{GREEN}" class="sweep"/>
  </g>
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="12" fill="url(#sg-scan)" pointer-events="none"/>
  <!-- Corner ticks -->
  <path d="M 14 26 L 14 14 L 26 14" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} 14 L {W - 14} 14 L {W - 14} 26" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M 14 {h - 26} L 14 {h - 14} L 26 {h - 14}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} {h - 14} L {W - 14} {h - 14} L {W - 14} {h - 26}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <!-- Minimal companion header -->
  <circle cx="32" cy="24" r="3.5" fill="{GREEN}" class="pulse"/>
  <text x="44" y="28" font-size="11.5" font-weight="700" class="mono" fill="{GREEN}">TOOLING MATRIX // ACTIVE STACK</text>
  <text x="{W - 28}" y="28" text-anchor="end" font-size="10.8" class="dim">4 DOMAINS // {total_tools} TOOLS</text>
  <line x1="22" y1="38" x2="{W - 22}" y2="38" stroke="{GREEN}" stroke-opacity="0.45" stroke-width="1"/>
{"".join(cards)}
</svg>"""


def generate() -> None:
    write_svg("skills-grid.svg", build_skills_grid())


if __name__ == "__main__":
    generate()