import requests,re,os
import time
import sys
from os import system
from time import sleep
import os
os.system("git pull")
def slow(t):
    for e in t + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.06)
line="\033[1;34m═\033[1;37m"*50
def banner():
  os.system("clear")
  print("\n\n")
  os.system("figlet -f slant DARK-RA|lolcat")
  print(line)
  print("""
   Tools Name   : \033[1;32mRANDOM CC TV HACK\033[1;37m
   Tools Author : \033[1;32mDARK-RA\033[1;37m
   Github       : \033[1;32mgithub.com/DARK-RA\033[1;37m
   Facebook     : \033[1;32 mMUHAMMADRONI AKONDO\033[1;37m
  """)
def menu():
  print(line)
  print("""                CHOOSE AN OPTION
  
   [1] Start Cracking
   [2] 𝐅𝐎𝐋𝐋𝐎𝐖 𝐌𝐘 𝐅𝐁 𝐀𝐂𝐂𝐎𝐔𝐍𝐓
   [3] 𝐅𝐎𝐋𝐋𝐎𝐖 𝐌𝐘 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐂𝐇𝐄𝐍𝐄𝐋
   [4] Our More Tools
   [5] Exit Tools""")
  choose()
def choose():
  a=input("\n\n   [>>>] Enter Your Option : ")
  if a=="1" or a=="01":
    os.system("xdg-open https://www.facebook.com/MUHAMMAD.RONI.AKONDO?mibextid=ZbWKwL")
    os.system("clear")
    banner()
    hack()
  elif a=="2" or a=="02":
    os.system("xdg-open https://www.facebook.com/MUHAMMAD.RONI.AKONDO?mibextid=ZbWKwL")
    sys.exit()
  elif a=="3" or a=="03":
    os.system("xdg-open https://t.me/dark_ra12")
    sys.exit()
  elif a=="4" or a=="04":
    os.system("xdg-open https://github.com/DARK-RA-cyber/DARK-RA-cyber")
    sys.exit()
  elif a=="5" or a=="05":
    slow("\n   [•] Exit Successfully\n")
    sys.exit()
  else:
    slow("\033[1;37m\n   [•] Wrong Value Entered")
    slow("   [•] Try Again\n\033[1;37m")
    menu()
def massage():
  print(line)
  slow("\033[1;37m    All Done.......")
  slow("    Please Wait....")
  slow("    CC TV Hack Tools Is Starting...")
  slow("    Copy CC TV IP Address....")
  slow("    Then Search On Any Browser..\033[1;37m")
  print(line)
def hack():
  print(line)
  print("""             CHOOSE A COUNTRY
  
    [01] Russian Federation
    [02] United States
    [03] Japan
    [04] Canada
    [05] New Zealand
    [06] Ukraine
    [07] Germany
    [08] Australia
    [09] Spain
    [10] Turkey
    [11] Hong Kong
    [12] Greece
    [13] Portugal
    [14] Singapore
    [15] Columbia

  """)
  num = input("    >>> \033[1;32m")
  if num == "1" or num=="01":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,82):
  			
                  url = ("http://www.insecam.org/en/bycountry/RU/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
  
                       count += 1
          except:
              print ("") 
  elif num == "2" or num=="02":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,720):
  			
                  url = ("http://www.insecam.org/en/bycountry/US/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass
  elif num == "3" or num=="03":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,232):
  			
                  url = ("http://www.insecam.org/en/bycountry/JP/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass
  elif num == "4" or num=="04":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,38):
  			
                  url = ("http://www.insecam.org/en/bycountry/CA/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass             
  elif num =="5" or num =="05":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,5):
  			
                  url = ("http://www.insecam.org/en/bycountry/NZ/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass             
  elif num =="06" or num=="6":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
              for page in range (0,2):
                  url = ("http://www.insecam.org/en/bycountry/UK/?page="+str(page))
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                       count += 1
          except:
              pass 
  elif num == "7" or num=="07":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,107):
  			
                  url = ("http://www.insecam.org/en/bycountry/DE/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass
  elif num == "8" or num=="08":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,48):
  			
                  url = ("http://www.insecam.org/en/bycountry/AT/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                       count += 1
          except:
              pass           
  elif num == "9" or num=="09":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,39):
  			
                  url = ("http://www.insecam.org/en/bycountry/ES/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass  
  elif num == "10":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,54):
  			
                  url = ("http://www.insecam.org/en/bycountry/TR/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass             
  elif num == "11":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,7):
  			
                  url = ("http://www.insecam.org/en/bycountry/HK/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass  
  elif num == "12":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,8):
  			
                  url = ("http://www.insecam.org/en/bycountry/GR/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass           
  elif num == "13":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,7):
  			
                  url = ("http://www.insecam.org/en/bycountry/PT/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass        
  elif num == "14":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,7):
  			
                  url = ("http://www.insecam.org/en/bycountry/SG/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
  
                       count += 1
          except:
              pass      
  elif num == "15":
          massage()
          try:
              headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
              for page in range (0,6):
  			
                  url = ("http://www.insecam.org/en/bycountry/CO/?page="+str(page))
              
                  res = requests.get(url, headers=headers)
                  findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                  count = 0
                                  
                  for _ in findip:
                       hasil = findip[count]
                       print("\033[1;37m  [•] CC IP: \033[1;32m",end="")
                       slow(hasil)
                       f = open('logs.txt' , 'a')
                       f.write(f'{findip}' + '\n')
                       f.close()
                   
                       count += 1
          except:
              pass
  else:
    slow("\033[1;37m\n   [•] Wrong Value Entered")
    slow("   [•] Try Again\n\033[1;37m")
    hack()
banner()
menu()
