import os, sys, webbrowser
from modules import google_dork, sqli_scanner, login_bypass, admin_finder, report_generator, logger

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""\nFORHAD-SCANNER-PRO\n""")

def main():
    while True:
        clear(); banner()
        print("[1] Google Dork\n[2] SQLi Scanner\n[3] Login Bypass\n[4] Admin Finder\n[5] Report\n[6] Logs\n[7] GitHub\n[8] Exit\n")
        try:
            choice = input("Select > ")
            if choice == "1": google_dork.scan(input("URL: "))
            elif choice == "2": sqli_scanner.scan(input("URL: "))
            elif choice == "3": login_bypass.test(input("URL: "))
            elif choice == "4": admin_finder.find(input("URL: "))
            elif choice == "5": report_generator.generate()
            elif choice == "6": logger.view_logs()
            elif choice == "7": webbrowser.open("https://github.com/Forhadj/FORHAD-SCANNER-PRO")
            elif choice == "8": sys.exit()
        except KeyboardInterrupt: sys.exit()

if __name__ == "__main__": main()
