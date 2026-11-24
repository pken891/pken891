#!/usr/bin/env python3
"""Generate projects.svg (featured projects card)."""

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


def build_projects() -> str:
    h = 336
    projects = [
        (
            "ASSEMBLY-AI-TOOL",
            "IN PROGRESS",
            GOLD,
            "Hybrid local + cloud AI dashboard (LiteLLM, Streamlit, portable USB llama.cpp)",
            "github.com/pken891/Assembly-AI-Tool",
        ),
        (
            "CS457 // TEXAS HOLD'EM SHOWDOWN",
            "WORK IN PROGRESS",
            GOLD,
            "1v1 raw TCP poker engine: binary JSON framing, FSM logic, multi-subnet Cisco/DNS",
            "github.com/pken891/CS457---Texas-Holdem-Showdown",
        ),
        (
            "CS456 // FAULT-TOLERANCE &amp; SECURITY AUDIT",
            "COMPLETE",
            GREEN,
            "Passive redundancy hardened with PID fencing &amp; HMAC-SHA256 checkpoint verification",
            "github.com/pken891/CS456-Security-Group-Project",
        ),
    ]

    rows = []
    ry = 52
    for title, status, color, desc, repo in projects:
        pill_w = len(status) * 7.2 + 20
        pill_x = W - 38 - pill_w
        pulse_cls = "pulse" if color == GOLD else ""
        # Pip-Boy square marker (filled when active, check-bordered when complete)
        marker = (
            f'<rect x="40" y="{ry + 16}" width="10" height="10" fill="{color}" class="{pulse_cls}"/>'
            if color == GOLD
            else f'<rect x="40" y="{ry + 16}" width="10" height="10" fill="{color}" fill-opacity="0.25" stroke="{color}" stroke-width="1.5"/>'
            f'<path d="M 42 {ry + 21} L 44.5 {ry + 24} L 48.5 {ry + 18}" fill="none" stroke="{color}" stroke-width="1.6"/>'
        )
        rows.append(
            f"""  <rect x="26" y="{ry}" width="{W - 52}" height="74" rx="6" fill="{BG_BOX}" stroke="{GREEN_DIM}" stroke-width="1.2"/>
  {marker}
  <text x="60" y="{ry + 25}" font-size="13.5" font-weight="700" class="mono" fill="{GREEN}">{title}</text>
  <rect x="{pill_x:.1f}" y="{ry + 11}" width="{pill_w:.1f}" height="20" rx="3" fill="{color}" fill-opacity="0.14" stroke="{color}" stroke-width="1"/>
  <text x="{pill_x + pill_w / 2:.1f}" y="{ry + 25}" text-anchor="middle" font-size="10.5" font-weight="700" class="mono" fill="{color}">{status}</text>
  <text x="60" y="{ry + 46}" font-size="11.5" class="sub">{desc}</text>
  <text x="60" y="{ry + 63}" font-size="10.5" class="dim">&gt; {repo}</text>"""
        )
        ry += 82

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">
{shared_defs("pr", h)}
{pipboy_frame("pr", h, "PROJECTS", "FEATURED REPOSITORIES // 3", ("ACTIVE: 2", "PUBLIC SOURCE // CLEAN OPSEC", "COMPLETED: 1"))}
{"".join(rows)}
</svg>"""


def generate() -> None:
    write_svg("projects.svg", build_projects())


if __name__ == "__main__":
    generate()