#!/usr/bin/python3
# coding=utf-8 -*-
# coded by khamdihiXV

import requests, json, rich, re, platform, os, sys, time
from rich.console import Console
from rich.panel import Panel

def khamdihi(kuntul,memek):
    return Console(width=50).print(Panel(kuntul,style=memek),justify='center')

def panel(samsudin, kayajembut):
    return Console(width=50).print(Panel(samsudin),style=kayajembut)

def banner():
    khamdihi('''[bold white]╔═╗╦ ╦╔╗╔╔╦╗╦╦╔═  ╦╔═╗
╚═╗║ ║║║║ ║ ║╠╩╗  ║║ ╦
╚═╝╚═╝╝╚╝ ╩ ╩╩ ╩  ╩╚═╝
( di buat oleh [bold green]khamdihi [bold white]) ''','color(8)')

def Terminal():
    return os.system('cls') if platform.system() == 'win' else os.system('clear')

def jalan(e):
    for x in e:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.02)

def menu():
    Terminal() ; banner()
    panel('''[bold white][[bold yellow]1[bold white]] suntik followers ([bold green]indofoll[bold white])
[bold white][[bold yellow]2[bold white]] suntik followers ([bold green]qliz[bold white])
[bold white][[bold yellow]3[bold white]] suntik like instagram ([bold green]indofoll[bold white])
[bold white][[bold yellow]4[bold white]] suntik like instagram ([bold green]qliz[bold white])
[bold white][[bold yellow]0[bold white]] keluar pemrograman..''','color(8)')
    indonesia = input('   • masukan pilihan mu : ')
    if indonesia in ['1','01']:
       panel('[bold white]masukan data-data akun tumbal anda gunakan tanda | untuk pemisahan username dan password contoh data yang harus anda masukan : my username|my password','color(8)')
       data = input('   • masukan data akun : ')
       try:username,password = data.split('|')
       except:exit('\n   • data yang anda masukan salah contoh data yang benar : khamdihi_dev|masukan password akun')
       target = input('   • masukan username yang mau di follow : ')
       follow(username,password,target)

    elif indonesia in ['2','02']:
       panel('[bold white]masukan username target yang mau di follow contoh khamdihi_dev','color(8)')
       data = input('   • masukan target : ')
       follow_qliz(data)

    elif indonesia in ['3','03']:
       panel('[bold white]masukan data-data akun tumbal anda gunakan tanda | untuk pemisahan username dan password contoh khamdihi_dev|my password','color(8)')
       data = input('   • masukan data akun : ')
       try:username,password = data.split('|')
       except:exit('\n   • data yang anda masukan salah contoh username ig kamu|password kamu')
       panel('[bold white]masukan link postingan kamu contoh : https://www.instagram.com/p/Cg_bR6UhkNj/','color(8)')
       link = input('   • masukan link target : ')
       like(username, password, link)

    elif indonesia in ['4','04']:
       panel('[bold white]masukan link postingan kamu contoh : https://www.instagram.com/p/Cg_bR6UhkNj/','color(8)')
       date = input('   • masukan link target : ')
       like_qliz(date)
    elif indonesia in ['0','00']:exit()
    else:menu()

def follow(username,password,target):
    with requests.Session() as xyz:
        try:
             xyz.headers.update({
                 'Host': 'indofoll.com',
                 'content-length': '66',
                 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                 'x-csrf-token': 'rf58VwCYddLG41ycdUK81G55yeQBc9ZCyYk4Axua',
                 'sec-ch-ua-mobile': '?1',
                 'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'accept': '*/*',
                 'x-requested-with': 'XMLHttpRequest',
                 'origin': 'https://indofoll.com',
                 'sec-fetch-site': 'same-origin',
                 'sec-fetch-mode': 'cors',
                 'sec-fetch-dest': 'empty',
                 'referer': 'https://indofoll.com/tembak-followers',
             })
             data = {
                 'username':username,
                 'password':password,
                 'code':'',
                 'target':target
             }
             posz = xyz.post('https://indofoll.com/tembak-followers', data=data).text
             if 'Good!' in posz:panel('[bold green]penambahan followers sedang di proses, silakan cek akun anda...','color(8)')
             elif 'Kamu sudah claim followers untuk hari ini, kembali lagi besok' in posz:panel('[bold red]maaf, kamu sudah mengklaim followers hari ini, tapi tenang kamu bisa klaim lagi dengan akun tumbal yang lain♥','color(8)')
             elif "wait" in posz:panel('[bold yellow]tollong tunggu sebentar.. ','color(8)');folow(username, password, target)
             elif "Akun target tidak ditemukan!" in posz:panel('[bold red]akun yang mau kamu follow tidak di temukan :(','color(8)');exit(0)
             elif 'Kami mengirimkan anda kode (email atau SMS). Silahkan login lagi dengan memasukkan kode pada kolom yang tersedia untuk sukses login.' in posz:panel('[bold red]tumbal kamu terkena chekpoint di web ini :(','color(8)');exit(0)
             else:
                 panel(f'[bold green]response web tidak terbaca : {posz}','color(8)');exit(0)
        except Exception as asu:exit(str(asu))


def like(username,password,link):
    with requests.Session() as xyz:
         xyz.headers.update({
            'Host': 'indofoll.com',
            'content-length': '121',
            'x-csrf-token': 'rf58VwCYddLG41ycdUK81G55yeQBc9ZCyYk4Axua',
            'sec-ch-ua-mobile': '?1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://indofoll.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://indofoll.com/like-instagram-gratis'})
         data = {
           'username':username,
           'password':password,
           'code':'',
           'link':link
         }
         xzyx = xyz.post('https://indofoll.com/like-instagram-gratis', data=data).text
         if 'Good!' in xzyx:panel('[bold green]proses penambahan like kamu sedang di proses','color(8)')
         elif 'Kamu sudah claim likes untuk hari ini, kembali lagi besok!' in xzyx:panel('[bold red]Akun anda telah melakukan permintaan ini, ganti akun tumbal untuk melakukan permintaan','color(8)')
         else:panel(f'[bold red]response tidak terbaca : {xzyx}','color(8)')

def follow_qliz(username):
    with requests.Session() as xyz:
         try:
              link = xyz.get('https://instagram.qlizz.com/autofollowers').text
              toke = re.search('name="_token" value="(.*?)"',str(link)).group(1)
              xyz.headers.update({
                  'Host': 'instagram.qlizz.com',
                  'content-length': '84',
                  'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                  'accept': '*/*',
                  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'x-requested-with': 'XMLHttpRequest',
                  'sec-ch-ua-mobile': '?1',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                  'sec-ch-ua-platform': '"Android"',
                  'origin': 'https://instagram.qlizz.com',
                  'sec-fetch-site': 'same-origin',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-dest': 'empty',
                  'referer': 'https://instagram.qlizz.com/autofollowers'
              })
              data = {
                  '_token':toke,
                  'link':username,
                  'tool':'autofollowers'
              }
              posz = xyz.post('https://instagram.qlizz.com/send', data=data).text
              panel(f'[bold green]response qliz : {posz}','color(8)')
         except Exception as e:panel(f'[bold red]response error : [bold red]{e}','color(8)')

def like_qliz(sadiyah):
    with requests.Session() as xyz:
         try:
             link = xyz.get('https://instagram.qlizz.com/autoliker').text
             toke = re.search('name="_token" value="(.*?)"',str(link)).group(1)
             xyz.headers.update({
                 'Host': 'instagram.qlizz.com',
                 'content-length': '120',
                 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                 'accept': '*/*',
                 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'x-requested-with': 'XMLHttpRequest',
                 'sec-ch-ua-mobile': '?1',
                 'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                 'sec-ch-ua-platform': '"Android"',
                 'origin': 'https://instagram.qlizz.com',
                 'sec-fetch-site': 'same-origin',
                 'sec-fetch-mode': 'cors',
                 'sec-fetch-dest': 'empty',
                 'referer': 'https://instagram.qlizz.com/autoliker'
             })
             data = {
                 '_token':toke,
                 'link':sadiyah,
                 'tool':'autoliker'
             }
             posz = xyz.post('https://instagram.qlizz.com/send', data=data).text
             panel(f'[bold white]response qliz : [bold green]{posz}','color(8)')
         except Exception as e:panel(f'[bold white]response error : [bold red]{e}','color(8)')


if __name__ == '__main__':
   menu()

# MAU NGAPAIN OM?
