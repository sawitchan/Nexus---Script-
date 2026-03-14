#!/bin/bash
clear

if [ -f core/banner.sh ]; then bash core/banner.sh; fi

GOLD='\033[38;5;214m'; BOLD='\033[1m'; RESET='\033[0m'; BLUE='\033[1;34m'; WHITE='\033[1;37m'; RED='\033[1;31m'

echo -e "${GOLD}${BOLD} ══════════════════════════════════════════════════════════════${RESET}"
echo -e " ${WHITE}NEXUS-OMNI SYSTEM | ${GOLD} DASHBOARD ${RESET}"
echo -e "${GOLD}${BOLD} ══════════════════════════════════════════════════════════════${RESET}"
echo -e " ${GOLD}[01]${WHITE} WEB-SHIELD PROTECTOR    ${GOLD}[11]${WHITE} CPU ARCHITECTURE"
echo -e " ${GOLD}[02]${WHITE} NEXUS-AUTH (KEYGEN)      ${GOLD}[12]${WHITE} RAM USAGE INFO"
echo -e " ${GOLD}[03]${WHITE} ANTI-SNIFF MONITOR       ${GOLD}[13]${WHITE} STORAGE ANALYZER"
echo -e " ${GOLD}[04]${WHITE} BRUTE-FORCE DETECTOR     ${GOLD}[14]${WHITE} RUNNING PROCESS"
echo -e " ${GOLD}[05]${WHITE} IP GEOLOCATION TRACKER   ${GOLD}[15]${WHITE} CHECK MY PUBLIC IP"
echo -e " ${GOLD}[06]${WHITE} NEXUS-OCR (AI SCAN)       ${GOLD}[16]${WHITE} ARP NETWORK SCAN"
echo -e " ${GOLD}[07]${WHITE} WIFI DEVICE DISCOVERY    ${GOLD}[17]${WHITE} PORT SCAN LOCAL"
echo -e " ${GOLD}[08]${WHITE} OS SYSTEM INFORMATION    ${GOLD}[18]${WHITE} PING GOOGLE TEST"
echo -e " ${GOLD}[09]${WHITE} TERMUX STORAGE SETUP     ${GOLD}[19]${WHITE} CLEAN CACHE TEMP"
echo -e " ${GOLD}[20]${WHITE} EXIT SYSTEM              ${GOLD}[21]${WHITE} GLOBAL CYBER MONITOR"
echo -e "${GOLD}${BOLD} ══════════════════════════════════════════════════════════════${RESET}"
read -p " NEXUS-OMNI >> " opt

case $opt in
    01) python3 core/shield.py ;;
    02) python3 core/auth.py ;;
    03) bash core/anti_sniff.sh ;;
    04) python3 core/detector.py ;;
    05) python3 core/ip_tracker.py ;;
    06) python3 core/ocr_scan.py ;;
    07) bash core/wifi_scan.sh ;;
    11) lscpu; read -p "Enter..." ;;
    12) free -h; read -p "Enter..." ;;
    13) df -h; read -p "Enter..." ;;
    14) ps aux | head -n 15; read -p "Enter..." ;;
    15) curl -s ifconfig.me; echo ""; read -p "Enter..." ;;
    16) bash core/arp_scan.sh ;;
    17) bash core/port_scan.sh ;;
    18) bash core/ping_test.sh ;;
    19) pkg clean && rm -rf ~/.cache/*; echo -e "${GOLD}[+] Cache Cleaned!${RESET}"; sleep 1 ;;
    21) bash core/cyber_monitor.sh ;;
    20) exit ;;
    *) echo -e "${RED}[!] Modul $opt Sedang Dalam Sinkronisasi Logic...${RESET}"; sleep 1 ;;
esac
bash core/scripts/menu.sh
