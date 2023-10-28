import requests
from pyfiglet import Figlet
import folium
import socket
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Define ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def get_phone_info(phone_number):
    num = phonenumbers.parse(phone_number)
    Carrier = carrier.name_for_number(num, 'en')
    Region = geocoder.description_for_number(num, 'en')
    Valid = phonenumbers.is_possible_number(num)
    Possible = phonenumbers.is_possible_number(num)
    timeZone = timezone.time_zones_for_number(num)

    print(f"{Colors.BLUE}[Phone Number]: {Colors.RESET}{phone_number}")
    print(f"{Colors.BLUE}[Is Valid]: {Colors.RESET}{Valid}")
    print(f"{Colors.BLUE}[Is Possible]: {Colors.RESET}{Possible}")
    print(f"{Colors.BLUE}[Carrier]: {Colors.RESET}{Carrier}")
    print(f"{Colors.BLUE}[Region]: {Colors.RESET}{Region}")
    print(f"{Colors.BLUE}[Time Zones]: {Colors.RESET}{' '.join(timeZone)}")

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            f'{Colors.BLUE}[IP]{Colors.RESET}': response.get('query'),
            f'{Colors.BLUE}[Int prov]{Colors.RESET}': response.get('isp'),
            f'{Colors.BLUE}[Org]{Colors.RESET}': response.get('org'),
            f'{Colors.BLUE}[Country]{Colors.RESET}': response.get('country'),
            f'{Colors.BLUE}[Region Name]{Colors.RESET}': response.get('regionName'),
            f'{Colors.BLUE}[City]{Colors.RESET}': response.get('city'),
            f'{Colors.BLUE}[ZIP]{Colors.RESET}': response.get('zip'),
            f'{Colors.BLUE}[Lat]{Colors.RESET}': response.get('lat'),
            f'{Colors.BLUE}[Lon]{Colors.RESET}': response.get('lon'),
        }

        for k, v in data.items():
            print(k, v)

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print(f'{Colors.RED}[!] Please check your connection!{Colors.RESET}')

def get_ip_by_hostname():
    hostname = input(f'{Colors.YELLOW}Please enter a website address (URL): {Colors.RESET}')
    try:
        ip = socket.gethostbyname(hostname)
        return f'\nHostname: {hostname}\nIP address: {ip}'
    except socket.gaierror as error:
        return f'\nInvalid Hostname - {error}'

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

def check_twitter(username):
    url = f"https://twitter.com/{username}"
    headers = {"User-Agent": USER_AGENT}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 404 or "Page not found" in response.text:
            return False
        else:
            return url
    except Exception as e:
        print(f"Error checking Twitter: {e}")
        return None

def check_tiktok(username):
    url = f"https://www.tiktok.com/@{username}"

    try:
        response = requests.head(url, allow_redirects=False, timeout=5)
        if response.status_code == 404 or response.headers.get("Location") == "https://www.tiktok.com/foryou":
            return False
        else:
            return url
    except Exception as e:
        print(f"Error checking Tiktok: {e}")
        return None

def check_instagram(username):
    url = f"https://www.instagram.com/{username}"

    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=5)
        if response.status_code == 404 or "Page Not Found" in response.text:
            return False
        else:
            return url
    except Exception as e:
        print(f"Error checking Instagram: {e}")
        return None

def check_twitch(username):
    url = f"https://www.twitch.tv/{username}"

    try:
        response = requests.head(url, allow_redirects=False, timeout=5)
        if response.status_code == 404 or response.headers.get("Location") == "https://www.twitch.tv/directory/following":
            return False
        else:
            return url
    except Exception as e:
        print(f"Error checking Twitch: {e}")
        return None

def check_spotify(username):
    url = f"https://open.spotify.com/search/{username}"

    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=5)
        if username not in response.text:
            return False
        else:
            return url
    except Exception as e:
        print(f"Error checking Spotify: {e}")
        return None

def check_github(username):
    url = f"https://github.com/{username}"

    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=5)
        if response.status_code == 404:
            return False
        else:
            return url
    except:
        print(f"Error checking Github for {username}")
        return None

# Pinterest check
def check_pinterest(username):
    url = f"https://www.pinterest.com/{username}"

    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=5)
        if response.status_code == 404 or "Page Not Found" in response.text:
            return False
        else:
            return url
    except:
        print(f"Error checking Pinterest for {username}")
        return None

def check_onlyfans(username):
    url = f"https://onlyfans.com/{username}"

    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=5)
        if response.status_code == 404:
            return False
        else:
            return url
    except:
        print(f"Error checking OnlyFans for {username}")
        return None

def check_pornhub(username):
  url = f"https://rt.pornhub.com/{username}"

  try:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=5)
    if response.status_code == 404:
      return False
    else:
      return url
  except:
    print(f"Error checking Pornhub for {username}")
    return None

def main():
    while True:
        print(f'{Colors.GREEN}{Figlet(font="slant").renderText("HESUDA")}{Colors.RESET}')

        print(f'\n{Colors.YELLOW}Menu:{Colors.RESET}')
        print("1. IP Lookup")
        print("2. Hostname to IP Lookup")
        print("3. Phone number Lookup")
        print("4. Discord Support")
        print("5. Social Media Profiles Lookup")
        print("6. Exit")
        choice = input(f"{Colors.YELLOW}Enter your choice (1/2/3/4/5/6): {Colors.RESET}")

        if choice == '1':
            ip = input(f'{Colors.YELLOW}Please enter a target IP: {Colors.RESET}')
            print(get_info_by_ip(ip=ip))
        elif choice == '2':
            print(get_ip_by_hostname())
        elif choice == '3':
            phone_number = input(f'{Colors.YELLOW}Please enter a phone number (with country code): {Colors.RESET}')
            get_phone_info(phone_number)
        elif choice == '4':
            print("discord support: https://discord.gg/FfQ3FRNV")
        elif choice == '5':
            username = input("Enter username: ")
            pornhub = check_pornhub(username)
            onlyfans = check_onlyfans(username)
            twitter = check_twitter(username)
            tiktok = check_tiktok(username)
            instagram = check_instagram(username)
            twitch = check_twitch(username)
            spotify = check_spotify(username)
            github = check_github(username)
            pinterest = check_pinterest(username)

            if twitter:
                print("Twitter:", twitter)
            else:
                print(f"Twitter profile '{username}' does not exist")

            if tiktok:
                print("TikTok:", tiktok)
            else:
                print(f"TikTok profile '{username}' does not exist")

            if instagram:
                print("Instagram:", instagram)
            else:
                print(f"Instagram profile '{username}' does not exist")

            if twitch:
                print("Twitch:", twitch)
            else:
                print(f"Twitch profile '{username}' does not exist")

            if spotify:
                print("Spotify:", spotify)
            else:
                print(f"Spotify profile '{username}' does not exist")

            if github:
                print(f"GitHub: {github}")
            else:
                print(f"GitHub profile '{username}' does not exist")

            if pinterest:
                print(f"Pinterest: {pinterest}")
            else:
                print(f"Pinterest profile '{username}' does not exist")

            if onlyfans:
                print(f"OnlyFans: {onlyfans}")
            else:
                print(f"OnlyFans profile '{username}' does not exist")

            if pornhub:
                print(f"Pornhub: {pornhub}")
            else:
                print(f"Pornhub profile '{username}' does not exist")
        elif choice == '6':
            print(f"{Colors.YELLOW}Goodbye!{Colors.RESET}")
            break
        else:
            print(f'{Colors.RED}Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.{Colors.RESET}')

if __name__ == '__main__':
    art = [
        "⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠊⠉⠉⠉⠉⢉⠝⠉⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⢀⡴⣋⠀⠀⣤⣒⡠⢀⠀⠐⠂⠀⠤⠤⠈⠓⢦⡀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⣰⢋⢬⠀⡄⣀⠤⠄⠀⠓⢧⠐⠥⢃⣴⠤⣤⠀⢀⡙⣆⠀⠀⠀⠀",
        "⠀⠀⠀⠀⢠⡣⢨⠁⡘⠉⠀⢀⣤⡀⠀⢸⠀⢀⡏⠑⠢⣈⠦⠃⠦⡘⡆⠀⠀⠀",
        "⠀⠀⠀⠀⢸⡠⠊⠀⣇⠀⠀⢿⣿⠇⠀⡼⠀⢸⡀⠠⣶⡎⠳⣸⡠⠃⡇⠀⠀⠀",
        "⢀⠔⠒⠢⢜⡆⡆⠀⢿⢦⣤⠖⠒⢂⣽⢁⢀⠸⣿⣦⡀⢀⡼⠁⠀⠀⡇⠒⠑⡆",
        "⡇⠀⠐⠰⢦⠱⡤⠀⠈⠑⠪⢭⠩⠕⢁⣾⢸⣧⠙⡯⣿⠏⠠⡌⠁⡼⢣⠁⡜⠁",
        "⠈⠉⠻⡜⠚⢀⡏⠢⢆⠀⠀⢠⡆⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⣼⠾⢬⣹⡾⠀⠀",
        "⠀⠀⠀⠉⠀⠉⠀⠀⠈⣇⠀⠀⠀⣴⡟⢣⣀⡔⡭⣳⡈⠃⣼⠀⠀⠀⣼⣧⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⣸⣿⣿⣿⡿⣷⣿⣿⣷⠀⡇⠀⠀⠀⠙⠊⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣠⠀⢻⠛⠭⢏⣑⣛⣙⣛⠏⠀⡇⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠠⠜⠓⠉⠉⠀⠐⢒⡒⡍⠐⡇⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠢⠤⣀⣀⣀⣀⣘⠧⠤⠞⠁"
    ]

    for line in art:
        print(f"{Colors.GREEN}{line}{Colors.RESET}")

    main()
