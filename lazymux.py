import os, sys

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


os.system('clear')
print ' __                                      '
print '|  |    ___  ___  _ _  _____  _ _  _ _   '
print "|  |__ | .'||- _|| | ||     || | ||_'_|  "
print '|_____||__,||___||_  ||_|_|_||___||_,_|  '
print '                 |___|                   '
print ' [A] Author: DedSecTL & ID_OUT96         '
print ' [D] Date: 05-10-2017 (18:22)            '
print ' [G] Blackhole Programming Security      '
print ' [T] AndroSec1337 Cyber Team             '
print ' [G] https://github.com/Gameye98         '
print ' [B] http://droidsec9798-com.mwapblog.com'
print ' [B] http://androsec1337.cf              '
print
print '  [01] Sudo            [11] SQLMap'
print '  [02] NMap            [12] Black Hydra'
print '  [03] Hydra           [13] Fl00d & Fl00d2'
print '  [04] FB Brute Force  [14] Infoga'
print '  [05] Webdav          [15] LANs.py'
print '  [06] RED HAWK        [16] Pagodo'
print '  [07] Brutal          [17] FBUP'
print '  [08] Metasploit      [18] KnockMail'
print '  [09] 1337Hash        [19] Ufonet'
print '  [10] IPLoc           [20] Commix\n'
print '  [21] D-Tect          [31] ReconDog'
print '  [22] A-Rat           [32] Meisha'
print '  [23] Torshammer      [33] Kali NetHunter'
print '  [24] Slowloris       [34] Ngrok'
print '  [25] DSSS            [35] Weeman'
print '  [26] SQLiv           [36] Cupp'
print '  [27] Wifite          [37] Hash-Buster'
print '  [28] Wifite 2        [38] Routersploit'
print '  [29] MSFPC           [39] Ubuntu'
print '  [30] Kwetza          [40] Fedora'
lazymux = raw_input('\nlazymux > ')
if lazymux.strip() in ('01 1').split():
    print '---# Installing sudo'
    os.system('apt update && apt upgrade')
    os.system('apt install ncurses-utils git')
    os.system('git clone https://github.com/st42/termux-sudo')
    os.system('cd termux-sudo')
    os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
    os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('02 2').split():
    print '---# Installing NMap...'
    os.system('apt update && apt upgrade')
    os.system('apt install nmap')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('03 3').split():
    print '---# Installing Hydra'
    os.system('apt update && apt upgrade')
    os.system('apt install hydra')
    print '---# Done'
elif lazymux.strip() in ('04 4').split():
    print '---# Installing Facebook Brute Force'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev wget')
    os.system('pip2 install mechanize')
    os.system('mkdir /data/data/com.termux/files/home/facebook-brute;cd /data/data/com.termux/files/home/facebook-brute')
    os.system('wget http://override.waper.co/files/facebook.apk')
    os.system('wget http://override.waper.co/files/password.apk')
    os.system('mv facebook.apk facebook.py;mv password.apk password.txt')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('05 5').split():
    print '---# Installing Webdav'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev openssl curl libcurl')
    os.system('pip2 install urllib3 chardet certifi idna requests')
    os.system('mkdir /data/data/com.termux/files/home/webdav;cd /data/data/com.termux/files/home/webdav')
    os.system('curl -k -O https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR webdav.py')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('06 6').split():
    print '---# Installing RED HAWK'
    os.system('apt update && apt upgrade')
    os.system('apt install git php')
    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('07 7').split():
    print '---# Installing Brutal'
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/Screetsec/Brutal;cd Brutal;chmod +x Brutal.sh')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('08 8').split():
    print '---# Installing Metasploit'
    os.system('bash meta-install.sh')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('09 9').split():
    print '---# Installing 1337Hash'
    os.system('apt update && apt upgrade')
    os.system('apt install git python2 python2-dev')
    os.system('git clone https://github.com/Gameye98/1337Hash')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('10').split():
    print '---# Installing IPLoc'
    os.system('apt update && apt upgrade')
    os.system('apt install git python2 python2-dev')
    os.system('git clone https://github.com/Gameye98/IPLoc')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('11').split():
    print '---# Installing SQLMap'
    os.system('apt update && apt upgrade')
    os.system('apt install git python2 python2-dev')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('12').split():
    print '---# Installing Black Hydra'
    os.system('apt update && apt upgrade')
    os.system('apt install hydra git python2 python2-dev')
    os.system('git clone https://github.com/Gameye98/Black-Hydra')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('13').split():
    print '---# Installing Fl00d & Fl00d2'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev wget')
    os.system('mkdir /data/data/com.termux/files/home/fl00d;cd /data/data/com.termux/files/home/fl00d')
    os.system('wget http://override.waper.co/files/fl00d.apk')
    os.system('wget http://override.waper.co/files/fl00d2.apk')
    os.system('mv fl00d.apk fl00d.py;mv fl00d2.apk fl00d2.py')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('14').split():
    print '---# Installing Infoga'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('pip2 install requests urllib3 urlparse')
    os.system('git clone https://github.com/m4ll0k/Infoga')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('15').split():
    print '---# Installing LANs.py'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('pip2 install scapy twisted requests')
    os.system('git clone https://github.com/DanMcInerney/LANs.py')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('16').split():
    print '---# Installing Pagodo'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('pip2 install bs4 google')
    os.system('git clone https://github.com/opsdisk/pagodo')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('17').split():
    print '---# Installing FBUP'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('pip2 install urllib3 chardet certifi idna requests')
    os.system('git clone https://github.com/mrSilent0598/FBUPv2.0')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('18').split():
    print '---# Installing KnockMail'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('pip2 install validate_email pyDNS')
    os.system('git clone https://github.com/4w4k3/KnockMail')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('19').split():
    print '---# Installing Ufonet'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('pip2 install pycurl geoip whois pycrypto requests')
    os.system('git clone https://github.com/epsylon/ufonet')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('20').split():
    print '---# Installing Commix'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/commixproject/commix')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('21').split():
    print '---# Installing D-Tect'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('22').split():
    print '---# Installing A-Rat'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/Xi4u7/A-Rat')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('23').split():
    print '---# Installing Torshammer'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/dotfighter/torshammer')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('24').split():
    print '---# Installing Slowloris'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/gkbrk/slowloris')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('25').split():
    print '---# Installing DSSS'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/stamparm/DSSS')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('26').split():
    print '---# Installing SQLiv'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/Hadesy2k/sqliv')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('27').split():
    print '---# Installing Wifite'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/derv82/wifite')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('28').split():
    print '---# Installing Wifite 2'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/derv82/wifite2')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('29').split():
    print '---# Installing MSFPC'
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/g0tmi1k/mpc')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('30').split():
    print '---# Installing Kwetza'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/sensepost/kwetza')
    os.system('pip2 install beautifulsoup4')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('31').split():
    print '---# Installing ReconDog'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/UltimateHackers/ReconDog')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('32').split():
    print '---# Installing Meisha'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/Gameye98/Meisha')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('33').split():
    print '---# Installing Kali NetHunter'
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
    os.system('cd Nethunter-In-Termux;chmod +x kalinethunter')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('34').split():
    print '---# Installing Ngrok'
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/themastersunil/ngrok')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('35').split():
    print '---# Installing Weeman'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/evait-security/weeman')
    os.system('cd weeman;chmod +x weeman.py')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('36').split():
    print '---# Installing Cupp'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/Mebus/cupp')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('37').split():
    print '---# Installing Hash-Buster'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/UltimateHackers/Hash-Buster')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('38').split():
    print '---# Installing Routersploit'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/reverse-shell/routersploit')
    os.system('cd routersploit;pip2 install -r requirements.txt;pip2 install -r requirements-dev.txt;pip2 install -r requests')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('39').split():
    print '---# Installing Ubuntu'
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev git')
    os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
    os.system('cd termux-ubuntu && bash ubuntu.sh')
    print '---# Done'
    sys.exit()
elif lazymux.strip() in ('40').split():
    print '---# Installing Fedora'
    os.system('apt update && apt upgrade')
    os.system('apt install wget git')
    os.system('/data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
    print '---# Done'
    sys.exit()
else:
    print '[!] ERROR: Wrong Input'
    restart_program()
