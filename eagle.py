import os
import time
import socket
import sys
import random
import string
import barcode
from barcode.writer import ImageWriter
import qrcode
import phonenumbers
from phonenumbers import geocoder, carrier
import requests
from tqdm import tqdm
from pyfiglet import Figlet

# ---------- Banner ----------
def display_banner():
    banner = Figlet(font="slant").renderText("EAGLE")
    print(banner)


# ---------- Loading Bar ----------
def loading():
    for _ in tqdm(range(100), desc="LOADING...", ascii=True, ncols=75):
        time.sleep(0.01)
    print("LOADING DONE!")

# ---------- Font Function ----------
def font(text):
    cool_text = Figlet(font="slant")
    return str(cool_text.renderText(text))

# ---------- Clear/Resize Console ----------
def window_size(columns=80, height=20):
    os.system("cls" if os.name == "nt" else "clear")
    if os.name == "nt":
        os.system(f"mode con: cols={columns} lines={height}")

# ---------- Tool 1: Show My IP ----------
def show_my_ip():
    window_size(80, 20)
    print(font("FIND MY IP"))
    loading()
    try:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print(f"YOUR DEVICE IP IS: {IPAddr}")
    except Exception as e:
        print(f"Error: {e}")
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 2: Password Generator ----------
def password_generator():
    window_size(100, 25)
    print(font("PASSWORD GEN"))
    loading()
    length = input("Enter password length: ")
    if not length.isdigit():
        print("Please enter a valid number.")
        return
    length = int(length)
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}")
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 3: Wordlist Generator ----------
def wordlist_generator():
    window_size(100, 25)
    print(font("WORDLIST GEN"))
    loading()
    base = input("Enter a base word (e.g. 'admin'): ")
    suffixes = ['123', '2024', 'admin', '!', '@123', '321']
    wordlist = [base + s for s in suffixes]
    file_name = f"{base}_wordlist.txt"
    with open(file_name, "w") as f:
        for word in wordlist:
            f.write(word + "\n")
    print(f"Wordlist saved as {file_name}")
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 4: Barcode Generator ----------
def barcode_generator():
    window_size(100, 25)
    print(font("BARCODE GEN"))
    loading()
    code = input("Enter data to encode (e.g. 123456789): ")
    barcode_class = barcode.get_barcode_class('code128')
    my_barcode = barcode_class(code, writer=ImageWriter())
    filename = my_barcode.save("barcode_output")
    print(f"Barcode saved as {filename}.png")
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 5: QR Code Generator ----------
def qrcode_generator():
    window_size(100, 25)
    print(font("QRCODE GEN"))
    loading()
    data = input("Enter data to encode into QR code: ")
    img = qrcode.make(data)
    img.save("qrcode_output.png")
    print("QR Code saved as qrcode_output.png")
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 6: Phone Number Info ----------
def phone_number_info():
    window_size(100, 25)
    print(font("PHONE INFO"))
    loading()
    number = input("Enter phone number with country code (e.g. +919876543210): ")
    try:
        parsed = phonenumbers.parse(number)
        print("Region:", geocoder.description_for_number(parsed, "en"))
        print("Carrier:", carrier.name_for_number(parsed, "en"))
    except Exception as e:
        print("Error:", e)
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 7: Subdomain Scanner ----------
def subdomain_scanner():
    window_size(100, 25)
    print(font("SUBDOMAIN SCAN"))
    loading()
    domain = input("Enter target domain (e.g. example.com): ")
    subdomains = ["www", "mail", "ftp", "test", "blog", "dev"]
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url)
            print(f"[+] Found: {url}")
        except:
            pass
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 8: Port Scanner ----------
def port_scanner():
    window_size(100, 25)
    print(font("PORT SCANNER"))
    loading()
    target = input("Enter IP or domain to scan: ")
    ports = [21, 22, 23, 80, 443, 8080]
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 9: DDoS Simulator ----------
def ddos_attack():
    window_size(100, 25)
    print(font("DDOS SIM"))
    loading()
    target = input("Enter target IP or domain: ")
    print(f"Simulating DDoS attack on {target}...\n(This is just a mockup. No real traffic is being sent.)")
    for _ in range(10):
        print(f"Pinging {target} ...")
        time.sleep(0.3)
    print("Mock DDoS complete.")
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Tool 10: Admin Panel Finder ----------
def admin_panel_finder():
    window_size(100, 25)
    print(font("ADMIN FINDER"))
    loading()
    target = input("Enter website (e.g. example.com): ")
    paths = ["admin", "admin/login", "adminpanel", "login"]
    for path in paths:
        url = f"http://{target}/{path}"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"[+] Found admin panel: {url}")
        except:
            pass
    input("PRESS ENTER TO RETURN TO MENU")

# ---------- Menu ----------
def main_menu():
    while True:
        display_banner()
        options = (
            "Find me on insta :@chaitanyaa.exe\n"
            "\n"
            "1 - MY IP ADDRESS\n"
            "2 - PASSWORD GENERATOR\n"
            "3 - WORDLIST GENERATOR\n"
            "4 - BARCODE GENERATOR\n"
            "5 - QRCODE GENERATOR\n"
            "6 - PHONE NUMBER INFO\n"
            "7 - SUBDOMAIN SCANNER\n"
            "8 - PORT SCANNER\n"
            "9 - DDOS ATTACK (use this tool on our own risk)\n"
            "10 - ADMIN PANEL FINDER\n"
            "0 - EXIT\n"
            "\n"
            "THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSE"

            
        )
        print(options)
        try:
            choice = int(input("ENTER YOUR CHOICE >>>>>> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            show_my_ip()
        elif choice == 2:
            password_generator()
        elif choice == 3:
            wordlist_generator()
        elif choice == 4:
            barcode_generator()
        elif choice == 5:
            qrcode_generator()
        elif choice == 6:
            phone_number_info()
        elif choice == 7:
            subdomain_scanner()
        elif choice == 8:
            port_scanner()
        elif choice == 9:
            ddos_attack()
        elif choice == 10:
            admin_panel_finder()
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Option not implemented yet. Try again!")

if __name__ == "__main__":
    main_menu()
