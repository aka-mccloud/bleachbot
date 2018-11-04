#!/usr/bin/python3

import re
import json
import requests
import random
import urllib
import urllib3

from lxml import html
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SERVER = 'S40'

cookies = None
loginKey = None
userData = None
gameSettings = None
serverInfo = None
serviceAccount = None
flashAccount = None
flashVars = None
swfUrl = None

def login():
	global cookies
	global loginKey

	url = "https://gnlogin.ru"
	payload = {
		'login': 'yivanov00@gmail.com',
		'password': 'lM0Qxec!',
		'captcha': '',
		'mid': 167782638,
		'browserhwid': '9733da0ae13896cc2e51efa625751930',
		'rp': '',
		'trustedLocation': 1,
		'code2fa': '',
		'json': 1,
		'2fa': 1
	}
	headers = {
		'Content-Type': "application/x-www-form-urlencoded",
		'Origin': "https://gamenet.ru",
		'Referer': "https://gamenet.ru/"
	}

	response = requests.post(url, data=payload, headers=headers, cookies=cookies)

	if response.ok:
		cookies = response.cookies
		response = json.loads(response.text)
		loginKey = response['key']


def getGameInfo():
	global cookies
	global userData
	global gameSettings

	url = "https://gamenet.ru/games/bleach/play"
	querystring = {
	   'k': loginKey
	}

	page = requests.get(url, params=querystring, cookies=cookies)

	tree = html.fromstring(page.content)
	scripts = tree.xpath('//script[@type="text/javascript"]/text()')
	script = next(s for s in scripts if 'userData' in s)
	script = script[script.find('{'):script.find('};')+1]
	script = re.sub(r'([\{\s,])(\w+)(:)', r'\1"\2"\3', script)
	script = script.replace("'", '"')
	userData = json.loads(script)

	script = next(s for s in scripts if 'gameSettings' in s)
	script = script[script.find('{'):script.find('},')+1]
	script = re.sub(r'([\{\s,])(\w+)(:)', r'\1"\2"\3', script)
	script = script.replace("'", '"')
	gameSettings = json.loads(script)


def getServerInfo():
	global cookies
	global userData
	global gameSettings
	global serverInfo

	url = "https://gnapi.com/"
	querystring = {
		'method': 'games.getServers',
		'format': 'json',
		'gameId': gameSettings['gameId'],
		'userId': userData['userId']
	}

	response = requests.get(url, params=querystring, cookies=cookies)

	serverInfo = json.loads(response.text)['response'][0]


def getServiceAccount():
	global cookies
	global userData
	global gameSettings
	global serverInfo
	global serviceAccount

	ts = int(datetime.now().timestamp())

	url = "https://gnapi.com/restapi"
	querystring = {
		'userId': userData['userId'],
		'appKey': userData['appKey'],
		'serviceId': gameSettings['serviceId'],
		'serverId': serverInfo['serverId'],
		'browserHwid': '',
		'format': 'json',
		'method': 'user.getServiceAccount',
		'_': ts
	}

	response = requests.get(url, params=querystring, cookies=cookies)

	serviceAccount = json.loads(response.text)['response']['serviceAccount']


def getFlashAccount():
	global cookies
	global userData
	global serviceAccount
	global flashAccount

	url = "https://sg.playxp.ru/platform/gamenet"
	querystring = {
		'game': 'shinigame',
		'userId': userData['userId'],
		'appKey': userData['appKey'],
		'token': serviceAccount['token'],
		'rnd': random.random(),
		'wmode': 'transparent'
	}

	page = requests.get(url, params=querystring, cookies=cookies)

	tree = html.fromstring(page.content)
	scripts = tree.xpath('//script/text()')
	serversUrl = next(s for s in scripts if 'window.g_config.serversUrl' in s)
	serversUrl = serversUrl[serversUrl.find('window.g_config.serversUrl'):]
	serversUrl = serversUrl[serversUrl.find('?')+1:]
	serversUrl = serversUrl[:serversUrl.find('"')]

	flashAccount = dict(urllib.parse.parse_qsl(serversUrl))


def getServerId(serverName):
	global cookies
	global flashAccount

	url = "https://sg.playxp.ru/platform/gamenet/serverlist"
	querystring = {
		'app': flashAccount['app'],
		'game': flashAccount['game'],
		'userId': flashAccount['userId'],
		'sign': flashAccount['sign']
	}

	page = requests.get(url, params=querystring, cookies=cookies)

	tree = html.fromstring(page.content)
	servers = tree.xpath('//div[@class="server-box server-list"]/ul/li/a/i')
	server = next(s for s in servers if serverName in s.tail)
	server = server.getparent()
	match = re.match(r'^javascript:play\((\d+)\);$', server.attrib['href'])

	return match[1]


def getFlashVars():
	global cookies
	global flashAccount
	global flashVars
	global swfUrl

	url = "https://sg.playxp.ru/platform/gamenet/play"
	querystring = {
		'app': flashAccount['app'],
		'game': flashAccount['game'],
		'userId': flashAccount['userId'],
		'sign': flashAccount['sign'],
		'serverId': getServerId(SERVER)
	}

	page = requests.get(url, params=querystring, cookies=cookies, verify=False)

	tree = html.fromstring(page.content)
	scripts = tree.xpath('//script[@type="text/javascript"]/text()')
	script = next(s for s in scripts if 'xiSwfUrlStr' in s)
	script = script[script.find('var xiSwfUrlStr ='):]
	script = script[script.find('"')+1:]
	swfUrl = script[:script.find('"')]
	swfUrl = swfUrl.replace('https://', 'http://')

	script = script[script.find('var flashvars='):]
	script = script[script.find('"')+1:]
	flashvars = script[:script.find('"')]
	
	flashVars = flashvars.replace('https%3A%2F%2F', 'http%3A%2F%2F')


login()
getGameInfo()
getServerInfo()
getServiceAccount()
getFlashAccount()
getFlashVars()

#print(json.dumps(dict(urllib.parse.parse_qsl(flashVars)), indent=2))

print(swfUrl + '?' + flashVars)

