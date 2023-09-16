import os
import subprocess

def scan_wifi_networks():
    try:
        # Use subprocess to run the 'iwlist' command to scan for Wi-Fi networks
        wifi_scan_results = subprocess.check_output(["iwlist", "wlan0", "scan"])
        wifi_scan_results = wifi_scan_results.decode("utf-8")

        # Extract and display the list of available Wi-Fi networks
        networks = []
        lines = wifi_scan_results.split("\n")
        for line in lines:
            if "ESSID:" in line:
                network = line.strip().split('"')[1]
                networks.append(network)

        print("Available Wi-Fi networks:")
        for network in networks:
            print(network)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    scan_wifi_networks()
