#!/usr/bin/env python3
"""Generate architecture-map.svg (system architecture diagram card)."""

from pipboy_theme import (
    BG_BOX,
    GOLD,
    GREEN,
    GREEN_DIM,
    GREEN_SOFT,
    W,
    shared_defs,
    write_svg,
)


def build_architecture_map() -> str:
    h = 372
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">
{shared_defs("ar", h)}
  <style>
    @keyframes flow {{ to {{ stroke-dashoffset: -28; }} }}
    .flow {{ stroke-dasharray: 6 8; animation: flow 1.6s linear infinite; }}
  </style>
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="12" fill="url(#ar-bg)" stroke="{GREEN_DIM}" stroke-width="2"/>
  <rect x="6" y="6" width="{W - 12}" height="{h - 12}" rx="9" fill="none" stroke="{GREEN}" stroke-opacity="0.25" stroke-width="1"/>
  <g clip-path="url(#ar-clip)">
    <rect x="0" y="0" width="{W}" height="18" fill="{GREEN}" class="sweep"/>
  </g>
  <rect x="2" y="2" width="{W - 4}" height="{h - 4}" rx="12" fill="url(#ar-scan)" pointer-events="none"/>
  <!-- Corner ticks -->
  <path d="M 14 26 L 14 14 L 26 14" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} 14 L {W - 14} 14 L {W - 14} 26" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M 14 {h - 26} L 14 {h - 14} L 26 {h - 14}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <path d="M {W - 26} {h - 14} L {W - 14} {h - 14} L {W - 14} {h - 26}" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <!-- Top Tab Bar (single active tab) -->
  <rect x="28" y="12" width="118" height="24" rx="2" fill="{GREEN}" fill-opacity="0.14"/>
  <path d="M 28 36 L 28 12 L 146 12 L 146 36" fill="none" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="87" y="28" text-anchor="middle" font-size="11.5" font-weight="700" class="mono" fill="{GREEN}">ARCHITECTURE</text>
  <text x="{W - 28}" y="27" text-anchor="end" font-size="11" class="dim">SYSTEMS // TOPOLOGY</text>
  <line x1="22" y1="36" x2="28" y2="36" stroke="{GREEN}" stroke-opacity="0.7" stroke-width="1.5"/>
  <line x1="146" y1="36" x2="{W - 22}" y2="36" stroke="{GREEN}" stroke-opacity="0.7" stroke-width="1.5"/>

  <!-- Section Column Labels -->
  <text x="128" y="60" text-anchor="middle" font-size="10.8" font-weight="700" class="gold">[ PORTABLE USB NODE ]</text>
  <text x="421" y="60" text-anchor="middle" font-size="10.8" font-weight="700" class="gold">[ HARDWARE-AWARE AI ROUTING ]</text>
  <text x="715" y="60" text-anchor="middle" font-size="10.8" font-weight="700" class="gold">[ NETWORK &amp; SECURITY LAB ]</text>

  <!-- Animated flow connectors (USB -> Model Tiers / LiteLLM) -->
  <path d="M 230 154 L 286 106" fill="none" stroke="{GREEN}" stroke-width="2" class="flow"/>
  <path d="M 230 185 L 286 185" fill="none" stroke="{GREEN}" stroke-width="2" class="flow"/>
  <path d="M 230 216 L 286 264" fill="none" stroke="{GOLD}" stroke-width="2" class="flow"/>

  <!-- Pillar Divider (Portable AI | Network & Security Lab) -->
  <line x1="576" y1="68" x2="576" y2="300" stroke="{GREEN_DIM}" stroke-width="1.2" stroke-dasharray="4 4"/>

  <!-- Left: Portable USB AI Node -->
  <rect x="26" y="102" width="204" height="166" rx="7" fill="{BG_BOX}" stroke="{GREEN}" stroke-width="1.5"/>
  <circle cx="43" cy="122" r="4" fill="{GREEN}" class="pulse"/>
  <text x="55" y="126" font-size="12" font-weight="700" class="mono" fill="{GREEN}">PORTABLE USB DRIVE</text>
  <line x1="38" y1="137" x2="218" y2="137" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="40" y="158" font-size="11.2" class="sub">Runtime: llama.cpp</text>
  <text x="40" y="178" font-size="11.2" class="sub">Models: Quantized GGUF</text>
  <text x="40" y="198" font-size="11.2" class="sub">Entry: windows_start.bat</text>
  <text x="40" y="218" font-size="11.2" class="sub">Check: Host RAM Tier</text>
  <text x="40" y="244" font-size="10" class="dim">Zero-install cross-device</text>
  <text x="40" y="258" font-size="10" class="dim">Windows execution</text>

  <!-- Center: Tiered Model Targets -->
  <rect x="286" y="72" width="270" height="68" rx="6" fill="{BG_BOX}" stroke="{GREEN}" stroke-width="1.3"/>
  <text x="300" y="94" font-size="11" font-weight="700" class="mono" fill="{GREEN}">HOST &lt;= 16GB RAM (LAPTOP)</text>
  <text x="300" y="113" font-size="11.5" class="sub">&gt; Qwen 2.5 Coder 7B (GGUF)</text>
  <text x="300" y="129" font-size="10" class="dim">Low-footprint offline coding</text>

  <rect x="286" y="151" width="270" height="68" rx="6" fill="{BG_BOX}" stroke="{GREEN}" stroke-width="1.3"/>
  <text x="300" y="173" font-size="11" font-weight="700" class="mono" fill="{GREEN}">HOST &gt;= 20GB RAM (WORKSTATION)</text>
  <text x="300" y="192" font-size="11.5" class="sub">&gt; Qwen 3 Coder 30B-A3B</text>
  <text x="300" y="208" font-size="10" class="dim">High-capacity MoE local inference</text>

  <rect x="286" y="230" width="270" height="68" rx="6" fill="{BG_BOX}" stroke="{GOLD}" stroke-width="1.3"/>
  <text x="300" y="252" font-size="11" font-weight="700" class="gold">DASHBOARD &amp; CLOUD (LITELLM)</text>
  <text x="300" y="271" font-size="11.5" class="sub">&gt; Streamlit UI + API Router</text>
  <text x="300" y="287" font-size="10" class="dim">Local-first + optional cloud fallback</text>

  <!-- Right: Network & Security Lab -->
  <rect x="596" y="72" width="238" height="68" rx="6" fill="{BG_BOX}" stroke="{GREEN_DIM}" stroke-width="1.3"/>
  <text x="610" y="94" font-size="11" font-weight="700" class="mono" fill="{GREEN}">RAW TCP + FSM ENGINE</text>
  <text x="610" y="113" font-size="11.2" class="sub">Binary JSON Framing</text>
  <text x="610" y="129" font-size="10" class="dim">Authoritative DNS + Multi-thread</text>

  <rect x="596" y="151" width="238" height="68" rx="6" fill="{BG_BOX}" stroke="{GREEN_DIM}" stroke-width="1.3"/>
  <text x="610" y="173" font-size="11" font-weight="700" class="mono" fill="{GREEN}">SPLIT-BRAIN DEFENSE</text>
  <text x="610" y="192" font-size="11.2" class="sub">PID Fencing + HMAC-SHA256</text>
  <text x="610" y="208" font-size="10" class="dim">Tamper-evident checkpoints</text>

  <rect x="596" y="230" width="238" height="68" rx="6" fill="{BG_BOX}" stroke="{GREEN_DIM}" stroke-width="1.3"/>
  <text x="610" y="252" font-size="11" font-weight="700" class="mono" fill="{GREEN}">PKI &amp; AUDIT TOOLCHAIN</text>
  <text x="610" y="271" font-size="11.2" class="sub">OpenSSL / Syft / Grype</text>
  <text x="610" y="287" font-size="10" class="dim">Wireshark / Kali / CML / Azure</text>

  <!-- Legend -->
  <line x1="26" y1="312" x2="{W - 26}" y2="312" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="430" y="328" text-anchor="middle" font-size="10.2" class="dim">LEGEND:  [---] GREEN = OFFLINE LOCAL PATH   |   [---] GOLD = OPTIONAL CLOUD ROUTING</text>

  <!-- 2-segment HUD footer -->
  <rect x="26" y="{h - 34}" width="400" height="20" rx="2" fill="{GREEN_SOFT}" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="38" y="{h - 20}" font-size="10.5" font-weight="700" class="mono" fill="{GREEN}">PORTABLE AI INFRASTRUCTURE</text>
  <rect x="434" y="{h - 34}" width="400" height="20" rx="2" fill="{GREEN_SOFT}" stroke="{GREEN_DIM}" stroke-width="1"/>
  <text x="822" y="{h - 20}" text-anchor="end" font-size="10.5" font-weight="700" class="mono" fill="{GOLD}">NETWORK &amp; SECURITY LABS</text>
</svg>"""


def generate() -> None:
    write_svg("architecture-map.svg", build_architecture_map())


if __name__ == "__main__":
    generate()