import requests
import socket
import json

BANNER = """
❄️ LUXA OSINT PRO TOOL ❄️
-------------------------
Secure Open Source Intelligence Tool
"""

def ip_lookup(ip):
    try:
        return requests.get(f"http://ip-api.com/json/{ip}").json()
    except:
        return {"error": "ip lookup failed"}

def dns_lookup(domain):
    try:
        return {"A": socket.gethostbyname(domain)}
    except:
        return {"error": "invalid domain"}

def run():
    print(BANNER)

    target = input("Enter domain or IP: ")

    result = {
        "LUXA": target,
        "IP_INFO": ip_lookup(target),
        "DNS_INFO": dns_lookup(target)
    }

    print("\n=== LUXA RESULT ===\n")
    print(json.dumps(result, indent=4))

    with open("LUXA_REPORT.json", "w") as f:
        json.dump(result, f, indent=4)

    print("\nSaved -> LUXA_REPORT.json")

if __name__ == "__main__":
    run()
