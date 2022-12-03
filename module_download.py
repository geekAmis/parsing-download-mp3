try:  from fake_headers import Headers;import requests;from bs4 import BeautifulSoup as bs;from webbrowser import open_new_tab as ontab;import random;import os;from tqdm import tqdm;main_url = 'https://ru.hitmotop.com';dopper = '/genre/44/start/0';path = 'music';page=2
except:  import os;os.system('pip install tqdm bs4 fake_headers requests html5lib');from fake_headers import Headers;import requests;import random;from bs4 import BeautifulSoup as bs;from webbrowser import open_new_tab as ontab;import os;from tqdm import tqdm;main_url = 'https://ru.hitmotop.com';dopper = '/genre/44/start/0';path = 'music';page=2
if not os.path.exists(path):  os.mkdir(path)
if os.path.exists('names.py'):  from names import Name as Nnn;NnN =Nnn
else:  NnN = ''
def get(url):
	headers = Headers().generate();print(headers);return requests.get(url,headers=headers)
def Soup(req):  return bs(req.text,'html5lib')
def writa(soup):
	with open('index.html','w',encoding='UTF-8') as file:  file.write(str(soup));ontab('index.html')
def all_dwndloads(soup):  return [i.get('href') for i in soup.find_all('a',class_='track__download-btn')]
def next_page(soup):
	try:  return [i.find('a') for i in soup.find_all('li',class_='pagination__item')][::-1][1:][0].get('href')
	except:  quit(f'All pages be downloadet\n\nYou was downloaded: {len(os.listdir(path))} Music\'s')
def remember(name):  
	with open('names.py','w',encoding='UTF-8') as pypy:  pypy.write(f'Name = "{name}"')
def download_list(mas,NnN):
	for music in tqdm(mas,ascii='Њ™›®І'):
		if not os.path.exists(path+'/'+music.split('/')[::-1][0]) or NnN == music.split('/')[::-1][0]:
			with open(path+'/'+music.split('/')[::-1][0],'wb') as mp3:
				remember(music.split('/')[::-1][0])
				try:
					mp3.write(get(music).content)
				except Exception as error:
					print(error);os.remove(path+'/'+music.split('/')[::-1][0])
				if NnN == music.split('/')[::-1][0]:  NnN = ''
	return NnN 
while True:
	try:
		soup = Soup(get(main_url+dopper));print('Get page: ',get(main_url+dopper).status_code)
		allse = all_dwndloads(soup);print(str(allse)+'\n\nGet all!')
		NnN = download_list(allse,NnN);print('Download Page');os.system(f'color 0{random.randint(1,7)}');print(f'Page: {page}')
		dopper = str(next_page(soup));print('Get next page!');page+=1
	except Exception as error:
		print('Error',error);#writa(soup)