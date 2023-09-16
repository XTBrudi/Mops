from colorama import init, Style, Fore; init()
import random; import time; import sys
Fake_id = random.randint(19008,10090090)
HowManyUsersFound = random.randint(14,122)
IP_STARTS = ["192", "35", "33", "135", "77", "111", "155", "134", "136", "112", "94", "86", "30", "45", "54", "64", "46"]
PORTS = ["8080", "1111", "4040", "7777", "8888"]
PRIVATE = ["TRUE", "FALSE"]
n="IP_BUILD: 192.192.192.134:ROOT"


randomIP = f"{random.choice(IP_STARTS)}.{random.choice(IP_STARTS)}.{random.choice(IP_STARTS)}.{random.choice(IP_STARTS)}"


def main():
    print(f"{Fore.CYAN}[#] Scanning Networks. . .\n{Style.RESET_ALL}")
    time.sleep(random.randint(4,7))
    print(f"{Fore.GREEN}[+] Antennae found! {Fore.MAGENTA}(With id: {Fake_id}, Port: {random.choice(PORTS)}, Private = {random.choice(PRIVATE)}, IP: **.***.***.***:****){Style.RESET_ALL}")
    us_i = input(f"{Fore.YELLOW}[?] Do you wan't to continue with this Network? (Y/n): {Style.RESET_ALL}")
    if us_i == "Y":
        print(f"{Fore.GREEN}[+] Setting your root to http://su-root:localhost (Default: http://4433:localhost/anonym). . {Style.RESET_ALL}")
        time.sleep(random.randint(3,4))
        print(f"{Fore.GREEN}[+] Success. Scanning in Wifi/s for user/s.\n{Style.RESET_ALL}")
        time.sleep(random.randint(7,10))
        print(f"{Fore.GREEN}[+] Success. Total users found: {HowManyUsersFound}\n{Style.RESET_ALL}")
        for _ in range(HowManyUsersFound):
            ip = ".".join([random.choice(IP_STARTS) for _ in range(4)])
            print(f"{random.choice(PRIVATE)} / {random.randint(19008,10090090)} // {ip}")

    elif us_i == "n":
        us_i2 = input(f"{Fore.YELLOW}[?] Do You wan't to rescan (R) or exit (E)? (R/E): {Style.RESET_ALL}")
        if us_i2 == "E":
            sys.exit()
        elif us_i2 == "R":
            main()
        else:
            print(f"{Fore.YELLOW}[?] Unavaiable command. Exiting. . .{Style.RESET_ALL}")
            sys.exit()
    else:
        print(f"{Fore.RED}[!] Please use Y or n. Exiting. . .{Style.RESET_ALL}")
        sys.exit()


if __name__ == "__main__":
    main()
