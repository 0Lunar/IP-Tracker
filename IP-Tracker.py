import os, src.banner, src.iptrack, src.help
try:
    import requests
    from colorama import Fore
except:
    print("first install the requirements")

if __name__ == "__main__":
    os.system("cls||clear")
    option = ""
    src.banner.banner()
    while(option != 4):
        try:
            option = int(input(Fore.RED + "\n Track ==> "))
            if(option == 1):
                myip = requests.get("https://api.ipify.org").text
                src.iptrack.ip(myip)
            elif(option == 2):
                ipaddr = input("   |\n   -- Enter the ip address ==> ")
                src.iptrack.ip(ipaddr)
            elif(option == 3):
                src.help.help()
        except ValueError:
            print("\n Error. only int value")
        except requests.exceptions.ConnectionError:
            print("\n you are offilne")
        except KeyboardInterrupt:
            break;
    print("\n Bye :)")