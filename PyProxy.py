import os
import requests
from bs4 import BeautifulSoup as bs

Siyah = "\033[30m"
Kırmızı = "\033[31m"
Yeşil = "\033[32m"
Sarı = "\033[33m"
Mavi = "\033[34m"
Mor = "\033[35m"
Cyan = "\033[36m"
Reset = "\033[0m"

def clear_screen():
    os.system('clear')

def print_banner():
    banner = """
\033[33m
                    ██████████
                  ██░░░░░░░░░░██
                ██░░░░░░░░░░░░░░██
                ██░░░░░░░░████░░██████████
    ██          ██░░░░░░░░████░░██▒▒▒▒▒▒██
  ██░░██        ██░░░░░░░░░░░░░░██▒▒▒▒▒▒██
  ██░░░░██      ██░░░░░░░░░░░░░░████████
  ██░░░░░░██      ██░░░░░░░░░░░░██
██░░░░░░░░████████████░░░░░░░░██
██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░██
  ██████░░░░░░░░░░░░░░░░████
        ████████████████
\033[36m
██████╗░██╗░░░██╗██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝
██████╔╝░╚████╔╝░██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░
██╔═══╝░░░╚██╔╝░░██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░
██║░░░░░░░░██║░░░██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░
╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
\033[31m[ + ] Instagram: \033[32mcoderfenrir\033[0m
\033[31m[ + ] Github: \033[32mcoderfenrir\033[0m
\033[31m[ + ] Version: \033[32m1.2\033[0m
"""
    print(banner)

def get_proxy(URL, file_name):
    r = requests.get(URL)
    s = bs(r.content, "html.parser")

    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} Zaten mevcut. Eski dosya kaldırıldı.")

    with open(file_name, "w") as f:
        f.write(s.text)
        print(f"{file_name} kaydedildi!")

clear_screen()
print_banner()

while True:
    print("\033[35mSeçeneklerden birini girin [ↆ]\033[0m")
    print("")
    user_input = input("http/socks4/socks5: ")

    if user_input.lower() in ["http", "socks4", "socks5"]:
        get_proxy(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={user_input.lower()}&timeout=10000&country=all&ssl=all&anonymity=all", f"{user_input.lower()}.txt")
    else:
        print("Geçersiz komut. Lütfen 'http', 'socks4', or 'socks5'.")
