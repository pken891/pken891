#!/usr/bin/env python3
"""Generate career-card.svg (open to opportunities card)."""

from pipboy_theme import (
    BG_BOX,
    GOLD,
    GREEN,
    GREEN_DIM,
    W,
    pipboy_frame,
    shared_defs,
    write_svg,
)


def build_career_card() -> str:
    h = 282
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">
{shared_defs("cr", h)}
{pipboy_frame("cr", h, "CAREER", "AVAILABILITY // EARLY-CAREER", ("FORT COLLINS, CO", "CSU // CS &amp; INFO SYSTEMS", "OPEN TO ROLES"))}

  <!-- Card Header -->
  <circle cx="36" cy="61" r="4.5" fill="{GOLD}" class="pulse"/>
  <text x="50" y="66" font-size="15" font-weight="700" class="gold">OPEN TO OPPORTUNITIES // INTERNSHIPS &amp; ENTRY-LEVEL ROLES</text>

  <!-- Left Column: Education & Focus -->
  <rect x="26" y="80" width="394" height="156" rx="6" fill="{BG_BOX}" stroke="{GREEN_DIM}" stroke-width="1.3"/>
  <text x="42" y="103" font-size="12" font-weight="700" class="mono" fill="{GREEN}">[ EDUCATION &amp; FOCUS ]</text>
  <line x1="42" y1="111" x2="404" y2="111" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="42" y="133" font-size="11.5" class="sub">&gt; B.S. Computer Science &amp; Info Systems</text>
  <text x="56" y="149" font-size="10.8" class="dim">Colorado State University</text>
  <text x="42" y="172" font-size="11.5" class="sub">&gt; Target Roles:</text>
  <text x="56" y="188" font-size="11.2" class="sub">InfoSec, Cloud/SWE, IT Support</text>
  <text x="42" y="211" font-size="11.5" class="sub">&gt; Focus: Hardening systems &amp; protecting</text>
  <text x="56" y="226" font-size="11.2" class="sub">everyday users from cyber threats</text>

  <!-- Right Column: Hands-On Experience -->
  <rect x="440" y="80" width="394" height="156" rx="6" fill="{BG_BOX}" stroke="{GREEN_DIM}" stroke-width="1.3"/>
  <text x="456" y="103" font-size="12" font-weight="700" class="mono" fill="{GREEN}">[ HANDS-ON EXPERIENCE ]</text>
  <line x1="456" y1="111" x2="818" y2="111" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="456" y="133" font-size="11.5" class="sub">&gt; Tech office IT &amp; systems operations</text>
  <text x="456" y="156" font-size="11.5" class="sub">&gt; Fault-tolerant &amp; HMAC-verified systems</text>
  <text x="456" y="179" font-size="11.5" class="sub">&gt; Raw TCP protocols &amp; Cisco/DNS labs</text>
  <text x="456" y="202" font-size="11.5" class="sub">&gt; Portable USB local AI (llama.cpp)</text>
  <text x="456" y="225" font-size="11.5" class="sub">&gt; PKI, SBOM &amp; vulnerability auditing</text>
</svg>"""


def generate() -> None:
    write_svg("career-card.svg", build_career_card())


if __name__ == "__main__":
    generate()