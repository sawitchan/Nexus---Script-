import requests

def scan_image(image_path):
    # API key yang Tuan punya sebelumnya
    api_key = "K83088163488957"
    url = "https://api.ocr.space/parse/image"
    
    with open(image_path, 'rb') as f:
        r = requests.post(url, files={'image': f}, data={'apikey': api_key})
    
    result = r.json()
    return result.get("ParsedResults")[0].get("ParsedText")

if __name__ == "__main__":
    print("[*] AI OCR Scan Ready...")
