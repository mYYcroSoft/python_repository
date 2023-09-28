import uuid
import socket
import os

def get_network_interface_info():
    interfaces = []
    if os.name == "posix":  # Unix-based systems (Linux, macOS)
        with os.popen("ifconfig") as f:
            ifconfig_output = f.read()
        lines = ifconfig_output.split("\n\n")
        for line in lines:
            if "flags" in line and "RUNNING" in line:
                info = {}
                name = line.split(":")[0].strip()
                info["name"] = name
                mac = line.split("ether ")[1].split()[0]
                info["mac"] = mac
                interfaces.append(info)
    elif os.name == "nt":  # Windows
        for interface in uuid.getnode().to_bytes(6, 'big'):
            interfaces.append(interface)
    return interfaces

def main():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    network_interfaces = get_network_interface_info()

    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print("Network Interfaces:")
    for interface in network_interfaces:
        print(f"  Name: {interface.get('name')}, MAC Address: {interface.get('mac')}")

if __name__ == "__main__":
    main()
