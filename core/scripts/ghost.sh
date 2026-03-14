#!/bin/bash
while true; do
    rm -rf ~/.cache/*
    pkg clean
    sleep 120
    cd ~/Nexus-Omni
    git pull origin main # Ambil update terbaru biar gak bentrok
    git add .
    git commit -m "V30.0: Maintenance & Secure Sync"
    git push origin main
    sleep 300
done
