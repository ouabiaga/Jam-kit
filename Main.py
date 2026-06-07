from colorama import Fore, Back, Style, init
import os
import sys
import time
    
from Deauth_Attach import deauth_attack
from WifiJammer import wifi_jammer


init(autoreset=True)

def menu():
    while True:
        try:

            os.system('cls' if os.name == 'nt' else 'clear')
            print(r"""
It is a crime to use this tool on systems you do not have permission to use. If used, Serpten is not responsible.
Use for legal purposes.""")
            i=input()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.CYAN + "==========================================")
            print(Fore.CYAN + "         JAM-KIT: WIRELESS AUDIT KIT      ")
            print(Fore.CYAN + "==========================================")
            print(Fore.WHITE + "1- Wi-Fi Deauth (Targeted)")
            print(Fore.WHITE + "2- Wi-Fi Jammer (Broadcast)")
            print(Fore.RED +   "3- Exit")
            print(Fore.GREEN +   "             writed by serpten")
            print(Fore.CYAN + "==========================================")
            

            user_input = input(Fore.YELLOW + "Enter process number: ").strip()
            
            if user_input == "1":
                deauth_attack()
                input(Fore.YELLOW + "\nPress Enter to return to menu...")
            elif user_input == "2":
                wifi_jammer()
                input(Fore.YELLOW + "\nPress Enter to return to menu...")
            elif user_input == "3":
                print(Fore.RED + "\n[-] Exiting Jam-Kit. Goodbye!")
                sys.exit()
            else:
                print(Fore.RED + "\n[-] Invalid selection! Please enter 1, 2, or 3.")
                time.sleep(2) 
        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[-] Program interrupted. Exiting...")
            sys.exit()
        except Exception as e:
            print(Fore.RED + f"\n[-] An error occurred: {e}")
            input(Fore.YELLOW + "Press Enter to continue...")


print(Fore.RED + r"""
       _                             _  ___ _     _______          _ 
      | |                           | |/ (_) |   |__   __|        | |
      | | __ _ _ __ ___   ___ _ __  | ' / _| |_     | | ___   ___ | |
  _   | |/ _` | '_ ` _ \ / _ \ '__| |  < | | __|    | |/ _ \ / _ \| |
 | |__| | (_| | | | | | |  __/ |    | . \| | |_     | | (_) | (_) | |
  \____/ \__,_|_| |_| |_|\___|_|    |_|\_\_|\__|    |_|\___/ \___/|_|                                                                   
""")
print(Style.RESET_ALL)


import time
time.sleep(2)

menu()
