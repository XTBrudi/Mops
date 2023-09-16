import subprocess
import re

# Run nmcli to list available Wi-Fi SSIDs
wifi_list = subprocess.run(["nmcli", "-t", "-f", "SSID", "device", "wifi"], capture_output=True, text=True).stdout.strip().split('\n')

wifi_profiles = []

for wifi_ssid in wifi_list:
    wifi_profile = {}
    wifi_profile["ssid"] = wifi_ssid
    
    # Run nmcli to retrieve the Wi-Fi password for the current SSID
    wifi_password = subprocess.run(["nmcli", "--show-secrets", "connection", "show", wifi_ssid], capture_output=True, text=True)
    
    # Extract the password using regular expressions
    password_match = re.search(r'802-11-wireless-security.psk: (.+)', wifi_password.stdout)
    if password_match:
        wifi_profile["password"] = password_match.group(1)
    else:
        wifi_profile["password"] = None
    
    wifi_profiles.append(wifi_profile)

# Print the list of Wi-Fi profiles and their passwords
for wifi_profile in wifi_profiles:
    print("SSID:", wifi_profile["ssid"])
    print("Password:", wifi_profile["password"])
    print("=" * 30)
