echo 'import os
import sys
import webbrowser
from modules import google_dork, sqli_scanner, login_bypass, admin_finder, report_generator, logger

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print(r"""
    ███████╗████████╗██╗  ██╗██╗ ██████╗ █████╗ ██╗      ██████╗ 
    ██╔════╝╚══██╔══╝██║  ██║██║██╔════╝██╔══██╗██║     ██╔═══██╗
    █████╗     ██║   ███████║██║██║     ███████║██║     ██║   ██║
    ██╔══╝     ██║   ██╔══██║██║██║     ██╔══██║██║     ██║   ██║
    ███████╗   ██║   ██║  ██║██║╚██████╗██║  ██║███████╗╚██████╔╝
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ 
    """)

def main():
    while True:
        clear_screen()
        print_banner()
        print("[1] Google Dork Scanner")
        print("[2] SQLi Vulnerability Scanner")
        print("[3] Login Bypass Tester")
        print("[4] Admin Panel Finder")
        print("[5] Generate Report")
        print("[6] View Logs")
        print("[7] Open GitHub Repo")
        print("[8] Help & Usage")
        print("[9] Exit\n")
        
        try:
            choice = input("Select an option > ")
            
            if choice == "1":
                target = input("Enter target URL: ")
                google_dork.scan(target)
            elif choice == "2":
                url = input("Enter target URL: ")
                sqli_scanner.scan(url)
            elif choice == "3":
                url = input("Enter login page URL: ")
                login_bypass.test(url)
            elif choice == "4":
                url = input("Enter target URL: ")
                admin_finder.find(url)
            elif choice == "5":
                report_generator.generate()
            elif choice == "6":
                logger.view_logs()
            elif choice == "7":
                webbrowser.open("https://github.com/yourusername/Ethical-Hacking-Toolkit")
            elif choice == "8":
                print("Help information...")
            elif choice == "9":
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid option")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            sys.exit()

if __name__ == "__main__":
    main()' > main.py
