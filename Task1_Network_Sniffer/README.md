# Task 1 - Network Sniffer

## CodeAlpha Cybersecurity Internship

## 📌 Objective
Build a basic network sniffer using Python to capture and analyze live network traffic passing through the system. The tool identifies key details of each packet, including source and destination IP addresses, protocol type (TCP/UDP), and port numbers.

## 🛠️ Tools & Technologies
- **Language:** Python 3.14
- **Library:** Scapy
- **Driver:** Npcap (required on Windows for raw packet capture)

## ⚙️ How It Works
The script uses Scapy's `sniff()` function to capture live packets from the network interface. For every packet captured:
1. It checks whether the packet contains an IP layer.
2. It extracts the source IP and destination IP.
3. It checks whether the packet is TCP or UDP, and extracts the corresponding source/destination ports.
4. It prints this information in a clean, readable format.

## ▶️ How to Run
1. Install the required library:
   ```
   pip install scapy
   ```
2. On Windows, install [Npcap](https://npcap.com) with "WinPcap API-compatible Mode" enabled.
3. Run the script (Administrator terminal recommended):
   ```
   python sniffer.py
   ```

## 📄 Code
```python
from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")

        if packet.haslayer(TCP):
            print(f"Protocol: TCP | Src Port: {packet[TCP].sport} | Dst Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"Protocol: UDP | Src Port: {packet[UDP].sport} | Dst Port: {packet[UDP].dport}")

        print("-" * 50)

sniff(prn=process_packet, count=10)
```

## 📊 Sample Output
```
Source IP: 192.168.10.37 -> Destination IP: 20.184.175.2
Protocol: TCP | Src Port: 51677 | Dst Port: 443
--------------------------------------------------
Source IP: 192.168.10.1 -> Destination IP: 192.168.10.37
Protocol: UDP | Src Port: 53 | Dst Port: 57942
--------------------------------------------------
```

## 🔍 Key Learnings
- How packets are structured in layers (Ethernet → IP → TCP/UDP)
- The difference between TCP (reliable, connection-based) and UDP (fast, connectionless)
- How ports identify which application/service traffic belongs to
- How to trace traffic back to its origin using IP WHOIS lookups
- Real-world network sniffing requires OS-level driver support (Npcap on Windows)

## ⚠️ Disclaimer
This tool was built strictly for educational purposes as part of the CodeAlpha Cybersecurity Internship, and was tested only on my own local network traffic.
