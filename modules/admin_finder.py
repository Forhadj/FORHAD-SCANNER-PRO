import requests
from concurrent.futures import ThreadPoolExecutor

def find(url):
    print(f"[Admin Finder] {url}")
    with open("wordlists/admin_panels.txt") as f:
        paths = [x.strip() for x in f]
    def check(p):
        try:
            res = requests.get(f"{url}/{p}", timeout=5)
            if res.status_code == 200:
                print(f"[+] Found: {url}/{p}")
                if 'x-admin-secret' in res.headers:
                    print(f"[!] Secret: {res.headers['x-admin-secret']}")
        except: pass
    with ThreadPoolExecutor(10) as ex: ex.map(check, paths)
