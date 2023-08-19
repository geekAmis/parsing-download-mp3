page_url = 'https://wow4.supermusic.me{}/page/{}/'
jenres = '/rock_pesni,/klubnyak,/popsa,/rap_2023,/muzyka_dlya_relaksatsii'.split(',')
from bs4 import BeautifulSoup as bs 
import requests
from fake_headers import Headers 
import os

print('Выбери твой жанр. :\n-------------\n'+'\n'.join([f'{jenres.index(i)}. {i}' for i in jenres])+'\n-------------')
while True:
	try:
		jenre = int(input('Цифра: '))
		break
	except:
		print('Введите цифру, а нечисло или спец. символы')



if not os.path.exists('a'):
	os.mkdir('a')

def loadPage(page):
	return  bs(requests.get(page_url.format(jenres[jenre],page),headers=Headers().generate()).text,'html5lib')


for count_apge in range(1,20):
	page = loadPage(count_apge)

	with open('a.html','w',encoding='UTF-8') as file:
		file.write(str(page))

	for i in page.find_all('div',class_='music-popular-wrapper'):
		soung = i.find('a',class_='popular-play__item').get('data-url')
		name = soung.split('/')[-1]
		with open(f'a/{name}','wb') as song_file:
			song_file.write(requests.get(soung,headers=Headers().generate()).content)

