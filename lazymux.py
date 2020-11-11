## lazymux.py - Lazymux v4.0
##
import os, sys
import readline
from time import sleep as timeout
from core.lzmcore import *

def main():
	banner()
	print("   [01] Information Gathering")
	print("   [02] Vulnerability Analysis")
	print("   [03] Web Hacking")
	print("   [04] Database Assessment")
	print("   [05] Password Attacks")
	print("   [06] Wireless Attacks")
	print("   [07] Reverse Engineering")
	print("   [08] Exploitation Tools")
	print("   [09] Sniffing and Spoofing")
	print("   [10] Reporting Tools")
	print("   [11] Forensic Tools")
	print("   [12] Stress Testing")
	print("   [13] Install Linux Distro")
	print("   [14] Termux Utility")
	print("   [15] Shell Function [.bashrc]")
	print("   [16] Install CLI Games")
	print("\n   [00] Exit the Lazymux\n")
	lazymux = input("lzmx > set_install ")

	# 01 - Information Gathering
	if lazymux.strip() == "1" or lazymux.strip() == "01":
		print("\n    [01] Nmap: Utility for network discovery and security auditing")
		print("    [02] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
		print("    [03] D-TECT: All-In-One Tool for Penetration Testing")
		print("    [04] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [05] Infoga: Tool for Gathering Email Accounts Informations")
		print("    [06] ReconDog: Information Gathering and Vulnerability Scanner tool")
		print("    [07] AndroZenmap")
		print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [09] AstraNmap: Security scanner used to find hosts and services on a computer network")
		print("    [10] weeman: HTTP server for phishing in python")
		print("    [11] Easymap: Nmap Shortcut")
		print("    [12] BlackBox: A Penetration Testing Framework")
		print("    [13] XD3v: Powerful tool that lets you know all the essential details about your phone")
		print("    [14] Crips: This Tools is a collection of online IP Tools that can be used to quickly get information about IP Address's, Web Pages and DNS records")
		print("    [15] SIR: Resolve from the net the last known ip of a Skype Name")
		print("    [16] EvilURL: Generate unicode evil domains for IDN Homograph Attack and detect them")
		print("    [17] Striker: Recon & Vulnerability Scanning Suite")
		print("    [18] Xshell: ToolKit")
		print("    [19] OWScan: OVID Web Scanner")
		print("    [20] OSIF: Open Source Information Facebook")
		print("    [21] Devploit: Simple Information Gathering Tool")
		print("    [22] Namechk: Osint tool based on namechk.com for checking usernames on more than 100 websites, forums and social networks")
		print("    [23] AUXILE: Web Application Analysis Framework")
		print("    [24] inther: Information gathering using shodan, censys and hackertarget")
		print("    [25] GINF: GitHub Information Gathering Tool")
		print("    [26] GPS Tracking")
		print("    [27] ASU: Facebook Hacking ToolKit")
		print("    [28] fim: Facebook Image Downloader")
		print("    [29] MaxSubdoFinder: Tool for Discovering Subdomain")
		print("    [30] pwnedOrNot: OSINT Tool for Finding Passwords of Compromised Email Accounts")
		print("    [31] Mac-Lookup: Finds information about a Particular Mac address")
		print("    [32] BillCipher: Information Gathering tool for a Website or IP address")
		print("    [33] dnsrecon: Security assessment and network troubleshooting")
		print("    [34] zphisher: Automated Phishing Tool")
		print("    [35] Mr.SIP: SIP-Based Audit and Attack Tool")
		print("    [36] Sherlock: Hunt down social media accounts by username")
		print("    [37] userrecon: Find usernames across over 75 social networks")
		print("    [38] PhoneInfoga: One of the most advanced tools to scan phone numbers using only free resources")
		print("\n    [00] Back to main menu\n")
		infogathering = input("lzmx > set_install ")
		if infogathering == "@":
			infogathering = ""
			for x in range(1,38):
				infogathering += f"{x} "
		if len(infogathering.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for infox in infogathering.split():
			if infox.strip() == "01" or infox.strip() == "1": nmap()
			elif infox.strip() == "02" or infox.strip() == "2": red_hawk()
			elif infox.strip() == "03" or infox.strip() == "3": dtect()
			elif infox.strip() == "04" or infox.strip() == "4": sqlmap()
			elif infox.strip() == "05" or infox.strip() == "5": infoga()
			elif infox.strip() == "06" or infox.strip() == "6": reconDog()
			elif infox.strip() == "07" or infox.strip() == "7": androZenmap()
			elif infox.strip() == "08" or infox.strip() == "8": sqlmate()
			elif infox.strip() == "09" or infox.strip() == "9": astraNmap()
			elif infox.strip() == "10": weeman()
			elif infox.strip() == "11": easyMap()
			elif infox.strip() == "12": blackbox()
			elif infox.strip() == "13": xd3v()
			elif infox.strip() == "14": crips()
			elif infox.strip() == "15": sir()
			elif infox.strip() == "16": evilURL()
			elif infox.strip() == "17": striker()
			elif infox.strip() == "18": xshell()
			elif infox.strip() == "19": owscan()
			elif infox.strip() == "20": osif()
			elif infox.strip() == "21": devploit()
			elif infox.strip() == "22": namechk()
			elif infox.strip() == "23": auxile()
			elif infox.strip() == "24": inther()
			elif infox.strip() == "25": ginf()
			elif infox.strip() == "26": gpstr()
			elif infox.strip() == "27": asu()
			elif infox.strip() == "28": fim()
			elif infox.strip() == "29": maxsubdofinder()
			elif infox.strip() == "30": pwnedOrNot()
			elif infox.strip() == "31": maclook()
			elif infox.strip() == "32": billcypher()
			elif infox.strip() == "33": dnsrecon()
			elif infox.strip() == "34": zphisher()
			elif infox.strip() == "35": mrsip()
			elif infox.strip() == "36": sherlock()
			elif infox.strip() == "37": userrecon()
			elif infox.strip() == "38": phoneinfoga()
			elif infox.strip() == "00" or infox.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 02 - Vulnerability Analysis
	elif lazymux.strip() == "2" or lazymux.strip() == "02":
		print("\n    [01] Nmap: Utility for network discovery and security auditing")
		print("    [02] AndroZenmap")
		print("    [03] AstraNmap: Security scanner used to find hosts and services on a computer network")
		print("    [04] Easymap: Nmap Shortcut")
		print("    [05] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
		print("    [06] D-TECT: All-In-One Tool for Penetration Testing")
		print("    [07] Damn Small SQLi Scanner: A fully functional SQL injection vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code")
		print("    [08] SQLiv: massive SQL injection vulnerability scanner")
		print("    [09] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [10] sqlscan: Quick SQL Scanner, Dorker, Webshell injector PHP")
		print("    [11] Wordpresscan: WPScan rewritten in Python + some WPSeku ideas")
		print("    [12] WPScan: Free wordPress security scanner")
		print("    [13] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [14] termux-wordpresscan")
		print("    [15] TM-scanner: websites vulnerability scanner for termux")
		print("    [16] Rang3r: Multi Thread IP + Port Scanner")
		print("    [17] Striker: Recon & Vulnerability Scanning Suite")
		print("    [18] Routersploit: Exploitation Framework for Embedded Devices")
		print("    [19] Xshell: ToolKit")
		print("    [20] SH33LL: Shell Scanner")
		print("    [21] BlackBox: A Penetration Testing Framework")
		print("    [22] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
		print("    [23] OWScan: OVID Web Scanner")
		print("\n    [00] Back to main menu\n")
		vulnsys = input("lzmx > set_install ")
		if vulnsys == "@":
			vulnsys = ""
			for x in range(1,24):
				vulnsys += f"{x} "
		if len(vulnsys.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for vulnx in vulnsys.split():
			if vulnsys.strip() == "01" or vulnsys.strip() == "1": nmap()
			elif vulnsys.strip() == "02" or vulnsys.strip() == "2": androZenmap()
			elif vulnsys.strip() == "03" or vulnsys.strip() == "3": astraNmap()
			elif vulnsys.strip() == "04" or vulnsys.strip() == "4": easyMap()
			elif vulnsys.strip() == "05" or vulnsys.strip() == "5": red_hawk()
			elif vulnsys.strip() == "06" or vulnsys.strip() == "6": dtect()
			elif vulnsys.strip() == "07" or vulnsys.strip() == "7": dsss()
			elif vulnsys.strip() == "08" or vulnsys.strip() == "8": sqliv()
			elif vulnsys.strip() == "09" or vulnsys.strip() == "9": sqlmap()
			elif vulnsys.strip() == "10": sqlscan()
			elif vulnsys.strip() == "11": wordpreSScan()
			elif vulnsys.strip() == "12": wpscan()
			elif vulnsys.strip() == "13": sqlmate()
			elif vulnsys.strip() == "14": wordpresscan()
			elif vulnsys.strip() == "15": tmscanner()
			elif vulnsys.strip() == "16": rang3r()
			elif vulnsys.strip() == "17": striker()
			elif vulnsys.strip() == "18": routersploit()
			elif vulnsys.strip() == "19": xshell()
			elif vulnsys.strip() == "20": sh33ll()
			elif vulnsys.strip() == "21": blackbox()
			elif vulnsys.strip() == "22": xattacker()
			elif vulnsys.strip() == "23": owscan()
			elif vulnsys.strip() == "00" or vulnsys.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)

	# 03 - Web Hacking
	elif lazymux.strip() == "3" or lazymux.strip() == "03":
		print("\n    [01] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [02] WebDAV: WebDAV File Upload Exploiter")
		print("    [03] MaxSubdoFinder: Tool for Discovering Subdomain")
		print("    [04] Webdav Mass Exploit")
		print("    [05] Atlas: Quick SQLMap Tamper Suggester")
		print("    [06] sqldump: Dump sql result sites with easy")
		print("    [07] Websploit: An advanced MiTM Framework")
		print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [09] inther: Information gathering using shodan, censys and hackertarget")
		print("    [10] HPB: HTML Pages Builder")
		print("    [11] Xshell: ToolKit")
		print("    [12] SH33LL: Shell Scanner")
		print("    [13] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
		print("    [14] XSStrike: Most advanced XSS Scanner")
		print("    [15] Breacher: An advanced multithreaded admin panel finder")
		print("    [16] OWScan: OVID Web Scanner")
		print("    [17] ko-dork: A simple vuln web scanner")
		print("    [18] ApSca: Powerful web penetration application")
		print("    [19] amox: Find backdoor or shell planted on a site via dictionary attack")
		print("    [20] FaDe: Fake deface with kindeditor, fckeditor and webdav")
		print("    [21] AUXILE: Auxile Framework")
		print("    [22] xss-payload-list: Cross Site Scripting ( XSS ) Vulnerability Payload List")
		print("\n    [00] Back to main menu\n")
		webhack = input("lzmx > set_install ")
		if webhack == "@":
			webhack = ""
			for x in range(1,23):
				webhack += f"{x} "
		if len(webhack.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for webhx in webhack.split():
			if webhx.strip() == "01" or webhx.strip() == "1": sqlmap()
			elif webhx.strip() == "02" or webhx.strip() == "2": webdav()
			elif webhx.strip() == "03" or webhx.strip() == "3": maxsubdofinder()
			elif webhx.strip() == "04" or webhx.strip() == "4": webmassploit()
			elif webhx.strip() == "05" or webhx.strip() == "5": atlas()
			elif webhx.strip() == "06" or webhx.strip() == "6": sqldump()
			elif webhx.strip() == "07" or webhx.strip() == "7": websploit()
			elif webhx.strip() == "08" or webhx.strip() == "8": sqlmate()
			elif webhx.strip() == "09" or webhx.strip() == "9": inther()
			elif webhx.strip() == "10": hpb()
			elif webhx.strip() == "11": xshell()
			elif webhx.strip() == "12": sh33ll()
			elif webhx.strip() == "13": xattacker()
			elif webhx.strip() == "14": xsstrike()
			elif webhx.strip() == "15": breacher()
			elif webhx.strip() == "16": owscan()
			elif webhx.strip() == "17": kodork()
			elif webhx.strip() == "18": apsca()
			elif webhx.strip() == "19": amox()
			elif webhx.strip() == "20": fade()
			elif webhx.strip() == "21": auxile()
			elif webhx.strip() == "22": xss_payload_list()
			elif webhx.strip() == "00" or webhx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 04 - Database Assessment
	elif lazymux.strip() == "4" or lazymux.strip() == "04":
		print("\n    [01] DbDat: DbDat performs numerous checks on a database to evaluate security")
		print("    [02] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [03] NoSQLMap: Automated NoSQL database enumeration and web application exploitation tool")
		print("    [04] audit_couchdb: Detect security issues, large or small, in a CouchDB server")
		print("    [05] mongoaudit: An automated pentesting tool that lets you know if your MongoDB instances are properly secured")
		print("\n    [00] Back to main menu\n")
		dbssm = input("lzmx > set_install ")
		if dbssm == "@":
			dbssm = ""
			for x in range(1,6):
				dbssm += f"{x} "
		if len(dbssm.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for dbsx in dbssm.split():
			if dbsx.strip() == "01" or dbsx.strip() == "1": dbdat()
			elif dbsx.strip() == "02" or dbsx.strip() == "2": sqlmap()
			elif dbsx.strip() == "03" or dbsx.strip() == "3": nosqlmap
			elif dbsx.strip() == "04" or dbsx.strip() == "4": audit_couchdb()
			elif dbsx.strip() == "05" or dbsx.strip() == "5": mongoaudit()
			elif dbsx.strip() == "00" or dbsx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 05 - Password Attacks
	elif lazymux.strip() == "5" or lazymux.strip() == "05":
		print("\n    [01] Hydra: Network logon cracker supporting different services")
		print("    [02] FMBrute: Facebook Multi Brute Force")
		print("    [03] HashID: Software to identify the different types of hashes")
		print("    [04] Facebook Brute Force 3")
		print("    [05] Black Hydra: A small program to shorten brute force sessions on hydra")
		print("    [06] Hash Buster: Crack hashes in seconds")
		print("    [07] FBBrute: Facebook Brute Force")
		print("    [08] Cupp: Common User Passwords Profiler")
		print("    [09] InstaHack: Instagram Brute Force")
		print("    [10] Indonesian Wordlist")
		print("    [11] Xshell")
		print("    [12] Aircrack-ng: WiFi security auditing tools suite")
		print("    [13] BlackBox: A Penetration Testing Framework")
		print("    [14] Katak: An open source software login brute-forcer toolkit and hash decrypter")
		print("    [15] Hasher: Hash cracker with auto detect hash")
		print("    [16] Hash-Generator: Beautiful Hash Generator")
		print("    [17] nk26: Nkosec Encode")
		print("    [18] Hasherdotid: A tool for find an encrypted text")
		print("    [19] Crunch: Highly customizable wordlist generator")
		print("    [20] Hashcat: World's fastest and most advanced password recovery utility")
		print("    [21] ASU: Facebook Hacking ToolKit")
		print("\n    [00] Back to main menu\n")
		passtak = input("lzmx > set_install ")
		if passtak == "@":
			passtak = ""
			for x in range(1,22):
				passtak += f"{x} "
		if len(passtak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for passx in passtak.split():
			if passx.strip() == "01" or passx.strip() == "1": hydra()
			elif passx.strip() == "02" or passx.strip() == "2": fmbrute()
			elif passx.strip() == "03" or passx.strip() == "3": hashid()
			elif passx.strip() == "04" or passx.strip() == "4": fbBrute()
			elif passx.strip() == "05" or passx.strip() == "5": black_hydra()
			elif passx.strip() == "06" or passx.strip() == "6": hash_buster()
			elif passx.strip() == "07" or passx.strip() == "7": fbbrutex()
			elif passx.strip() == "08" or passx.strip() == "8": cupp()
			elif passx.strip() == "09" or passx.strip() == "9": instaHack()
			elif passx.strip() == "10": indonesian_wordlist()
			elif passx.strip() == "11": xshell()
			elif passx.strip() == "12": aircrackng()
			elif passx.strip() == "13": blackbox()
			elif passx.strip() == "14": katak()
			elif passx.strip() == "15": hasher()
			elif passx.strip() == "16": hashgenerator()
			elif passx.strip() == "17": nk26()
			elif passx.strip() == "18": hasherdotid()
			elif passx.strip() == "19": crunch()
			elif passx.strip() == "20": hashcat()
			elif passx.strip() == "21": asu()
			elif passx.strip() == "00" or passx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 06 - Wireless Attacks
	elif lazymux.strip() == "6" or lazymux.strip() == "06":
		print("\n    [01] Aircrack-ng: WiFi security auditing tools suite")
		print("    [02] Wifite: An automated wireless attack tool")
		print("    [03] Wifiphisher: The Rogue Access Point Framework")
		print("    [04] Routersploit: Exploitation Framework for Embedded Devices")
		print("\n    [00] Back to main menu\n")
		wiretak = input("lzmx > set_install ")
		if wiretak == "@":
			wiretak = ""
			for x in range(1,5):
				wiretak += f"{x} "
		if len(wiretak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for wirex in wiretak.split():
			if wirex.strip() == "01" or wirex.strip() == "1": aircrackng()
			elif wirex.strip() == "02" or wirex.strip() == "2": wifite()
			elif wirex.strip() == "03" or wirex.strip() == "3": wifiphisher()
			elif wirex.strip() == "04" or wirex.strip() == "4": routersploit()
			elif wirex.strip() == "00" or wirex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 07 - Reverse Engineering
	elif lazymux.strip() == "7" or lazymux.strip() == "07":
		print("\n    [01] Binary Exploitation")
		print("    [02] jadx: DEX to JAVA Decompiler")
		print("    [03] apktool: A utility that can be used for reverse engineering Android applications")
		print("    [04] uncompyle6: Python cross-version byte-code decompiler")
		print("    [05] ddcrypt: DroidScript APK Deobfuscator")
		print("\n    [00] Back to main menu\n")
		reversi = input("lzmx > set_install ")
		if reversi == "@":
			reversi = ""
			for x in range(1,6):
				reversi += f"{x} "
		if len(reversi.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for revex in reversi.split():
			if revex.strip() == "01" or revex.strip() == "1": binploit()
			elif revex.strip() == "02" or revex.strip() == "2": jadx()
			elif revex.strip() == "03" or revex.strip() == "3": apktool()
			elif revex.strip() == "04" or revex.strip() == "4": uncompyle()
			elif revex.strip() == "05" or revex.strip() == "5": ddcrypt()
			elif revex.strip() == "00" or revex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 08 - Exploitation Tools
	elif lazymux.strip() == "8" or lazymux.strip() == "08":
		print("\n    [01] Metasploit: Advanced open-source platform for developing, testing and using exploit code")
		print("    [02] commix: Automated All-in-One OS Command Injection and Exploitation Tool")
		print("    [03] BlackBox: A Penetration Testing Framework")
		print("    [04] Brutal: Payload for teensy like a rubber ducky but the syntax is different")
		print("    [05] TXTool: An easy pentesting tool")
		print("    [06] XAttacker: Website Vulnerability Scanner & Auto Exploiter")  
		print("    [07] Websploit: An advanced MiTM Framework")
		print("    [08] Routersploit: Exploitation Framework for Embedded Devices")
		print("\n    [00] Back to main menu\n")
		exploitool = input("lzmx > set_install ")
		if exploitool == "@":
			exploitool = ""
			for x in range(1,9):
				exploitool += f"{x} "
		if len(exploitool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for explx in exploitool.split():
			if explx.strip() == "01" or explx.strip() == "1": metasploit()
			elif explx.strip() == "02" or explx.strip() == "2": commix()
			elif explx.strip() == "03" or explx.strip() == "3": blackbox()
			elif explx.strip() == "04" or explx.strip() == "4": brutal()
			elif explx.strip() == "05" or explx.strip() == "5": txtool()
			elif explx.strip() == "06" or explx.strip() == "6": xattacker()
			elif explx.strip() == "07" or explx.strip() == "7": websploit()
			elif explx.strip() == "08" or explx.strip() == "8": routersploit()
			elif explx.strip() == "00" or explx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 09 - Sniffing and Spoofing
	elif lazymux.strip() == "9" or lazymux.strip() == "09":
		print("\n    [01] KnockMail: Verify if Email Exists")
		print("    [02] tcpdump: A powerful command-line packet analyzer")
		print("    [03] Hac")
		print("    [04] hping3: hping is a command-line oriented TCP/IP packet assembler/analyzer")
		print("    [05] SocialFish: Educational Phishing Tool & Information Collector")
		print("    [06] santet-online: Social Engineering Tool")
		print("    [07] SpazSMS: Send unsolicited messages repeatedly on the same phone number")
		print("    [08] LiteOTP: Multi Spam SMS OTP")
		print("    [09] tshark: Network protocol analyzer and sniffer")
		print("    [10] Ettercap: Comprehensive suite for MITM attacks, can sniff live connections, do content filtering on the fly and much more")
		print("\n    [00] Back to main menu\n")
		sspoof = input("lzmx > set_install ")
		if sspoof == "@":
			sspoof = ""
			for x in range(1,11):
				sspoof += f"{x} "
		if len(sspoof.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for sspx in sspoof.split():
			if sspx.strip() == "01" or sspx.strip() == "1": knockmail()
			elif sspx.strip() == "02" or sspx.strip() == "2": tcpdump()
			elif sspx.strip() == "03" or sspx.strip() == "3": hac()
			elif sspx.strip() == "04" or sspx.strip() == "4": hping3()
			elif sspx.strip() == "05" or sspx.strip() == "5": socfish()
			elif sspx.strip() == "06" or sspx.strip() == "6": sanlen()
			elif sspx.strip() == "07" or sspx.strip() == "7": spazsms()
			elif sspx.strip() == "08" or sspx.strip() == "8": liteotp()
			elif sspx.strip() == "09" or sspx.strip() == "9": tshark()
			elif sspx.strip() == "10": ettercap()
			elif sspx.strip() == "00" or sspx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 10 - Reporting Tools
	elif lazymux.strip() == "10":
		print("\n    [01] dos2unix: Converts between DOS and Unix text files")
		print("    [02] exiftool: Utility for reading, writing and editing meta information in a wide variety of files")
		print("    [03] iconv: Utility converting between different character encodings")
		print("    [04] mediainfo: Command-line utility for reading information from media files")
		print("    [05] pdfinfo: PDF document information extractor")
		print("\n    [00] Back to main menu\n")
		reportls = input("lzmx > set_install ")
		if reportls == "@":
			reportls = ""
			for x in range(1,6):
				reportls += f"{x} "
		if len(reportls.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for reportx in reportls.split():
			if reportx.strip() == "01" or reportx.strip() == "1": dos2unix()
			elif reportx.strip() == "02" or reportx.strip() == "2": exiftool()
			elif reportx.strip() == "03" or reportx.strip() == "3": iconv()
			elif reportx.strip() == "04" or reportx.strip() == "4": mediainfo()
			elif reportx.strip() == "05" or reportx.strip() == "5": pdfinfo()
			elif reportx.strip() == "00" or reportx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 11 - Forensic Tools
	elif lazymux.strip() == "11":
		print("\n    [01] steghide: Embeds a message in a file by replacing some of the least significant bits")
		print("    [02] tesseract: Tesseract is probably the most accurate open source OCR engine available")
		print("    [03] sleuthkit: The Sleuth Kit (TSK) is a library for digital forensics tools")
		print("\n    [00] Back to main menu\n")
		forensc = input("lzmx > set_install ")
		if forensc == "@":
			forensc = ""
			for x in range(1,4):
				forensc += f"{x} "
		if len(forensc.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for forenx in forensc.split():
			if forenx.strip() == "01" or forenx.strip() == "1": steghide()
			elif forenx.strip() == "02" or forenx.strip() == "2": tesseract()
			elif forenx.strip() == "03" or forenx.strip() == "3": sleuthkit()
			elif forenx.strip() == "00" or forenx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 12 - Stress Testing
	elif lazymux.strip() == "12":
		print("\n    [01] Torshammer: Slow post DDOS tool")
		print("    [02] Slowloris: Low bandwidth DoS tool")
		print("    [03] Fl00d & Fl00d2: UDP Flood tool")
		print("    [04] GoldenEye: GoldenEye Layer 7 (KeepAlive+NoCache) DoS test tool")
		print("    [05] Xerxes: The most powerful DoS tool")
		print("    [06] Planetwork-DDOS")
		print("    [07] Xshell")
		print("    [08] santet-online: Social Engineering Tool")
		print("\n    [00] Back to main menu\n")
		stresstest = input("lzmx > set_install ")
		if stresstest == "@":
			stresstest = ""
			for x in range(1,9):
				stresstest += f"{x} "
		if len(stresstest.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for stressx in stresstest.split():
			if stressx.strip() == "01" or stressx.strip() == "1": torshammer()
			elif stressx.strip() == "02" or stressx.strip() == "2": slowloris()
			elif stressx.strip() == "03" or stressx.strip() == "3": fl00d12()
			elif stressx.strip() == "04" or stressx.strip() == "4": goldeneye()
			elif stressx.strip() == "05" or stressx.strip() == "5": xerxes()
			elif stressx.strip() == "06" or stressx.strip() == "6": planetwork_ddos()
			elif stressx.strip() == "07" or stressx.strip() == "7": xshell()
			elif stressx.strip() == "08" or stressx.strip() == "8": sanlen()
			elif stressx.strip() == "00" or stressx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 13 - Install Linux Distro
	elif lazymux.strip() == "13":
		print("\n    [01] Ubuntu")
		print("    [02] Fedora")
		print("    [03] Kali Nethunter")
		print("    [04] Parrot")
		print("    [05] Arch Linux")
		print("\n    [00] Back to main menu\n")
		innudis = input("lzmx > set_install ")
		if innudis == "@":
			innudis = ""
			for x in range(1,6):
				innudis += f"{x} "
		if len(innudis.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for innux in innudis.split():
			if innux.strip() == "01" or innux.strip() == "1": ubuntu()
			elif innux.strip() == "02" or innux.strip() == "2": fedora()
			elif innux.strip() == "03" or innux.strip() == "3": nethunter()
			elif innux.strip() == "04" or innux.strip() == "4": parrot()
			elif innux.strip() == "05" or innux.strip() == "5": archlinux()
			elif innux.strip() == "00" or innux.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 14 - Termux Utility
	elif lazymux.strip() == "14":
		print("\n    [01] SpiderBot: Curl website using random proxy and user agent")
		print("    [02] Ngrok: tunnel local ports to public URLs and inspect traffic")
		print("    [03] Sudo: sudo installer for Android")
		print("    [04] google: Python bindings to the Google search engine")
		print("    [05] kojawafft")
		print("    [06] ccgen: Credit Card Generator")
		print("    [07] VCRT: Virus Creator")
		print("    [08] E-Code: PHP Script Encoder")
		print("    [09] Termux-Styling")
		print("    [11] xl-py: XL Direct Purchase Package")
		print("    [12] BeanShell: A small, free, embeddable Java source interpreter with object scripting language features, written in Java")
		print("    [13] vbug: Virus Maker")
		print("    [14] Crunch: Highly customizable wordlist generator")
		print("    [15] Textr: Simple tool for running text")
		print("    [16] heroku: CLI to interact with Heroku")
		print("    [17] RShell: Reverse shell for single listening")
		print("    [18] TermPyter: Fix all error Jupyter installation on termux")
		print("    [19] F4K3: Fake User Data Generator")
		print("    [20] shc: Shell script compiler")
		print("    [21] Octave: Scientific Programming Language")
		print("    [22] fp-compiler: Free Pascal is a 32, 64 and 16 bit professional Pascal compiler")
		print("    [23] Numpy: The fundamental package for scientific computing with Python")
		print("    [24] ClickBot: Earn money using telegram bot")
		print("\n    [00] Back to main menu\n")
		moretool = input("lzmx > set_install ")
		if moretool == "@":
			moretool = ""
			for x in range(1,24):
				moretool += f"{x} "
		if len(moretool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for moret in moretool.split():
			if moret.strip() == "01" or moret.strip() == "1": spiderbot()
			elif moret.strip() == "02" or moret.strip() == "2": ngrok()
			elif moret.strip() == "03" or moret.strip() == "3": sudo()
			elif moret.strip() == "04" or moret.strip() == "4": google()
			elif moret.strip() == "05" or moret.strip() == "5": kojawafft()
			elif moret.strip() == "06" or moret.strip() == "6": ccgen()
			elif moret.strip() == "07" or moret.strip() == "7": vcrt()
			elif moret.strip() == "08" or moret.strip() == "8": ecode()
			elif moret.strip() == "09" or moret.strip() == "9": stylemux()
			elif moret.strip() == "10": passgencvar()
			elif moret.strip() == "11": xlPy()
			elif moret.strip() == "12": beanshell()
			elif moret.strip() == "13": vbug()
			elif moret.strip() == "14": crunch()
			elif moret.strip() == "15": textr()
			elif moret.strip() == "16": heroku()
			elif moret.strip() == "17": rshell()
			elif moret.strip() == "18": termpyter()
			elif moret.strip() == "19": f4k3()
			elif moret.strip() == "20": shc()
			elif moret.strip() == "21": octave()
			elif moret.strip() == "22": fpcompiler()
			elif moret.strip() == "23": numpy()
			elif moret.strip() == "24": clickbot()
			elif moret.strip() == "00" or moret.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 15 - Shell Function [.bashrc]
	elif lazymux.strip() == "15":
		print("\n    [01] FBVid (FB Video Downloader)")
		print("    [02] cast2video (Asciinema Cast Converter)")
		print("    [03] iconset (AIDE App Icon)")
		print("    [04] readme (GitHub README.md)")
		print("    [05] makedeb (DEB Package Builder)")
		print("    [06] quikfind (Search Files)")
		print("    [07] pranayama (4-7-8 Relax Breathing)")
		print("    [08] sqlc (SQLite Query Processor)")
		print("\n    [00] Back to main menu\n")
		myshf = input("lzmx > set_install ")
		if myshf == "@":
			myshf = ""
			for x in range(1,9):
				myshf += f"{x} "
		if len(myshf.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for mysh in myshf.split():
			if mysh.strip() == "01" or mysh.strip() == "1": fbvid()
			elif mysh.strip() == "02" or mysh.strip() == "2": cast2video()
			elif mysh.strip() == "03" or mysh.strip() == "3": iconset()
			elif mysh.strip() == "04" or mysh.strip() == "4": readme()
			elif mysh.strip() == "05" or mysh.strip() == "5": makedeb()
			elif mysh.strip() == "06" or mysh.strip() == "6": quikfind()
			elif mysh.strip() == "07" or mysh.strip() == "7": pranayama()
			elif mysh.strip() == "08" or mysh.strip() == "8": sqlc()
			elif mysh.strip() == "00" or mysh.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 16 - Install CLI Games
	elif lazymux.strip() == "16":
		print("\n    [01] Flappy Bird")
		print("    [02] Street Car")
		print("    [03] Speed Typing")
		print("    [04] NSnake: The classic snake game with textual interface")
		print("    [05] Moon buggy: Simple game where you drive a car across the moon's surface")
		print("    [06] Nudoku: ncurses based sudoku game")
		print("    [07] tty-solitaire")
		print("    [08] Pacman4Console")
		print("\n    [00] Back to main menu\n")
		cligam = input("lzmx > set_install ")
		if cligam == "@":
			cligam = ""
			for x in range(1,23):
				cligam += f"{x} "
		if len(cligam.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for clig in cligam.split():
			if clig.strip() == "01" or clig.strip() == "1": flappy_bird()
			elif clig.strip() == "02" or clig.strip() == "2": street_car()
			elif clig.strip() == "03" or clig.strip() == "3": speed_typing()
			elif clig.strip() == "04" or clig.strip() == "4": nsnake()
			elif clig.strip() == "05" or clig.strip() == "5": moon_buggy()
			elif clig.strip() == "06" or clig.strip() == "6": nudoku()
			elif clig.strip() == "07" or clig.strip() == "7": ttysolitaire()
			elif clig.strip() == "08" or clig.strip() == "8": pacman4console()
			elif clig.strip() == "00" or clig.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	elif lazymux.strip() == "00":
		sys.exit()
	
	else:
		print("\nERROR: Wrong Input")
		timeout(1)
		restart_program()

if __name__ == "__main__":
	os.system("clear")
	main()
