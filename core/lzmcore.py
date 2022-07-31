## lzmcore.py - useful module of Lazymux
##
import os, sys, time
import urllib.request
from subprocess import check_output as inputstream

current_dir = os.getcwd()
lazymux_banner = """
 _
( )
| |       _ _  ____  _   _   ___ ___   _   _
| |  _  /'_` )(_  ,)( ) ( )/' _ ` _ `\( ) ( )(`\/')
| |_( )( (_| | /'/_ | (_) || ( ) ( ) || (_) | >  <
(____/'`\__,_)(____)`\__, |(_) (_) (_)`\___/'(_/\_)
                    ( )_| |
                    `\___/'
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Lazymux
"""

prefix = os.getenv("PREFIX")
configBase = "[HOME] = ~"
configFile = "../lazymux.conf"
cache_1 = prefix+"/tmp/lazymux_1"

def repo_check(sources_list):
	if os.path.isfile(os.getenv("PREFIX")+"/etc/apt/sources.list.d/"+sources_list):
		return True
	return False

def writeStatus(statusId):
	open(cache_1,"w").write(str(statusId))

def readStatus():
	try:
		statusId = open(cache_1,"r").read()
		if statusId == "1":
			return True
		return False
	except IOError:
		return False

def checkConfigFile():
	if os.path.exists(configFile):
		if os.path.isdir(configFile):
			os.system(f"rm -rf {configFile}")
			open(configFile,"w").write(configBase)
	else:
		open(configFile,"w").write(configBase)

def loadConfigFile():
	checkConfigFile()
	lfile = ""
	try:
		lfile = [x.split("=")[-1].strip() for x in open(configFile,"r").splitlines() if x.split("=")[0].strip() == "[HOME]"][0]
	except Exception as e:
		lfile = "~"
	return lfile

homeDir = loadConfigFile()

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	if not readStatus():
		print(backtomenu_banner)
		backtomenu = input("lzmx > ")
		
		if backtomenu == "99":
			restart_program()
		elif backtomenu == "0" or backtomenu == "00":
			sys.exit()
		else:
			print("\nERROR: Wrong Input")
			time.sleep(2)
			restart_program()

def banner():
	print(lazymux_banner)

### Repo Installer
def pointless_repo():
	urllib.request.urlretrieve('https://its-pointless.github.io/setup-pointless-repo.sh','setup-pointless-repo.sh')
	os.system('bash setup-pointless-repo.sh')
	os.remove('setup-pointless-repo.sh')
	os.system('apt update -y && apt upgrade -y')
###

def nmap():
	print('\n###### Installing Nmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nmap')
	print('###### Done')
	print("###### Type 'nmap' to start.")
	backtomenu_option()

def red_hawk():
	print('\n###### Installing RED HAWK')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dtect():
	print('\n###### Installing D-TECT')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	os.system('mv D-Tech {}/D-TECT'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmap():
	print('\n###### Installing sqlmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def infoga():
	print('\n###### Installing Infoga')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def reconDog():
	print('\n###### Installing ReconDog')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/ReconDog')
	os.system('mv ReconDog {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androZenmap():
	print('\n###### Installing AndroZenmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir {}/AndroZenmap'.format(homeDir))
	os.system('mv androzenmap.sh {}/AndroZenmap'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmate():
	print('\n###### Installing sqlmate')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/s0md3v/sqlmate')
	os.system('mv sqlmate {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def astraNmap():
	print('\n###### Installing AstraNmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def weeman():
	print('\n###### Installing weeman')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clang git python2')
	os.system('python2 -m pip bs4 html5lib lxml')
	os.system('git clone https://github.com/evait-security/weeman')
	os.system('mv weeman {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def easyMap():
	print('\n###### Installing Easymap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap {}'.format(homeDir))
	os.system('cd {}/Easymap && sh install.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xd3v():
	print('\n###### Installing XD3v')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh {0}/../usr/bin/xd3v && chmod +x {0}/../usr/bin/xd3v'.format(homeDir))
	print('###### Done')
	print("###### Type 'xd3v' to start.")
	backtomenu_option()

def crips():
	print('\n###### Installing Crips')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sir():
	print('\n###### Installing SIR')
	os.system("apt update && apt upgrade")
	os.system("apt install python2 git")
	os.system("python2 -m pip install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def xshell():
	print('\n###### Installing Xshell')
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def evilURL():
	print('\n###### Installing EvilURL')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def striker():
	print('\n###### Installing Striker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/s0md3v/Striker')
	os.system('mv Striker {}'.format(homeDir))
	os.system('cd {}/Striker && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dsss():
	print('\n###### Installing DSSS')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqliv():
	print('\n###### Installing SQLiv')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/the-robot/sqliv')
	os.system('mv sqliv {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlscan():
	print('\n###### Installing sqlscan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wordpreSScan():
	print('\n###### Installing Wordpresscan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan {}'.format(homeDir))
	os.system('cd {}/Wordpresscan && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wpscan():
	print('\n###### Installing WPScan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan {0} && cd {0}/wpscan'.format(homeDir))
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print('###### Done')
	backtomenu_option()

def wordpresscan():
	print('\n###### Installing wordpresscan(2)')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan {}'.format(homeDir))
	print('###### Done')
	print("###### Type 'wordpresscan' to start.")
	backtomenu_option()

def routersploit():
	print('\n###### Installing Routersploit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/threat9/routersploit')
	os.system('mv routersploit {0};cd {0}/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def torshammer():
	print('\n###### Installing Torshammer')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def slowloris():
	print('\n###### Installing Slowloris')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fl00d12():
	print('\n###### Installing Fl00d & Fl00d2')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 curl')
	os.system('mkdir {}/fl00d'.format(homeDir))
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	os.system('mv fl00d.py {0}/fl00d && mv fl00d2.py {0}/fl00d'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def goldeneye():
	print('\n###### Installing GoldenEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xerxes():
	print('\n###### Installing Xerxes')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/baraalmasri/xerxes')
	os.system('mv xerxes {}'.format(homeDir))
	os.system('cd {}/xerxes && clang xerxes.c -o xerxes'.format(homeDir))
	os.system('chmod 755 {0}/xerxes/xerxes && cp {0}/xerxes/xerxes $PREFIX/bin'.format(homeDir))
	print('###### Done')
	print('###### Usage: xerxes ​www.fakesite.com​ 80')
	backtomenu_option()

def planetwork_ddos():
	print('\n###### Installing Planetwork-DDOS')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hydra():
	print('\n###### Installing Hydra')
	os.system('apt update -y && apt upgrade -y')
	os.system('')
	os.system('git clone https://github.com/vanhauser-thc/thc-hydra')
	print('###### Done')
	backtomenu_option()

def black_hydra():
	print('\n###### Installing Black Hydra')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cupp():
	print('\n###### Installing Cupp')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def asu():
	print('\n###### Installing ASU')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hash_buster():
	print('\n###### Installing Hash-Buster')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/Hash-Buster')
	os.system('mv Hash-Buster {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def instaHack():
	print('\n###### Installing InstaHack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Slayeri4/instahack')
	os.system('mv instahack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def indonesian_wordlist():
	print('\n###### Installing indonesian-wordlist')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	os.system('mv indonesian-wordlist {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fbBrute():
	print('\n###### Installing Facebook Brute Force 3')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install curl python2')
	os.system('python2 -m pip install mechanize')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt')
	os.system('mkdir {}/facebook-brute-3'.format(homeDir))
	os.system('mv facebook3.py {0}/facebook-brute-3 && mv password.txt {0}/facebook-brute-3'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def webdav():
	print('\n###### Installing WebDAV')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 openssl curl libcurl')
	os.system('python2 -m pip install urllib3 chardet certifi idna requests')
	os.system('mkdir {}/webdav'.format(homeDir))
	os.system('curl -k -O https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR {}/webdav/webdav.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def webmassploit():
	print('\n###### Installing Webdav Mass Exploiter')
	os.system("apt update && apt upgrade")
	os.system("apt install python2 openssl curl libcurl")
	os.system("python2 -m pip install requests")
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir {0}/webdav-mass-exploit && mv webdav.py {0}/webdav-mass-exploit".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqldump():
	print('\n###### Installing sqldump')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 curl')
	os.system('python2 -m pip install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir {0}/sqldump && chmod +x sqldump.py && mv sqldump.py {0}/sqldump'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def websploit():
	print('\n###### Installing Websploit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def metasploit():
	print('\n###### Installing Metasploit')
	os.system("apt update && apt upgrade")
	os.system("apt install unstable-repo")
	os.system("cd {} && apt install metasploit".format(homeDir))
	print('###### Done')
	print("###### Type 'msfconsole' to start.")
	backtomenu_option()

def commix():
	print('\n###### Installing Commix')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutal():
	print('\n###### Installing Brutal')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def knockmail():
	print('\n###### Installing KnockMail')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('python2 -m pip install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hac():
	print('\n###### Installing Hac')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rang3r():
	print('\n###### Installing Rang3r')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sh33ll():
	print('\n###### Installing SH33LL')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def social():
	print('\n###### Installing Social-Engineering')
	os.system("apt update && apt upgrade")
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def spiderbot():
	print('\n###### Installing SpiderBot')
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def ngrok():
	print('\n###### Installing Ngrok')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sudo():
	print('\n###### Installing sudo')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo {0} && cd {0}/termux-sudo && chmod 777 *'.format(homeDir))
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print('###### Done')
	backtomenu_option()

def ubuntu():
	"""
	print('\n###### Installing Ubuntu')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu {0} && cd {0}/termux-ubuntu && bash ubuntu.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()
	"""
	print('\n###### Installing Ubuntu')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install ubuntu')
	print('###### Done')
	backtomenu_option()

def fedora():
	"""
	print('\n###### Installing Fedora')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()
	"""
	print('\n###### Installing Ubuntu')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install fedora')
	print('###### Done')
	backtomenu_option()

def nethunter():
	print('\n###### Installing Kali NetHunter')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def blackbox():
	print('\n###### Installing BlackBox')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xattacker():
	print('\n###### Installing XAttacker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vcrt():
	print('\n###### Installing VCRT')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def socfish():
	print('\n###### Installing SocialFish')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ecode():
	print('\n###### Installing ECode')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xsstrike():
	print('\n###### Installing XSStrike')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/s0md3v/XSStrike')
	os.system('mv XSStrike {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def breacher():
	print('\n###### Installing Breacher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests argparse')
	os.system('git clone https://github.com/s0md3v/Breacher')
	os.system('mv Breacher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def stylemux():
	print('\n###### Installing Termux-Styling')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def txtool():
	print('\n###### Installing TXTool')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def passgencvar():
	print('\n###### Installing PassGen')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def owscan():
	print('\n###### Installing OWScan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sanlen():
	print('\n###### Installing santet-online')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def spazsms():
	print('\n###### Installing SpazSMS')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasher():
	print('\n###### Installing Hasher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install passlib binascii progressbar')
	os.system('git clone https://github.com/CiKu370/hasher')
	os.system('mv hasher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashgenerator():
	print('\n###### Installing Hash-Generator')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/CiKu370/hash-generator')
	os.system('mv hash-generator {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kodork():
	print('\n###### Installing ko-dork')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/CiKu370/ko-dork')
	os.system('mv ko-dork {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def snitch():
	print('\n###### Installing snitch')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def osif():
	print('\n###### Installing OSIF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/CiKu370/OSIF')
	os.system('mv OSIF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nk26():
	print('\n###### Installing nk26')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/milio48/nk26')
	os.system('mv nk26 {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def devploit():
	print('\n###### Installing Devploit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasherdotid():
	print('\n###### Installing Hasherdotid')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	os.system('mv hasherdotid {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def namechk():
	print('\n###### Installing Namechk')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xlPy():
	print('\n###### Installing xl-py')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git')
	os.system('git clone https://github.com/albertoanggi/xl-py')
	os.system('mv xl-py {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def beanshell():
	print('\n###### Installing Beanshell')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	print('###### Done')
	print("###### Type 'bsh' to start.")
	backtomenu_option()

def crunch():
	print('\n###### Installing Crunch')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	print("###### Done")
	print("###### Type 'crunch' to start.")
	backtomenu_option()

def binploit():
	print('\n###### Installing Binary Exploitation')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install unstable-repo')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	print("###### Done")
	print("###### Tutorial: https://youtu.be/3NTXFUxcKPc")
	backtomenu_option()

def textr():
	print('\n###### Installing Textr')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	print('###### Done')
	print("###### Type 'textr' to start.")
	backtomenu_option()

def apsca():
	print('\n###### Installing ApSca')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	print('###### Done')
	print("###### Type 'apsca' to start.")
	backtomenu_option()

def amox():
	print('\n###### Installing amox')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	print('###### Done')
	print("###### Type 'amox' to start.")
	backtomenu_option()

def fade():
	print('\n###### Installing FaDe')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FaDe')
	os.system('mv FaDe {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ginf():
	print('\n###### Installing GINF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def auxile():
	print('\n###### Installing AUXILE')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def inther():
	print('\n###### Installing inther')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hpb():
	print('\n###### Installing HPB')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	print('###### Done')
	print("###### Type 'hpb' to start.")
	backtomenu_option()

def fmbrute():
	print('\n###### Installing FMBrute')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FMBrute')
	os.system('mv FMBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashid():
	print('\n###### Installing HashID')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 && python2 -m pip install hashid')
	print("###### Done")
	print("###### Type 'hashid -h' to show usage of hashid")
	backtomenu_option()

def gpstr():
	print('\n###### Installing GPS Tracking')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	os.system('mv gps_tracking {}'.format(homeDir))
	print("###### Done")
	backtomenu_option()

def pret():
	print('\n###### Installing PRET')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 imagemagick git')
	os.system('python2 -m pip install colorama pysnmp')
	os.system('git clone https://github.com/RUB-NDS/PRET')
	os.system('mv PRET {}'.format(homeDir))
	print("###### Done")
	backtomenu_option()

def atlas():
	print('\n###### Installing Atlas')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/m4ll0k/Atlas')
	os.system('mv Atlas {}'.format(homeDir))
	print("###### Done")
	backtomenu_option()

def hashcat():
	print('\n###### Installing Hashcat')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	print("###### Done")
	print("###### Type 'hashcat' to start.")
	backtomenu_option()

def liteotp():
	print('\n###### Installing LiteOTP')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite')
	print("###### Done")
	print("###### Type 'lite' to start.")
	backtomenu_option()

def fbbrutex():
	print('\n###### Installing FBBrute')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FBBrute')
	os.system('mv FBBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fim():
	print('\n###### Installing fim')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	os.system('mv fim {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rshell():
	print('\n###### Installing RShell')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install colorama')
	os.system('git clone https://github.com/Jishu-Epic/RShell')
	os.system('mv RShell {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def termpyter():
	print('\n###### Installing TermPyter')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/Jishu-Epic/TermPyter')
	os.system('mv TermPyter {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maxsubdofinder():
	print('\n###### Installing MaxSubdoFinder')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	os.system('mv MaxSubdoFinder {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def jadx():
	print('\n###### Installing jadx')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
	os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
	os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	print('###### Done')
	print("###### Type 'jadx' to start.")
	backtomenu_option()

def pwnedOrNot():
	print('\n###### Installing pwnedOrNot')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	os.system('mv pwnedOrNot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maclook():
	print('\n###### Installing Mac-Lookup')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	os.system('mv Mac-Lookup {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def f4k3():
	print('\n###### Installing F4K3')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Gameye98/Gameye98.github.io/blob/master/package/f4k3_1.0_all.deb')
	os.system('dpkg -i f4k3_1.0_all.deb')
	os.system('rm -rf f4k3_1.0_all.deb')
	print('###### Done')
	print("###### Type 'f4k3' to start.")
	backtomenu_option()

def katak():
	print('\n###### Installing Katak')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests progressbar')
	os.system('git clone https://github.com/Gameye98/Katak')
	os.system('mv Katak {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def heroku():
	print('\n###### Installing heroku')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nodejs')
	os.system('npm install heroku -g')
	print('###### Done')
	print("###### Type 'heroku' to start.")
	backtomenu_option()

def google():
	print('\n###### Installing google')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python')
	os.system('python -m pip install google')
	print('###### Done')
	print("###### Type 'google' to start.")
	backtomenu_option()

def billcypher():
	print('\n###### Installing BillCypher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install argparse dnspython requests urllib3 colorama')
	os.system('git clone https://github.com/GitHackTools/BillCipher')
	os.system('mv BillCypher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vbug():
	print('\n###### Installing vbug')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Gameye98/vbug')
	os.system('mv vbug {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kojawafft():
	print('\n###### Installing kojawafft')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nodejs')
	os.system('git clone https://github.com/sandalpenyok/kojawafft')
	os.system('mv kojawafft {}'.format(homeDir))
	os.system('cd $HOME/kojawafft && unzip node_modules.zip && cd -')
	print('###### Done')
	backtomenu_option()

def aircrackng():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing aircrack-ng')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo aircrack-ng')
		print('###### Done')
		print("###### Type 'aircrack-ng' to start.")
	backtomenu_option()

def ettercap():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing ettercap')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo ettercap')
		print('###### Done')
		print("###### Type 'ettercap' to start.")
	backtomenu_option()

def ccgen():
	print('\n###### Installing ccgen')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ccgen')
	os.system('mv ccgen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ddcrypt():
	print('\n###### Installing ddcrypt')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ddcrypt')
	os.system('mv ddcrypt {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dnsrecon():
	print('\n###### Installing dnsrecon')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/darkoperator/dnsrecon')
	os.system('python -m pip install -r dnsrecon/requirements.txt')
	os.system('mv dnsrecon {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def zphisher():
	print('\n###### Installing zphisher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php openssh curl')
	os.system('git clone https://github.com/htr-tech/zphisher')
	os.system('mv zphisher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def apktool():
	print('\n###### Installing apktool')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git dpkg')
	os.system('git clone https://github.com/Lexiie/Termux-Apktool')
	os.system('mv Termux-Apktool {}'.format(homeDir))
	os.system('cd {}/Termux-Apktool && dpkg -i *.deb'.format(homeDir))
	print('###### Done')
	print("###### Type 'apktool' to start.")
	backtomenu_option()

def uncompyle():
	print('\n###### Installing uncompyle6')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python python2')
	os.system('python2 -m pip install uncompyle6')
	os.system('mv $PREFIX/bin/uncompyle6 $PREFIX/bin/uncompyle')
	os.system('python -m pip install uncompyle6')
	print('###### Done')
	print('###### (py2) Usage: uncompyle')
	print('###### (py3) Usage: uncompyle6')
	backtomenu_option()

def wifite():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing Wifite')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install git python2')
		os.system('git clone https://github.com/derv82/wifite')
		os.system('mv wifite {}'.format(homeDir))
		print('###### Done')
	backtomenu_option()

def parrot():
	print('\n###### Installing Parrot')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget openssl-tool proot -y && hash -r && cd {} && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Parrot/parrot.sh && bash parrot.sh'.format(homeDir))
	os.system('cd {} && bash start-parrot.sh'.format(homeDir))
	print('###### Done')
	print('###### Make sure visit: https://techriz.com/how-to-install-parrot-linux-on-android-without-root/')
	os.system('am start -a android.intent.action.VIEW -d "https://techriz.com/how-to-install-parrot-linux-on-android-without-root/"')
	backtomenu_option()

def archlinux():
	"""
	print('\n###### Installing Arch Linux')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('cd $HOME && git clone https://github.com/sdrausty/TermuxArch')
	os.system('cd $HOME && bash TermuxArch/setupTermuxArch.sh')
	print('###### Done')
	backtomenu_option()
	"""
	print('\n###### Installing Arch Linux')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install archlinux')
	print('###### Done')
	print("###### Type 'proot-distro login archlinux' to start.")
	backtomenu_option()

def tshark():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing tshark')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo tshark')
		print('###### Done')
		print("###### Type 'tshark' to start.")
	backtomenu_option()

def dos2unix():
	print('\n###### Installing dos2unix')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dos2unix')
	print('###### Done')
	print("###### Type 'dos2unix' to start.")
	backtomenu_option()

def exiftool():
	print('\n###### Installing exiftool')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install exiftool')
	print('###### Done')
	print("###### Type 'exiftool' to start.")
	backtomenu_option()

def iconv():
	print('\n###### Installing iconv')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install iconv')
	print('###### Done')
	print("###### Type 'iconv' to start.")
	backtomenu_option()

def mediainfo():
	print('\n###### Installing mediainfo')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install mediainfo')
	print('###### Done')
	print('###### Usage: mediainfo filename.pdf')
	backtomenu_option()

def pdfinfo():
	print('\n###### Installing pdfinfo')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install poppler')
	print('###### Done')
	print('###### Usage: pdfinfo filename.pdf')
	backtomenu_option()

def tcpdump():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing tcpdump')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo tcpdump')
		print('###### Done')
		print("###### Type 'tcpdump' to start.")
	backtomenu_option()

def hping3():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\nERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing hping3')
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo hping3')
		print('###### Done')
		print("###### Type 'hping3' to start.")
	backtomenu_option()

def dbdat():
	print('\n###### Installing DbDat')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install MySQL-python psycopg2 cx_Oracle pymssql ibm_db pymongo pyyaml couchdb')
	os.system('git clone https://github.com/foospidy/DbDat')
	os.system('mv DbDat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nosqlmap():
	print('\n###### Installing NoSQLMap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 unstable-repo metasploit')
	os.system('python2 -m pip install pymongo httplib2')
	os.system('git clone https://github.com/codingo/NoSQLMap')
	os.system('mv NoSQLMap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def audit_couchdb():
	print('\n###### Installing audit_couchdb')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nodejs')
	os.system('npm install -g npm@next audit_couchdb')
	os.system('git clone https://github.com/iriscouch/audit_couchdb')
	os.system('mv audit_couchdb {}'.format(homeDir))
	print('###### Done')
	print('###### Usage: audit_couchdb https://admin:secret@localhost:5984')
	backtomenu_option()

def mongoaudit():
	print('\n###### Installing mongoaudit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install pymongo mongoaudit')
	print('###### Done')
	print("###### Type 'mongoaudit' to start.")
	backtomenu_option()

def wifiphisher():
	print('\n###### Installing Wifiphisher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install setuptools scapy')
	os.system('git clone https://github.com/wifiphisher/wifiphisher')
	os.system('mv wifiphisher {0} && cd {0}/wifiphisher && python setup.py install'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sherlock():
	print('\n###### Installing sherlock')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/sherlock-project/sherlock')
	os.system('mv sherlock {0} && cd {0}/sherlock && python -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def shc():
	print('\n###### Installing shc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install shc -y')
	print('###### Done')
	print("###### Type 'shc' to start.")
	backtomenu_option()

def steghide():
	print('\n###### Installing steghide')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install steghide -y')
	print('###### Done')
	print("###### Type 'steghide' to start.")
	backtomenu_option()

def tesseract():
	print('\n###### Installing tesseract')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install tesseract -y')
	print('###### Done')
	print("###### Type 'tesseract' to start.")
	backtomenu_option()

def sleuthkit():
	print('\n###### Installing sleuthkit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install sleuthkit -y')
	print('###### Done')
	print("###### Type 'pkg files sleuthkit | grep usr/bin' to check executable file related to sleuthkit package.")
	backtomenu_option()

def octave():
	print('\n###### Installing Octave')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install octave -y')
	print('###### Done')
	print("###### Type 'octave' to start.")
	backtomenu_option()

def fpcompiler():
	print('\n###### Installing fp-compiler')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install fp-compiler -y')
	print('###### Done')
	print("###### Type 'fpc' to start.")
	backtomenu_option()

def numpy():
	print('\n###### Installing numpy')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install numpy -y')
	print('###### Done')
	print("###### Type 'pkg files numpy | grep usr/bin' to check executable file related to numpy package.")
	backtomenu_option()

def userrecon():
	print('\n###### Installing userrecon')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget dpkg curl -y')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	os.system('dpkg -i userrecon_1.0_all.deb')
	os.system('rm userrecon_1.0_all.deb')
	print('###### Done')
	print("###### Type 'userrecon' to start.")
	backtomenu_option()

def mrsip():
	print('\n###### Installing Mr.SIP')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	os.system('git clone https://github.com/meliht/Mr.SIP')
	os.system('mv Mr.SIP {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tmscanner():
	print('\n###### Installing TM-scanner')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python python2 nmap git -y')
	os.system('python -m pip install colorama requests')
	os.system('python2 -m pip install colorama requests')
	os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
	os.system('mv TM-scanner {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xss_payload_list():
	print('\n###### Installing xss-payload-list')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/payloadbox/xss-payload-list')
	os.system('mv xss-payload-list {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clickbot():
	print('\n###### Installing ClickBot')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ziziwho/clickbot')
	os.system("python -m pip install asyncio colorama telethon rsa pyaes asyncio async_generator colorama bs4 requests")
	os.system('mv clickbot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def phoneinfoga():
	print('\n###### Installing PhoneInfoga')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
	os.chdir("PhoneInfoga")
	os.system("python -m pip install -r requirements.txt")
	os.chdir("..")
	os.system('mv PhoneInfoga {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def btc2idr():
	print('\n###### Installing BTC-to-IDR-checker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/guruku/BTC-to-IDR-checker')
	os.system('mv BTC-to-IDR-checker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sitebroker():
	print('\n###### Installing SiteBroker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python php git -y')
	os.system('git clone https://github.com/Anon-Exploiter/SiteBroker')
	os.chdir("SiteBroker")
	os.system('python -m pip install -r requirements.txt')
	os.system('python -m pip install html5lib')
	os.chdir("..")
	os.system('mv SiteBroker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dostattack():
	print('\n###### Installing dost-attack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/verluchie/dost-attack')
	os.system('mv dost-attack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cfr():
	print('\n###### Installing CFR')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dx wget -y')
	os.system('mkdir $PREFIX/bin/lib')
	os.system('wget https://www.benf.org/other/cfr/cfr-0.151.jar -O $PREFIX/bin/lib/cfr-0.151.jar')
	os.chdir(prefix+"/bin/lib")
	os.system('dx --dex --output=cfr-0.151.dex cfr-0.151.jar')
	with open(prefix+"/bin/cfr","w") as f:
		f.write("#!/usr/bin/bash\n")
		f.write("dalvikvm -cp $PREFIX/bin/lib/cfr-0.151.dex org/benf/cfr/reader/Main \"$@\"")
	os.system('chmod 755 $PREFIX/bin/cfr')
	os.system('chmod 755 $PREFIX/bin/lib/cfr-0.151.dex')
	os.chdir(current_dir)
	print('###### Done')
	print("###### Type 'cfr' to start.")
	backtomenu_option()

def upx():
	print('\n###### Installing UPX')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget tar -y')
	os.system('wget https://github.com/upx/upx/releases/download/v3.96/upx-3.96-arm64_linux.tar.xz')
	os.system('tar xf upx-3.96-arm64_linux.tar.xz')
	os.system('mv upx-3.96-arm64_linux/upx $PREFIX/bin/upx')
	os.system('rm -rf upx-3.96-arm64_linux upx-3.96-arm64_linux.tar.xz')
	os.system('chmod 755 $PREFIX/bin/upx')
	print('###### Done')
	print("###### Type 'upx' to start.")
	backtomenu_option()

def pyinstxtractor():
	print('\n###### Installing pyinstxtractor')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/extremecoders-re/pyinstxtractor')
	os.system('mv pyinstxtractor {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def innoextract():
	print('\n###### Installing innoextract')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git clang -y')
	os.system('git clone https://github.com/dscharrer/innoextract')
	os.chdir("innoextract")
	os.system('mkdir -p build')
	os.chdir("build")
	os.system('cmake .. && make')
	os.system('mv innoextract $PREFIX/bin && chmod 755 $PREFIX/bin/innoextract')
	os.chdir(current_dir)
	os.system('rm -rf innoextract')
	print('###### Done')
	print("###### Type 'innoextract' to start.")
	backtomenu_option()

def lynis():
	print('\n###### Installing Lynis')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/CISOfy/lynis')
	os.system('mv lynis {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def chkrootkit():
	print('\n###### Installing Chkrootkit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clang git -y')
	os.system('git clone https://github.com/Magentron/chkrootkit')
	os.system('mv chkrootkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clamav():
	print('\n###### Installing ClamAV')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clamav -y')
	os.system('freshclam')
	print('###### Done')
	print("###### Type 'clamscan' to start.")
	backtomenu_option()

def yara():
	print('\n###### Installing Yara')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install yara -y')
	print('###### Done')
	print("###### Type 'yara' to start.")
	backtomenu_option()

def virustotal():
	print('\n###### Installing VirusTotal-CLI')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install virustotal-cli -y')
	print('###### Done')
	print("###### Type 'vt' to start.")
	backtomenu_option()

def maigret():
	print('\n###### Installing maigret')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python -y')
	os.system('python -m pip install maigret')
	print('###### Done')
	print("###### Usage: maigret <username>")
	print("###### Usage: maigret -h")
	backtomenu_option()

def xplsearch():
	print('\n###### Installing XPL-SEARCH')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php -y')
	os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
	os.system('mv XPL-SEARCH {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xadmin():
	print('\n###### Installing Xadmin')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git perl -y')
	os.system('git clone https://github.com/Manisso/Xadmin')
	os.system('mv Xadmin {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def credmap():
	print('\n###### Installing Credmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/lightos/credmap')
	os.system('mv credmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def mapeye():
	print('\n###### Installing MapEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	os.system('mv MapEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gathetool():
	print('\n###### Installing GatheTOOL')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	os.system('mv GatheTOOL {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def avpass():
	print('\n###### Installing avpass')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 python -y')
	os.system('git clone https://github.com/sslab-gatech/avpass')
	os.system('mv avpass {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def binwalk():
	print('\n###### Installing binwalk')
	os.system('apt update -y && apt upgrade -y')
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install gzip bzip2 tar arj lhasa p7zip cabextract sleuthkit lzop mtd-utils cmake build-essential make numpy scipy python git -y')
	os.system('git clone https://github.com/ReFirmLabs/binwalk')
	os.chdir("binwalk")
	os.system('python setup.py install')
	os.chdir("..")
	os.system('mv binwalk {}'.format(homeDir))
	print('###### Done')
	print("###### Type 'binwalk' to start.")
	backtomenu_option()

def arat():
	print('\n###### Installing A-Rat')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git -y')
	os.system('git clone https://github.com/RexTheGod/A-Rat')
	os.system('mv A-Rat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def adbtk():
	print('\n###### Installing ADB-Toolkit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	os.system('mv ADB-Toolkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androbugs():
	print('\n###### Installing AndroBugs_Framework')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install pymongo')
	os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
	os.system('mv AndroBugs_Framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tekdefense():
	print('\n###### Installing TekDefense-Automater')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	os.system('mv TekDefense-Automater {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def baf():
	print('\n###### Installing BAF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests bs4 selenium colored termcolor')
	os.system('git clone https://github.com/engMaher/BAF')
	os.system('mv BAF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutex():
	print('\n###### Installing BruteX')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git hydra -y')
	os.system('git clone https://github.com/1N3/BruteX')
	os.system('mv BruteX {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cmseek():
	print('\n###### Installing CMSeeK')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/Tuhinshubhra/CMSeeK')
	os.system('mv CMSeeK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cmsmap():
	print('\n###### Installing CMSmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/Dionach/CMSmap')
	os.system('mv CMSmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clickjacking():
	print('\n###### Installing Clickjacking-Tester')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/D4Vinci/Clickjacking-Tester')
	os.system('mv Clickjacking-Tester {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cookiestealer():
	print('\n###### Installing Cookie-stealer')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php -y')
	os.system('git clone https://github.com/Xyl2k/Cookie-stealer')
	os.system('mv Cookie-stealer {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dhcpig():
	print('\n###### Installing DHCPig')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/kamorin/DHCPig')
	os.system('mv DHCPig {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cyberscan():
	print('\n###### Installing CyberScan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/medbenali/CyberScan')
	os.system('mv CyberScan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dkmc():
	print('\n###### Installing DKMC')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/Mr-Un1k0d3r/DKMC')
	os.mkdir("DKMC/output")
	os.system('mv DKMC {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def crawlbox():
	print('\n###### Installing CrawlBox')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install tldextract requests requests_ntlm fake_useragent')
	os.system('git clone https://github.com/abaykan/CrawlBox')
	os.system('mv CrawlBox {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def eagleeye():
	print('\n###### Installing EagleEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install termcolor opencv-python selenium face_recognition WeasyPrint requests-html')
	os.system('git clone https://github.com/ThoughtfulDev/EagleEye')
	os.system('mv EagleEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gemailhack():
	print('\n###### Installing Gemail-Hack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/Ha3MrX/Gemail-Hack')
	os.system('mv Gemail-Hack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def eyewitness():
	print('\n###### Installing EyeWitness')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/FortyNorthSecurity/EyeWitness')
	os.system('mv EyeWitness {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def goblinwordgenerator():
	print('\n###### Installing GoblinWordGenerator')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/UndeadSec/GoblinWordGenerator')
	os.system('mv GoblinWordGenerator {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def inspy():
	print('\n###### Installing InSpy')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests==2.20.1 BeautifulSoup==3.2.1')
	os.system('git clone https://github.com/leapsecurity/InSpy')
	os.system('mv InSpy {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def leaked():
	print('\n###### Installing Leaked')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/GitHackTools/Leaked')
	os.system('mv Leaked {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gloomframework():
	print('\n###### Installing Gloom-Framework')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nmap python -y')
	os.system('python -m pip install mechanize pythonwhois')
	os.system('git clone https://github.com/StreetSec/Gloom-Framework')
	os.system('mv Gloom-Framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def lfisuite():
	print('\n###### Installing LFISuite')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/D35m0nd142/LFISuite')
	os.system('mv LFISuite {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def parsero():
	print('\n###### Installing Parsero')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/behindthefirewalls/Parsero')
	os.system('mv Parsero {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def pwnstar():
	print('\n###### Installing PwnSTAR')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/SilverFoxx/PwnSTAR')
	os.system('mv PwnSTAR {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def pybozocrack():
	print('\n###### Installing PyBozoCrack')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install wheel==0.22.0')
	os.system('git clone https://github.com/ikkebr/PyBozoCrack')
	os.system('mv PyBozoCrack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def pyrit():
	print('\n###### Installing Pyrit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install httplib2==0.10.3 colorlog==2.10.0 beautifulsoup4==4.5.3 protobuf==3.2.0rc2 requests==2.11.1 google==1.9.3')
	os.system('git clone https://github.com/JPaulMora/Pyrit')
	os.system('mv Pyrit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sn1per():
	print('\n###### Installing Sn1per')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/1N3/Sn1per')
	os.chdir("Sn1per")
	os.system("bash install.sh")
	os.chdir("..")
	os.system('mv Sn1per {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sublist3r():
	print('\n###### Installing Sublist3r')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install argparse dnspython requests')
	os.system('git clone https://github.com/aboul3la/Sublist3r')
	os.system('mv Sublist3r {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wppluginscanner():
	print('\n###### Installing WP-plugin-scanner')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/mintobit/WP-plugin-scanner')
	os.system('mv WP-plugin-scanner {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def whatweb():
	print('\n###### Installing WhatWeb')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/urbanadventurer/WhatWeb')
	os.system('mv WhatWeb {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def zerodoor():
	print('\n###### Installing Zerodoor')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git gcc nmap-ncat python2 -y')
	os.system('git clone https://github.com/Souhardya/Zerodoor')
	os.system('mv Zerodoor {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutespray():
	print('\n###### Installing brutespray')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install argcomplete==1.10.0')
	os.system('git clone https://github.com/x90skysn3k/brutespray')
	os.system('mv brutespray {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()


def pycdc():
	print('\n###### Installing pycdc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python clang cmake make -y')
	os.system('git clone https://github.com/zrax/pycdc')
	os.system('mv pycdc {}'.format(homeDir))
	os.chdir(homeDir)
	os.chdir("pycdc")
	os.system('cmake .')
	os.system('make')
	os.system('make check')
	os.chdir(current_dir)
	print('###### Done')
	backtomenu_option()

def apkid():
	print('\n###### Installing APKiD')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python yara yara-static -y')
	os.system('python -m pip install apkid')
	print('###### Done')
	print("###### Type 'apkid' to start.")
	backtomenu_option()

def dtlx():
	print('\n###### Installing DTL-X')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python git apktool apksigner openjdk-17 -y')
	os.system('python -m pip install loguru')
	os.system('git clone https://github.com/Gameye98/DTL-X')
	os.system('mv DTL-X {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def crowbar():
	print('\n###### Installing crowbar')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install paramiko==2.7.1')
	os.system('git clone https://github.com/galkan/crowbar')
	os.system('mv crowbar {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def voidLinux():
	print('\n###### Installing Void Linux')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install proot-distro')
	os.system('proot-distro install void')
	print("###### Type 'proot-distro login void' to start.")
	print('###### Done')
	backtomenu_option()

def apkleaks():
	print('\n###### Installing APKLeaks')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python -y')
	if not os.path.isfile(os.getenv("PREFIX")+"/bin/jadx"):
		os.system('apt install dpkg wget -y')
		os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
		os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
		os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	os.system('python -m pip install apkleaks')
	print('###### Done')
	print("###### Type 'apkleaks' to start.")
	print("###### Usage: apkleaks -f /path/file.apk")
	backtomenu_option()

def apkmitm():
	print('\n###### Installing apk-mitm')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nodejs apktool -y')
	os.system('npm i -g apk-mitm')
	open(os.getenv("HOME")+"/.bashrc","a").write("\nalias apk-mitm=\"apk-mitm --apktool $PREFIX/share/java/apktool.jar\"\n")
	print('###### Done')
	print("###### Type 'apk-mitm' to start.")
	print("###### Usage: apk-mitm /path/file.apk")
	backtomenu_option()

def ssl_pinning_remover():
	print('\n###### Installing ssl_pinning_remover')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python -y')
	os.system('python -m pip install ssl-pinning-remover')
	print('###### Done')
	print("###### Type 'ssl_pinning_remover' to start.")
	print("###### Usage: ssl_pinning_remover -i /path/file.apk -v")
	backtomenu_option()

def elpscrk():
	print('\n###### Installing elpscrk')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install colorama~=0.4.4 psutil~=5.8.0 click~=8.0.1 phonenumbers~=8.12.27')
	os.system('git clone https://github.com/D4Vinci/elpscrk')
	os.system('mv elpscrk {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def evilginx():
	print('\n###### Installing evilginx')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nginx python2 -y')
	os.system('git clone https://github.com/kgretzky/evilginx')
	os.system('mv evilginx {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fbht():
	print('\n###### Installing fbht')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('apt install python2-numpy')
	os.system('python2 -m pip install mechanize')
	os.system('git clone https://github.com/chinoogawa/fbht')
	os.system('mv fbht {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fierce():
	print('\n###### Installing fierce')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install dnspython==1.16.0 fierce')
	print('###### Done')
	print("###### Usage: fierce -h")
	backtomenu_option()

def fuxploider():
	print('\n###### Installing fuxploider')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install requests coloredlogs bs4')
	os.system('git clone https://github.com/almandin/fuxploider')
	os.system('mv fuxploider {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gasmask():
	print('\n###### Installing gasmask')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install validators python-whois dnspython requests shodan censys')
	os.system('git clone https://github.com/twelvesec/gasmask')
	os.system('mv gasmask {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

### Compiler/Interpreter
def python2():
	print('\n###### Installing Python2')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 -y')
	print('###### Done')
	print("###### Type 'python2' to start.")
	backtomenu_option()

def ecj():
	print('\n###### Installing ecj')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ecj -y')
	print('###### Done')
	print("###### Type 'ecj' to start.")
	backtomenu_option()

def golang():
	print('\n###### Installing Golang')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install golang -y')
	print('###### Done')
	print("###### Type 'go' to start.")
	backtomenu_option()

def ldc():
	print('\n###### Installing ldc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ldc -y')
	print('###### Done')
	print("###### Type 'ldc2' to start.")
	backtomenu_option()

def nim():
	print('\n###### Installing Nim')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nim -y')
	print('###### Done')
	print("###### Type 'nim' to start.")
	backtomenu_option()

def shc():
	print('\n###### Installing shc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install shc -y')
	print('###### Done')
	print("###### Type 'shc' to start.")
	backtomenu_option()

def tcc():
	print('\n###### Installing TCC')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install tcc -y')
	print('###### Done')
	print("###### Type 'tcc' to start.")
	backtomenu_option()

def php():
	print('\n###### Installing PHP')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php -y')
	print('###### Done')
	print("###### Type 'php' to start.")
	backtomenu_option()

def ruby():
	print('\n###### Installing Ruby')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install ruby -y')
	print('###### Done')
	print("###### Type 'ruby' to start.")
	backtomenu_option()

def perl():
	print('\n###### Installing Perl')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install perl -y')
	print('###### Done')
	print("###### Type 'perl' to start.")
	backtomenu_option()

def vlang():
	print('\n###### Installing Vlang')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install vlang -y')
	print('###### Done')
	print("###### Type 'vlang' to start.")
	backtomenu_option()

def blogc():
	print('\n###### Installing BlogC')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install blogc -y')
	print('###### Done')
	print("###### Type 'blogc' to start.")
	backtomenu_option()

def dart():
	print('\n###### Installing Dart')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dart -y')
	print('###### Done')
	print("###### Type 'dart' to start.")
	backtomenu_option()

def yasm():
	print('\n###### Installing Yasm')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install yasm -y')
	print('###### Done')
	print("###### Type 'yasm' to start.")
	backtomenu_option()

def nasm():
	print('\n###### Installing Nasm')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nasm -y')
	print('###### Done')
	print("###### Type 'nasm' to start.")
	backtomenu_option()

### termux games
def street_car():
	print('\n###### Installing street-car')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python python2 -y')
	os.system('git clone https://github.com/JustaHackers/street_car')
	os.system('mv street_car {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def flappy_bird():
	print('\n###### Installing flappy-bird')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/flappy_bird')
	os.system('mv flappy_bird {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def speed_typing():
	print('\n###### Installing Speed Typing')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/typing-speed-test')
	os.system('mv typing-speed-test {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nsnake():
	print('\n###### Installing nsnake')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nsnake -y')
	print('###### Done')
	print("###### Type 'nsnake' to start.")
	backtomenu_option()

def nudoku():
	print('\n###### Installing Sudoku')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nudoku -y')
	print('###### Done')
	print("###### Type 'nudoku' to start.")
	backtomenu_option()

def moon_buggy():
	print('\n###### Installing Moon-Buggy')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install moon-buggy -y')
	print('###### Done')
	print("###### Type 'moon-buggy' to start.")
	backtomenu_option()

def ttysolitaire():
	print('\n###### Installing tty-solitaire')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install tty-solitaire -y')
	print('###### Done')
	print("###### Type 'ttysolitaire' to start.")
	backtomenu_option()

def pacman4console():
	print('\n###### Installing Pacman4Console')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install pacman4console -y')
	print('###### Done')
	print("###### Type 'pacman' to start.")
	backtomenu_option()

### bash function ---
def fbvid():
	print('\n###### Installing fbvid')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python ffmpeg -y')
	os.system('python -m pip install youtube-dl')
	fbvid_code = open(".myshfunc/fbvid.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(fbvid_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: fbvid "POST_URL"')
	backtomenu_option()

def cast2video():
	print('\n###### Installing cast2video')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install clang python ffmpeg -y')
	os.system('python -m pip install CPython ttygif')
	cast2video_code = open(".myshfunc/cast2video.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(cast2video_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: cast2video file.cast')
	backtomenu_option()

def iconset():
	print('\n###### Installing iconset')
	iconset_code = open(".myshfunc/iconset.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(iconset_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: iconset project_name icon.png')
	backtomenu_option()

def readme():
	print('\n###### Installing readme')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install curl -y')
	readme_code = open(".myshfunc/readme.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(readme_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: readme User/Repo')
	backtomenu_option()

def makedeb():
	print('\n###### Installing makedeb')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install dpkg neovim -y')
	makedeb_code = open(".myshfunc/makedeb.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(makedeb_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: makedeb')
	backtomenu_option()

def quikfind():
	print('\n###### Installing quikfind')
	quikfind_code = open(".myshfunc/quikfind.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(quikfind_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: quikfind')
	backtomenu_option()

def pranayama():
	print('\n###### Installing pranayama')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install termux-api -y')
	pranayama_code = open(".myshfunc/pranayama.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(pranayama_code)
	os.system('source '+os.getenv("HOME")+"./bashrc")
	print('###### Done')
	print('###### Usage: pranayama')
	print('######            or')
	print('######        pranayama [n]')
	backtomenu_option()

def sqlc():
	print('\n###### Installing sqlc')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python sqlite3 -y')
	sqlc_code = open(".myshfunc/sqlc.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(sqlc_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: sqlc db_file sql_script')
	backtomenu_option()