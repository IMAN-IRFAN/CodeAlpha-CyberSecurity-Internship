from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")

        if packet.haslayer(TCP):
            print(f"Protocol: TCP | Src Port: {packet[TCP].sport} | Dst Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"Protocol: UDP | Src Port: {packet[UDP].sport} | Dst Port: {packet[UDP].dport}")

        print("-" * 50)

sniff(prn=process_packet, count=10)