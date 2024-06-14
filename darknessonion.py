import os
import shutil
import subprocess

from colorama import Fore, Style

tamerrorsay = 0
tamothersay = 0
secreterrorsay = 0
tam = 0
other = 0
secret = 0

def kontrol(hostnamefile, errorsay):
    if os.path.exists(hostnamefile):
        with open(hostnamefile, "r") as readfile:
            readhostname = readfile.read()
            print("\n")
            print(Fore.RED)
            print("Onion Link: " + readhostname)
            print(Style.RESET_ALL)
    elif errorsay == 0:
        errorsay = 1
        getlink()
    elif errorsay == 1:
        errorsay = 2
        getlink()
    else:
        errorsay = 0
        if os.path.exists(hostnamefile):
            with open(hostnamefile, "r") as readfile:
                readhostname = readfile.read()
                print("\n")
                print(Fore.RED)
                print("Onion Link: " + readhostname)
                print(Style.RESET_ALL)
        else:
            print("Try Again - hidden_service folder or hostname file was not found This error is not about us")


def otherkontrol(hostnamefile, errorsay):
    if os.path.exists(hostnamefile):
        with open(hostnamefile, "r") as readfile:
            readhostname = readfile.read()
            print("\n")
            print(Fore.RED)
            print("Onion Link: " + readhostname)
            print(Style.RESET_ALL)
    elif errorsay == 0:
        errorsay = 1
        othergetlink()
    elif errorsay == 1:
        errorsay = 2
        othergetlink()
    else:
        errorsay = 0
        if os.path.exists(hostnamefile):
            with open(hostnamefile, "r") as readfile:
                readhostname = readfile.read()
                print("\n")
                print(Fore.RED)
                print("Other Onion Link: " + readhostname)
                print(Style.RESET_ALL)
        else:
            print("Try Again - other_hidden_service folder or hostname file was not found This error is not about us")


def secretkontrol(hostnamefile, errorsay):
    if os.path.exists(hostnamefile):
        with open(hostnamefile, "r") as readfile:
            readhostname = readfile.read()
            print("\n")
            print(Fore.RED)
            print("Onion Link: " + readhostname)
            print(Style.RESET_ALL)
    elif errorsay == 0:
        errorsay = 1
        getlink()
    elif errorsay == 1:
        errorsay = 2
        getlink()
    else:
        errorsay = 0
        if os.path.exists(hostnamefile):
            with open(hostnamefile, "r") as readfile:
                readhostname = readfile.read()
                print("\n")
                print(Fore.RED)
                print("Secret Onion Link: " + readhostname)
                print(Style.RESET_ALL)
        else:
            print("Try Again - secret_hidden_service folder or hostname file was not found This error is not about us")


def getlink():
    torconfig = "configtor.txt"

    if os.path.exists("/etc/tor/torrc"):

        with open("/etc/tor/torrc", "w") as file, open(torconfig, "r") as readfile:
            read = readfile.readlines()
            for line in read:
                file.write(line)

        subprocess.run(["service", "tor", "stop"], stderr=subprocess.DEVNULL)
        subprocess.run(["service", "tor", "start"], stderr=subprocess.DEVNULL)

        process = subprocess.run(["dpkg", "-s", "nginx"], stdout=subprocess.DEVNULL)
        if process.returncode != 0:
            print("You need a web server for your Onion connection to work. That's why Nginx is installing")
            print("\n")
            subprocess.run(["apt", "install", "nginx"], input=b"y", stdout=subprocess.DEVNULL)

        subprocess.run(["service", "tor", "stop"], stderr=subprocess.DEVNULL)
        subprocess.run(["service", "tor", "start"], stderr=subprocess.DEVNULL)
        fullhostnamefile = "/var/lib/tor/hidden_service/hostname"
        global tamerrorsay
        kontrol(fullhostnamefile, tamerrorsay)


    else:
        print("/etc/tor/torrc not found! Please start the program as sudo or install Tor. 1) sudo apt install tor -y"
              " 2) sudo python3 dark-onion" "Also, for a reason not caused by us, the program does not work in Tails "
              " and Whonix.")


def othergetlink():
    torconfig = "configtor2.txt"

    if os.path.exists("/etc/tor/torrc"):

        with open("/etc/tor/torrc", "w") as file, open(torconfig, "r") as readfile:
            for line in readfile.readlines():
                file.write(line)


        subprocess.run(["service", "tor", "stop"], stderr=subprocess.DEVNULL)
        subprocess.run(["service", "tor", "start"], stderr=subprocess.DEVNULL)

        process = subprocess.run(["dpkg", "-s", "nginx"], stdout=subprocess.DEVNULL)
        if process.returncode != 0:
            print("You need a web server for your Onion connection to work. That's why Nginx is installing")
            print("\n")
            subprocess.run(["apt", "install", "nginx"], input=b"y", stdout=subprocess.DEVNULL)

        subprocess.run(["service", "tor", "stop"], stderr=subprocess.DEVNULL)
        subprocess.run(["service", "tor", "start"], stderr=subprocess.DEVNULL)
        fullhostnamefile = "/var/lib/tor/other_hidden_service/hostname"
        global tamothersay
        otherkontrol(fullhostnamefile, tamothersay)



    else:
        print("/etc/tor/torrc not found Please start the program as sudo or install Tor. 1) sudo apt install tor -y"
              " 2) sudo python3 darknessonion.py" "Also, for a reason not caused by us, the program does not work in "
              "Tails"
              " and Whonix.")


def secretgetlink():
    torconfig = "configtor3.txt"

    if os.path.exists("/etc/tor/torrc"):

        with open("/etc/tor/torrc", "w") as file, open(torconfig, "r") as readfile:
            for line in readfile.readlines():
                file.write(line)


        subprocess.run(["service", "tor", "stop"], stderr=subprocess.DEVNULL)
        subprocess.run(["service", "tor", "start"], stderr=subprocess.DEVNULL)

        process = subprocess.run(["dpkg", "-s", "nginx"], stdout=subprocess.DEVNULL)
        if process.returncode != 0:
            print("You need a web server for your Onion connection to work. That's why Nginx is installing")
            print("\n")
            subprocess.run(["apt", "install", "nginx"], input=b"y", stdout=subprocess.DEVNULL)

        subprocess.run(["service", "tor", "stop"], stderr=subprocess.DEVNULL)
        subprocess.run(["service", "tor", "start"], stderr=subprocess.DEVNULL)
        fullhostnamefile = "/var/lib/tor/secret_hidden_service/hostname"
        global secreterrorsay
        secretkontrol(fullhostnamefile, secreterrorsay)


    else:
        print("/etc/tor/torrc not found! Please start the program as sudo or install Tor. 1) sudo apt install tor -y"
              " 2) sudo python3 dark-onion" "Also, for a reason not caused by us, the program does not work in Tails "
              " and Whonix.")


def newlink(deletehidden, error, message, selectlink):
    if os.path.exists(deletehidden):
        shutil.rmtree(deletehidden)
        selectlink()
    elif error == 0:
        error = 1
        selectlink()
    elif error == 1:
        error = 2
        selectlink()
    else:
        error = 0
        print(message)

def newgetlink():
    newlink("/var/lib/tor/hidden_service", tam, "hidden_service folder file not found. Try option 1 first", getlink)


def othernewgetlink():
    newlink("/var/lib/tor/other_hidden_service", other, "other_hidden_service folder file not found. Try option 2 first", othergetlink)


def secretnewgetlink():
    newlink("/var/lib/tor/secret_hidden_service", secret, "secret_hidden_service folder file not found. Try option 3 first", secretgetlink)



if __name__ == '__main__':
    os.system('clear')
    print(Fore.RED)
    ard = """                                                                                                                                               
    ██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ██╗███████╗███████╗███████╗     ██████╗ ███╗   ██╗██╗ ██████╗ ███╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝████╗  ██║██╔════╝██╔════╝██╔════╝    ██╔═══██╗████╗  ██║██║██╔═══██╗████╗  ██║
    ██║  ██║███████║██████╔╝█████╔╝ ██╔██╗ ██║█████╗  ███████╗███████╗    ██║   ██║██╔██╗ ██║██║██║   ██║██╔██╗ ██║
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║╚██╗██║██╔══╝  ╚════██║╚════██║    ██║   ██║██║╚██╗██║██║██║   ██║██║╚██╗██║
    ██████╔╝██║  ██║██║  ██║██║  ██╗██║ ╚████║███████╗███████║███████║    ╚██████╔╝██║ ╚████║██║╚██████╔╝██║ ╚████║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                                                               
     """

    print(ard)
    print(Style.RESET_ALL)

    print("\n")

    print(Fore.LIGHTBLUE_EX + "[1] Get Onion Link" + Style.RESET_ALL + "\n")

    print(Fore.MAGENTA + "[2] Get Other Onion Link" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTGREEN_EX + "[3] Get Secret Onion Link" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTBLUE_EX + "[4] Get New Onion Link (First Onion Link Disappears)" + Style.RESET_ALL + "\n")

    print(Fore.MAGENTA + "[5] Get Other New Onion Links (Other Onion Link Disappears)" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTGREEN_EX + "[6] Get Secret New Onion Links (Secret Onion Link Disappears)" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTYELLOW_EX + "[7] How to Edit Website?" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTCYAN_EX + "[8] Onion Links Error Codes" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTWHITE_EX + "[9] Exit" + Style.RESET_ALL + "\n")

    while True:
        try:
            print(" ")
            secim = int(input(">"))

            if secim == 1:
                print("")
                getlink()

            elif secim == 2:
                print("")
                othergetlink()

            elif secim == 3:
                print("")
                secretgetlink()

            elif secim == 4:
                print("")
                newgetlink()

            elif secim == 5:
                print("")
                othernewgetlink()

            elif secim == 6:
                print("")
                secretnewgetlink()

            elif secim == 7:
                print("")
                print(
                    "For HTML file, open the file under /var/www/html folder as administrator. Ex: sudo nano "
                    "/var/www/html/index.nginx-debian.html")

            elif secim == 8:
                print("")
                print("https://tb-manual.torproject.org/onion-services/")

            elif secim == 9:
                break


        except ValueError:
            print("")
