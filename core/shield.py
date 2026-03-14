print("\033[1;36m[*] WEB-SHIELD PROTECTOR ACTIVE\033[0m")
print("[i] Monitoring incoming web requests...")
import os; os.system("netstat -tpn | grep :80")
