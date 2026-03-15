#!/bin/bash
while true
do
    git add .
    git commit -m "V15.5 Final: Auto-Save Protection"
    git push origin main
    
    # Notifikasi ke Tuan Markus
    curl -s "https://api.telegram.org/bot8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0/sendMessage?chat_id=8358311702&text=🛡️ **LAPORAN TUAN:**%0ABackup Cloud Sukses! Data Aman. 🚀&parse_mode=Markdown"
    
    sleep 3600
done
