#!/bin/bash
clear
if [ -f core/banner.sh ]; then bash core/banner.sh; fi

GOLD='\033[38;5;214m'; BOLD='\033[1m'; RESET='\033[0m'; WHITE='\033[1;37m'; RED='\033[1;31m'
P="          " 

echo -e "${GOLD}${BOLD}${P}╔════════════════════════════════════════════════╗${RESET}"
echo -e "${P}║ ${WHITE}    NEXUS-OMNI SYSTEM | ${GOLD}GLOBAL ACCESS  ${P}║"
echo -e "${GOLD}${BOLD}${P}╚════════════════════════════════════════════════╝${RESET}"
echo -e "${P} ${GOLD}[01]${WHITE} WEB-SHIELD (DDoS)     ${GOLD}[11]${WHITE} CPU ARCHITECTURE"
echo -e "${P} ${GOLD}[02]${WHITE} NEXUS-AUTH (KEYGEN)   ${GOLD}[12]${WHITE} RAM USAGE INFO"
echo -e "${P} ${GOLD}[03]${WHITE} ANTI-SNIFF MONITOR    ${GOLD}[13]${WHITE} STORAGE ANALYZER"
echo -e "${P} ${GOLD}[04]${WHITE} BRUTE-FORCE DETECT    ${GOLD}[14]${WHITE} RUNNING PROCESS"
echo -e "${P} ${GOLD}[05]${WHITE} IP GEOLOCATION        ${GOLD}[15]${WHITE} CHECK PUBLIC IP"
echo -e "${P} ${GOLD}[06]${WHITE} NEXUS-OCR (AI SCAN)   ${GOLD}[16]${WHITE} ARP NETWORK SCAN"
echo -e "${P} ${GOLD}[07]${WHITE} WIFI EXPLOIT SCAN     ${GOLD}[17]${WHITE} PORT SCAN LOCAL"
echo -e "${P} ${GOLD}[08]${WHITE} OS SYSTEM INFO        ${GOLD}[18]${WHITE} PING GOOGLE TEST"
echo -e "${P} ${GOLD}[09]${WHITE} TERMUX STORAGE        ${GOLD}[19]${WHITE} CLEAN CACHE"
echo -e "${P} ${GOLD}[20]${WHITE} EXIT SYSTEM           ${GOLD}[21]${WHITE} CYBER MONITOR"
echo -e "${P} ${GOLD}[22]${WHITE} VPN/PROXY GATEWAY (PUBLIC ACCESS)"
echo -e "${GOLD}${BOLD}${P}══════════════════════════════════════════════════${RESET}"
read -p " NEXUS-OMNI >> " opt

case $opt in
    01) python3 core/shield.py ;;
    02) python3 core/auth.py ;;
    03) bash core/anti_sniff.sh ;;
    04) python3 core/detector.py ;;
    05) python3 core/ip_tracker.py ;;
    07) bash core/wifi_scan.sh ;;
    11) lscpu; read -p "Enter..." ;;
    12) free -h; read -p "Enter..." ;;
    13) df -h; read -p "Enter..." ;;
    14) ps aux | head -n 15; read -p "Enter..." ;;
    15) curl -s ifconfig.me; echo ""; read -p "Enter..." ;;
    16) bash core/arp_scan.sh ;;
    17) bash core/port_scan.sh ;;
    18) bash core/ping_test.sh ;;
    19) pkg clean && rm -rf ~/.cache/*; echo -e "${GOLD}[+] Cleaned!${RESET}"; sleep 1 ;;
    21) bash core/cyber_monitor.sh ;;
    22) echo -e "${GOLD}[*] Connecting to Nexus Proxy...${RESET}"
        export https_proxy="http://127.0.0.1:8080" # Contoh setting proxy
        echo -e "${WHITE}[+] Global Access Tunnel Active via Proxy.${RESET}"
        sleep 2 ;;
    20) exit ;;
    *) echo -e "${RED}[!] Modul $opt Syncing Logic...${RESET}"; sleep 1 ;;
esac
bash core/scripts/menu.sh
