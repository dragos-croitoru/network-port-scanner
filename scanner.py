import socket


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "necunoscut"

        print(f"  [DESCHIS] Port {port} -> {service}")

    sock.close()


network = input("Introdu reteaua: ")

start_ip = int(input("Introdu ultimul numar al IP-ului de inceput: "))
end_ip = int(input("Introdu ultimul numar al IP-ului final: "))

start_port = int(input("Introdu portul de inceput: "))
end_port = int(input("Introdu portul final: "))

print("\n=== NETWORK & PORT SCANNER ===\n")

for host in range(start_ip, end_ip + 1):

    target = f"{network}.{host}"

    print(f"\nScanare IP: {target}")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)

print("\nScanarea s-a terminat.")