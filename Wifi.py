import subprocess
import re

# Get a list of available wireless profiles
profiles = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8')

# Use regular expressions to extract SSID names
ssid_list = re.findall(r'ESSID:"([^"]*)"', profiles)

for ssid in ssid_list:
    # Get the key for each SSID
    try:
        key_data = subprocess.check_output(['iwconfig', 'wlan0', 'essid', ssid, 'key', 's:']).decode('utf-8')
        key = re.search(r'key:([^"]*)', key_data).group(1)
        print("{:<30}| {:<}".format(ssid, key))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(ssid, "Key not found"))
