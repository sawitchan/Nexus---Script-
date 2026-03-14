#!/bin/bash
clear
if [ -f core/banner.sh ]; then bash core/banner.sh; fi
GOLD='\033[38;5;214m'; BOLD='\033[1m'; RESET='\033[0m'; WHITE='\033[1;37m'; RED='\033[1;31m'
P="      "

echo -e "${P}${GOLD}╔══════════════════════════════════════════════════════════╗${RESET}"
echo -e "${P}║ ${WHITE}         NEXUS-OMNI SYSTEM | ${GOLD}GLOBAL ACCESS  ${P}${WHITE}║"
echo -e "${P}${GOLD}╠══════════════════════════════════════════════════════════╣${RESET}"
echo -e "${P}║ ${GOLD}[01]${WHITE} WEB-SHIELD (DDoS)      ${GOLD}[11]${WHITE} CPU ARCHITECTURE      ${P}║"
echo -e "${P}║ ${GOLD}[02]${WHITE} NEXUS-AUTH (KEYGEN)    ${GOLD}[12]${WHITE} RAM USAGE INFO        ${P}║"
echo -e "${P}║ ${GOLD}[03]${WHITE} ANTI-SNIFF MONITOR     ${GOLD}[13]${WHITE} STORAGE ANALYZER      ${P}║"
echo -e "${P}║ ${GOLD}[04]${WHITE} BRUTE-FORCE DETECT     ${GOLD}[14]${WHITE} RUNNING PROCESS       ${P}║"
echo -e "${P}║ ${GOLD}[05]${WHITE} IP GEOLOCATION         ${GOLD}[15]${WHITE} CHECK PUBLIC IP       ${P}║"
echo -e "${P}║ ${GOLD}[06]${WHITE} NEXUS-OCR (AI SCAN)    ${GOLD}[16]${WHITE} ARP NETWORK SCAN      ${P}║"
echo -e "${P}║ ${GOLD}[07]${WHITE} WIFI EXPLOIT SCAN      ${GOLD}[17]${WHITE} PORT SCAN LOCAL       ${P}║"
echo -e "${P}║ ${GOLD}[08]${WHITE} OS SYSTEM INFO         ${GOLD}[18]${WHITE} PING GOOGLE TEST      ${P}║"
echo -e "${P}║ ${GOLD}[09]${WHITE} TERMUX STORAGE         ${GOLD}[19]${WHITE} CLEAN CACHE           ${P}║"
echo -e "${P}║ ${GOLD}[20]${WHITE} EXIT SYSTEM            ${GOLD}[21]${WHITE} CYBER MONITOR         ${P}║"
echo -e "${P}${GOLD}╠══════════════════════════════════════════════════════════╣${RESET}"
echo -e "${P}║ ${GOLD}[22]${WHITE} VPN/PROXY GATEWAY (PUBLIC ACCESS)                 ${P}║"
echo -e "${P}${GOLD}╚══════════════════════════════════════════════════════════╝${RESET}"
read -p " NEXUS-OMNI >> " opt

case $opt in
    01) python3 core/shield.py ;;
    02) python3 core/auth.py ;;
    03) bash core/anti_sniff.sh ;;
    04) python3 core/detector.py ;;
    05) python3 core/ip_tracker.py ;;
    06) python3 core/ocr_scan.py ;;
    07) bash core/wifi_scan.sh ;;
    08) python3 core/sys_info.py ;;
    09) termux-setup-storage ;;
    11) lscpu; read -p "Enter..." ;;
    12) free -h; read -p "Enter..." ;;
    13) df -h; read -p "Enter..." ;;
    14) ps aux | head -n 15; read -p "Enter..." ;;
    15) curl -s ifconfig.me; echo ""; read -p "Enter..." ;;
    16) bash core/arp_scan.sh ;;
    17) bash core/port_scan.sh ;;
    18) ping -c 4 8.8.8.8; read -p "Enter..." ;;
    19) pkg clean; rm -rf ~/.cache/*; echo -e "${GOLD}[+] Cleaned!${RESET}"; sleep 1 ;;
    21) bash core/cyber_monitor.sh ;;
    22) bash core/proxy_gate.sh ;;
    20) exit ;;
    *) echo -e "${RED}[!] Modul $opt Error!${RESET}"; sleep 1 ;;
esac
bash core/scripts/menu.sh
