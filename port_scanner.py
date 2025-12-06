import socket

def scan_port(ip, port, timeout=0.5):
    """Return True if port is open, False if closed/unreachable."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((ip, port))  # 0 = success
    s.close()
    return result == 0

def main():
    print("Simple Port Scanner")
    print("Only use this on localhost (127.0.0.1) or scanme.nmap.org")
    print()

    host = input("Enter host (127.0.0.1, localhost, or scanme.nmap.org): ").strip()

    # Resolve the host name to an IP address
    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Could not resolve host. Check the name and try again.")
        return

    # Ask for a port range
    start_str = input("Enter start port (e.g., 20): ").strip()
    end_str = input("Enter end port (e.g., 1024): ").strip()

    # Validate input
    try:
        start_port = int(start_str)
        end_port = int(end_str)
    except ValueError:
        print("Port numbers must be integers.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Ports must be between 1 and 65535 and start <= end.")
        return

    print(f"\nScanning {host} ({target_ip}) from port {start_port} to {end_port}...\n")

    # Scan each port
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

        s.close()

    print("\nScan finished.")

if __name__ == "__main__":
    main()