import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]  # Use the first available wireless interface

iface.scan()
scan_results = iface.scan_results()

for result in scan_results:
    ssid = result.ssid
    profile = iface.profile(ssid)
    
    if profile is not None:
        key = profile.key
        print(f"SSID: {ssid}, Password: {key}")
    else:
        print(f"SSID: {ssid}, Password not found")
