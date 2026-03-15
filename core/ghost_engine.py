import requests
import random

def get_global_proxy():
    """Mencari Proxy Global secara otomatis & Memblokir Server Indonesia"""
    try:
        # Mengambil list proxy HTTP/S dari provider global
        api_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=anonymous"
        raw_list = requests.get(api_url, timeout=10).text.split('\r\n')
        
        # Filter: Pastikan tidak kosong
        proxies = [p for p in raw_list if p]
        
        # Ambil satu secara acak
        selected = random.choice(proxies)
        
        # Validasi Lokasi (Pastikan Bukan Indonesia)
        check = requests.get(f"http://ip-api.com/json/{selected.split(':')[0]}").json()
        if check.get('countryCode') == 'ID':
            return get_global_proxy() # Cari lagi kalau dapet Indonesia
            
        return {
            "http": f"http://{selected}",
            "https": f"http://{selected}",
            "info": f"{check.get('country')} ({check.get('city')})"
        }
    except:
        return None
