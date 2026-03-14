#!/bin/bash
clear
GOLD='\033[38;5;214m'; RESET='\033[0m'
echo -e "${GOLD}NEXUS-OMNI REAL-TIME DASHBOARD${RESET}"
echo -e "[01] DDoS Shield   [02] Auth Keygen   [03] Anti-Sniff"
echo -e "[05] IP Tracker    [08] System Info   [12] RAM Usage"
echo -e "[15] Global IP     [21] Cyber Live    [22] Proxy Gate"
echo -ne "${GOLD}>> ${RESET}"
read opt
case $opt in
 1|01) python3 core/shield.py ;;
 2|02) python3 core/auth.py ;;
 3|03) bash core/anti_sniff.sh ;;
 5|05) python3 core/ip_tracker.py ;;
 8|08) python3 core/sys_info.py ;;
 12) python3 core/ram_monitor.py ;;
 15) python3 core/ip_global.py ;;
 21) python3 core/cyber_live.py ;;
 22) bash core/proxy_gate.sh ;;
 *) echo "Modul tidak ditemukan..." ;;
esac
echo -e "\nKlik Enter untuk kembali..."
read
bash core/scripts/menu.sh
