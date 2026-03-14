import os
print('\033[1;31m[!] SHIELD ACTIVE: MONITORING LIVE CONNECTIONS...\033[0m')
os.system('netstat -tnup | grep ESTABLISHED || netstat -tupln')
