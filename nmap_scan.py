import subprocess

def scan(target):
    print(f"Scanning {target} with Nmap...")

    result = subprocess.run(
        ["nmap", "-F", target],
        capture_output=True,
        text=True
    )

    print(result.stdout)

if __name__ == "__main__":
    target = input("Target IP/Domain: ")
    scan(target)
import subprocess

def whois(domain):
    result = subprocess.run(["whois", domain], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    domain = input("Domain: ")
    whois(domain)
import socket

def dns(domain):
    try:
        print("A record:", socket.gethostbyname(domain))
    except:
        print("DNS lookup failed")

if __name__ == "__main__":
    domain = input("Domain: ")
    dns(domain)import requests

def ip_info(ip):
    data = requests.get(f"http://ip-api.com/json/{ip}").json()
    print(data)

if __name__ == "__main__":
    ip = input("IP: ")
    ip_info(ip)# simple helper (opens reverse image search)
import webbrowser

img = input("Image URL: ")
webbrowser.open(f"https://images.google.com/searchbyimage?image_url={img}")import socket

def check(host, port):
    s = socket.socket()
    s.settimeout(2)

    try:
        s.connect((host, int(port)))
        print(f"Port {port} OPEN")
    except:
        print(f"Port {port} CLOSED")
    finally:
        s.close()

if __name__ == "__main__":
    host = input("Host: ")
    port = input("Port: ")
    check(host, port)import os

print("""
❄️ LUXA OSINT MENU ❄️
1. Nmap Scan
2. WHOIS Lookup
3. DNS Lookup
4. IP Info
5. Port Check
""")

choice = input("Select: ")

if choice == "1":
    os.system("python3 nmap_scan.py")
elif choice == "2":
    os.system("python3 whois_lookup.py")
elif choice == "3":
    os.system("python3 dns_enum.py")
elif choice == "4":
    os.system("python3 ip_geo.py")
elif choice == "5":
    os.system("python3 port_checker.py")
