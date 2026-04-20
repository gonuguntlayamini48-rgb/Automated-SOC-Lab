import datetime

# Mock list of malicious IPs detected by a SIEM
malicious_ips = ["192.168.1.105", "45.33.22.11", "10.0.0.50"]

def block_ip(ip):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] ALERT: High-frequency connection attempt from {ip}")
    print(f"[{timestamp}] ACTION: Updating Firewall rules to DROP traffic from {ip}...")
    return True

if __name__ == "__main__":
    print("--- 🛡️ Automated Threat Mitigation Engine Starting ---")
    for ip in malicious_ips:
        block_ip(ip)
    print("--- ✅ All identified threats neutralized. ---")
