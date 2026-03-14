#!/bin/bash
clear
GOLD='\033[38;5;214m'; RESET='\033[0m'
echo -e "${GOLD}[*] INITIALIZING SECURE PROXY GATEWAY...${RESET}"

# Jalankan Tor di background jika belum jalan
if ! pgrep -x "tor" > /dev/null; then
    tor > /dev/null 2>&1 &
    sleep 5
fi

# Setel proxy sistem Termux agar semua request lewat Tor (Port 9050)
export http_proxy="socks5://127.0.0.1:9050"
export https_proxy="socks5://127.0.0.1:9050"

echo -e "${GOLD}[+] Nexus Tunnel Established!${RESET}"
echo -e "[*] Mengecek Lokasi Baru Tuan..."
# Tes IP setelah pakai proxy
curl -s --socks5-hostname 127.0.0.1:9050 https://ipapi.co/json/ | grep -E "ip|city|country_name"

echo -e "\n${GOLD}[!] Sekarang koneksi Tuan terenkripsi dan anonim.${RESET}"
read -p "Tekan Enter untuk kembali ke Menu..."
