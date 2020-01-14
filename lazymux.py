## lazymux.py - Lazymux v3.1
# -*- coding: utf-8 -*-
##
import os
import sys
from time import sleep as timeout
from core.lzmcore import *

def main():
	banner()
	print("   [01] Information Gathering")
	print("   [02] Vulnerability Scanner")
	print("   [03] Stress Testing")
	print("   [04] Password Attacks")
	print("   [05] Web Hacking")
	print("   [06] Exploitation Tools")
	print("   [07] Sniffing & Spoofing")
	print("   [08] Other\n")
	print("   [10] Exit the Lazymux\n")
	lazymux = input("lzmx > ")
	
	if lazymux.strip() == "1" or lazymux.strip() == "01":
		print("\n    [01] Nmap")
		print("    [02] Red Hawk")
		print("    [03] D-Tect")
		print("    [04] sqlmap")
		print("    [05] Infoga")
		print("    [06] ReconDog")
		print("    [07] AndroZenmap")
		print("    [08] sqlmate")
		print("    [09] AstraNmap")
		print("    [10] WTF")
		print("    [11] Easymap")
		print("    [12] BlackBox")
		print("    [13] XD3v")
		print("    [14] Crips")
		print("    [15] SIR")
		print("    [16] EvilURL")
		print("    [17] Striker")
		print("    [18] Xshell")
		print("    [19] OWScan")
		print("    [20] OSIF")
		print("    [21] Devploit")
		print("    [22] Namechk")
		print("    [23] AUXILE")
		print("    [24] inther")
		print("    [25] GINF")
		print("    [26] GPS Tracking")
		print("    [27] ASU")
		print("    [28] fim")
		print("    [29] MaxSubdoFinder")
		print("    [30] pwnedOrNot")
		print("    [31] Mac-Lookup")
		print("    [32] BillCypher\n")
		print("    [00] Back to main menu\n")
		infogathering = input("lzmx > ")
		
		if infogathering.strip() == "01" or infogathering.strip() == "1":
			nmap()
		elif infogathering.strip() == "02" or infogathering.strip() == "2":
			red_hawk()
		elif infogathering.strip() == "03" or infogathering.strip() == "3":
			dtect()
		elif infogathering.strip() == "04" or infogathering.strip() == "4":
			sqlmap()
		elif infogathering.strip() == "05" or infogathering.strip() == "5":
			infoga()
		elif infogathering.strip() == "06" or infogathering.strip() == "6":
			reconDog()
		elif infogathering.strip() == "07" or infogathering.strip() == "7":
			androZenmap()
		elif infogathering.strip() == "08" or infogathering.strip() == "8":
			sqlmate()
		elif infogathering.strip() == "09" or infogathering.strip() == "9":
			astraNmap()
		elif infogathering.strip() == "10":
			wtf()
		elif infogathering.strip() == "11":
			easyMap()
		elif infogathering.strip() == "12":
			blackbox()
		elif infogathering.strip() == "13":
			xd3v()
		elif infogathering.strip() == "14":
			crips()
		elif infogathering.strip() == "15":
			sir()
		elif infogathering.strip() == "16":
			evilURL()
		elif infogathering.strip() == "17":
			striker()
		elif infogathering.strip() == "18":
			xshell()
		elif infogathering.strip() == "19":
			owscan()
		elif infogathering.strip() == "20":
			osif()
		elif infogathering.strip() == "21":
			devploit()
		elif infogathering.strip() == "22":
			namechk()
		elif infogathering.strip() == "23":
			auxile()
		elif infogathering.strip() == "24":
			inther()
		elif infogathering.strip() == "25":
			ginf()
		elif infogathering.strip() == "26":
			gpstr()
		elif infogathering.strip() == "27":
			asu()
		elif infogathering.strip() == "28":
			fim()
		elif infogathering.strip() == "29":
			maxsubdofinder()
		elif infogathering.strip() == "30":
			pwnedOrNot()
		elif infogathering.strip() == "31":
			maclook()
		elif infogathering.strip() == "32":
			billcypher()
		elif infogathering.strip() == "00" or infogathering.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "2" or lazymux.strip() == "02":
		print("\n    [01] Nmap")
		print("    [02] AndroZenmap")
		print("    [03] AstraNmap")
		print("    [04] Easymap")
		print("    [05] Red Hawk")
		print("    [06] D-Tect")
		print("    [07] Damn Small SQLi Scanner")
		print("    [08] SQLiv")
		print("    [09] sqlmap")
		print("    [10] sqlscan")
		print("    [11] Wordpresscan")
		print("    [12] WPScan")
		print("    [13] sqlmate")
		print("    [14] wordpresscan")
		print("    [15] WTF")
		print("    [16] Rang3r")
		print("    [17] Striker")
		print("    [18] Routersploit")
		print("    [19] Xshell")
		print("    [20] SH33LL")
		print("    [21] BlackBox")
		print("    [22] XAttacker")
		print("    [23] OWScan\n")
		print("    [00] Back to main menu\n")
		vulnscan = input("lzmx > ")
		
		if vulnscan.strip() == "01" or vulnscan.strip() == "1":
			nmap()
		elif vulnscan.strip() == "02" or vulnscan.strip() == "2":
			androZenmap()
		elif vulnscan.strip() == "03" or vulnscan.strip() == "3":
			astraNmap()
		elif vulnscan.strip() == "04" or vulnscan.strip() == "4":
			easyMap()
		elif vulnscan.strip() == "05" or vulnscan.strip() == "5":
			red_hawk()
		elif vulnscan.strip() == "06" or vulnscan.strip() == "6":
			dtect()
		elif vulnscan.strip() == "07" or vulnscan.strip() == "7":
			dsss()
		elif vulnscan.strip() == "08" or vulnscan.strip() == "8":
			sqliv()
		elif vulnscan.strip() == "09" or vulnscan.strip() == "9":
			sqlmap()
		elif vulnscan.strip() == "10":
			sqlscan()
		elif vulnscan.strip() == "11":
			wordpreSScan()
		elif vulnscan.strip() == "12":
			wpscan()
		elif vulnscan.strip() == "13":
			sqlmate()
		elif vulnscan.strip() == "14":
			wordpresscan()
		elif vulnscan.strip() == "15":
			wtf()
		elif vulnscan.strip() == "16":
			rang3r()
		elif vulnscan.strip() == "17":
			striker()
		elif vulnscan.strip() == "18":
			routersploit()
		elif vulnscan.strip() == "19":
			xshell()
		elif vulnscan.strip() == "20":
			sh33ll()
		elif vulnscan.strip() == "21":
			blackbox()
		elif vulnscan.strip() == "22":
			xattacker()
		elif vulnscan.strip() == "23":
			owscan()
		elif vulnscan.strip() == "00" or vulnscan.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "3" or lazymux.strip() == "03":
		print("\n    [01] Torshammer")
		print("    [02] Slowloris")
		print("    [03] Fl00d & Fl00d2")
		print("    [04] GoldenEye")
		print("    [05] Xerxes")
		print("    [06] Planetwork-DDOS")
		print("    [07] Hydra")
		print("    [08] Black Hydra")
		print("    [09] Xshell")
		print("    [10] santet-online\n")
		print("    [00] Back to main menu\n")
		stresstest = input("lzmx > ")
		
		if stresstest.strip() == "01" or stresstest.strip() == "1":
			torshammer()
		elif stresstest.strip() == "02" or stresstest.strip() == "2":
			slowloris()
		elif stresstest.strip() == "03" or stresstest.strip() == "3":
			fl00d12()
		elif stresstest.strip() == "04" or stresstest.strip() == "4":
			goldeneye()
		elif stresstest.strip() == "05" or stresstest.strip() == "5":
			xerxes()
		elif stresstest.strip() == "06" or stresstest.strip() == "6":
			planetwork_ddos()
		elif stresstest.strip() == "07" or stresstest.strip() == "7":
			hydra()
		elif stresstest.strip() == "08" or stresstest.strip() == "8":
			black_hydra()
		elif stresstest.strip() == "09" or stresstest.strip() == "9":
			xshell()
		elif stresstest.strip() == "10":
			sanlen()
		elif stresstest.strip() == "00" or stresstest.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "4" or lazymux.strip() == "04":
		print("\n    [01] Hydra")
		print("    [02] FMBrute")
		print("    [03] HashID")
		print("    [04] Facebook Brute Force 3")
		print("    [05] Black Hydra")
		print("    [06] Hash Buster")
		print("    [07] FBBrute")
		print("    [08] Cupp")
		print("    [09] InstaHack")
		print("    [10] Indonesian Wordlist")
		print("    [11] Xshell")
		print("    [12] Social-Engineering")
		print("    [13] BlackBox")
		print("    [14] Hashzer")
		print("    [15] Hasher")
		print("    [16] Hash-Generator")
		print("    [17] nk26")
		print("    [18] Hasherdotid")
		print("    [19] Crunch")
		print("    [20] Hashcat")
		print("    [21] ASU")
		print("    [22] Katak\n")
		print("    [00] Back to main menu\n")
		passtak = input("lzmx > ")
		
		if passtak.strip() == "01" or passtak.strip() == "1":
			hydra()
		elif passtak.strip() == "02" or passtak.strip() == "2":
			fmbrute()
		elif passtak.strip() == "03" or passtak.strip() == "3":
			hashid()
		elif passtak.strip() == "04" or passtak.strip() == "4":
			fbBrute()
		elif passtak.strip() == "05" or passtak.strip() == "5":
			black_hydra()
		elif passtak.strip() == "06" or passtak.strip() == "6":
			hash_buster()
		elif passtak.strip() == "07" or passtak.strip() == "7":
			fbbrutex()
		elif passtak.strip() == "08" or passtak.strip() == "8":
			cupp()
		elif passtak.strip() == "09" or passtak.strip() == "9":
			instaHack()
		elif passtak.strip() == "10":
			indonesian_wordlist()
		elif passtak.strip() == "11":
			xshell()
		elif passtak.strip() == "12":
			social()
		elif passtak.strip() == "13":
			blackbox()
		elif passtak.strip() == "14":
			hashzer()
		elif passtak.strip() == "15":
			hasher()
		elif passtak.strip() == "16":
			hashgenerator()
		elif passtak.strip() == "17":
			nk26()
		elif passtak.strip() == "18":
			hasherdotid()
		elif passtak.strip() == "19":
			crunch()
		elif passtak.strip() == "20":
			hashcat()
		elif passtak.strip() == "21":
			asu()
		elif passtak.strip() == "22":
			katak()
		elif passtak.strip() == "00" or passtak.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "5" or lazymux.strip() == "05":
		print("\n    [01] sqlmap")
		print("    [02] Webdav")
		print("    [03] xGans")
		print("    [04] Webdav Mass Exploit")
		print("    [05] WPSploit")
		print("    [06] sqldump")
		print("    [07] Websploit")
		print("    [08] sqlmate")
		print("    [09] sqlokmed")
		print("    [10] zones")
		print("    [11] Xshell")
		print("    [12] SH33LL")
		print("    [13] XAttacker")
		print("    [14] XSStrike")
		print("    [15] Breacher")
		print("    [16] OWScan")
		print("    [17] ko-dork")
		print("    [18] ApSca")
		print("    [19] amox")
		print("    [20] FaDe")
		print("    [21] AUXILE")
		print("    [22] HPB")
		print("    [23] inther")
		print("    [24] Atlas")
		print("    [25] MaxSubdoFinder\n")
		print("    [00] Back to main menu\n")
		webhack = input("lzmx > ")
		
		if webhack.strip() == "01" or webhack.strip() == "1":
			sqlmap()
		elif webhack.strip() == "02" or webhack.strip() == "2":
			webdav()
		elif webhack.strip() == "03" or webhack.strip() == "3":
			xGans()
		elif webhack.strip() == "04" or webhack.strip() == "4":
			webmassploit()
		elif webhack.strip() == "05" or webhack.strip() == "5":
			wpsploit()
		elif webhack.strip() == "06" or webhack.strip() == "6":
			sqldump()
		elif webhack.strip() == "07" or webhack.strip() == "7":
			websploit()
		elif webhack.strip() == "08" or webhack.strip() == "8":
			sqlmate()
		elif webhack.strip() == "09" or webhack.strip() == "9":
			sqlokmed()
		elif webhack.strip() == "10":
			zones()
		elif webhack.strip() == "11":
			xshell()
		elif webhack.strip() == "12":
			sh33ll()
		elif webhack.strip() == "13":
			xattacker()
		elif webhack.strip() == "14":
			xsstrike()
		elif webhack.strip() == "15":
			breacher()
		elif webhack.strip() == "16":
			owscan()
		elif webhack.strip() == "17":
			kodork()
		elif webhack.strip() == "18":
			apsca()
		elif webhack.strip() == "19":
			amox()
		elif webhack.strip() == "20":
			fade()
		elif webhack.strip() == "21":
			auxile()
		elif webhack.strip() == "22":
			hpb()
		elif webhack.strip() == "23":
			inther()
		elif webhack.strip() == "24":
			atlas()
		elif webhack.strip() == "25":
			maxsubdofinder()
		elif webhack.strip() == "00" or webhack.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "6" or lazymux.strip() == "06":
		print("\n    [01] Metasploit")
		print("    [02] commix")
		print("    [03] sqlmap")
		print("    [04] Brutal")
		print("    [05] A-Rat")
		print("    [06] WPSploit")  
		print("    [07] Websploit")
		print("    [08] Routersploit")
		print("    [09] BlackBox")
		print("    [10] XAttacker")
		print("    [11] TXTool")
		print("    [12] MSF-Pg")
		print("    [13] Binary Exploitation")
		print("    [14] ASU\n")
		print("    [00] Back to main menu\n")
		exploitool = input("lzmx > ")
		
		if exploitool.strip() == "01" or exploitool.strip() == "1":
			metasploit()
		elif exploitool.strip() == "02" or exploitool.strip() == "2":
			commix()
		elif exploitool.strip() == "03" or exploitool.strip() == "3":
			sqlmap()
		elif exploitool.strip() == "04" or exploitool.strip() == "4":
			brutal()
		elif exploitool.strip() == "05" or exploitool.strip() == "5":
			a_rat()
		elif exploitool.strip() == "06" or exploitool.strip() == "6":
			wpsploit()
		elif exploitool.strip() == "07" or exploitool.strip() == "7":
			websploit()
		elif exploitool.strip() == "08" or exploitool.strip() == "8":
			routersploit()
		elif exploitool.strip() == "09" or exploitool.strip() == "9":
			blackbox()
		elif exploitool.strip() == "10":
			xattacker()
		elif exploitool.strip() == "11":
			txtool()
		elif exploitool.strip() == "12":
			msfpg()
		elif exploitool.strip() == "13":
			binploit()
		elif exploitool.strip() == "14":
			asu()
		elif exploitool.strip() == "00" or exploitool.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "7" or lazymux.strip() == "07":
		print("\n    [01] KnockMail")
		print("    [02] Spammer-Grab")
		print("    [03] Hac")
		print("    [04] Spammer-Email")
		print("    [05] SocialFish")
		print("    [06] santet-online")
		print("    [07] SpazSMS")
		print("    [08] LiteOTP")
		print("    [09] ASU\n")
		print("    [00] Back to main menu\n")
		sspoof = input("lzmx > ")
		
		if sspoof.strip() == "01" or sspoof.strip() == "1":
			knockmail()
		elif sspoof.strip() == "02" or sspoof.strip() == "2":
			spammer_grab()
		elif sspoof.strip() == "03" or sspoof.strip() == "3":
			hac()
		elif sspoof.strip() == "04" or sspoof.strip() == "4":
			spammer_email()
		elif sspoof.strip() == "05" or sspoof.strip() == "5":
			socfish()
		elif sspoof.strip() == "06" or sspoof.strip() == "6":
			sanlen()
		elif sspoof.strip() == "07" or sspoof.strip() == "7":
			spazsms()
		elif sspoof.strip() == "08" or sspoof.strip() == "8":
			liteotp()
		elif sspoof.strip() == "09" or sspoof.strip() == "9":
			asu()
		elif sspoof.strip() == "00" or sspoof.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "8" or lazymux.strip() == "08":
		print("\n    [01] SpiderBot")
		print("    [02] Ngrok")
		print("    [03] Sudo")
		print("    [04] Ubuntu")
		print("    [05] Fedora")
		print("    [06] Kali Nethunter")
		print("    [07] VCRT")
		print("    [08] E-Code")
		print("    [09] Termux-Styling")
		print("    [10] PassGen")
		print("    [11] xl-py")
		print("    [12] BeanShell")
		print("    [13] WebConn")
		print("    [14] Crunch")
		print("    [15] Textr")
		print("    [16] AutoVisitor")
		print("    [17] RShell")
		print("    [18] TermPyter")
		print("    [19] jadx")
		print("    [20] F4K3")
		print("    [21] heroku")
		print("    [22] google")
		print("    [23] vbug")
		print("    [24] kojawafft\n")
		print("    [00] Back to main menu\n")
		moretool = input("lzmx > ")
		
		if moretool.strip() == "01" or moretool.strip() == "1":
			spiderbot()
		elif moretool.strip() == "02" or moretool.strip() == "2":
			ngrok()
		elif moretool.strip() == "03" or moretool.strip() == "3":
			sudo()
		elif moretool.strip() == "04" or moretool.strip() == "4":
			ubuntu()
		elif moretool.strip() == "05" or moretool.strip() == "5":
			fedora()
		elif moretool.strip() == "06" or moretool.strip() == "6":
			nethunter()
		elif moretool.strip() == "07" or moretool.strip() == "7":
			vcrt()
		elif moretool.strip() == "08" or moretool.strip() == "8":
			ecode()
		elif moretool.strip() == "09" or moretool.strip() == "9":
			stylemux()
		elif moretool.strip() == "10":
			passgencvar()
		elif moretool.strip() == "11":
			xlPy()
		elif moretool.strip() == "12":
			beanshell()
		elif moretool.strip() == "13":
			webconn()
		elif moretool.strip() == "14":
			crunch()
		elif moretool.strip() == "15":
			textr()
		elif moretool.strip() == "16":
			autovisitor()
		elif moretool.strip() == "17":
			rshell()
		elif moretool.strip() == "18":
			termpyter()
		elif moretool.strip() == "19":
			jadx()
		elif moretool.strip() == "20":
			f4k3()
		elif moretool.strip() == "21":
			heroku()
		elif moretool.strip() == "22":
			google()
		elif moretool.strip() == "23":
			vbug()
		elif moretool.strip() == "24":
			kojawafft()
		elif moretool.strip() == "00" or moretool.strip() == "0":
			restart_program()
		else:
			print("\nERROR: Wrong Input")
			timeout(2)
			restart_program()
	
	elif lazymux.strip() == "10":
		sys.exit()
	
	else:
		print("\nERROR: Wrong Input")
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()