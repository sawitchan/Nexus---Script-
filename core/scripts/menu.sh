#!/bin/bash
clear
GOLD='\033[38;5;214m'; WHITE='\033[1;37m'; RED='\033[1;31m'; RESET='\033[0m'; BLUE='\033[1;34m'
P="      "

echo -e "${P}${GOLD}╔══════════════════════════════════════════════════════════╗${RESET}"
echo -e "${P}║ ${WHITE}         NEXUS-OMNI SYSTEM | ${GOLD}CYBER MONITOR    ${P}${WHITE}║"
echo -e "${P}${GOLD}╠══════════════════════════════════════════════════════════╣${RESET}"
echo -e "${P}║ ${GOLD}[01]${WHITE} DDoS SHIELD ACTIVE     ${GOLD}[11]${WHITE} CPU REAL-TIME INFO    ${P}║"
echo -e "${P}║ ${GOLD}[02]${WHITE} KEYGEN GENERATOR       ${GOLD}[12]${WHITE} RESPONSIVE RAM INFO   ${P}║"
echo -e "${P}║ ${GOLD}[03]${WHITE} ANTI-SNIFF (LIVE)      ${GOLD}[13]${WHITE} DEEP STORAGE ANALYZE  ${P}║"
echo -e "${P}║ ${GOLD}[04]${WHITE} BRUTE-FORCE DETECT     ${GOLD}[14]${WHITE} SMART PROCESS MONITOR ${P}║"
echo -e "${P}║ ${GOLD}[05]${WHITE} IP GEO-TRACKER         ${GOLD}[15]${WHITE} GLOBAL PUBLIC IP      ${P}║"
echo -e "${P}║ ${GOLD}[06]${WHITE} AI SCANNER (OCR)       ${GOLD}[16]${WHITE} ARP NETWORK SCANNER   ${P}║"
echo -e "${P}║ ${GOLD}[07]${WHITE} WEB EXPLOIT SCAN       ${GOLD}[17]${WHITE} GLOBAL PORT SCANNER   ${P}║"
echo -e "${P}║ ${GOLD}[08]${WHITE} SYSTEM KERNEL INFO     ${GOLD}[18]${WHITE} LATENCY MONITOR       ${P}║"
echo -e "${P}║ ${GOLD}[09]${WHITE} STORAGE SETUP          ${GOLD}[19]${WHITE} PURGE SYSTEM CACHE    ${P}║"
echo -e "${P}║ ${GOLD}[20]${WHITE} EXIT SYSTEM            ${GOLD}[21]${WHITE} LIVE CYBER ATTACKS    ${P}║"
echo -e "${P}${GOLD}╠══════════════════════════════════════════════════════════╣${RESET}"
echo -e "${P}║ ${GOLD}[22]${WHITE} PROXY/VPN TUNNEL (AUTO-SOCKS5)                    ${P}║"
echo -e "${P}${GOLD}╚══════════════════════════════════════════════════════════╝${RESET}"
read -p " NEXUS-OMNI >> " opt

case $opt in
    12) python3 core/ram_monitor.py ;;
    13) python3 core/storage_deep.py ;;
    14) python3 core/process_monitor.py ;;
    15) python3 core/ip_global.py ;;
    21) python3 core/cyber_live.py ;;
    22) bash core/proxy_gate.sh ;;
    01) python3 core/shield.py ;;
    02) python3 core/auth.py ;;
    03) bash core/anti_sniff.sh ;;
    04) python3 core/detector.py ;;
    05) python3 core/ip_tracker.py ;;
    06) python3 core/ocr_scan.py ;;
    07) bash core/wifi_scan.sh ;;
    08) python3 core/sys_info.py ;;
    11) lscpu; read -p "Enter..." ;;
    16) bash core/arp_scan.sh ;;
    17) bash core/port_scan.sh ;;
    18) ping -c 4 8.8.8.8; read -p "Enter..." ;;
    19) pkg clean; rm -rf ~/.cache/*; echo -e "${GOLD}[+] Purged!${RESET}"; sleep 1 ;;
    20) exit ;;
    *) echo -e "${RED}[!] Modul $opt Syncing...${RESET}"; sleep 1 ;;
esac
bash core/scripts/menu.sh
