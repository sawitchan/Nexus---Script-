#!/bin/bash
clear
echo -e "\033[1;33mNEXUS-OMNI REAL-TIME DASHBOARD\033[0m"
echo "[01] DDoS Shield   [02] Auth Keygen   [03] Anti-Sniff"
echo "[05] IP Tracker    [08] System Info   [12] RAM Usage"
echo "[15] Global IP     [21] Cyber Live    [22] Proxy Gate"
echo -e "\033[1;32m[25] Health Check  [26] IDS Sniffer   [27] Telegram Alert    [28] Auto Clean\033[0m"
echo "--------------------------------------------------------"
read -p ">> " choice

case $choice in
    01) python3 core/ddos_shield.py ;;
    25) python3 core/health_check.py ;;
    26) python3 core/intrusion_detect.py ;;
    27) python3 core/telegram_alert.py ;;
    28) python3 core/auto_clean.py ;;
    *) echo -e "\n\033[1;31mModul tidak ditemukan...\033[0m" ;;
esac

echo -e "\nKlik Enter untuk kembali..."
read
bash core/scripts/menu.sh
