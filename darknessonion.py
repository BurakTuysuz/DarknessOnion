import os
import shutil
import subprocess

from colorama import Fore, Style

tamerrorsay = 0
tamothersay = 0


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
                print("Onion Link: " + readhostname)
                print(Style.RESET_ALL)
        else:
            print("Try Again - other_hidden_service folder or hostname file was not found This error is not about us")


def getlink():
    torconfig = """## Configuration file for a typical Tor user
    ## Last updated 9 October 2013 for Tor 0.2.5.2-alpha.
    ## (may or may not work for much older or much newer versions of Tor.)
    ##
    ## Lines that begin with "## " try to explain what's going on. Lines
    ## that begin with just "#" are disabled commands: you can enable them
    ## by removing the "#" symbol.
    ##
    ## See 'man tor', or https://www.torproject.org/docs/tor-manual.html,
    ## for more options you can use in this file.
    ##
    ## Tor will look for this file in various places based on your platform:
    ## https://www.torproject.org/docs/faq#torrc

    ## Tor opens a socks proxy on port 9050 by default -- even if you don't
    ## configure one below. Set "SocksPort 0" if you plan to run Tor only
    ## as a relay, and not make any local application connections yourself.
    #SocksPort 9050 # Default: Bind to localhost:9050 for local connections.
    #SocksPort 192.168.0.1:9100 # Bind to this address:port too.

    ## Entry policies to allow/deny SOCKS requests based on IP address.
    ## First entry that matches wins. If no SocksPolicy is set, we accept
    ## all (and only) requests that reach a SocksPort. Untrusted users who
    ## can access your SocksPort may be able to learn about the connections
    ## you make.
    #SocksPolicy accept 192.168.0.0/16
    #SocksPolicy reject *

    ## Logs go to stdout at level "notice" unless redirected by something
    ## else, like one of the below lines. You can have as many Log lines as
    ## you want.
    ##
    ## We advise using "notice" in most cases, since anything more verbose
    ## may provide sensitive information to an attacker who obtains the logs.
    ##
    ## Send all messages of level 'notice' or higher to /var/log/tor/notices.log
    #Log notice file /var/log/tor/notices.log
    ## Send every possible message to /var/log/tor/debug.log
    #Log debug file /var/log/tor/debug.log
    ## Use the system log instead of Tor's logfiles
    #Log notice syslog
    ## To send all messages to stderr:
    #Log debug stderr

    ## Uncomment this to start the process in the background... or use
    ## --runasdaemon 1 on the command line. This is ignored on Windows;
    ## see the FAQ entry if you want Tor to run as an NT service.
    #RunAsDaemon 1

    ## The directory for keeping all the keys/etc. By default, we store
    ## things in $HOME/.tor on Unix, and in Application Data\tor on Windows.
    #DataDirectory /var/lib/tor

    ## The port on which Tor will listen for local connections from Tor
    ## controller applications, as documented in control-spec.txt.
    #ControlPort 9051
    ## If you enable the controlport, be sure to enable one of these
    ## authentication methods, to prevent attackers from accessing it.
    #HashedControlPassword 16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C
    #CookieAuthentication 1

    ############### This section is just for location-hidden services ###

    ## Once you have configured a hidden service, you can look at the
    ## contents of the file ".../hidden_service/hostname" for the address
    ## to tell people.
    ##
    ## HiddenServicePort x y:z says to redirect requests on port x to the
    ## address y:z.

    HiddenServiceDir /var/lib/tor/hidden_service/
    HiddenServicePort 80 127.0.0.1:80

    #HiddenServiceDir /var/lib/tor/other_hidden_service/
    #HiddenServicePort 80 127.0.0.1:80
    #HiddenServicePort 22 127.0.0.1:22

    ################ This section is just for relays #####################
    #
    ## See https://www.torproject.org/docs/tor-doc-relay for details.

    ## Required: what port to advertise for incoming Tor connections.
    #ORPort 9001
    ## If you want to listen on a port other than the one advertised in
    ## ORPort (e.g. to advertise 443 but bind to 9090), you can do it as
    ## follows.  You'll need to do ipchains or other port forwarding
    ## yourself to make this work.
    #ORPort 443 NoListen
    #ORPort 127.0.0.1:9090 NoAdvertise

    ## The IP address or full DNS name for incoming connections to your
    ## relay. Leave commented out and Tor will guess.
    #Address noname.example.com

    ## If you have multiple network interfaces, you can specify one for
    ## outgoing traffic to use.
    # OutboundBindAddress 10.0.0.5

    ## A handle for your relay, so people don't have to refer to it by key.
    #Nickname ididnteditheconfig

    ## Define these to limit how much relayed traffic you will allow. Your
    ## own traffic is still unthrottled. Note that RelayBandwidthRate must
    ## be at least 20 KB.
    ## Note that units for these config options are bytes per second, not bits
    ## per second, and that prefixes are binary prefixes, i.e. 2^10, 2^20, etc.
    #RelayBandwidthRate 100 KB  # Throttle traffic to 100KB/s (800Kbps)
    #RelayBandwidthBurst 200 KB # But allow bursts up to 200KB/s (1600Kbps)

    ## Use these to restrict the maximum traffic per day, week, or month.
    ## Note that this threshold applies separately to sent and received bytes,
    ## not to their sum: setting "4 GB" may allow up to 8 GB total before
    ## hibernating.
    ##
    ## Set a maximum of 4 gigabytes each way per period.
    #AccountingMax 4 GB
    ## Each period starts daily at midnight (AccountingMax is per day)
    #AccountingStart day 00:00
    ## Each period starts on the 3rd of the month at 15:00 (AccountingMax
    ## is per month)
    #AccountingStart month 3 15:00

    ## Administrative contact information for this relay or bridge. This line
    ## can be used to contact you if your relay or bridge is misconfigured or
    ## something else goes wrong. Note that we archive and publish all
    ## descriptors containing these lines and that Google indexes them, so
    ## spammers might also collect them. You may want to obscure the fact that
    ## it's an email address and/or generate a new address for this purpose.
    #ContactInfo Random Person <nobody AT example dot com>
    ## You might also include your PGP or GPG fingerprint if you have one:
    #ContactInfo 0xFFFFFFFF Random Person <nobody AT example dot com>

    ## Uncomment this to mirror directory information for others. Please do
    ## if you have enough bandwidth.
    #DirPort 9030 # what port to advertise for directory connections
    ## If you want to listen on a port other than the one advertised in
    ## DirPort (e.g. to advertise 80 but bind to 9091), you can do it as
    ## follows.  below too. You'll need to do ipchains or other port
    ## forwarding yourself to make this work.
    #DirPort 80 NoListen
    #DirPort 127.0.0.1:9091 NoAdvertise
    ## Uncomment to return an arbitrary blob of html on your DirPort. Now you
    ## can explain what Tor is if anybody wonders why your IP address is
    ## contacting them. See contrib/tor-exit-notice.html in Tor's source
    ## distribution for a sample.
    #DirPortFrontPage /etc/tor/tor-exit-notice.html

    ## Uncomment this if you run more than one Tor relay, and add the identity
    ## key fingerprint of each Tor relay you control, even if they're on
    ## different networks. You declare it here so Tor clients can avoid
    ## using more than one of your relays in a single circuit. See
    ## https://www.torproject.org/docs/faq#MultipleRelays
    ## However, you should never include a bridge's fingerprint here, as it would
    ## break its concealability and potentionally reveal its IP/TCP address.
    #MyFamily $keyid,$keyid,...

    ## A comma-separated list of exit policies. They're considered first
    ## to last, and the first match wins. If you want to _replace_
    ## the default exit policy, end this with either a reject *:* or an
    ## accept *:*. Otherwise, you're _augmenting_ (prepending to) the
    ## default exit policy. Leave commented to just use the default, which is
    ## described in the man page or at
    ## https://www.torproject.org/documentation.html
    ##
    ## Look at https://www.torproject.org/faq-abuse.html#TypicalAbuses
    ## for issues you might encounter if you use the default exit policy.
    ##
    ## If certain IPs and ports are blocked externally, e.g. by your firewall,
    ## you should update your exit policy to reflect this -- otherwise Tor
    ## users will be told that those destinations are down.
    ##
    ## For security, by default Tor rejects connections to private (local)
    ## networks, including to your public IP address. See the man page entry
    ## for ExitPolicyRejectPrivate if you want to allow "exit enclaving".
    ##
    #ExitPolicy accept *:6660-6667,reject *:* # allow irc ports but no more
    #ExitPolicy accept *:119 # accept nntp as well as default exit policy
    #ExitPolicy reject *:* # no exits allowed

    ## Bridge relays (or "bridges") are Tor relays that aren't listed in the
    ## main directory. Since there is no complete public list of them, even an
    ## ISP that filters connections to all the known Tor relays probably
    ## won't be able to block all the bridges. Also, websites won't treat you
    ## differently because they won't know you're running Tor. If you can
    ## be a real relay, please do; but if not, be a bridge!
    #BridgeRelay 1
    ## By default, Tor will advertise your bridge to users through various
    ## mechanisms like https://bridges.torproject.org/. If you want to run
    ## a private bridge, for example because you'll give out your bridge
    ## address manually to your friends, uncomment this line:
    #PublishServerDescriptor 0 """

    if os.path.exists("/etc/tor/torrc"):

        file = open("/etc/tor/torrc", "w")
        file.write(torconfig)

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
    torconfig = """## Configuration file for a typical Tor user
    ## Last updated 9 October 2013 for Tor 0.2.5.2-alpha.
    ## (may or may not work for much older or much newer versions of Tor.)
    ##
    ## Lines that begin with "## " try to explain what's going on. Lines
    ## that begin with just "#" are disabled commands: you can enable them
    ## by removing the "#" symbol.
    ##
    ## See 'man tor', or https://www.torproject.org/docs/tor-manual.html,
    ## for more options you can use in this file.
    ##
    ## Tor will look for this file in various places based on your platform:
    ## https://www.torproject.org/docs/faq#torrc

    ## Tor opens a socks proxy on port 9050 by default -- even if you don't
    ## configure one below. Set "SocksPort 0" if you plan to run Tor only
    ## as a relay, and not make any local application connections yourself.
    #SocksPort 9050 # Default: Bind to localhost:9050 for local connections.
    #SocksPort 192.168.0.1:9100 # Bind to this address:port too.

    ## Entry policies to allow/deny SOCKS requests based on IP address.
    ## First entry that matches wins. If no SocksPolicy is set, we accept
    ## all (and only) requests that reach a SocksPort. Untrusted users who
    ## can access your SocksPort may be able to learn about the connections
    ## you make.
    #SocksPolicy accept 192.168.0.0/16
    #SocksPolicy reject *

    ## Logs go to stdout at level "notice" unless redirected by something
    ## else, like one of the below lines. You can have as many Log lines as
    ## you want.
    ##
    ## We advise using "notice" in most cases, since anything more verbose
    ## may provide sensitive information to an attacker who obtains the logs.
    ##
    ## Send all messages of level 'notice' or higher to /var/log/tor/notices.log
    #Log notice file /var/log/tor/notices.log
    ## Send every possible message to /var/log/tor/debug.log
    #Log debug file /var/log/tor/debug.log
    ## Use the system log instead of Tor's logfiles
    #Log notice syslog
    ## To send all messages to stderr:
    #Log debug stderr

    ## Uncomment this to start the process in the background... or use
    ## --runasdaemon 1 on the command line. This is ignored on Windows;
    ## see the FAQ entry if you want Tor to run as an NT service.
    #RunAsDaemon 1

    ## The directory for keeping all the keys/etc. By default, we store
    ## things in $HOME/.tor on Unix, and in Application Data\tor on Windows.
    #DataDirectory /var/lib/tor

    ## The port on which Tor will listen for local connections from Tor
    ## controller applications, as documented in control-spec.txt.
    #ControlPort 9051
    ## If you enable the controlport, be sure to enable one of these
    ## authentication methods, to prevent attackers from accessing it.
    #HashedControlPassword 16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C
    #CookieAuthentication 1

    ############### This section is just for location-hidden services ###

    ## Once you have configured a hidden service, you can look at the
    ## contents of the file ".../hidden_service/hostname" for the address
    ## to tell people.
    ##
    ## HiddenServicePort x y:z says to redirect requests on port x to the
    ## address y:z.

    #HiddenServiceDir /var/lib/tor/hidden_service/
    #HiddenServicePort 80 127.0.0.1:80

    HiddenServiceDir /var/lib/tor/other_hidden_service/
    HiddenServicePort 80 127.0.0.1:80
    HiddenServicePort 22 127.0.0.1:22

    ################ This section is just for relays #####################
    #
    ## See https://www.torproject.org/docs/tor-doc-relay for details.

    ## Required: what port to advertise for incoming Tor connections.
    #ORPort 9001
    ## If you want to listen on a port other than the one advertised in
    ## ORPort (e.g. to advertise 443 but bind to 9090), you can do it as
    ## follows.  You'll need to do ipchains or other port forwarding
    ## yourself to make this work.
    #ORPort 443 NoListen
    #ORPort 127.0.0.1:9090 NoAdvertise

    ## The IP address or full DNS name for incoming connections to your
    ## relay. Leave commented out and Tor will guess.
    #Address noname.example.com

    ## If you have multiple network interfaces, you can specify one for
    ## outgoing traffic to use.
    # OutboundBindAddress 10.0.0.5

    ## A handle for your relay, so people don't have to refer to it by key.
    #Nickname ididnteditheconfig

    ## Define these to limit how much relayed traffic you will allow. Your
    ## own traffic is still unthrottled. Note that RelayBandwidthRate must
    ## be at least 20 KB.
    ## Note that units for these config options are bytes per second, not bits
    ## per second, and that prefixes are binary prefixes, i.e. 2^10, 2^20, etc.
    #RelayBandwidthRate 100 KB  # Throttle traffic to 100KB/s (800Kbps)
    #RelayBandwidthBurst 200 KB # But allow bursts up to 200KB/s (1600Kbps)

    ## Use these to restrict the maximum traffic per day, week, or month.
    ## Note that this threshold applies separately to sent and received bytes,
    ## not to their sum: setting "4 GB" may allow up to 8 GB total before
    ## hibernating.
    ##
    ## Set a maximum of 4 gigabytes each way per period.
    #AccountingMax 4 GB
    ## Each period starts daily at midnight (AccountingMax is per day)
    #AccountingStart day 00:00
    ## Each period starts on the 3rd of the month at 15:00 (AccountingMax
    ## is per month)
    #AccountingStart month 3 15:00

    ## Administrative contact information for this relay or bridge. This line
    ## can be used to contact you if your relay or bridge is misconfigured or
    ## something else goes wrong. Note that we archive and publish all
    ## descriptors containing these lines and that Google indexes them, so
    ## spammers might also collect them. You may want to obscure the fact that
    ## it's an email address and/or generate a new address for this purpose.
    #ContactInfo Random Person <nobody AT example dot com>
    ## You might also include your PGP or GPG fingerprint if you have one:
    #ContactInfo 0xFFFFFFFF Random Person <nobody AT example dot com>

    ## Uncomment this to mirror directory information for others. Please do
    ## if you have enough bandwidth.
    #DirPort 9030 # what port to advertise for directory connections
    ## If you want to listen on a port other than the one advertised in
    ## DirPort (e.g. to advertise 80 but bind to 9091), you can do it as
    ## follows.  below too. You'll need to do ipchains or other port
    ## forwarding yourself to make this work.
    #DirPort 80 NoListen
    #DirPort 127.0.0.1:9091 NoAdvertise
    ## Uncomment to return an arbitrary blob of html on your DirPort. Now you
    ## can explain what Tor is if anybody wonders why your IP address is
    ## contacting them. See contrib/tor-exit-notice.html in Tor's source
    ## distribution for a sample.
    #DirPortFrontPage /etc/tor/tor-exit-notice.html

    ## Uncomment this if you run more than one Tor relay, and add the identity
    ## key fingerprint of each Tor relay you control, even if they're on
    ## different networks. You declare it here so Tor clients can avoid
    ## using more than one of your relays in a single circuit. See
    ## https://www.torproject.org/docs/faq#MultipleRelays
    ## However, you should never include a bridge's fingerprint here, as it would
    ## break its concealability and potentionally reveal its IP/TCP address.
    #MyFamily $keyid,$keyid,...

    ## A comma-separated list of exit policies. They're considered first
    ## to last, and the first match wins. If you want to _replace_
    ## the default exit policy, end this with either a reject *:* or an
    ## accept *:*. Otherwise, you're _augmenting_ (prepending to) the
    ## default exit policy. Leave commented to just use the default, which is
    ## described in the man page or at
    ## https://www.torproject.org/documentation.html
    ##
    ## Look at https://www.torproject.org/faq-abuse.html#TypicalAbuses
    ## for issues you might encounter if you use the default exit policy.
    ##
    ## If certain IPs and ports are blocked externally, e.g. by your firewall,
    ## you should update your exit policy to reflect this -- otherwise Tor
    ## users will be told that those destinations are down.
    ##
    ## For security, by default Tor rejects connections to private (local)
    ## networks, including to your public IP address. See the man page entry
    ## for ExitPolicyRejectPrivate if you want to allow "exit enclaving".
    ##
    #ExitPolicy accept *:6660-6667,reject *:* # allow irc ports but no more
    #ExitPolicy accept *:119 # accept nntp as well as default exit policy
    #ExitPolicy reject *:* # no exits allowed

    ## Bridge relays (or "bridges") are Tor relays that aren't listed in the
    ## main directory. Since there is no complete public list of them, even an
    ## ISP that filters connections to all the known Tor relays probably
    ## won't be able to block all the bridges. Also, websites won't treat you
    ## differently because they won't know you're running Tor. If you can
    ## be a real relay, please do; but if not, be a bridge!
    #BridgeRelay 1
    ## By default, Tor will advertise your bridge to users through various
    ## mechanisms like https://bridges.torproject.org/. If you want to run
    ## a private bridge, for example because you'll give out your bridge
    ## address manually to your friends, uncomment this line:
    #PublishServerDescriptor 0 """

    if os.path.exists("/etc/tor/torrc"):

        file = open("/etc/tor/torrc", "w")
        file.write(torconfig)

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


def newgetlink():
    deletehidden = "/var/lib/tor/hidden_service"
    global tamerrorsay
    if os.path.exists(deletehidden):
        shutil.rmtree(deletehidden)
        getlink()
    elif tamerrorsay == 0:
        tamerrorsay = 1
        getlink()
    elif tamerrorsay == 1:
        tamerrorsay = 2
        getlink()
    else:
        tamerrorsay = 0
        print("hidden_service folder file not found. Try option 1 first")


def othernewgetlink():
    deleteotherhidden = "/var/lib/tor/other_hidden_service"
    global tamothersay
    if os.path.exists(deleteotherhidden):
        shutil.rmtree(deleteotherhidden)
        othergetlink()
    elif tamothersay == 0:
        tamothersay = 1
        othergetlink()
    elif tamothersay == 1:
        tamothersay = 2
        othergetlink()
    else:
        tamothersay = 0
        print("other_hidden_service folder file not found. Try option 2 first")


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

    print(Fore.LIGHTCYAN_EX + "[2] Get Other Onion Link" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTMAGENTA_EX + "[3] Get New Onion Link (First Onion Link Disappears)" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTYELLOW_EX + "[4] Get Other New Onion Links (Other Onion Link Disappears)" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTGREEN_EX + "[5] How to Edit Website?" + Style.RESET_ALL + "\n")

    print(Fore.BLUE + "[6] Onion Links Error Codes" + Style.RESET_ALL + "\n")

    print(Fore.LIGHTWHITE_EX + "[7] Exit" + Style.RESET_ALL + "\n")

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
                newgetlink()

            elif secim == 4:
                print("")
                othernewgetlink()

            elif secim == 5:
                print("")
                print(
                    "Open the file under the /var/www/html folder as an administrator and make your changes. Example: "
                    "sudo nano"
                    "/var/www/html/myhtml.txt")

            elif secim == 6:
                print("")
                print("https://tb-manual.torproject.org/onion-services/")

            elif secim == 7:
                break


        except ValueError:
            print("")
