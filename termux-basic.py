#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m


            ███████████████████████████████████
            █─█─██▀▄─██─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
            █─▄─██─▀─██─███▀██─▄▀███─▄█▀██─▄─▄█
            ▀▄▀▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
   ███████████████████████████████████████████████████
   █─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▀█▀─▄█▄─▄█▄─▀█▄─▄██▀▄─██▄─▄███
   ███─████─▄█▀██─▄─▄██─█▄█─███─███─█▄▀─███─▀─███─██▀█
   ▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Anonymous  | version : 2.0  |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] php
[04] git
[05] perl
[06] bash
[07] cowsay
[08] fish
[09] unzip
[10] tor
[11] nano
[12] curl
[13] openssl
[14] openssh
[15] wget
[16] screenfetch
[17] clang
[18] nmap
[19] w3m
[20] hydra
[21] toilet
[22] figlet
[23] jq
[24] cmatrix
[25] zip
[26] ruby
[27] dnsutils
[28] coreutils
[29] tar
[30] wcalc
[31] bmon ''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update -y")
os.system ("apt upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")
os.system ("apt install cowsay -y")
os.system ("apt install fish -y")
os.system ("apt install unzip -y")
os.system ("apt install tor -y")


print ("wait for second and start hacking")

os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install screenfetch -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")
os.system ("apt install toilet -y")
os.system ("apt install figlet -y")
os.system ("apt install jq -y")
os.system ("apt install cmatrix -y")
os.system ("apt install zip -y")

print ("""
subscribe Hacker_terminal""")

os.system ("apt install ruby -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")
os.system ("apt install tar -y")
os.system ("apt install wcalc -y")
os.system ("apt install bmon -y")



print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+--------------------------------------------------+")
slowprint('''\033[95m|             Welcome To Hacker_terminal           |
|           Subscribe Our YouTube Channel          |
|      Watch Ours Tutorials For Learn Hacking      |''')
print("+--------------------------------------------------+")

input("\n\nPress the enter key to exit : ")
