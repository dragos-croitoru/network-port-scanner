# Network & Port Scanner

A simple TCP network and port scanner built with Python.

This project was created to practice Python programming, TCP/IP networking, and basic cybersecurity concepts.

## Features

- Scan a range of IPv4 addresses
- Scan a custom range of TCP ports
- Detect open TCP ports
- Identify common services running on open ports
- Configure connection timeout

## Technologies

- Python
- Python `socket` module
- TCP/IP
- IPv4

## How It Works

The scanner generates IP addresses from the network and host range provided by the user.

For each IP address, it attempts a TCP connection to every port in the selected range using Python's `socket` module.

If the connection succeeds, the port is displayed as open and the scanner attempts to identify the associated service.

## Usage

Run the scanner:

```bash
python scanner.py
```

Enter the network and the ranges you want to scan:

```text
Enter the network: 192.168.1
Enter the last number of the starting IP: 1
Enter the last number of the ending IP: 10
Enter the starting port: 20
Enter the ending port: 100
```

## Example Output

```text
=== NETWORK & PORT SCANNER ===

Scanning IP: 192.168.1.1
  [OPEN] Port 80 -> http

Scanning IP: 192.168.1.2
  [OPEN] Port 22 -> ssh

Scan completed.
```

## Limitations

- Supports IPv4 networks using the current `/24`-style input format
- Performs TCP connect scans only
- Scanning is sequential and may be slow for large ranges
- Service identification is based on standard port mappings

## Future Improvements

- Multithreading for faster scanning
- Improved IP address validation
- Export scan results to a file
- Command-line arguments

## Disclaimer

This project is intended for educational purposes and authorized security testing only. Only scan systems and networks you own or have permission to test.
