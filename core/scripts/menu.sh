#!/bin/bash
clear
# Panggil Banner
if [ -f core/banner.sh ]; then bash core/banner.sh; fi

C='\033[1;36m'; W='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; R='\033[1;31m'

echo -e "$W  NEXUS-OMNI (20 MODULES ACTIVE)"
echo -e "$C [01] WEB-SHIELD PROTECTOR    [11] CPU ARCHITECTURE"
echo -e " [02] NEXUS-AUTH (KEYGEN)      [12] RAM USAGE INFO"
echo -e " [03] ANTI-SNIFF MONITOR       [13] STORAGE ANALYZER"
echo -e " [04] BRUTE-FORCE DETECTOR     [14] RUNNING PROCESS"
echo -e " [05] IP GEOLOCATION TRACKER   [15] CHECK MY PUBLIC IP"
echo -e " [06] NEXUS-OCR (AI SCAN)       [16] ARP NETWORK SCAN"
echo -e " [07] WIFI DEVICE DISCOVERY    [17] PORT SCAN LOCAL"
echo -e " [08] OS SYSTEM INFORMATION    [18] PING GOOGLE TEST"
echo -e " [09] TERMUX STORAGE SETUP     [19] CLEAN CACHE TEMP"
echo -e " [20] EXIT SYSTEM"
echo -e " [21] TECH-WORLD MONITOR (REAL-TIME)"
echo -e "$C ══════════════════════════════════════════════════════════════"
read -p " NEXUS-OMNI >> " opt

case $opt in
    01) python3 core/shield.py ;;
    02) python3 core/auth.py ;;
    03) if [ -f core/anti_sniff.sh ]; then bash core/anti_sniff.sh; else echo -e "$R[!] File missing"; sleep 1; fi ;;
    04) python3 core/detector.py ;;
    05) python3 core/ip_tracker.py ;;
    06) python3 core/ocr_scan.py ;;
    07) if [ -f core/wifi_scan.sh ]; then bash core/wifi_scan.sh; else echo -e "$R[!] File missing"; sleep 1; fi ;;
    09) termux-setup-storage ;;
    11) lscpu; read -p "Enter..." ;;
    12) free -h; read -p "Enter..." ;;
    15) curl ifconfig.me; echo ""; read -p "Enter..." ;;
    19) echo -e "$Y[*] Cleaning..."; pkg clean && rm -rf ~/.cache/*; echo -e "$G[+] Cleaned!"; sleep 1 ;;
    20) exit ;;
    21) 
        echo -e "$Y[*] Fetching Technology News..."
        curl -s "https://news.google.com/rss/search?q=technology" | grep -oP '(?<=<title>).*?(?=</title>)' | head -n 7
        read -p "Enter..." ;;
    *) echo -e "$Y[!] Modul $opt Active (Simulated)..."; sleep 1 ;;
esac

# Auto Re-run menu supaya gak close
bash core/scripts/menu.sh
