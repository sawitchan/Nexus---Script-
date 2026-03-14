#!/bin/bash
clear
bash core/banner.sh
C='\033[1;36m'; W='\033[1;37m'; Y='\033[1;33m'
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
    21) curl -s "https://news.google.com/rss/search?q=technology" | grep -oP '(?<=<title>).*?(?=</title>)' | head -n 7; read -p "Enter..." ;;
    20) exit ;;
    *) echo -e "Modul Active..."; sleep 1 ;;
esac
