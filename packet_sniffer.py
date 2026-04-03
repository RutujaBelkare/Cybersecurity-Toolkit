from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

def start_sniffer():
    print("Sniffing started...")
    sniff(prn=process_packet, count=10)
