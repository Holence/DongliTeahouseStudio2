import requests
import urllib #淦！最新版的urllib3不支持代理。pip install urllib3==1.25.11就行了
from lxml import etree

def GetWebPageResponse(url,cookie="") -> requests.Response:
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response
	else:
		return None

def GetWebPageHTML(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response.text
	else:
		return None

def GetWebPageHeaders(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response.headers
	else:
		return None

def GetWebPageType(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response["Content-Type"]
	else:
		return None

def GetWebPageTitle(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		html=response.text
		try:
			tree=etree.HTML(html)
			title=tree.xpath(".//title/text()")[0]
			title=urllib.parse.unquote(title,'utf-8')
			return str(title)
		except:
			return None
	else:
		return None


def GetWebFavIcon(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		try:
			html=response.text
			tree=etree.HTML(html)
			icon_url=tree.xpath("//*[@rel='icon']/@href | //*[@rel='shortcut icon']/@href")[-1]
			if "http" not in icon_url:
				icon_url=urllib.parse.urljoin(url,icon_url)
			res=GetWebPageResponse(icon_url)
			if res!=None:
				return res.content
			else:
				return None
		except:
			return None
	else:
		return None

def GetWebPagePic(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	
	if response.ok:
		return response.content
	else:
		return None