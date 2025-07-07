#!/usr/bin/env python3
import os, requests, sys, time
from bs4 import BeautifulSoup
from colorama import Fore, Style

# Colors
R, G, Y, B = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE
N = Style.RESET_ALL

def banner():
    print(f"""{G}
╔══════════════════════════════════════════╗
║         🔎 FORHAD SCANNER PRO v1.0       ║
╚══════════════════════════════════════════╝{N}
""")

def google_dork_scanner():
    print(f"{Y}[*] Google Dork Scanner running...{N}")
    dork = input("Enter Google Dork: ")
    print(f"{G}Searching for: {dork}{N}")
    # This is just a placeholder
    print("Fake result: https://example.com/vuln")

def sqli_scanner():
    print(f"{Y}[*] SQLi Scanner running...{N}")
    url = input("Enter URL to test: ")
    test_url = url + "'"
    try:
        r = requests.get(test_url, timeout=10)
        if "sql" in r.text.lower() or "error" in r.text.lower():
            print(f"{G}[+] Vulnerable!{N}")
        else:
            print(f"{R}[-] Not vulnerable.{N}")
    except:
        print(f"{R}[-] Request failed.{N}")

def login_bypass():
    print(f"{Y}[*] Login Bypass Test...{N}")
    print(f"{G}Try injecting ' OR '1'='1 in login fields.{N}")

def generate_report():
    with open("data/report.txt", "w") as f:
        f.write("Dummy Report - FORHAD SCANNER PRO\n")
    print(f"{G}[+] Report saved to data/report.txt{N}")

def view_logs():
    try:
        with open("data/logs.txt") as f:
            print(f.read())
    except:
        print(f"{R}[-] No logs found.{N}")

def open_github():
    print(f"{Y}[*] Opening GitHub Repo...{N}")
    os.system("xdg-open https://github.com/Forhadj/FORHAD-SCANNER-PRO")

def help_menu():
    print(f"""{G}
Usage:
 [1] Google Dork Scanner - Search vulnerable links
 [2] SQLi Scanner - Detect SQL injection points
 [3] Login Bypass Tester - Manual login test tips
 [4] Generate dummy report
 [5] View saved logs
 [6] Open GitHub Repository
 [7] Show this help
 [8] Admin Panel Finder
 [0] Exit
{N}""")

def admin_finder():
    print(f"{Y}[*] Admin Panel Finder started...{N}")
    target = input("Enter site URL (without / at end): ")
    paths = ["admin", "admin/login", "administrator", "cpanel", "admin.php"]
    for path in paths:
        url = f"{target}/{path}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{G}[+] Found: {url}{N}")
                break
        except:
            continue
    else:
        print(f"{R}[-] No admin panel found.{N}")

def main():
    while True:
        banner()
        print(f"""{G}
 [1] Google Dork Scanner
 [2] SQLi Vulnerability Scanner
 [3] Login Bypass Tester
 [4] Generate Report
 [5] View Logs
 [6] Open GitHub Repo
 [7] Help & Usage
 [8] Admin Panel Finder
 [0] Exit{N}""")
        choice = input("Select an option > ")
        if choice == "1":
            google_dork_scanner()
        elif choice == "2":
            sqli_scanner()
        elif choice == "3":
            login_bypass()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            view_logs()
        elif choice == "6":
            open_github()
        elif choice == "7":
            help_menu()
        elif choice == "8":
            admin_finder()
        elif choice == "0":
            print(f"{Y}Goodbye!{N}")
            break
        else:
            print(f"{R}Invalid option.{N}")
        input(f"{B}Press Enter to return to menu...{N}")

if __name__ == "__main__":
    main()
