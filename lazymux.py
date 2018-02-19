## lazymux.py - Lazymux v3.0
# -*- coding: utf-8 -*-
import os
import sys
from time import sleep as timeout
from core.lzmcore import *

def main():
	banner()
	print "   [01] Information Gathering"
	print "   [02] Vulnerability Scanner"
	print "   [03] Stress Testing"
	print "   [04] Password Attacks"
	print "   [05] Web Hacking"
	print "   [06] Exploitation Tools"
	print "   [07] Sniffing & Spoofing"
	print "   [08] Other\n"
	print "   [10] Exit the Lazymux\n"
	lazymux = raw_input("lzmx > ")
	
	if lazymux == "1" or lazymux == "01":
		print "\n    [01] Nmap"
		print "    [02] Red Hawk"
		print "    [03] D-Tect"
		print "    [04] sqlmap"
		print "    [05] Infoga"
		print "    [06] ReconDog"
		print "    [07] AndroZenmap"
		print "    [08] sqlmate"
		print "    [09] AstraNmap"
		print "    [10] WTF"
		print "    [11] Easymap"
		print "    [12] BlackBox"
		print "    [13] XD3v"
		print "    [14] Crips"
		print "    [15] SIR"
		print "    [16] EvilURL"
		print "    [17] Striker"
		print "    [18] Xshell\n"
		print "    [00] Back to main menu\n"
		infogathering = raw_input("lzmx > ")
		
		if infogathering == "01" or infogathering == "1":
			nmap()
		elif infogathering == "02" or infogathering == "2":
			red_hawk()
		elif infogathering == "03" or infogathering == "3":
			dtect()
		elif infogathering == "04" or infogathering == "4":
			sqlmap()
		elif infogathering == "05" or infogathering == "5":
			infoga()
		elif infogathering == "06" or infogathering == "6":
			reconDog()
		elif infogathering == "07" or infogathering == "7":
			androZenmap()
		elif infogathering == "08" or infogathering == "8":
			sqlmate()
		elif infogathering == "09" or infogathering == "9":
			astraNmap()
		elif infogathering == "10":
			wtf()
		elif infogathering == "11":
			easyMap()
		elif infogathering == "12":
			blackbox()
		elif infogathering == "13":
			xd3v()
		elif infogathering == "14":
			crips()
		elif infogathering == "15":
			sir()
		elif infogathering == "16":
			evilURL()
		elif infogathering == "17":
			striker()
		elif infogathering == "18":
			xshell()
		elif infogathering == "00" or infogathering == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif lazymux == "2" or lazymux == "02":
		print "\n    [01] Nmap"
		print "    [02] AndroZenmap"
		print "    [03] AstraNmap"
		print "    [04] Easymap"
		print "    [05] Red Hawk"
		print "    [06] D-Tect"
		print "    [07] Damn Small SQLi Scanner"
		print "    [08] SQLiv"
		print "    [09] sqlmap"
		print "    [10] sqlscan"
		print "    [11] Wordpresscan"
		print "    [12] WPScan"
		print "    [13] sqlmate"
		print "    [14] wordpresscan"
		print "    [15] WTF"
		print "    [16] Rang3r"
		print "    [17] Striker"
		print "    [18] Routersploit"
		print "    [19] Xshell"
		print "    [20] SH33LL"
		print "    [21] BlackBox"
		print "    [22] XAttacker\n"
		print "    [00] Back to main menu\n"
		vulnscan = raw_input("lzmx > ")
		
		if vulnscan == "01" or vulnscan == "1":
			nmap()
		elif vulnscan == "02" or vulnscan == "2":
			androZenmap()
		elif vulnscan == "03" or vulnscan == "3":
			astraNmap()
		elif vulnscan == "04" or vulnscan == "4":
			easyMap()
		elif vulnscan == "05" or vulnscan == "5":
			red_hawk()
		elif vulnscan == "06" or vulnscan == "6":
			dtect()
		elif vulnscan == "07" or vulnscan == "7":
			dsss()
		elif vulnscan == "08" or vulnscan == "8":
			sqliv()
		elif vulnscan == "09" or vulnscan == "9":
			sqlmap()
		elif vulnscan == "10":
			sqlscan()
		elif vulnscan == "11":
			wordpreSScan()
		elif vulnscan == "12":
			wpscan()
		elif vulnscan == "13":
			sqlmate()
		elif vulnscan == "14":
			wordpresscan()
		elif vulnscan == "15":
			wtf()
		elif vulnscan == "16":
			rang3r()
		elif vulnscan == "17":
			striker()
		elif vulnscan == "18":
			routersploit()
		elif vulnscan == "19":
			xshell()
		elif vulnscan == "20":
			sh33ll()
		elif vulnscan == "21":
			blackbox()
		elif vulnscan == "":
			xattacker()
		elif vulnscan == "00" or vulnscan == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif lazymux == "3" or lazymux == "03":
		print "\n    [01] Torshammer"
		print "    [02] Slowloris"
		print "    [03] Fl00d & Fl00d2"
		print "    [04] GoldenEye"
		print "    [05] Xerxes"
		print "    [06] Planetwork-DDOS"
		print "    [07] Hydra"
		print "    [08] Black Hydra"
		print "    [09] Xshell\n"
		print "    [00] Back to main menu\n"
		stresstest = raw_input("lzmx > ")
		
		if stresstest == "01" or stresstest == "1":
			torshammer()
		elif stresstest == "02" or stresstest == "2":
			slowloris()
		elif stresstest == "03" or stresstest == "3":
			fl00d12()
		elif stresstest == "04" or stresstest == "4":
			goldeneye()
		elif stresstest == "05" or stresstest == "5":
			xerxes()
		elif stresstest == "06" or stresstest == "6":
			planetwork_ddos()
		elif stresstest == "07" or stresstest == "7":
			hydra()
		elif stresstest == "08" or stresstest == "8":
			black_hydra()
		elif stresstest == "09" or stresstest == "9":
			xshell()
		elif stresstest == "00" or stresstest == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif lazymux == "4" or lazymux == "04":
		print "\n    [01] Hydra"
		print "    [02] Facebook Brute Force"
		print "    [03] Facebook Brute Force 2"
		print "    [04] Facebook Brute Force 3"
		print "    [05] Black Hydra"
		print "    [06] Hash Buster"
		print "    [07] 1337Hash"
		print "    [08] Cupp"
		print "    [09] InstaHack"
		print "    [10] Indonesian Wordlist"
		print "    [11] Xshell"
		print "    [12] Social-Engineering"
		print "    [13] BlackBox"
		print "    [14] Hashzer\n"
		print "    [00] Back to main menu\n"
		passtak = raw_input("lzmx > ")
		
		if passtak == "01" or passtak == "1":
			hydra()
		elif passtak == "02" or passtak == "2":
			facebook_bruteForce()
		elif passtak == "03" or passtak == "3":
			facebook_BruteForce()
		elif passtak == "04" or passtak == "4":
			fbBrute()
		elif passtak == "05" or passtak == "5":
			black_hydra()
		elif passtak == "06" or passtak == "6":
			hash_buster()
		elif passtak == "07" or passtak == "7":
			leethash()
		elif passtak == "08" or passtak == "8":
			cupp()
		elif passtak == "09" or passtak == "9":
			instaHack()
		elif passtak == "10":
			indonesian_wordlist()
		elif passtak == "11":
			xshell()
		elif passtak == "12":
			social()
		elif passtak == "13":
			blackbox()
		elif passtak == "14":
			hashzer()
		elif passtak == "00" or passtak == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif lazymux == "5" or lazymux == "05":
		print "\n    [01] sqlmap"
		print "    [02] Webdav"
		print "    [03] xGans"
		print "    [04] Webdav Mass Exploit"
		print "    [05] WPSploit"
		print "    [06] sqldump"
		print "    [07] Websploit"
		print "    [08] sqlmate"
		print "    [09] sqlokmed"
		print "    [10] zones"
		print "    [11] Xshell"
		print "    [12] SH33LL"
		print "    [13] XAttacker"
		print "    [14] XSStrike"
		print "    [15] Breacher\n"
		print "    [00] Back to main menu\n"
		webhack = raw_input("lzmx > ")
		
		if webhack == "01" or webhack == "1":
			sqlmap()
		elif webhack == "02" or webhack == "2":
			webdav()
		elif webhack == "03" or webhack == "3":
			xGans()
		elif webhack == "04" or webhack == "4":
			webmassploit()
		elif webhack == "05" or webhack == "5":
			wpsploit()
		elif webhack == "06" or webhack == "6":
			sqldump()
		elif webhack == "07" or webhack == "7":
			websploit()
		elif webhack == "08" or webhack == "8":
			sqlmate()
		elif webhack == "09" or webhack == "9":
			sqlokmed()
		elif webhack == "10":
			zones()
		elif webhack == "11":
			xshell()
		elif webhack == "12":
			sh33ll()
		elif webhack == "13":
			xattacker()
		elif webhack == "14":
			xsstrike()
		elif webhack == "15":
			breacher()
		elif webhack == "00" or webhack == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	elif lazymux == "6" or lazymux == "06":
		print "\n    [01] Metasploit"
		print "    [02] commix"
		print "    [03] sqlmap"
		print "    [04] Brutal"
		print "    [05] A-Rat"
		print "    [06] WPSploit"  
		print "    [07] Websploit"
		print "    [08] Routersploit"
		print "    [09] BlackBox"
		print "    [10] XAttacker\n"
		print "    [00] Back to main menu\n"
		exploitool = raw_input("lzmx > ")
		
		if exploitool == "01" or exploitool == "1":
			metasploit()
		elif exploitool == "02" or exploitool == "2":
			commix()
		elif exploitool == "03" or exploitool == "3":
			sqlmap()
		elif exploitool == "04" or exploitool == "4":
			brutal()
		elif exploitool == "05" or exploitool == "5":
			a_rat()
		elif exploitool == "06" or exploitool == "6":
			wpsploit()
		elif exploitool == "07" or exploitool == "7":
			websploit()
		elif exploitool == "08" or exploitool == "8":
			routersploit()
		elif exploitool == "09" or exploitool == "9":
			blackbox()
		elif exploitool == "10":
			xattacker()
		elif exploitool == "00" or exploitool == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	elif lazymux == "7" or lazymux == "07":
		print "\n    [01] KnockMail"
		print "    [02] Spammer-Grab"
		print "    [03] Hac"
		print "    [04] Spammer-Email"
		print "    [05] SocialFish\n"
		print "    [00] Back to main menu\n"
		sspoof = raw_input("lzmx > ")
		
		if sspoof == "01" or sspoof == "1":
			knockmail()
		elif sspoof == "02" or sspoof == "2":
			spammer_grab()
		elif sspoof == "03" or sspoof == "3":
			hac()
		elif sspoof == "04" or sspoof == "4":
			spammer_email()
		elif sspoof == "05" or sspoof == "5":
			socfish()
		elif sspoof == "00" or sspoof == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif lazymux == "8" or lazymux == "08":
		print "\n    [01] SpiderBot"
		print "    [02] Ngrok"
		print "    [03] Sudo"
		print "    [04] Ubuntu"
		print "    [05] Fedora"
		print "    [06] Kali Nethunter"
		print "    [07] VCRT"
		print "    [08] E-Code"
		print "    [09] Termux-Styling\n"
		print "    [00] Back to main menu\n"
		moretool = raw_input("lzmx > ")
		
		if moretool == "01" or moretool == "1":
			spiderbot()
		elif moretool == "02" or moretool == "2":
			ngrok()
		elif moretool == "03" or moretool == "3":
			sudo()
		elif moretool == "04" or moretool == "4":
			ubuntu()
		elif moretool == "05" or moretool == "5":
			fedora()
		elif moretool == "06" or moretool == "6":
			nethunter()
		elif moretool == "07" or moretool == "7":
			vcrt()
		elif moretool == "08" or moretool == "8":
			ecode()
		elif moretool == "09" or moretool == "9":
			stylemux()
		elif moretool == "00" or moretool == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif lazymux == "10":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()