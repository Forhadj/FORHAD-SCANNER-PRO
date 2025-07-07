echo 'import requests
from concurrent.futures import ThreadPoolExecutor

def find(url):
    print(f"\nScanning for admin panels on {url}")
    
    with open("../wordlists/admin_panels.txt") as f:
        paths = [line.strip() for line in f]
    
    def check_path(path):
        try:
            target = f"{url}/{path}"
            res = requests.get(target, timeout=5)
            if res.status_code == 200:
                print(f"\033[92m[+] Found: {target}\033[0m")
                if "x-admin-secret" in res.headers:
                    print(f"\033[93m[!] Secret key: {res.headers['x-admin-secret']}\033[0m")
        except:
            pass
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_path, paths)' > modules/admin_finder.py
