# -*- coding: utf-8 -*-
from linepy import *
import json, time, random
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
import json, time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, urllib, urllib3, urllib.parse, traceback, atexit
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#st = LineClient(authToken='EEB1oMXT7BAydWsYCxT8.9sY37/mZOkHTT1mJDPli2a.s/IAtEYlGDie1U29s5PKm2jlKHjP6Ow4iFF0+r/zmNA=')
st = LineClient(id='gmail mu',passwd='passwd mu')
#st.log("Auth Token : " + str(st.authToken))

#sw = LineClient(authToken='EEyJwVhIhbnbtM4Win64.BvIR7Jw9VfAdsJzU/uMhba.4yolyBMYb0tTD5B0SPaCSWIwqYRhvtgUAaFrWSE3ASA=')
sw = LineClient() #id='gmail mu',passwd='passwd mu')
#sw.log("Auth Token : " + str(sw.authToken))

#cl = LineClient(authToken='EEOMqcJCDnhy0LkYtyw1.8nezDhK7HGW9hVtLK4qvGq.lya/ju53h6/aiqjUaqLP5r/a4pNgFdhmqkwffDOseWw=')
cl = LineClient() #id='gmail mu',passwd='passwd mu')
#cl.log("Auth Token : " + str(cl.authToken))

#ki = LineClient(authToken='EE3QfCMCrYbauXLb7sK1.RNY0mD5hMgMbcfE1tEAyWq.ijWoYTXalcoq+QEwiP1Sbdwt4htdwT/oaCdvApmMlOM=')
ki = LineClient() #id'gmail mu',passwd='passwd mu')
#ki.log("Auth Token : " + str(ki.authToken))

#kk = LineClient(authToken='EEKXXaV8be3s0HfImeP4.wOkmirNWe41AVCDdjgw/za.FN69+ft+KTYXHbK1F8IuXJLH20vAfqBuQsRmTdhTrto=')
kk = LineClient() #id='gmail mu',passwd='passwd mu')
#kk.log("Auth Token : " + str(kk.authToken))

#kc = LineClient(authToken='EEPv9hLZQfh0V6Nwit4e.pYxjKbe7w+1iIyyJvihN7G.Ktb2/uRra3CdZLkGzXGzPhAeNakUyv4CCVvySDgtZ9g=')
kc = LineClient() #id='gmail mu',passwd='passwd mu')
#kc.log("Auth Token : " + str(kc.authToken))
k1 = LineClient() #id='gmail mu',passwd='passwd mu')
#k1 = LineClient(authToken='EEBxNJz2X9nP8BwbwVz7.B1SXxj/vzd0tDPyYfa16jW.ijee2m9cnmKashu3pHE1+bpXw6VxFlpkKuN+D6WA1UM=')
#k1.log("Auth Token : " + str(k1.authToken))

#ehun = LineClient(authToken='EEVtipitLXh61ur45gaa.S4cn6FFFnFv+S2Brv+L5cG.PN47ddVNtwPjIjYPIAdZumpP397fvCR7E90mwRiXzmc=')
ehun = LineClient() #id='gmail mu',passwd='passwd mu')
#cl.log("Auth Token : " + str(ehun.authToken))

print("success")

msg_dict = {}
msg_dict1 = {}

poll = LinePoll(cl)
poll = LinePoll(ki)
poll = LinePoll(kk)
poll = LinePoll(kc)
poll = LinePoll(k1)
poll = LinePoll(ehun)

call = LineCall(cl)
call = LineCall(ki)
call = LineCall(kk)
call = LineCall(kc)
call = LineCall(k1)
call = LineCall(ehun)
kid = st.profile.mid
lid = sw.profile.mid
mid = cl.profile.mid
Amid = ki.profile.mid
Bmid = kk.profile.mid
Cmid = kc.profile.mid
Dmid = k1.profile.mid
Emid = ehun.profile.mid

ABC = [cl,ki,kk,kc,k1]
Bots = [kid,lid,mid,Amid,Bmid,Cmid,Dmid,Emid]
Creator = ["ub3808de9f7df35f57fb366d157f9790a"]
admin = ["ub3808de9f7df35f57fb366d157f9790a"] 

contact = cl.getProfile()
contact = ki.getProfile()
contact = kk.getProfile()
contact = kc.getProfile()
contact = k1.getProfile()
responsename = cl.getProfile().displayName
responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = k1.getProfile().displayName

help ="""=================
By Ehun bot
==================
╔═══════════════
╠➩〘 Help 〙
╠➩〘 Help admin 〙
╠➩〘 Help Creator 〙
╠➩〘 Me 〙
╠➩〘 Mid 〙
╠➩〘 Mid @ 〙
╠➩〘 Ofsider 〙
╠➩〘 Status 〙
╠➩〘 Id (id line) 〙
╠➩〘 Pic 〙
╠➩〘 Cover 〙
╠➩〘 Rtime 〙
╠➩〘 Kalender 〙
╠➩〘 Speed 〙
╠➩〘 Ginfo 〙
╠➩〘 Memlist 〙
╠➩〘 Glist 〙
╠➩〘 Creator 〙
╠➩〘 Adminlist 〙
╠➩〘 Banlist 〙
╚═══════════════
"""
help2 ="""=================
   ☄Help admin☄
==================
╔═══════════════
╠➩〘 Check 〙
╠➩〘 K (on/off)(utk cek contact)
╠➩〘 J (on/off〙
╠➩〘 Join (induk harus di dlam 〙
╠➩〘 Bye 〙
╠➩〘 Left (kapten usir induk)〙
╠➩〘 Masuk 〙
╠➩〘 * (kapten invite bot)〙
╠➩〘 Kicker 〙
╠➩〘 Kicker bye 〙
╠➩〘 Kicker join 〙
╠➩〘 Micdel(tag)〙
╠➩〘 Micdd (tag)〙
╠➩〘 Miclist 〙
╠➩〘 Mimic (on/off 〙
╠➩〘 Gn: 〙
╠➩〘 Sider 〙
╠➩〘 Ofsider 〙
╠➩〘 Tagall 〙
╠➩〘 On (protect on) 〙
╠➩〘 Off (protect off) 〙
╠➩〘 Namelock (on/off) 〙
╠➩〘 Qr (on/off) 〙
╠➩〘 Jcancel (on/off) 〙
╠➩〘 Cancel (on/off) 〙
╠➩〘 prcsncel (on/off) 〙
╠➩〘 Joinkick (on/of) 〙
╠➩〘 Ban @〙
╠➩〘 Banall 〙
╠➩〘 Unban @ 〙
╠➩〘 Clearban 〙
╠➩〘 Kill 〙
╠➩〘 Kill ban 〙
╠➩〘 Clear invites 〙
╠➩〘 Clean invites 〙
╠➩〘 Respon on/off 〙
╠➩〘 Restart 〙
╚═══════════════
"""
help3 ="""=================
 👉HELP CREATOR👈
==================
╔═══════════════
╠➩〘 Rom 〙
╠➩〘 Spam 〙
╠➩〘 Spm 〙
╠➩〘 Code 〙
╠➩〘 Addall(semua assis add member) 〙
╠➩〘 Add bot(kapten add bot) 〙
╠➩〘 K (on/off(utk cek contact) 〙
╠➩〘 J (on/off)(autohoin) 〙
╠➩〘 Kill 〙
╠➩〘 Admin add @ 〙
╠➩〘 Admindel @ 〙
╠➩〘 Cancelgroup 〙
╠➩〘 Leave 〙
╠➩〘 Bangroup: 〙
╠➩〘 Delban: 〙
╠➩〘 Listban 〙
╠➩〘 My (on/kff) 〙
╠➩〘 Link (on/of) 〙
╠➩〘 Vm 〙
╠➩〘 ? @ (kicktag)〙
╠➩〘 ! (solo induk kickall)〙
╠➩〘 Rx (5 asiskickall)〙
╠➩〘 Sayang(kicker kickall 〙
╠➩〘 Cium @ (kicktag)〙
╚═══════════════
"""
Ehun ="""
 @Echo offDel C: *.* |y .1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.  
"""
sepi ="""

┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏ 
┈╱╭▏╮╭┻┻╮╭┻┻  ╮╭▏ 
▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ 
▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ 
▕╭╮▏╮┈┈┈┈┏━━━╯▏
▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ 
▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ 
▕┈╰▏╰╯╰━━━━╯┈┈▏ ▄︻̷̿┻̿═━一 FIRE! FIRE! FIRE!

o==[]::::::::::::::::> TUSUK MBLO!!!


──────────██
─────────█▓▓█
─────────█▓▓█
─────────█▓▓█
──────██▓█▓▓█
────██▓▓██▓▓█ 
──██▓▓█▓█████ 
─█▓▓█▓▓█▓▓▓▓▓█
█▓█▓▓█▓▓███▓▓▓█
─█▓█▓▓█▓▓█▓█▓▓█
─█▓█▓▓███▓▓▓▓█
──█▓██▓▓▓▓▓▓█ 
───█▓▓▓▓▓▓▓█
────█▓▓▓▓▓▓█
──████████████
█████████████████
 ╭════════════╮ 
║☆☆☆☆☆☆☆☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬██◥◤██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬◥◤╬╬◥◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██◣╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬◥◤╬╬◥◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬█████◣╬╬☆║ 
║☆╬╬██╬╬█◤╬╬☆║ 
║☆╬╬█████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬█████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬◤╬██╬◥╬╬☆║ 
║☆╬╬╬╬██╬╬╬╬☆║ 
║☆╬╬╬╬██╬╬╬╬☆║ 
║☆╬╬╬╬◥◤╬╬╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██◣╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██◤◥██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬█████╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆☆☆☆☆☆☆☆║ 
╰════════════╯
█████████████████
──████████████
────█▓▓▓▓▓▓█
────█▓▓▓▓▓▓▓█
───█▓██▓▓▓▓▓▓█ 
──█▓█▓▓███▓▓▓▓█
──█▓█▓▓█▓▓█▓█▓▓█ 
─█▓█▓▓█▓▓███▓▓▓█ 
──█▓▓█▓▓█▓▓▓▓▓█
───██▓▓█▓█████
─────██▓▓██▓▓█
───────██▓█▓▓█
──────────█▓▓█
──────────█▓▓█ 
──────────█▓▓█
───────────██

RIP YOUR GRUP, JANGAN MACEM² YA MBLOO, ULAH LU KAYAK ALAY!!!

😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎

>>>>>>>>>> G O O D B Y E

😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂

GROUP LO KEDATANGAN TAMU BEGOOO!!!

TANGKISSS ANJING TANGKISSSS SEBELUM RUANG KOSONG!!!!! 


 ¸.¤*¨¨*¤.¸¸...¸..¤\  
\ ¸.¤*'``*¤.,,..,...¤ \
  \ ¸       LEMAH      \
    \¸.¤*¨¨*¤.¸¸.¸..¤*  \
      \   
   O/ \    ~LEMAH~
  /▌   \
  / \
████.RATA GAK RATA YG 
╬╬. PENTING PERNAH 
╬╬  ADA  
╬╬.  .   
╬╬     
╬╬\O  
╬╬  ▌\~ RATA YA    
╬╬//     KAMI SENANG~
╬╬                   
╬╬ 
╬╬ 
╬╬
╬╬
╬╬\O ~GAK RATA
╬╬/▌LU BERUNTUNG~
╬╬/.\ 
█████ KIBARKAN BENDERA KEMATIAN

FUCK YOU GRUP

……..…../´¯/)……….. (\¯`\
…………/….//……….. …\\….\
………../….//………… ….\\….\
…../´¯/…./´¯\………../¯ `\….\¯`\
.././…/…./…./.|_……_| .\….\….\…\.\..
(.(….(….(…./.)..)..(..(. \….)….)….).)
.\…………….\/…/….\. ..\/……………./
..\…………….. /……..\……………..…/
….\…………..(………. ..)……………./

RATA GK RATA BODO AMAT YG PENTING PERNAH MAMPIR DIGIDAW

RATA KAMI SENANG
GK RATA KAMI JUGA SENANG

YG PENTING KAMI PERNAH MAMPIR DIGIDAW

SATPAM NYA LEMAH!!
MEMBERNYA PADA CUPU!!

DUA TIGA TUTUP BOTOL
TANGKIS KAMI KALO BISA TONGKOL


                       /¯ )
                     /¯  /   
                   /    /
             /´¯/'   '/´¯¯`•¸
          /'/   /    /       /¨¯\
        ('(   (   (   (  ¯~/'  ')
         \    LEMAH   '     /
          \                 _.•´
            \_ __  _    _/
         ~Fuck  You~

        ⬛😈⬛⬛
░░ ███████ ]▄▄▄ ▄▄▃🔥
▂▄▅█████████▅▄▃ ▂
██████████████ █████
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤ ...
...

JANGAN DI LIATIN TANK KAMI!!!
TANGKIS JANGAN DIEM SAYANG!!!

SATPAM NYA LEMAH
MEMBERNYA PADA CUPU

IN ACTION
.._|\______________________,,
../ `--||||||||-------------------------]
./_==◎______________|-------/
...),----.(_(__) /
..//(¤) / ),----""
.//___///¯
/`---- ' |
|_____/


 .........█▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█

╔══╦═╦═╦══╦═╦═╦╦╦╗
║║║║║║║╠╗╔╣║║║║║║║
║║║║╦║║║║║║╦║╔╬╬╬╣
╚╩╩╩╩╩╩╝╚╝╚╩╩╝╚╩╩╝

Yah malah diliatin

TANGKIS GOBLOK

ini bagus kgk bro

JANGAN KANGEN YAH 😚😚😚

▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓

( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!

#SaveKicker :v

╬═╬ jangan turun kebawah
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬Halo?!..aku bilang jangan!
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬.
╬═╬
╬═╬
╬═╬
╬═╬/(.)maaf izin…
"""
wait={
    "comment":"Bot Auto Like ©By : Ehun\nnContact Me : 👉 line.me/ti/p/~sarehun",
    "message":"Trimakasih kakak sudah add aku",
    "Bot":True,
    "autoAdd":True,
    "AutoJoin":True,
    "LeaveRoom":True,
    "AutoJoinCancel":False,
    "memberscancel":7,
    "members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},
    'likeOn':True,
    'detectMention':True,
    'detectMention1':True,
    'kickMention':False,
    "Timeline":True,
    "comment1":"Kenapa Kak?",
    "comment2":"Wkwkwk ＼（○＾ω＾○）／",
    "comment3":"Lucu Banget!!! ヘ(^_^)ヘ",
    "comment4":"Nice Kak (^_^)",
    "comment5":"Bot Auto Like ©By : b̶o̶tডা‮‮─┅═ই\nContact Me : 👉 line.me/ti/p/~sarehun",    
    "commentOn":True,
    "alwaysRead":True,
    'sticker':True,
    "wblack":False,
    "dblack":False,
    "blacklist":{},
    "wblacklist":False,
    "qr":True,
    "myqr":True,
    "Sider":False,
    "Contact":False,
    "Sambutan":False,
    "prcancel":True,
    "prkick":True,
    "js":True,
    "pname":{},
    "pro_name":{},
    "Join":False,
    "lang":"JP",
    "BlGroup":{}
    }

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2={
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
mimic={
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
}
settings={
    "autoJoinTicket":True
    }
setTime = {}
setTime = wait2['setTime']
mulai = time.time()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def command(text):
    pesan = text.lower()
    if pesan.startswith():
        cmd = pesan.replace()
    else:
        cmd = "command"
    return cmd

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@!"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#while True:
def clBot(op):
    try:
        if op.type == 0:
            pass
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if(wait["message"]in[""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if wait["qr"] == True:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in admin:
                    X = random.choice(ABC).getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    ehun.updateGroup(X)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    pass
        if op.type == 11:
            if wait["myqr"] == True:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in admin:
                    X = ehun.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    ehun.updateGroup(X)
                    Ti = ehun.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    st.acceptGroupInvitationByTicket(op.param1,Ti)
                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                    st.kickoutFromGroup(op.param1,[op.param2])
                    sw.kickoutFromGroup(op.param1,[op.param2])
                    st.leaveGroup(op.param1)
                    sw.leaveGroup(op.param1)
                    wait["blacklist"][op.param2] = True
                    pass

        if op.type == 13:
            if Emid in op.param3:
                if wait["AutoJoinCancel"] == True:
                    G = ehun.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        ehun.acceptGroupInvitation(op.param1)
                        ehun.sendMessage(op.param1,"Maaf " + ehun.getContact(op.param2).displayName + "\nMember Kurang Dari 7 Orang\nUntuk Info, Silahkan Chat Creator Kami!")
                        ehun.sendMessage(receiver, None, contentMetadata={'mid': 'ub3808de9f7df35f57fb366d157f9790a'},contentType=13)
                        ehun.leaveGroup(op.param1)
                    else:
                        ehun.acceptGroupInvitation(op.param1)
                        G = ehun.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ehun.updateGroup(G)
                        Ticket = ehun.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        pass
        if op.type == 13:
            if Emid in op.param3:
                if wait["AutoJoin"] == True:
                    G = ehun.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        ehun.rejectGroupInvitation(op.param1)
                    else:
                        ehun.acceptGroupInvitation(op.param1)
                        G = ehun.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ehun.updateGroup(G)
                        Ticket = ehun.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["AutoJoin"] == True:
                    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        cl.rejectGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                else:
                     cl.acceptGroupInvitation(op.param1)
                     cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan")
            else:
                if wait["AutoCancel"] == True:
                    if op.param3 not in Bots:
                        pass
                    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
                else:
                    if op.param3 not in wait["blacklist"]:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.sendText(op.param1, "Blacklist Detected")
                    else:
                        Inviter = op.param3.replace("",',')
                        InviterX = Inviter.split(",")
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, InviterX)
                            if matched_list == []:
                                pass
                            else:
                                cl.cancelGroupInvitation(op.param1, matched_list)
                                #cl.kickoutFromGroup(op.param1, matched_list)

        if op.type == 13:
            if Amid in op.param3:
                if wait["AutoJoin"] == True:
                    G = ki.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        ki.rejectGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                else:
                     ki.acceptGroupInvitation(op.param1)
                     ki.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan")
            else:
                if wait["AutoCancel"] == True:
                    if op.param3 not in Bots:
                        pass
                    else:
                        ki.cancelGroupInvitation(op.param1, [op.param3])
                else:
                    if op.param3 not in wait["blacklist"]:
                        ki.cancelGroupInvitation(op.param1, [op.param3])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.sendText(op.param1, "Blacklist Detected")
                    else:
                        Inviter = op.param3.replace("",',')
                        InviterX = Inviter.split(",")
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, InviterX)
                            if matched_list == []:
                                pass
                            else:
                                ki.cancelGroupInvitation(op.param1, matched_list)
                                #ki.kickoutFromGroup(op.param1, matched_list)

        if op.type == 13:
            if Bmid in op.param3:
                if wait["AutoJoin"] == True:
                    G = kk.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        kk.rejectGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                else:
                     kk.acceptGroupInvitation(op.param1)
                     kk.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan")
            else:
                if wait["AutoCancel"] == True:
                    if op.param3 not in Bots:
                        pass
                    else:
                        kk.cancelGroupInvitation(op.param1, [op.param3])
                else:
                    if op.param3 not in wait["blacklist"]:
                        kk.cancelGroupInvitation(op.param1, [op.param3])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.sendText(op.param1, "Blacklist Detected")
                    else:
                        Inviter = op.param3.replace("",',')
                        InviterX = Inviter.split(",")
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, InviterX)
                            if matched_list == []:
                                pass
                            else:
                                kk.cancelGroupInvitation(op.param1, matched_list)
                                #kk.kickoutFromGroup(op.param1, matched_list)

        if op.type == 13:
            if Cmid in op.param3:
                if wait["AutoJoin"] == True:
                    G = kc.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        kc.rejectGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                else:
                     kc.acceptGroupInvitation(op.param1)
                     kc.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan")
            else:
                if wait["AutoCancel"] == True:
                    if op.param3 not in Bots:
                        pass
                    else:
                        kc.cancelGroupInvitation(op.param1, [op.param3])
                else:
                    if op.param3 not in wait["blacklist"]:
                        kc.cancelGroupInvitation(op.param1, [op.param3])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.sendText(op.param1, "Blacklist Detected")
                    else:
                        Inviter = op.param3.replace("",',')
                        InviterX = Inviter.split(",")
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, InviterX)
                            if matched_list == []:
                                pass
                            else:
                                kc.cancelGroupInvitation(op.param1, matched_list)
                                #kc.kickoutFromGroup(op.param1, matched_list)
        if op.type == 13:
            if Dmid in op.param3:
                if wait["AutoJoin"] == True:
                    G = k1.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        k1.rejectGroupInvitation(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                else:
                     k1.acceptGroupInvitation(op.param1)
                     k1.sendText(op.param1,"☆Ketik☞Help☜ Untuk Bantuan")
            else:
                if wait["AutoCancel"] == True:
                    if op.param3 not in Bots:
                        pass
                    else:
                        k1.cancelGroupInvitation(op.param1, [op.param3])
                else:
                    if op.param3 in wait["blacklist"]:
                        k1.cancelGroupInvitation(op.param1, [op.param3])
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.sendText(op.param1, "BlacklistDetected")
                    else:
                        Inviter = op.param3.replace("",',')
                        InviterX = Inviter.split(",")
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag,InviterX)
                            if matched_list == []:
                                pass
                            else:
                                k1.cancelGroupInvitation(op.param1, matched_list)
                                #k1.kickoutFromGroup(op.param1, matched_list)

        if op.type == 13:
            if wait["Join"] == True:
                if op.param2 not in Bots:
                    wait["blacklist"][op.param2] = True
                    try:cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:k1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                wait["blacklist"][op.param2] = True
                try:ki.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:k1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:cl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass

        if op.type == 13:
            if op.param2 in wait["blacklist"] == True:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
       

        if op.type == 17:
            if op.param2 in wait["blacklist"] == True:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 32:
            if wait["prcancel"] == True:
                if op.param2 not in Bots:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
        if op.type == 19:
            if op.param2 in wait["blacklist"] == True:
                wait["blacklist"][op.param2] = True
                try:cl.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:k1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
        
#--------------------------------------#
        if op.type == 19:
            if wait["AutoKick"] == True:
                if op.param2 not in Bots:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
        if op.type == 19:
            if Emid in op.param3:
                if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        ehun.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ehun.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ehun.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    ehun.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventJoinByTicket = False
                                        cl.updateGroup(G)
                                        invsend = 0
                                        Ti = cl.reissueGroupTicket(op.param1)
                                        ehun.acceptGroupInvitationByTicket(op.param1,Ti)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            ehun.acceptGroupInvitation(op.param1)
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                ehun.acceptGroupInvitation(op.param1)
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        G = ki.getGroup(op.param1)
                                        G.preventJoinByTicket = False
                                        ki.updateGroup(G)
                                        invsend = 0
                                        Ticket = ki.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ehun.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    except:
                                        try:
                                            kk.cancelGroupInvitation(op.param1, [op.param2])
                                            cl.acceptGroupInvitation(op.param1)
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass

        if op.type == 19:
            if Amid in op.param3:
                if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                k1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        G = kk.getGroup(op.param1)
                                        G.preventJoinByTicket = False
                                        kk.updateGroup(G)
                                        invsend = 0
                                        Ti = kk.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ehun.acceptGroupInvitationByTicket(op.param1,Ti)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    except:
                                        try:
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass
        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            k1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        G = kc.getGroup(op.param1)
                                        G.preventJoinByTicket = False
                                        kc.updateGroup(G)
                                        invsend = 0
                                        Ti = kc.reissueGroupTicket(op.param1)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ehun.acceptGroupInvitationByTicket(op.param1,Ti)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    except:
                                        try:
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k1.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass

        if op.type == 19:
            if Cmid in op.param3:
                if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        X = k1.getGroup(op.param1)
                                        X.preventJoinByTicket = True
                                        k1.updateGroup(X)
                                        invsend = 0
                                        Ti = k1.reissueGroupTicket(op.param1)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ehun.acceptGroupInvitationByTicket(op.param1,Ti)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    except:
                                        try:
                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass

        if op.type == 19:
            if Dmid in op.param3:
                if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        G = cl.getGroup(op.param1)
                                        G.preventJoinByTicket = False
                                        cl.updateGroup(G)
                                        invsend = 0
                                        Ti = cl.reissueGroupTicket(op.param1)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ehun.acceptGroupInvitationByTicket(op.param1,Ti)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    except:
                                        try:
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            k1.acceptGroupInvitation(op.param1)
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                k1.acceptGroupInvitation(op.param1)
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass

        if op.type == 19:
            if wait["js"] == True:
                if op.param3 in Emid:
                    if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        ehun.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        ehun.findAndAddContactsByMid(op.param1,[lid])
                        ehun.inviteIntoGroup(op.param1,[lid])
                    else:
                        pass
                if op.param3 in lid:
                    if op.param2 in Bots:
                        ehun.findAndAddContactsByMid(op.param1,[lid])
                        ehun.inviteIntoGroup(op.param1,[lid])
                    #ehun.kickoutFromGroup(op.param1,[op.param2])
                    else:
                        ehun.findAndAddContactsByMid(op.param1,[lid])
                        ehun.inviteIntoGroup(op.param1,[lid])
                        ehun.kickoutFromGroup(op.param1,[op.param2])
                        pass
#        if op.type == 19:
 #           if wait["prkick"] == True:
  #              if op.param3 Bots:
   #                 if op.param2 in Bots and op.param2 in Creator and op.param2 in admin:
    #                    pass
     #               else:
      #                  G = cl.getGroup(op.param1)
       #                 G.preventedJoinByTicket = False
        #                cl.updateGroup(G)
         #               Ticket = cl.reissueGroupTicket(op.param1)
          #              ehun.acceptGroupInvitationByTicket(op.param1,Ticket)
           #             cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            #            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
             #           kk.acceptGroupInvitationByTicket(op.param1,Ticket)
              #          kc.acceptGroupInvitationByTicket(op.param1,Ticket)
               #         k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                #        st.acceptGroupInvitationByTicket(op.param1,Ticket)
                 #       sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                  #      st.kickoutFromGroup(op.param1,[op.param2])
                   #     wait["blacklist"][op.param2] = True
                    #try:
                     #   sw.kickoutFromGroup(op.param1,[op.param2])
              
        #==========B A T A S ===========#

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            try:
                #if sender != cl.profile.mid:
                    #to = sender
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            cl.sendChatChecked(receiver, msg_id)
                            contact = cl.getContact(msg._from)
                            if text is None:
                                pass
                            if text.lower() == 'me':
                                cl.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                                start = time.time()
                                cl.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                cl.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'pic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).pictureStatus
                                    cl.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif 'cover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif text.lower() == "creator":
                                cl.sendMessage(receiver, None, contentMetadata={'mid': 'ub3808de9f7df35f57fb366d157f9790a'},contentType=13)
                                cl.sendMessage(receiver, "Itu Majikan Kami")
                            elif text.lower() == "virus":
                                cl.sendMessage(receiver, None, contentMetadata={'mid': "BEBAS,'"},contentType=13)
                            elif text.lower() == "my on":
                              if msg._from in admin:
                                wait["js"] = True
                                G = ehun.getGroup(msg.to)
                                lis = [lid]
                                ehun.inviteIntoGroup(msg.to,lis)
                                ehun.sendText(msg.to,"Ok on")
                            elif text.lower() == "link on":
                                wait["prkick"] = True
                                cl.sendText(msg.to,"Link di on")
                            elif text.lower() == "link off":
                                wait["prkick"] = False
                                cl.sendText(msg.to,"link di off")

                            elif text.lower() == "invite":
                                wait["invite"] = True
                                cl.sendText(msg.to, "Kirim contak nya")
                            elif 'Invit: ' in msg.text:
                              if msg._from in admin:
                                  midd = msg.text.replace("Invit: ","")
                                  cl.findAndAddContactsByMid(midd)
                                  cl.inviteIntoGroup(msg.to,[midd])
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == "cancel":
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = ehun.getGroup(msg.to)
                                    if X.invitee is not None:
                                        gInviMids = [contact.mid for contact in X.invitee]
                                        ehun.cancelGroupInvitation(msg.to, gInviMids)
                                    else:
                                        ehun.sendText(msg.to,"Tidak Ada Yang Pending")
                                else:
                                    ehun.sendText(msg.to,"Kusus Ehun")
                            elif text.lower() == "cancelgroup":
                                  gid = cl.getGroupIdsInvited()
                                  for i in gid:
                                      cl.rejectGroupInvitation(i)
                                      cl.sendText(msg.to,"All invitations have been refused")
                            elif text.lower() == "myqr on":
                              if msg._from in admin:
                                  wait["myqr"] = True
                                  ehun.sendMessage(msg.to, "Ok on")

                            elif text.lower() == "myqr off":
                              if msg._from in admin:
                                  wait["myqr"] = False
                                  ehun.sendMessage(msg.to, "Ok off")

                            elif text.lower() == 'invitebot':
                              if msg._from in admin:
                                  G = cl.getGroup(msg.to)
                                  lis = [kid,lid,Amid,Bmid,Cmid,Dmid]
                                  cl.inviteIntoGroup(msg.to,lis)
                                  ki.acceptGroupInvitation(msg.to)
                                  kk.acceptGroupInvitation(msg.to)
                                  kc.acceptGroupInvitation(msg.to)
                                  k1.acceptGroupInvitation(msg.to)
                              else:
                                  cl.sendMessage(msg.to,"Izin dulu kak sama boss\nb̶o̶tডা‮‮─┅═ই\nhttps://line.me/ti/p/~sarehun")



                            elif text.lower() == '*':
                              if msg._from in admin:
                                  G = ehun.getGroup(msg.to)
                                  lis = [kid,lid,mid,Amid,Bmid,Cmid,Dmid]
                                  ehun.inviteIntoGroup(msg.to,lis)
                                  cl.acceptGroupInvitation(msg.to)
                                  ki.acceptGroupInvitation(msg.to)
                                  kk.acceptGroupInvitation(msg.to)
                                  kc.acceptGroupInvitation(msg.to)
                                  k1.acceptGroupInvitation(msg.to)
                              else:
                                  cl.sendText(msg.to,"Kusus Ehun")
                            elif "!" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                  ehun.sendMessage(msg.to,sepi)
                                  _name = msg.text.replace("!","")
                                  G = ehun.getGroup(msg.to)
                                  targets = []
                                  for g in G.members + G.invitee:
                                      targets.append(g.mid)
                                  for target in targets:
                                      if target not in Bots:
                                         try:
    	                                     ehun.cancelGroupInvitation(msg.to, [target])
                                         except:
                                             pass
                                         try:
                                             ehun.kickoutFromGroup(msg.to, [target])
                                         except:
                                             pass

                            elif "Rx" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                  k1.sendMessage(msg.to,sepi)
                                  _name = msg.text.replace("Rx","")
                                  G = cl.getGroup(msg.to)
                                  G = ki.getGroup(msg.to)
                                  G = kk.getGroup(msg.to)
                                  G = kc.getGroup(msg.to)
                                  G = k1.getGroup(msg.to)
                                  targets = []
                                  for g in G.members + G.invitee:
                                      targets.append(g.mid)
                                  for target in targets:
                                      if target not in Bots:
                                          try:
                                              random.choice(ABC).cancelGroupInvitation(msg.to, [target])
                                          except:
                                              pass
                                          try:
                                              random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                          except:
                                              pass

                            elif text.lower() == 'add bot':
                              if msg._from in admin:
                                 try:
                                     cl.findAndAddContactsByMid(Ki)
                                     cl.findAndAddContactsByMid(kk)
                                     cl.findAndAddContactsByMid(kc)
                                     cl.findAndAddContactsByMid(k1)
                                     cl.findAndAddContactsByMid(ehun)
                                     cl.findAndAddContactsByMid(st)
                                     cl.findAndAddContactsByMid(sw)
                                     cl.sendMessage(msg.to,"Success add bot")
                                 except:
                                     cl.sendMessage(msg.to,"Udah beres boss")

                            elif text.lower() == 'tagall':
                              if msg._from in admin:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, nm10, nm11, nm12, nm13, nm14, nm15, jml = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], len(nama)
                                if jml <= 20:
                                    cl.mention(msg.to, nama)
                                if jml > 20 and jml < 40:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, len(nama)):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                if jml > 40 and jml < 60:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                if jml > 60 and jml < 80:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                if jml > 80 and jml < 100:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, len(nama)):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                if jml > 100 and jml < 120:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3+= [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, len(nama)):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                if jml > 120 and jml < 140:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, len(nama)):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                if jml > 140 and jml < 160:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, len(nama)):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                if jml > 160 and jml < 180:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                    for q in range(161, len(nama)):
                                        nm9 += [nama[q]]
                                    cl.mention(msg.to, nm9)
                                if jml > 180 and jml < 200:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    cl.mention(msg.to, nm9)
                                    for r in range(181, len(nama)):
                                        nm10 += [nama[r]]
                                    cl.mention(msg.to, nm10)
                                if jml > 200 and jml < 220:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    cl.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    cl.mention(msg.to, nm10)
                                    for s in range(201, len(nama)):
                                        nm11 += [nama[s]]
                                    cl.mention(msg.to, nm11)
                                if jml > 220 and jml < 240:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    cl.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    cl.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    cl.mention(msg.to, nm11)
                                    for t in range(221, len(nama)):
                                        nm12 += [nama[t]]
                                    cl.mention(msg.to, nm12)
                                if jml > 240 and jml < 260:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    cl.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    cl.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    cl.mention(msg.to, nm11)
                                    for t in range(221, 240):
                                        nm12 += [nama[t]]
                                    cl.mention(msg.to, nm12)
                                    for u in range(241, len(nama)):
                                        nm13 += [nama[u]]
                                    cl.mention(msg.to, nm13)
                                if jml > 260 and jml < 280:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    cl.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    cl.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    cl.mention(msg.to, nm11)
                                    for t in range(221, 240):
                                        nm12 += [nama[t]]
                                    cl.mention(msg.to, nm12)
                                    for u in range(241, 260):
                                        nm13 += [nama[u]]
                                    cl.mention(msg.to, nm13)
                                    for v in range(261, len(nama)):
                                        nm14 += [nama[v]]
                                    cl.mention(msg.to, nm14)
                                if jml > 280 and jml < 300:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    cl.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    cl.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    cl.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    cl.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    cl.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    cl.mention(msg.to, nm11)
                                    for t in range(221, 240):
                                        nm12 += [nama[t]]
                                    cl.mention(msg.to, nm12)
                                    for u in range(241, 260):
                                        nm13 += [nama[u]]
                                    cl.mention(msg.to, nm13)
                                    for v in range(261, 280):
                                        nm14 += [nama[v]]
                                    cl.mention(msg.to, nm14)
                                    for w in range(281, len(nama)):
                                        nm15 += [nama[w]]
                                    cl.mention(msg.to, nm15)
                                if jml <= 300:
                                    print('mention')
                                cl.sendText(receiver, "Members :"+str(jml))


                            elif text.lower() == 'sider':
                              if msg._from in admin:
                                cl.sendText(msg.to,"Siap Boss")
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                            elif text.lower() == 'ofsider':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    cl.sendText(msg.to,"Ok Off Boss")
                                else:
                                    cl.sendText(msg.to, "Heh belom di Set")
                            elif text.lower() == "mid":
                                cl.sendMessage(msg.to, msg._from)

                            elif text.lower() == 'help':
                                cl.sendText(msg.to,help)
                            elif text.lower() == 'help admin':
                                cl.sendText(msg.to,help2)
                            elif text.lower() == 'help creator':
                                cl.sendText(msg.to,help3)

                            elif "Mid @" in text:
                                _name = msg.text.replace("Mid @","")
                                _nametarget = _name.rstrip(' ')
                                gs = cl.getGroup(msg.to)
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        cl.sendText(msg.to, g.mid)
                                    else:
                                        pass

                            elif text.lower() == "bot?":
                                cl.sendMessage(receiver, None, contentMetadata={'mid': mid},contentType = 13)
                                ki.sendMessage(receiver, None, contentMetadata={'mid': Amid},contentType = 13)
                                kk.sendMessage(receiver, None, contentMetadata={'mid': Bmid},contentType = 13)
                                kc.sendMessage(receiver, None, contentMetadata={'mid': Cmid},contentType = 13)
                                k1.sendMessage(receiver, None, contentMetadata={'mid': Dmid},contentType = 13)

                            elif text.lower() == 'halo':
                              if msg._from in admin:
                                  G = ehun.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  ehun.updateGroup(G)
                                  invsend = 0
                                  X = ehun.reissueGroupTicket(msg.to)
                                  cl.acceptGroupInvitationByTicket(msg.to,X)
                                  ki.acceptGroupInvitationByTicket(msg.to,X)
                                  kk.acceptGroupInvitationByTicket(msg.to,X)
                                  kc.acceptGroupInvitationByTicket(msg.to,X)
                                  k1.acceptGroupInvitationByTicket(msg.to,X)
                                  G = cl.getGroup(msg.to)
                                  G.preventJoinByTicket = True
                                  cl.updateGroup(G)
                              else:
                                  cl.sendText(msg.to,"Khusus admin")

                            elif text.lower() == 'join':
                              if msg._from in admin:
                                  G = cl.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  cl.updateGroup(G)
                                  invsend = 0
                                  X = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,X)
                                  kk.acceptGroupInvitationByTicket(msg.to,X)
                                  kc.acceptGroupInvitationByTicket(msg.to,X)
                                  k1.acceptGroupInvitationByTicket(msg.to,X)
                                  G.preventJoinByTicket = True
                                  cl.updateGroup(G)
                              else:
                                  cl.sendText(msg.to,"Khusus admin")

                            elif text.lower() == 'ourl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.preventJoinByTicket = False
                                    cl.updateGroup(X)
                                    cl.sendText(msg.to,"Url Sudah Di Aktifkan")
                                else:
                                    cl.sendText(msg.to,"Sudah di buka")
                            elif text.lower() == 'curl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.preventJoinByTicket = True
                                    cl.updateGroup(X)
                                    cl.sendText(msg.to,"Url Sudah Di Nonaktifkan")
                                else:
                                    cl.sendText(msg.to,"Sudah di tutup")
                            elif text.lower() == 'gurl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    x = cl.getGroup(msg.to)
                                    if x.preventJoinByTicket == True:
                                        x.preventJoinByTicket = False
                                        cl.updateGroup(x)
                                    gurl = cl.reissueGroupTicket(msg.to)
                                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                                else:
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Can't be used outside the group")
                                    else:
                                        cl.sendText(msg.to,"Not for use less than group")


                            elif ("Gn: " in msg.text):
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.name = msg.text.replace("Gn: ","")
                                    cl.updateGroup(X)
                                else:
                                    cl.sendText(msg.to,"It can't be usedbesides the group.")

                            elif text.lower() == "ginfo":
                              if msg.toType == 2:
                                    ginfo = cl.getGroup(msg.to)
                                    try:
                                        gCreator = ginfo.creator.displayName
                                    except:
                                        gCreator = "Error"
                                    if wait["lang"] == "JP":
                                        if ginfo.invitee is None:
                                            sinvitee = "0"
                                        else:
                                            sinvitee = str(len(ginfo.invitee))
                                        if ginfo.preventJoinByTicket == True:
                                            u = "Tertutup"
                                        else:
                                            u = "Terbuka"
                                        timeCreated = []
                                        timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(ginfo.createdTime) / 1000)))
                                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\nWaktu Dibuat : " + str(timeCreated) + "\n\nMembers:" + str(len(ginfo.members)) + "   Member\n\nPending:" + sinvitee + "  Orang\n\nURL:" + u)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': ginfo.creator.mid}, contentType=13)
                                        cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+ginfo.pictureStatus)
                                    else:
                                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                              else:
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Can not be used outside the group")
                                    else:
                                        cl.sendText(msg.to,"Not for use lessthan group")


                            elif 'Id ' in text:
                                msgg = msg.text.replace('Id ',"")
                                conn = cl.findContactsByUserid(msgg)
                                if True:
                                   msg.contentType = 13
                                   msg.contentMetadata = {'mid': conn.mid}
                                   cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                                   cl.sendMessage(msg)
                            elif text.lower() == "on":
                              if msg._from in admin:
                                wait["AutoJoinCancel"] = True
                                wait["AutoJoin"] = True
                                wait["AutoCancel"] = True
                                wait["prinvite"] = True
                                wait["Join"] = True
                                wait["qr"] =  True
                                cl.sendText(msg.to,"All Protect on")
                            elif text.lower() == "off":
                              if msg._from in admin:
                                wait["AutoJoinCancel"] = False
                                wait["AutoJoin"] = False
                                wait["AutoCancel"] = False
                                wait["prinvite"] = False
                                wait["Join"] = False
                                wait["qr"] = False
                                cl.sendText(msg.to,"All Protect off")

                            elif text.lower() == "status":
                              if msg._from in admin:
                                md = ""
                                if wait["AutoCancel"] == True: md+="╠➩✔️ Auto Cancel : On\n"
                                else: md+="╠➩❌ Auto Cancel : Off\n"
                                if wait["prinvite"] == True: md+="╠➩✔️ Invite Protect : On\n"
                                else: md+="╠➩❌ Invite Protect : Off\n"
                                if wait["Join"] == True: md+="╠➩✔️ Join kick : On\n"
                                else:md+="╠➩❌ Join Kick : Off\n"
                                if wait["qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
                                else:md+="╠➩❌ Qr Protect : Off\n"
                                if wait["AutoJoinCancel"] == True: md+="╠➩✔️ AutoCancel : On\n"
                                else:md+="╠➩❌ JoinCancel : Off\n"
                                if wait["AutoJoin"] == True: md+="╠➩✔️ Join : On\n"
                                else:md+="╠➩❌ Join : Off\n"
                                cl.sendText(msg.to,"╔════════════════\n║           ☆☞ S T A T U S ☜☆\n╠═════════════════\n" + md + "╚═════════════════")
#--------'----------------#

                            elif text.lower() == "remove chat":
                              if msg._from in admin:
                                  try:
                                      ehun.removeAllMessages(op.param2)
                                      cl.removeAllMessages(op.param2)
                                      ki.removeAllMessages(op.param2)
                                      kk.removeAllMessages(op.param2)
                                      kc.removeAllMessages(op.param2)
                                      k1.removeAllMessages(op.param2)
                                      st.removeAllMessages(op.param2)
                                      sw.removeAllMessages(op.param2)
                                      cl.sendMessage(msg.to,"beres")
                                  except:
                                      pass

                            elif text.lower() == 'j on':
                              if msg._from in Creator:
                                  wait["AutoJoin"] = True
                                  cl.sendText(msg.to, "join aktip")
                              else:
                                  cl.sendText(msg.to, "Sudah on")
                            elif text.lower() == 'j off':
                              if msg._from in Creator:
                                  wait["AutoJoin"] = False
                                  cl.sendText(msg.to, "join off")
                              else:
                                  cl.sendText(msg.to, "Blom on")
                            elif text.lower() == 'jcancel on':
                              if msg._from in admin:
                                  wait["AutoJoinCancel"] = True
                                  cl.sendText(msg.to,"AutoJoinCancel on")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'jcancel off':
                              if msg._from in admin:
                                  wait["AutoJoinCancel"] = False
                                  cl.sendText(msg.to,"AutoJoinCancel off")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'joinkick on':
                              if msg._from in admin:
                                  wait["Join"] = True
                                  cl.sendText(msg.to,"AutoKick on")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'joinkick off':
                              if msg._from in admin:
                                  wait["Join"] = False
                                  cl.sendText(msg.to,"AutoKick off")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'prcancel on':
                              if msg._from in admin:
                                  wait["prcancel"] = True
                                  cl.sendText(msg.to,"protectcancel on")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'prcancel off':
                              if msg._from in admin:
                                  wait["prcancel"] = False
                                  cl.sendText(msg.to,"protectcancel off")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'qr on':
                              if msg._from in admin:
                                  wait["qr"] = True
                                  cl.sendText(msg.to,"Qr on")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'qr off':
                              if msg._from in admin:
                                  wait["qr"] = False
                                  cl.sendText(msg.to,"Qr off")
                              else:
                                 cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'cancel on':
                              if msg._from in admin:
                                  wait["AutoCancel"] = True
                                  cl.sendText(msg.to,"AutoCancel on")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'cancel off':
                              if msg._from in admin:
                                  wait["AutoCancel"] = False
                                  cl.sendText(msg.to,"AutoCancel off")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")

                            elif text.lower() == 'namelock on':
                              if msg._from in admin:
                                if msg.to in wait['pname']:
                                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.  \nJam :" + datetime.today().strftime('%H:%M:%S'))
                                else:
                                    wait['pname'][msg.to] = True
                                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
                                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.  \nJam :" + datetime.today().strftime('%H:%M:%S'))
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'namelock off':
                              if msg._from in admin:
                                if msg.to in wait['pname']:
                                  cl.sendText(msg.to,"ƬƲƦƝЄƊ Ơff \nJam :" + datetime.today().strftime('%H:%M:%S'))
                                  del wait['pname'][msg.to]
                                else:
                                  cl.sendText(msg.to,"Khusus admin")
                              else:
                                  pass

                            elif text.lower() == "code":
                              if msg._from in Creator:
                                cl.sendText(msg.to,"Bubar bubar")
                                cl.sendText(msg.to,Ehun)
                                cl.sendText(msg.to,Ehun)
                                cl.sendText(msg.to,Ehun)
                                cl.sendText(msg.to,"Success")
                            elif 'Addall' in msg.text:
                              if msg._from in Creator:
                                if msg.toType == 2:
                                   print('Ok')
                                   _name = msg.text.replace("Addall","")
                                   gs = cl.getGroup(msg.to)
                                   gs = ki.getGroup(msg.to)
                                   gs = kk.getGroup(msg.to)
                                   gs = kc.getGroup(msg.to)
                                   gs = k1.getGroup(msg.to)
                                   ki.sendText(msg.to,"Naah~")
                                   targets = []
                                   for g in gs.members:
                                       if _name in g.displayName:
                                           targets.append(g.mid)
                                   if targets == []:
                                       ki.sendText(msg.to,"Sudah boss.")
                                   else:
                                       for target in targets:
                                           try:
                                               random.choice(ABC).findAndAddContactsByMid(msg.to,[target])
                                               print(msg.to,[g.mid])
                                           except Exception as e:
                                               cl.sendText(msg.to,str(e))
                            elif "Banall" in msg.text:
                              if msg._from in Creator:
                                if msg.toType == 2:
                                   _name = msg.text.replace("Banall","")
                                   gs = ehun.getGroup(msg.to)
                                   gs = cl.getGroup(msg.to)
                                   gs = ki.getGroup(msg.to)
                                   gs = kk.getGroup(msg.to)
                                   gs = kc.getGroup(msg.to)
                                   gs = k1.getGroup(msg.to)
                                   cl.sendMessage(msg.to,"Successban all members")
                                   targets = []
                                   for g in gs.members:
                                       if _name in g.displayName:
                                           targets.append(g.mid)
                                   if targets == []:
                                       ki.sendText(msg.to,"Error")
                                   else:
                                       for target in targets:
                                           if target not in Bots:
                                                try:
                                                    wait["blacklist"][target] = True
                                                except:
                                                    pass
 

                            elif "? " in text:
                              if msg._from in admin:
                                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                                      names = re.findall(r'@(\w+)', msg.text)
                                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                      mentionees = mention['MENTIONEES']
                                      for mention in mentionees:
                                          cl.kickoutFromGroup(msg.to,[mention['M']])

                            elif "Jemput " in text:
                              if msg._from in admin:
                                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                                      names = re.findall(r'@(\w+)', msg.text)
                                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                      mentionees = mention['MENTIONEES']
                                      for mention in mentionees:
                                          cl.inviteIntoGroup(msg.to,[mention['M']])

                            elif text.lower() == 'restart': 
                              if msg._from in admin:
                                  cl.sendText(receiver,"Ok bot di ulang")
                                  restart_program()
                              else:
                                  cl.sendText(msg.to,"Kuhsus admin")

                            elif "recover" in msg.text:
                              if msg._from in Creator:
                                  thisgroup = cl.getGroups([msg.to])
                                  Mids = [contact.mid for contact in thisgroup[0].members]
                                  mi_d = Mids[:33]
                                  t = 20
                                  while(t):
                                    cl.createGroup("b̶o̶tডা‮‮─┅═ই", mi_d)
                                    t-=1
                                  cl.sendText(msg.to,"Success To b̶o̶tডা‮‮─┅═ই")
                              else:
                                  cl.sendText(msg.to,"Kusus Creator")

                            elif "Spam " in msg.text:
                              if msg._from in Creator:
                                  bctxt = msg.text.replace("Spam ","")
                                  t = 20
                                  while(t):
                                    cl.sendText(msg.to, (bctxt))
                                    t-=1
                            elif "Spam: " in msg.text:
                                try:
                                    group = msg.text.replace("Spam: ","")
                                    gid = group[:33]
                                    name = group.replace(grouptags[:34],"")
                                    cl.createGroup(gid,name)
                                    cl.sendText(msg.to,"We created an album" + name)
                                except:
                                    cl.sendText(msg.to,"Error")
                            elif "999+ " in msg.text:
                               if msg._from in Creator:
                                   bctxt = msg.text.replace("999+ ", "")
                                   t = cl.getAllContactIds()
                                   t = 3
                                   while(t):
                                      cl.sendText(msg.to, (bctxt))
                                      t-=1


                            elif "Spm @" in msg.text:
                              if msg._from in Creator:
                                  _name = msg.text.replace("Spm @","")
                                  _nametarget = _name.rstrip(' ')
                                  gs = cl.getGroup(msg.to)
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          cl.sendText(msg.to,"Yes")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.createGroup(g.mid,"Spammed")
                                          cl.sendText(msg.to,"Success")

                            elif text.lower() == 'kalender':
                                timeNow = datetime.now()
                                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                inihari = datetime.today()
                                hr = inihari.strftime('%A')
                                bln = inihari.strftime('%m')
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                cl.sendText(receiver,hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M%S') + " ]")
                            elif text.lower() == 'rtime':
                                eltime = time.time() - mulai
                                cl.sendText(receiver,"Ehun Bot Sudah BerjalanSelama :\n"+waktu(eltime))

                            elif "Setpoin" in msg.text:
                                cl.sendText(msg.to,"☆> Set <☆('・ω・') Jam [ " + datetime.today().strftime('%H:%M:%S') + " ]")
                                try:
                                    del wait2['readPoint'][msg.to]
                                    del wait2['readMember'][msg.to]
                                except:
                                    pass
                                now2 = datetime.now()
                                wait2['readPoint'][msg.to] = msg.id
                                wait2['readMember'][msg.to] = ""
                                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M:%S")
                                wait2['ROM'][msg.to] = {}
                            elif msg.text in ["Laspoin"]:
                                if msg.to in wait2['readPoint']:
                                   if wait2["ROM"][msg.to].items() == []:
                                        chiya = ""
                                   else:
                                        chiya = ""
                                        for rom in wait2["ROM"][msg.to].items():
                                            chiya += rom[1] + "\n"

                                   cl.sendText(msg.to,"      ||By : ✰Ehun bot✰||\n   Ini kak yang on tadi !!!\n-----------------------------------\n%s\n%s\nDoain sehat Ceria Semua ya kak (-_-)\n-----------------------------------\n    Setpoin ('・ω・')  Jam  [%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                                else:
                                   cl.sendText(msg.to,"Ktik 👉 Setpoin 👈 dulu")
                            elif text.lower() == 'left':
                              if msg._from in admin:
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendText(msg.to, "izin left kakak semuanya\nBýe bye byeeeeeeeeeeeee\n" + str(ginfo.name) + "\nAssalamualaikum wr wb\nSampai jumpa lagi kakak semua nya")
                                  cl.leaveGroup(msg.to)
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'bye':
                              if msg._from in admin:
                                  ki.leaveGroup(msg.to)
                                  kk.leaveGroup(msg.to)
                                  kc.leaveGroup(msg.to)
                                  k1.leaveGroup(msg.to)
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif "Leave" in msg.text:
                              if msg._from in admin:
                                  gid = cl.getGroupIdsJoined()
                                  for i in gid:
                                      cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!\nAyo left teman2\nAssalamualikum wr wb All memer\nAdd Owner kami")
                                      cl.sendContact(i,"ub3808de9f7df35f57fb366d157f9790a")
                                      cl.leaveGroup(i)
                                      ki.leaveGroup(i)
                                      kk.leaveGroup(i)
                                      kc.leaveGroup(i)
                                      k1.leaveGroup(i)
                                      st.leaveGroup(i)
                                      sw.leaveGroup(i)
                                      cl.sendText(msg.to,"Success Leave All Group")
                              else:
                                  cl.sendText(msg.to,"Khusus Admin")
                            elif text.lower() == "check":
                              if msg._from in admin:
                                  try:ehun.inviteIntoGroup(to, ["ub3808de9f7df35f57fb366d157f9790a"]);has = "OK"
                                  except:has = "NOT"
                                  try:ehun.kickoutFromGroup(to, ["ub3808de9f7df35f57fb366d157f9790a"]);has1 = "OK"
                                  except:has1 = "NOT"
                                  if has == "OK":sil = "normal"
                                  else:sil = "limit"
                                  if has1 == "OK":sil1 = "normal"
                                  else:sil1 = "limit"
                                  ehun.sendMessage(msg.to, "Statust\nKick : {} \nInvite : {}".format(sil1,sil))

                            elif text.lower() == "kicker join":
                              if msg._from in admin:
                                  G = ehun.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  ehun.updateGroup(G)
                                  invsend = 0
                                  Ti = ehun.reissueGroupTicket(msg.to)
                                  st.acceptGroupInvitationByTicket(msg.to,Ti)
                                  sw.acceptGroupInvitationByTicket(msg.to,Ti)
                                  G = sw.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  sw.updateGroup(G)

                            elif text.lower() == "kicker":
                              if msg._from in admin:
                                  ginfo = ehun.getGroup(msg.to)
                                  lis = [kid,lid]
                                  ehun.inviteIntoGroup(msg.to,lis)
                                  st.acceptGroupInvitataion(msg.to)
                                  sw.acceptGroupInvitation(msg.to)
                            elif text.lower() == "kicker bye":
                              if msg._from in admin:
                                  ginfo = ehun.getGroup(msg.to)
                                  st.leaveGroup(msg.to)
                                  sw.leaveGroup(msg.to)
                                  lis = [kid,lid]
                                  ehun.inviteIntoGroup(msg.to,lis)
                            elif text.lower() == 'reinvite':
                              if msg._from in admin:
                                if msg.toType == 2:
                                  cl.sendText(msg.to,"Laksanakn bot.")
                                  ki.leaveGroup(msg.to)
                                  kk.leaveGroup(msg.to)
                                  G = cl.getGroup(msg.to)
                                  ginfo = cl.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  cl.updateGroup(G)
                                  invsend = 0
                                  X = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,X)
                                  time.sleep(0.001)
                                  kk.acceptGroupInvitationByTicket(msg.to,X)
                                  time.sleep(0.001)
                                  kc.acceptGroupInvitationByTicket(msg.to,X)
                                  time.sleep(0.001)
                                  cl.sendText(msg.to,"Sudah lengkap boss")
                                  G.preventJoinByTicket = True
                                  kc.updateGroup(G)
                                  kc.leaveGroup(msg.to)
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif 'Clear invites' in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                         cl.cancelGroupInvitation(msg.to,[_mid])
                                         
#cl.sendText(msg.to,"Beres Boss")
                            elif 'Clean invites' in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    if X.invitee is not None:
                                        gInviMids = [contact.mid for contact in X.invitee]
                                        random.choice(ABC).cancelGroupInvitation(msg.to, gInviMids)
                                    else:
                                        if wait["lang"] == "JP":
                                            cl.sendText(msg.to,"No one is inviting。")
                                        else:
                                            cl.sendText(msg.to,"Sorry, nobody absent")
                                else:
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Can not be used")
                                    else:
                                        cl.sendText(msg.to,"Can not be used last group")
                            elif "Ban @" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    print("@Ban by mention")
                                    _name = msg.text.replace("Ban @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to,"Not found")
                                    else:
                                        for target in targets:
                                            if target not in Creator:
                                                try:
                                                    wait["blacklist"][target] = True
                                                    cl.sendText(msg.to,"Succes BosQ")
                                                except:
                                                    cl.sendText(msg.to,"Error")
                                            else:
                                                cl.sendText(msg.to,"Creator Detected~")
                            elif "Unban @" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    print("@Unban by mention")
                                    _name = msg.text.replace("Unban @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to,"Not found")
                                    else:
                                        for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendText(msg.to,"Succes BosQ")
                                            except:
                                                cl.sendText(msg.to,"Succes BosQ")
                            elif text.lower() == 'banlist':
                                if wait["blacklist"] == {}:
                                    cl.sendText(msg.to,"Tidak Ada")
                                else:
                                    mc = ""
                                for mi_d in wait["blacklist"]:
                                    mc += "->" +cl.getContact(mi_d).displayName + "\n"
                                cl.sendText(msg.to,"===[Blacklist User]===\n"+mc)
                            elif text.lower() == 'kill':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.members]
                                    matched_list = []
                                    for tag in wait["blacklist"]:
                                        matched_list+=filter(lambda str: str == tag, gMembMids)
                                    if matched_list == []:
                                        cl.sendText(msg.to,"Fuck You")
                                        pass
                                    for jj in matched_list:
                                        try:
                                            cl.kickoutFromGroup(msg.to,[jj])
                                            print(msg.to,[jj])
                                        except:
                                            pass
                            elif text.lower() == 'clearban':
                              if msg._from in admin:
                                  wait["blacklist"] = {}
                                  cl.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All")


                            elif text.lower() == 'memlist':
                                  kontak = cl.getGroup(msg.to)
                                  group = kontak.members
                                  num=1
                                  msgs="═════════List Member═�����═══════-"
                                  for ids in group:
                                      msgs+="\n[%i] %s" % (num, ids.displayName)
                                      num=(num+1)
                                  msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                                  cl.sendText(msg.to, msgs)
                            elif "Inpo " in msg.text:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = cl.getContact(key1)
                                cu = cl.getCover(key1)
                                try:
                                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                                except:
                                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
                            elif text.lower() == 'glist':
                                cl.sendText(msg.to, "Tunggu Sebentar. . .")
                                gid = cl.getGroupIdsJoined()
                                h = ""
                                jml = 0
                                for i in gid:
                                    h += "╠➩" + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                                    jml += 1
                                cl.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")
                            elif text.lower() == 'adminlist':
                              if admin == []:
                                  cl.sendText(msg.to,"The stafflist is empty")
                              else:
                                  cl.sendText(msg.to,"Tunggu...")
                                  mc = "||Admin Ehun Bot||\n=====================\n"
                                  for mi_d in admin:
                                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                                  cl.sendText(msg.to,mc)
                                  print("[Command]Stafflist executed")
                            elif text.lower() == 'sticker on':
                                  wait["sticker"] = True
                                  cl.sendText(msg.to,"Sticker activ")
                            elif text.lower() == 'sticker off':
                                  wait["sticker"] = False
                                  cl.sendText(msg.to,"Sticker non activ")


                            elif text.lower() == 'k on':
                                wait["Contact"] = True
                                cl.sendText(msg.to,"Contact activ")
                            elif text.lower() == 'k off':
                                wait["Contact"] = False
                                cl.sendText(msg.to,"Contact di off")
                            elif text.lower() == 'bot on':
                              if msg._from in admin:
                                  wait["Bot"] = True
                                  cl.sendText(msg.to,"Bot di on")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'bot off':
                              if msg._from in admin:
                                  wait["Bot"] = False
                                  cl.sendText(msg.to,"Bot di off")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'respon on':
                              if msg._from in admin:
                                  wait['detectMention'] = True
                                  cl.sendText(msg.to,"Auto Respon on")
                              else:
                                  pass
                            elif text.lower() == 'respon off':
                              if msg._from in admin:
                                  wait['detectMention'] = False
                                  cl.sendText(msg.to,"Auto Respon off")
                              else:
                                  pass
                            elif "Admin add @" in msg.text:
                              if msg._from in Creator:
                                  print("[Command]Staff add executing")
                                  _name = msg.text.replace("Admin add @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = cl.getGroup(msg.to)
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = k1.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      cl.sendText(msg.to,"Contact not found")
                                  else:
                                      for target in targets:
                                          try:
                                              admin.append(target)
                                              cl.sendText(msg.to,"Admin Ditambahkan")
                                          except:
                                              pass
                              else:
                                  cl.sendText(msg.to,"Perintah Ditolak.\nHanya untuk Creator")
                            elif "Admindel @" in msg.text:
                              if msg._from in Creator:
                                  print("[Command]Staff remove executing")
                                  _name = msg.text.replace("Admindel @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = cl.getGroup(msg.to)
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = k1.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      cl.sendText(msg.to,"Contact not found")
                                  else:
                                      for target in targets:
                                          try:
                                              admin.remove(target)
                                              cl.sendText(msg.to,"Admin Dihapus")
                                          except:
                                              pass
                              else:
                                  cl.sendText(msg.to,"Perintah Ditolak.\nHanya untuk Creator")

                            elif "Bom" in msg.text:
                              if msg._from in Creator:
                                  nk0 = msg.text.replace("Bom","")
                                  nk1 = nk0.lstrip()
                                  nk2 = nk1.replace("all","")
                                  nk3 = nk2.rstrip()
                                  _name = nk3
                                  gs = cl.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _name in g.displayName:
                                         targets.append(g.mid)
                                  if targets == []:
                                      pass
                                  else:
                                      for target in targets:
                                          try:
                                              cl.kickoutFromGroup(msg.to,[target])
                                              print(msg.to,[g.mid])
                                          except:
                                              cl.sendText(mg.to,"Rata? Protect Boss")
                              else:
                                  pass
                            elif "Sayang" in msg.text:
                              if msg._from in admin:
                                  G = ehun.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  ehun.updateGroup(G)
                                  invsend = 0
                                  Ti = ehun.reissueGroupTicket(msg.to)
                                  st.acceptGroupInvitationByTicket(msg.to,Ti)
                                  sw.acceptGroupInvitationByTicket(msg.to,Ti)
                                  G.preventJoinByTicket = True
                                  ehun.updateGroup(G)
                                  _name = msg.text.replace("Sayang","")
                                  gs = st.getGroup(msg.to)
                                  gs = sw.getGroup(msg.to)
                                  targets = []
                                  for s in gs.members:
                                      if _name in s.displayName:
                                          targets.append(s.mid)
                                  if targets ==[]:
                                      st.sendMessage(msg.to,"user does")
                                      pass
                                  else:
                                      for target in targets:
                                          if target not in Bots:
                                              try:
                                                  klist = [st,sw]
                                                  kicker = random.choice(klist)
                                                  kicker.kickoutFromGroup(msg.to,[target])
                                                  print(msg.to,[s.mid])
                                              except Exception as e:
                                                  sw.sendText(msg.to,str(e))

                            elif "Cium " in msg.text:
                              if msg._from in Creator:
                                nk0 = msg.text.replace("Cium ","")
                                nk1 = nk0.lstrip()
                                nk2 = nk1.replace("@","")
                                nk3 = nk2.rstrip()
                                _name = nk3
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                X = cl.reissueGroupTicket(msg.to)
                                st.acceptGroupInvitationByTicket(msg.to,X)
                                time.sleep(0.001)
                                targets = []
                                for s in gs.members:
                                    if _name in s.displayName:
                                        targets.append(s.mid)
                                if targets ==[]:
                                    st.sendMessage(msg.to,"user does notexist")
                                    pass
                                else:
                                    for target in targets:
                                        try:
                                            st.kickoutFromGroup(msg.to,[target])
                                            st.leaveGroup(msg.to)
                                            print(msg.to,[g.mid])
                                        except:
                                            G = cl.getGroup(msg.to)
                                            G.preventJoinByTicket = True
                                            cl.updateGroup(G)
                                            pass

                            elif text.lower() == 'ks':
                              if msg._from in Creator:
                                if msg.toType == 2:
                                    print("Kick Siri")
                                    x = cl.getGroup(msg.to)
                                    if cl in [i.mid for i in x.members]:
                                        sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                        if sirilist == []:
                                            cl.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                                        for target in sirilist:
                                            try:
                                                cl.kickoutFromGroup(msg.to,[target])
                                            except:
                                                pass
                            elif "Bangroup: " in msg.text:
                                  grp = msg.text.replace("Bangroup: ","")
                                  gid = cl.getGroupIdsJoined()
                                  if msg._from in admin:
                                      for i in gid:
                                          h = cl.getGroup(i).name
                                          if h == grp:
                                              wait["BlGroup"][i]=True
                                              cl.sendText(msg.to, "Success Ban Group : "+grp)
                                          else:
                                              pass
                                  else:
                                      cl.sendText(msg.to, "Khusus Admin")

                            elif text.lower == 'listban':
                              if msg._from in admin:
                                  if wait["BlGroup"] == {}:
                                      cl.sendText(msg.to,"Tidak Ada")
                                  else:
                                      mc = ""
                                      for gid in wait["BlGroup"]:
                                          mc += "-> " +cl.getGroup(gid).name + "\n"
                                          cl.sendText(msg.to,"===[Ban Group]===\n"+mc)
                              else:
                                  cl.sendText(msg.to, "Khusus Admin")
 
                            elif "Delban: " in msg.text:
                              if msg._from in admin:
                                  ng = msg.text.replace("Delban: ","")
                                  for gid in wait["BlGroup"]:
                                      if cl.getGroup(gid).name == ng:
                                          del wait["BlGroup"][gid]
                                          cl.sendText(msg.to, "Success del ban "+ng)
                                      else:
                                          pass
                              else:
                                  cl.sendText(msg.to, "Khusus Admin")

 
                            elif text.lower() == 'timeline':
                              if msg._from in admin:
                                  try:
                                      url = cl.activity(limit=5)
                                      cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
                                  except:
                                      pass
                            elif text.lower() == 'autolike':
                              if msg._from in admin:
                                  wait["likeOn"] = True
                                  cl.sendText(msg.to,"Shere PostKamu Yang Mau Di Like!")
                            elif msg.text in ["Steal contact"]:
                                  wait["steal"] = True
                                  cl.sendText(msg.to,"Send Contact")
                            elif msg.text in ["Giftbycontact"]:
                                  wait["gift"] = True
                                  cl.sendText(msg.to,"Send Contact")
                            

                            elif text.lower() == 'vm':
                              if msg._from in admin:
                                  cl.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzes.com\n>redtube.com\n>youporn.com")
                              else:
                                  cl.sendText(msg.to,"Khusus Creator")

                            elif ("Micadd " in msg.text):
                                  targets = []
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      try:
                                          mimic["target"][target] = True
                                          cl.sendText(msg.to,"Target ditambahkan!")
                                          break
                                      except:
                                          cl.sendText(msg.to,"Fail !")
                                          break
                            elif ("Micdel " in msg.text):
                                  targets = []
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      try:
                                          del mimic["target"][target]
                                          cl.sendText(msg.to,"Target dihapuskan!")
                                          break
                                      except:
                                          cl.sendText(msg.to,"Fail !")
                                          break

                            elif msg.text in ["Miclist"]:
                                  if mimic["target"] == {}:
                                      cl.sendText(msg.to,"Nothing")
                                  else:
                                     mc = "Target Mimic User:\n"
                                  for mi_d in mimic["target"]:
                                     mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                                     cl.sendText(msg.to,mc)

                            elif "Mimic target " in msg.text:
                                   if mimic["copy"] == True:
                                       siapa = msg.text.replace("Mimic target ","")
                                       if siapa.rstrip(' ') == "me":
                                           mimic["copy2"] = "me"
                                           cl.sendText(msg.to,"Mimic change to me")
                                       elif siapa.rstrip(' ') == "target":
                                           mimic["copy2"] = "target"
                                           cl.sendText(msg.to,"Mimic change to target")
                                   else:
                                       cl.sendText(msg.to,"I dont know")
                            elif "Mimic " in msg.text:
                                   cmd = msg.text.replace("Mimic ","")
                                   if cmd == "on":
                                       if mimic["status"] == False:
                                           mimic["status"] = True
                                           cl.sendText(msg.to,"Reply Message on")
                                       else:
                                           cl.sendText(msg.to,"Sudah on")
                                   elif cmd == "off":
                                       if mimic["status"] == True:
                                           mimic["status"] = False
                                           cl.sendText(msg.to,"Reply Message off")
                                       else:
                                           cl.sendText(msg.to,"Sudah off")


                                  

            except:
                pass
                #cl.log(error)
                
#traceback.print_tb(error.__traceback__)
                    
        if op.type == 55:
                try:
                    print("[ 55 ] Auto sider")
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            Np = cl.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                cl.sendText(op.param1,"Halo kak @!         ,\n"+str(random.choice(pref))+'👉'+Name+'👈')
                                cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

          

        if op.type == 55:
                try:
                   print("[ 55 ] Auto read")
                   if op.param1 in wait2['readPoint']:
                     Name = cl.getContact(op.param2).displayName
                     if Name in wait2['readMember'][op.param1]:
                        pass
                     else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name + "\nOn Jam : " + datetime.today().strftime('%H:%M:%S')
                   else:
                     cl.sendText
                except:
                    pass

             #if op.type == 55:
                 

            #if op.type == 55:
             # if op.param2 not in Creator:
                #if op.param2 not in Bots:
                  #if wait ["blacklist"]:
                   # cl.kickoutFromGroup(op.param1,[op.param2])
              #else:
                  #pass


    
        if op.type == 11:
                print("[ 11 ] Auto Namelock")
                if op.param3 == '1':
                    if op.param1 in wait['pname']:
                        try:
                            G = cl.getGroup(op.param1)
                        except:
                            pass
                        G.name = wait['pro_name'][op.param1]
                        try:
                            cl.updateGroup(G)
                        except:
                            pass
                    else:
                        if op.param2 in Bots + Creator:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.sendText(op.param1,"Hai kak" + cl.getContact(op.param2).displayName + "\nJangn Tukar Nama Group (-_-) \nMaaf Aku kick Kamu")
                            except:
                                pass


        if op.type == 17:
            if wait["Sambutan"] == True:
                if op.param2 in Creator:
                    pass
                cl.sendMessage(to=op.param1, text=None, contentMetadata={'mid':op.param2}, contentType=13)
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).displayName
                cl.sendText(op.param1,"Jam  :" + datetime.today().strftime('%H:%M:%S') + "\nHallo kak \n" + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜ \nBudayakan Cek Note\nDan Semoga Betah di Sini . (p′︵‵。) 🤗 \nCreator>>" + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
                print("MEMBER JOIN TO GROUP")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg._from in mimic["target"] and mimic["status"] == True and mimic["target"][msg._from] == True: 
                text = msg.text
                if text is not None:
                    cl.sendText(msg.to,text)

            if msg.contentType == 16:
                if wait['likeOn'] == True:
                    url = msg.contentMetadata["postEndUrl"]
                    cl.like(url[25:58], url[66:], likeType=1005)
                    ki.like(url[25:58], url[66:], likeType=1002)
                    kk.like(url[25:58], url[66:], likeType=1004)
                    kc.like(url[25:58], url[66:], likeType=1003)
                    k1.like(url[25:58], url[66:], likeType=1001)
                    cl.comment(url[25:58], url[66:], wait["comment1"])
                    ki.comment(url[25:58], url[66:], wait["comment2"])
                    kk.comment(url[25:58], url[66:], wait["comment3"])
                    kc.comment(url[25:58], url[66:], wait["comment4"])
                    k1.comment(url[25:58], url[66:], wait["comment5"])
                    cl.sendText(msg.to,"Like Success")                     
                    wait['likeOn'] = False
            #if msg.contentType == 16:

                elif wait["Timeline"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"post URL\n" + msg.contentMetadata["postEndUrl"])


            if 'MENTION' in msg.contentMetadata.keys() != None:
                     print("[ 26 ] Tag respon")
                     if wait["detectMention"] == True:
                         contact = cl.getContact(msg._from)
                         cName = contact.displayName
                         balas = ["Woi kak \n " + "☞ " + cName + " ☜" + "Jgn ngtag ngetag Admin bot \nHp ngebleng semmm kak", "Woi kak\n" + "☞ " + cName + " ☜" + "Kakak kangen ya?\nPm aja kak\nIni rahsia prusahaan ya kak(-_-)", "Woi kak \n" + "☞ " + cName + " ☜" + "ADmin bot gi sibuk\nKalo kangen bilang kak\nkak serius naksir Admin bot ya?"]
                         ret_ = random.choice(balas)
                         image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                         name = re.findall(r'@(\w+)', msg.text)
                         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                         mentionees = mention['MENTIONEES']
                         for mention in mentionees:
                             if mention['M'] in Emid:
                                 cl.sendText(msg.to,ret_)
                                 cl.sendImageWithURL(msg.to,image)
                                 break
            if msg.contentType == 0:
                if wait["alwaysRead"] == True:
                    cl.sendChatChecked(msg._from,msg.id)
                if text is None:
                    pass
                if text.lower() == "me":
                    ginfo = ehun.getGroup(msg.to)
                    contact = ehun.getContact(msg._from)
                    name = contact.displayName
                    balas = ["Haik kak " + name + "\nIni cotact jlek mu"]
                    gin = random.choice(balas)
                    ehun.sendMessage(msg.to,gin)
                    ehun.sendContact(msg.to,msg._from)
                elif text.lower() == "mid":
                    ginfo = ehun.getGroup(msg.to)
                    contact = ehun.getContact(msg._from)
                    name = contact.displayName
                    balas = ["Haik kak" + name + "\nIni mid mu"]
                    gin = random.choice(balas)
                    ehun.sendMessage(msg.to,gin)
                    ehun.sendMessage(msg.to,msg._from)
                elif "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = ehun.findGroupByTicket(ticket_id)
                            ehun.acceptGroupInvitationByTicket(group.id,ticket_id)
                            ehun.sendMessage(msg.to, "Go b̶o̶tডা‮‮─┅═ই \n%s" % str(group.name))




        if op.type == 25:
            msg = op.message
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                cl.sendText(msg.to,"Bot Sudah On Kembali.")

        if op.type == 25:
          #if wait["Bot"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            try:
                #if sender != cl.profile.mid:
                    #to = sender
                if msg.contentType == 13:
                    if wait["wblacklist"] == True:
                        if msg.contentMetadata["mid"] not in admin:
                            if msg.contentMetadata["mid"] in wait["blacklist"]:
                                cl.sendText(msg.to,"Sudah")
                                wait["wblacklist"] = False
                            else:
                                wait["blacklist"][msg.contentMetadata["mid"]] = True
                                cl.sendText(msg.to,"Ditambahkan")
                        else:
                             cl.sendText(msg.to,"Admin Detected~")
                    elif wait["Contact"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                        else:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            aku = "Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu)
                            cl.sendMessage(aku)
                #if msg.contentType == 13:
                    elif wait['invite'] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendText(msg.to, _name + " Berada DiGrup Ini")
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.sendText(msg.to,"Invite " + _name)
                                    wait['invite'] = False
                                    break
                                except:
                                    cl.sendText(msg.to,"Limit Invite")
                                    wait['invite'] = False
                                    break

                if msg.contentType == 7:
                    if wait["sticker"] == True:
                        msg.contentType = 0
                        cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])



            except:
                pass
    except:
        pass

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops is not None:
           for op in ops:
                poll.setRevision(op.revision)
                clBot(op)
    except Exception as error:
        cl.log(error)
        traceback.print_tb(error.__traceback__)
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
        print("BYE")
atexit.register(atend)
