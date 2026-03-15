#!/bin/bash
# NEXUS-OMNI AUTO-BACKUP SYSTEM

while true
do
    echo "[$(date)] Memulai Auto-Backup ke GitHub..."
    git add .
    git commit -m "Auto-Backup: $(date +'%Y-%m-%d %H:%M:%S') - Anti-Cache Protection"
    git push origin main
    
    echo "[+] Backup Selesai. Menunggu 1 jam untuk sesi berikutnya..."
    sleep 3600
done
