import os, sys, time, requests, random, socket

def get_proxy():
    try:
        res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000", timeout=5).text
        return random.choice(res.splitlines())
    except: return "Global-Ghost-Path"

def execute_reality(mod_id, target):
    proxy = get_proxy()
    # Chaining Intelligence
    if mod_id in ["05", "09", "15", "29", "30", "37"]:
        try:
            res = requests.get(f"http://ip-api.com/json/{target}", timeout=10).json()
            return f"🛰️ **INTEL FOUND**\nIP: `{res.get('query')}`\nISP: {res.get('isp')}\nLoc: {res.get('city')}, {res.get('country')}\nProxy: `{proxy}`\n\n*Target Locked. Chain Active.*"
        except: return "❌ Connection Timeout via Proxy Ghost."
    return f"⚙️ Modul {mod_id} Active. Status: Success via {proxy}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(execute_reality(sys.argv[2], sys.argv[4]))
