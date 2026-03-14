#!/bin/bash
while true; do
    # Pembersihan 5 Menit
    rm -rf ~/.cache/*
    pkg clean
    sleep 120
    # Sync GitHub 7 Menit
    cd ~/Nexus-Omni
    git add .
    git commit -m "V2.1: System Keep Alive & Auto-Maintenance"
    git push origin main
    sleep 300
done
