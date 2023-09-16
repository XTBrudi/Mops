import wifi

wifi_scan = wifi.scan()
for wifi_ssid in wifi_scan:
    print("SSID:", wifi_ssid.ssid)
    print("Signal Strength:", wifi_ssid.signal)
    print("Security:", wifi_ssid.sec)
    print()
