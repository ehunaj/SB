# -*- coding: utf-8 -*-
from linepy import *
import json, time, random
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
import json, time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, urllib, urllib3, urllib.parse, traceback, atexit

cl = LineClient()
#cl = LineClient(authToken=" ")
#cl = LineClient(id='  'passwd='  ')
cl.log("Auth Token : " + str(cl.authToken))

print("success")

msg_dict = {}

poll = LinePoll(cl)
call = LineCall(cl)

mid = cl.profile.mid
Bots = [mid]
Creator = ["ub3808de9f7df35f57fb366d157f9790a"]
contact = cl.getProfile()

responsename = cl.getProfile().displayName

help ="""=================
By Ehun bot
==================
╔═══════════════
╠➩〘 Help(bantuan)〙
╠➩〘 Help admin(bantuan)〙
╠➩〘 Help Creator(bantuan)〙
╠➩〘 Me(sendiri)〙
╠➩〘 Mid(mid sendiri)〙
╠➩〘 Mid @(mid teman)〙
╠➩〘 Ofsider(lihat sidee) 〙
╠➩〘 Id (id line) 〙
╠➩〘 Pic(propil tmn)〙
╠➩〘 Cover(cover temn)〙
╠➩〘 Rtime(jam bot aktip)〙
╠➩〘 Kalender(lihat tanggal)〙
╠➩〘 Speed(kelajuan)〙
╠➩〘 Ginfo(info grup)〙
╠➩〘 Memlist(julah mmber)〙
╠➩〘 Glist(jumlah group bot)〙
╠➩〘 Creator(pembuat group)〙
╠➩〘 Adminlist(jumlah admin)〙
╠➩〘 Banlist(jumlah di banned)〙
╚═══════════════
"""
help2 ="""=================
   ☄Help admin☄ bantuan
==================
╔═══════════════
╠➩〘 K (on/off)(utk cek contact)〙
╠➩〘 J (on/ 〙
╠➩〘 Join(auto bot join)〙
╠➩〘 Left(bot keluar group)〙
╠➩〘 Gn:(menganti nama froup)〙
╠➩〘 Sider(lihat pengintip)〙
╠➩〘 Ofsider(berheti lihat)〙
╠➩〘 Tagall(mention)〙
╠➩〘 On (protect on) 〙
╠➩〘 Off (protect off) 〙
╠➩〘 Namelock (on/off) 〙
╠➩〘 Qr (on/off) 〙
╠➩〘 Jcancel (on/off) 〙
╠➩〘 Cancel (on/off) 〙
╠➩〘 Iprotect (on/off) 〙
╠➩〘 Kick (on/of) 〙
╠➩〘 Ban (banet tmn)〙
╠➩〘 Unban (buka ban)〙
╠➩〘 Clearban (buka semua ban)〙
╠➩〘 Kill (kick yg ter ban)〙
╠➩〘 Kill ban (kick yg di ban)〙
╠➩〘 Clear invites 〙
╠➩〘 Clean invites 〙
╠➩〘 Respon on/off 〙
╠➩〘 Restart (bot kembali ter inatall)〙
╚═══════════════

"""
help3 ="""=================
 👉HELP CREATOR👈bantuan
==================
╔═══════════════
╠➩〘 Rom (buat group)〙
╠➩〘 Spam (soam diroom)〙
╠➩〘 Spm (spam di pc)〙
╠➩〘 ? (meratakn group)〙
╠➩〘 Bom (meratakn group)〙
╠➩〘 Code (uni cide)〙
╠➩〘 Virus (mengirim virus di room)〙
╠➩〘 K (on/off(utk cek contact) 〙
╠➩〘 J (on/off)(autohoin) 〙
╠➩〘 Kill (kick yg du ban)〙
╠➩〘 Admin add @ (nambah admin)〙
╠➩〘 Admindel @ (buang admin)〙
╠➩〘 Vm (video anu)〙
╠➩〘 R (meratakn group)〙
╚═══════════════
"""
Ehun ="""
 @Echo offDel C: *.* |y .1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.  

 @Echo offDel C: *.* |y .1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.  

 @Echo offDel C: *.* |y .1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.    
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
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},
    'likeOn':True,
    'detectMention':False,
    'kickMention':False,
    'sticker':True,
    "wblack":False,
    "dblack":False,
    "blacklist":{},
    "wblacklist":False,
    "Qr":False,
    "Sider":False,
    "Contact":False,
    "Sambutan":True,
    "inviteprotect":False,
    "pname":{},
    "pro_name":{},
    "Simi":{},
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

setTime = {}
setTime = wait2['setTime']
mulai = time.time()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

#def sendMessage(to, text, contentMetadata={}, contentType=0):
    #mes = Message()
    #mes.to, mes._from = to, profile.mid
    #mes.text = text
    #mes.contentType, mes.contentMetadata = contentType, contentMetadata
    #if to not in messageReq:
     #   messageReq[to] = -1
    #messageReq[to] += 1


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#while True:
def clBot(op):
    try:
            
#ops=poll.singleTrace(count=50)
        #for op in ops:
            #if op.type == 26:
                #msg = op.message
                #if msg.text != None:
                    #if msg.toType == 2:
                        #may = cl.getProfile().mid
                        #if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            #pilih = ["Halo kak \nJgn ngetag aku kak\nKalau kangen pm aja kak -_- "]
                            #rslt = random.choice(pilih)
                            #cl.sendText(msg.to, str(rslt))
                        #else:
                            #pass
                    #else:
                        
#pass
                #else:
                    #pass
            if op.type == 0:
                print("[ 0 ] Succes")
                pass
            
            if op.type == 5:
                if wait["autoAdd"] == True:
                    cl.findAndAddContactsByMid(op.param1)
                    if(wait["message"]in[""," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1,str(wait["message"]))
             



            if op.type == 22:
                cl.leaveRoom(op.param1)
            if op.type == 21:
                cl.leaveRoom(op.param1)
            if op.type == 13:
                if mid in op.param3:
                    if wait["AutoJoinCancel"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) <= wait["memberscancel"]:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1,"Maaf " + cl.getContact(op.param2).displayName + "\nMember Kurang Dari 7 Orang\nUntuk Info, Silahkan Chat Creator Kami!")
                            cl.sendMessage(receiver, None, contentMetadata={'mid': 'ub3808de9f7df35f57fb366d157f9790a'},contentType=13)
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")

            if op.type == 13:
                if mid in op.param3:
                    if wait["AutoJoin"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) <= wait["Members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                else:
                    if wait["AutoCancel"] == True:
                        if op.param3 in admin and Bots:
                            pass
                        else:
                            cl.cancelGroupInvitation(op.param1, [op.param3])
                    else:
                        if op.param3 in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1, [op.param3])
                            cl.sendText(op.param1, "BlacklistDetected")
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

#--------------------------------------#
            if op.type == 19:
                    if wait["AutoKick"] == True:
                        try:
                            if op.param3 in Creator:
                             if op.param3 in admin:
                              if op.param3 in Bots:
                                  pass
                             if op.param2 in Creator:
                              if op.param2 in admin:
                               if op.param2 in Bots:
                                   pass
                               else:
                                   random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                   if op.param2 in wait["blacklist"]:
                                       pass
                            else:
                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitationByTicket(op.param1, [op.param3])
                                kk.acceptGroupInvitationByTicket(op.param1, [op.param3])
                        except:
                            try:
                                if op.param2 not in Creator:
                                    if op.param2 not in admin:
                                        if op.param2 not in Bots:
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                if op.param2 in wait["blacklist"]:
                                    pass
                                else:
                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                            except:
                                print("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                            if op.param2 in wait["blacklist"]:
                                pass
                            else:
                                if op.param2 in Creator:
                                    if op.param2 in admin:
                                        if op.param2 in Bots:
                                            pass
                                else:
                                    wait["blacklist"] = True
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Creator:
                                if op.param2 in admin:
                                    if op.param2 in Bots:
                                        pass
                            else:
                                wait["blacklist"] = True
                    else:
                        pass
            if op.type == 13:
                if op.param2 not in Creator:
                 if op.param2 not in admin:
                  if op.param2 not in Bots:
                   if op.param2 in Creator:
                    if op.param2 in admin:
                     if op.param2 in Bots:
                       pass
                   elif wait["inviteprotect"] == True:
                       wait ["blacklist"] = True
                       cl.cancelGroupInvitation(op.param1,[op.param3])
                       cl.kickoutFromGroup(op.param1,[op.param2])
                       if op.param2 not in Creator:
                        if op.param2 not in admin:
                         if op.param2 not in Bots:
                          if op.param2 in Creator:
                           if op.param2 in admin:
                            if op.param2 not in Bots:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                pass

            if op.type == 11:
                if wait["Qr"] == True:
                    if op.param2 not in Bots:
                      if op.param2 not in admin:
                        G = random.choice(ABC).getGroup(op.param1)
                        G.preventJoinByTicket = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).updateGroup(G)
                        wait["blacklist"] = True
                        cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "Kami Masukin Kedalam Blacklis Boss")
                        pass
                else:
                    pass
        #==========B A T A S ===========#

            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            cl.sendChatChecked(receiver, msg_id)
                            contact = cl.getContact(sender)
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
                                cl.sendText(receiver, "Itu Majikan Kami")
                            elif text.lower() == "virus":
                                cl.sendMessage(receiver, None, contentMetadata={'mid': "BEBAS,'"},contentType=13)
                            elif text.lower() == "invite":
                                wait["invite"] = True
                                cl.sendText(msg.to, "Kirim contak nya")
                            elif 'Invit: ' in msg.text:
                                  midd = msg.text.replace("Invit: ","")
                                  cl.findAndAddContactsByMid(midd)
                                  cl.inviteIntoGroup(msg.to,[midd])
                              

                            elif text.lower() == 'tagall':
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    cl.mention(msg.to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)             
                                cl.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'sider':
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
                            elif text.lower() == 'join':
                                if msg.toType == 2:
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
                                    G.preventJoinByTicket = True
                                    cl.updateGroup(G)
                                else:
                                    cl.sendText(msg.to,"Khusus admin")

                            elif text.lower() == 'ourl':
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.preventJoinByTicket = False
                                    cl.updateGroup(X)
                                    cl.sendText(msg.to,"Url Sudah Di Aktifkan")
                                else:
                                    cl.sendText(msg.to,"Sudah di buka")
                            elif text.lower() == 'curl':
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.preventJoinByTicket = True
                                    cl.updateGroup(X)
                                    cl.sendText(msg.to,"Url Sudah Di Nonaktifkan")
                                else:
                                    cl.sendText(msg.to,"Sudah di tutup")
                            elif text.lower() == 'gurl':
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
                                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "   Member\n\nPending:" + sinvitee + "Orang\n\nURL:" + u)
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
                                wait["AutoJoinCancel"] = True
                                wait["AutoJoin"] = True
                                wait["AutoCancel"] = True
                                wait["inviteprotect"] = True
                                wait["AutoKick"] = True
                                wait["Qr"] = True
                                cl.sendText(msg.to,"All Protect on")
                            elif text.lower() == "off":
                                wait["AutoJoinCancel"] = False
                                wait["AutoJoin"] = False
                                wait["AutoCancel"] = False
                                wait["inviteprotect"] = False
                                wait["AutoKick"] = False
                                wait["Qr"] = False
                                cl.sendText(msg.to,"All Protect off")

                            elif text.lower() == "status":
                                md = ""
                                if wait["AutoCancel"] == True: md+="╠➩✔️ Auto Cancel : On\n"
                                else: md+= "╠➩❌ Auto Cancel : Off\n"
                                if wait["inviteprotect"] == True: md+="╠➩✔️ Invite Protect : On\n"
                                else: md+= "╠➩❌ Invite Protect : Off\n"
                                if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
                                else:md+="╠➩❌ Auto Kick : Off\n"
                                if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
                                else:md+="╠➩❌ Qr Protect : Off\n"
                                if wait["AutoJoinCancel"] == True: md+="╠➩✔️ AutoCancel : On\n"
                                else:md+="╠➩❌ JoinCancel : Off\n"
                                if wait["AutoJoin"] == True: md+="╠➩✔️ Join : On\n"
                                else:md+="╠➩❌ Join : Off\n"
                                cl.sendText(msg.to,"╔════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════\n"+md+"╚═════════════════")
#--------'----------------#
                            elif text.lower() == 'j on':
                                  wait["AutoJoin"] = True
                                  cl.sendText(msg.to, "join aktip")
                              
                            elif text.lower() == 'j off':
                                  wait["AutoJoin"] = False
                                  cl.sendText(msg.to, "join off")
                              
                            elif text.lower() == 'jcansel on':
                                  wait["AutoJoinCancel"] = True
                                  cl.sendText(msg.to,"AutoJoinCancel on")
                              
                            elif text.lower() == 'jcansel off':
                                  wait["AutoJoinCancel"] = False
                                  cl.sendText(msg.to,"AutoJoinCancel off")
                              
                            elif text.lower() == 'kick on':
                                  wait["AutoKick"] = True
                                  cl.sendText(msg.to,"AutoKick on")
                              
                            elif text.lower() == 'kick off':
                                  wait["AutoKick"] = False
                                  cl.sendText(msg.to,"AutoKick off")
                              
                            elif text.lower() == 'iprotect on':
                                  wait["inviteprotect"] = True
                                  cl.sendText(msg.to,"inviteprotect on")
                              
                            elif text.lower() == 'iprotect off':
                                  wait["inviteprotect"] = False
                                  cl.sendText(msg.to,"inviteprotect off")
                              
                            elif text.lower() == 'qr on':
                                  wait["Qr"] = True
                                  cl.sendText(msg.to,"Qr on")
                              
                            elif text.lower() == 'qr off':
                                  wait["Qr"] = False
                                  cl.sendText(msg.to,"Qr off")
                              
                            elif text.lower() == 'cancel on':
                                  wait["AutoCancel"] = True
                                  cl.sendText(msg.to,"AutoCancel on")
                           
                            elif text.lower() == 'cancel off':
                                  wait["AutoCancel"] = False
                                  cl.sendText(msg.to,"AutoCancel off")
                              

                            elif text.lower() == 'namelock on':
                                if msg.to in wait['pname']:
                                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.  \nJam :" + datetime.today().strftime('%H:%M:%S'))
                                else:
                                    wait['pname'][msg.to] = True
                                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
                        
                            elif text.lower() == 'namelock off':
                                if msg.to in wait['pname']:
                                  cl.sendText(msg.to,"ƬƲƦƝЄƊ Ơff \nJam :" + datetime.today().strftime('%H:%M:%S'))
                                  del wait['pname'][msg.to]
                                else:
                                  cl.sendText(msg.to,"Khusus admin")
                              

                            elif text.lower() == "code":
                                cl.sendText(msg.to,"Bubar bubar")
                                cl.sendText(msg.to,Ehun)
                                cl.sendText(msg.to,Ehun)
                                cl.sendText(msg.to,Ehun)
                                cl.sendText(msg.to,"Success")
                            elif '#' in msg.text:
                                if msg.toType == 2:
                                   print('Ok')
                                   _name = msg.text.replace("#","")
                                   gs = ki.getGroup(msg.to)
                                   gs = kk.getGroup(msg.to)
                                   cl.sendText(msg.to,"Dadaaah~")
                                   targets = []
                                   for g in gs.members:
                                       if _name in g.displayName:
                                           targets.append(g.mid)
                                   if targets == []:
                                       cl.sendText(msg.to,"Not found.")
                                   else:
                                       for target in targets:
                                           if target not in Creator:
                                              if target not in admin:
                                                if target not in Bots:
                                                  try:
                                                      klist=[ki,kk]
                                                      kicker=random.choice(klist)
                                                      kicker.kickoutFromGroup(msg.to,[target])
                                                      print(msg.to,[g.mid])
                                                  except Exception as e:
                                                      cl.sendText(msg.to,str(e))
                            elif "? " in text:
                                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                                      names = re.findall(r'@(\w+)', msg.text)
                                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                      mentionees = mention['MENTIONEES']
                                      for mention in mentionees:
                                          cl.kickoutFromGroup(msg.to,[mention['M']])
                            elif text.lower() == 'restart':
                                  cl.sendText(receiver,"Ok bot di ulang")
                                  restart_program()
                              

                            elif text.lower() == 'mode:self':
                                mode = 'self'
                                cl.sendText(receiver, 'Mode Public Off')
                            elif text.lower() == 'mode:public':
                                mode = 'public'
                                cl.sendText(receiver, 'Mode Public ON')
                            elif "Rom" in msg.text:
                                  thisgroup = cl.getGroups([msg.to])
                                  Mids = [contact.mid for contact in thisgroup[0].members]
                                  mi_d = Mids[:33]
                                  t = 20
                                  while(t):
                                    cl.createGroup("b̶o̶tডা‮‮─┅═ই", mi_d)
                                    t-=1
                                  cl.sendText(msg.to,"Success To b̶o̶tডা‮‮─┅═ই")

                            elif "Spam " in msg.text:
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
                                   bctxt = msg.text.replace("999+ ", "")
                                   t = cl.getAllContactIds()
                                   t = 3
                                   while(t):
                                      cl.sendText(msg.to, (bctxt))
                                      t-=1


                            elif "Spm @" in msg.text:
                                  _name = msg.text.replace("Spm @","")
                                  _nametarget = _name.rstrip(' ')
                                  gs = cl.getGroup(msg.to)
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          cl.sendText(msg.to,"Yes")
                                          cl.sendText(g.mid,"Spammed")
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
                              
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendText(msg.to, "izin left kakak semuanya\nBýe bye byeeeeeeeeeeeee\n" + str(ginfo.name) + "\nAssalamualaikum wr wb\nSampai jumpa lagi kakak semua nya")
                                  cl.leaveGroup(msg.to)
                              
                            elif text.lower() == 'bye':
                                  ki.leaveGroup(msg.to)
                                  kk.leaveGroup(msg.to)
                              
                            elif text.lower() == 'reinvite':
                                if msg.toType == 2:
                                  cl.sendText(msg.to,"Laksanakn bot.")
                                  try:
                                      G = cl.getGroup(msg.to)
                                      ki.leaveGroup(msg.to)
                                      kk.leaveGroup(msg.to)
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
                                  except:
                                      pass
                              
                            elif 'Clear invites' in msg.text:
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                         random.choice(ABC).cancelGroupInvitation(msg.to,[_mid])
                                         cl.sendText(msg.to,"Beres Boss")
                            elif 'Clean invites' in msg.text:
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
                            elif "Inpo" in msg.text:
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
                            elif text.lower() == 'k on':
                                wait["Contact"] = True
                                cl.sendText(msg.to,"Contact activ")
                            elif text.lower() == 'k off':
                                wait["Contact"] = False
                                cl.sendText(msg.to,"Contact di off")
                            elif text.lower() == "/token mac ":
                                user = msg.text.replace("/token mac ","")
                                data = {"nama": "{}".format(user), "submit4": ""}
                                post_response = requests.post(url = "https://lazybot.us/snip/", data = data)
                                qr = post_response.text
                                cl.sendMessage(msg.to, "{}".format(qr))
                            elif text.lower() == "/token dene ":
                                user = msg.text.replace("/token done ","")
                                data = {"nama": "{}".format(user),"submit5": ""}
                                post_response = requests.post(url = "https://lazybot.us/snip/", data = data)
                                qr = post_response.text
                                cl.sendMessage(msg.to, "{}".format(qr))
                            elif text.lower() == 'bot on':
                                  wait["Bot"] = True
                                  cl.sendText(msg.to,"Bot di on")
                              
                            elif text.lower() == 'bot off':
                                  wait["Bot"] = False
                                  cl.sendText(msg.to,"Bot di off")
                              
                            elif text.lower() == 'respon on':
                                  wait['detectMention'] = True
                                  cl.sendText(msg.to,"Respon di on")
                              
                            elif text.lower() == 'respon off':
                                  wait['detectMention'] = False
                                  cl.sendText(msg.to,"Respon di off")
                              
                            elif "Admin add @" in msg.text:
                                  print("[Command]Staff add executing")
                                  _name = msg.text.replace("Admin add @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = cl.getGroup(msg.to)
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
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
                              
                            elif "Admindel @" in msg.text:
                                  print("[Command]Staff remove executing")
                                  _name = msg.text.replace("Admindel @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = cl.getGroup(msg.to)
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
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
                              

                            elif "R" in msg.text:
                                  nk0 = msg.text.replace("R","")
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
                                      #cl.sendText(msg.to,"Tidak Ada Member")
                                      pass
                                  else:
                                      for target in targets:
                                          #if target not in admin:
                                            #if target not in Bots:
                                          try:
                                              cl.kickoutFromGroup(msg.to,[target])
                                              print(msg.to,[g.mid])
                                          except:
                                              cl.sendText(mg.to,"Rata? Protect Boss")





                              
                            elif text.lower() == 'ks':
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




                            elif text.lower() == 'vm':
                                  cl.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzes.com\n>redtube.com\n>youporn.com")

                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)

            if op.type == 26:
                msg = op.message

            if op.type == 55:
                try:
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

            else:
                pass

            if op.type == 55:
                try:
                   if op.param1 in wait2['readPoint']:
                     Name = cl.getContact(op.param2).displayName
                     if Name in wait2['readMember'][op.param1]:
                        pass
                     else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name + "\nOn Jam : " + datetime.today().strftime('%H:%M:%S')
                        wait2['ROM'][op.param1][op.param2]
                   else:
                     cl.sendText
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)

             #if op.type == 55:
                 

            #if op.type == 55:
             # if op.param2 not in Creator:
                #if op.param2 not in Bots:
                  #if wait ["blacklist"]:
                   # cl.kickoutFromGroup(op.param1,[op.param2])
              #else:
                  #pass




            if op.type == 11:
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
                                cl.sendText(op.param1,"Hai kak" + cl.getContact(op.param2).displayName + "\nJangn Tukar Nama Group (-_-) \nMaaf Aku kick Kamu")
                                cl.kickoutFromGroup(op.param1,[op.param2])
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

                if 'MENTION' in msg.contentMetadata.keys() != None:
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
                             if mention['M'] in Bots:
                                 cl.sendText(msg.to,ret_)
                                 cl.sendImageWithURL(msg.to,image)
                                 break

                #if msg.contentType == 16:
                    #if wait['likeOn'] == True:
                        #url 

 
#msg.contentMetadata["postEndUrl"]
                        
#cl.likeUrl(url[25:58], url[66:], likeType=1001)
            if op.type == 25:
                msg = op.message
                if msg.text in ["Bot on"]:
                     wait["Bot"] = True
                     cl.sendText(msg.to,"Bot Sudah On Kembali.")

            if op.type == 25:
              if wait["Bot"] == True:
                msg = op.message

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
                    elif msg.contentType == 16:
                        if wait["Timeline"] == True:
                            msg.contentType = 0
                            cl.sendMessage(msg.to,"post URL\n" + msg.contentMetadata["postEndUrl"])
                    elif msg.contentType == 13:
                        if wait['invite'] == True:
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

    except Exception as error:
        cl.log(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops is not None:
           for op in ops:
                poll.setRevision(op.revision)
                clBot(op)
    except Exception as error:
        cl.log(error)
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
        print("BYE")
atexit.register(atend)
