<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&weight=700&size=26&duration=3200&pause=1100&color=18FF62&center=true&vCenter=true&width=760&height=55&lines=Hi%2C+I'm+Peter+Kenoian;CS+%26+InfoSec+%40+Colorado+State+University;Building+Resilient+Systems+%26+Local+AI;Systems+Hardening+%26+Network+Security" alt="Typing intro" />

Focused on systems hardening, network security, portable AI infrastructure, and practical IT.<br/>
I learn how systems break by building them first—from raw TCP protocols to fault-tolerant clusters.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0066B1?style=for-the-badge&logo=linkedin&logoColor=F6D04D)](https://www.linkedin.com/in/peter-kenoian-1051652ba)
[![GitHub](https://img.shields.io/badge/GitHub-090D0A?style=for-the-badge&logo=github&logoColor=18FF62)](https://github.com/pken891)
![Based in Fort Collins, CO](https://img.shields.io/badge/Based_in-Fort_Collins,_CO-1B3B24?style=for-the-badge&labelColor=090D0A)

</div>

---

<div align="center">

<img src="assets/skills-banner.svg" alt="Technical Skills and Tools" width="100%" />

<br/><br/>

**🛡️ Defense, Auditing & PKI**<br/>
![OpenSSL](https://img.shields.io/badge/OpenSSL_PKI-090D0A?style=flat-square&logo=openssl&logoColor=18FF62)
![Wireshark](https://img.shields.io/badge/Wireshark-090D0A?style=flat-square&logo=wireshark&logoColor=18FF62)
![Syft](https://img.shields.io/badge/Syft_SBOM-090D0A?style=flat-square&logoColor=18FF62)
![Grype](https://img.shields.io/badge/Grype_Scanner-090D0A?style=flat-square&logoColor=18FF62)
![HMAC](https://img.shields.io/badge/HMAC--SHA256_Auth-1B3B24?style=flat-square)
![PID Fencing](https://img.shields.io/badge/PID_Fencing-1B3B24?style=flat-square)

<br/>

**☢️ Offense & Analysis**<br/>
![Kali Linux](https://img.shields.io/badge/Kali_Linux-090D0A?style=flat-square&logo=kalilinux&logoColor=F6D04D)
![Packet Analysis](https://img.shields.io/badge/Packet_Analysis-4A1010?style=flat-square)
![Fault & Tamper Testing](https://img.shields.io/badge/Fault_%26_Tamper_Testing-4A1010?style=flat-square)

<br/>

**⚙️ Systems, Cloud & Networking**<br/>
![Python](https://img.shields.io/badge/Python-0066B1?style=flat-square&logo=python&logoColor=F6D04D)
![Linux](https://img.shields.io/badge/Linux-090D0A?style=flat-square&logo=linux&logoColor=18FF62)
![Windows 11](https://img.shields.io/badge/Windows_11-0066B1?style=flat-square)
![Microsoft Azure](https://img.shields.io/badge/Microsoft_Azure-0066B1?style=flat-square)
![Cisco Modeling Labs](https://img.shields.io/badge/Cisco_Modeling_Labs-090D0A?style=flat-square&logo=cisco&logoColor=18FF62)
![VirtualBox](https://img.shields.io/badge/VirtualBox-090D0A?style=flat-square&logo=virtualbox&logoColor=18FF62)

<br/>

**🤖 Local & Cloud AI**<br/>
![llama.cpp](https://img.shields.io/badge/llama.cpp_(GGUF)-090D0A?style=flat-square)
![LiteLLM](https://img.shields.io/badge/LiteLLM-1B3B24?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-090D0A?style=flat-square&logo=streamlit&logoColor=18FF62)

</div>

---

<div align="center">

## 🎯 Featured Projects

<img src="assets/projects.svg" alt="Featured Projects: Assembly-AI-Tool (In Progress), CS457 Texas Hold'em Showdown (Work in Progress), CS456 Fault-Tolerance and Security Audit (Complete)" width="100%" />

<br/><br/>

[![Assembly-AI-Tool](https://img.shields.io/badge/View_Repo:_Assembly--AI--Tool-090D0A?style=for-the-badge&logo=github&logoColor=F6D04D)](https://github.com/pken891/Assembly-AI-Tool)
[![Texas Hold'em](https://img.shields.io/badge/View_Repo:_Texas--Holdem--Showdown-090D0A?style=for-the-badge&logo=github&logoColor=18FF62)](https://github.com/pken891/CS457---Texas-Holdem-Showdown)
[![Security Audit](https://img.shields.io/badge/View_Repo:_CS456--Security--Project-090D0A?style=for-the-badge&logo=github&logoColor=18FF62)](https://github.com/pken891/CS456-Security-Group-Project)

</div>

---

<!-- SYSTEM ARCHITECTURE SECTION (UNCOMMENT WHEN READY)

<div align="center">

## 🗺️ System Architecture

[SVG SLOT WHEN READY]:
<img src="assets/architecture-map.svg" alt="System Architecture diagram showing portable USB llama.cpp node, RAM-aware model routing, LiteLLM cloud fallback, and socket/security lab stack" width="100%" />

| Focus Area | Implementation |
| :--- | :--- |
| **Hardware-Aware AI Portability** | Runs from a portable USB drive, checks available host RAM, and serves quantized GGUF models (`Qwen 2.5 Coder 7B` on ≤16GB systems, `Qwen 3 Coder 30B-A3B` on ≥20GB workstations) with zero host installs. |
| **Custom Protocol Engineering** | Multi-threaded 1v1 Texas Hold'em engine built over raw TCP sockets using binary length-prefixed JSON framing, strict finite state machine validation, and authoritative DNS resolution. |
| **Split-Brain & Tamper Defense** | Fault-recovery architecture using PID fencing and HMAC-SHA256 checkpoint verification to survive forced process kills and state-file tampering. |

</div>

---

-->

<!-- LOCAL & CLOUD AI GATEWAY SECTION (UNCOMMENT WHEN READY)

<div align="center">

## 🖥️ Local & Cloud AI Gateway (`Assembly-AI-Tool`)

[SVG SLOT WHEN READY]:
<img src="assets/assembly-ai.svg" alt="Assembly-AI-Tool pipeline: host RAM detection, LiteLLM routing, portable USB llama.cpp server, and cloud API fallback" width="100%" />

A local-first AI interface engineered for cross-device portability and operational security.

| Capability | Details |
| :--- | :--- |
| **Unified Local + Cloud Routing** | Manages a portable `llama.cpp` server and online APIs through `LiteLLM` inside a green/red retro CRT dashboard. |
| **Operational Security** | Keeps sensitive code and configs local when needed, backed by strict pre-commit API key and metadata scrubbing. |
| **Planned Additions** | Real-time model loading progress bar, expanded token-usage analytics, and local file uploads. |

> *Running models locally keeps sensitive code and API keys under your own control.*

<details>
<summary>Assembly-AI-Tool roadmap</summary>

<br/>

| Status | Milestone |
| :---: | :--- |
| ✅ | Portable USB `llama.cpp` server across Windows hosts |
| ✅ | RAM-tiered GGUF model routing (`7B` vs `30B-A3B`) |
| ✅ | Retro green/red web dashboard with `LiteLLM` routing |
| ⬜ | Real-time model loading progress bar |
| ⬜ | Expanded per-conversation & cumulative token analytics |
| ⬜ | Local file upload & context ingestion |

</details>

</div>

---

-->

<div align="center">

## 💼 Open to Opportunities

<img src="assets/career-card.svg" alt="Open to Opportunities: B.S. Computer Science and Information Systems at Colorado State University; targeting early-career roles in Information Security, Cloud/Software Engineering, and IT Support" width="100%" />

<br/><br/>

[![Hire me on LinkedIn](https://img.shields.io/badge/Hiring%3F_Message_me_on_LinkedIn-0066B1?style=for-the-badge&logo=linkedin&logoColor=F6D04D)](https://www.linkedin.com/in/peter-kenoian-1051652ba)

</div>

---

<div align="center">

<img src="assets/github-stats-banner.svg" alt="GitHub Activity and Stats" width="100%" />

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api?username=pken891&show_icons=true&bg_color=090D0A&title_color=18FF62&text_color=B8E6C1&icon_color=F6D04D&border_color=18FF62" alt="GitHub stats" height="165" />
<img src="https://streak-stats.demolab.com?user=pken891&background=090D0A&border=18FF62&stroke=18FF62&ring=18FF62&fire=F6D04D&currStreakNum=18FF62&sideNums=18FF62&currStreakLabel=18FF62&sideLabels=B8E6C1&dates=7CA886" alt="GitHub streak" height="165" />

</div>