import json
import requests
import os

HOSTSPATH = 'C:\Windows\System32\drivers\etc\hosts'
urls = open("urls.txt", "r")
hosts = open(HOSTSPATH, "w+")
hostsDict = {}

for line in hosts.readlines():
    item = line.split(' ')
    if len(item) == 2:
        hostsDict[item[1].strip('\n')] = item[0]
        print("加入字典:"+item[1].strip('\n')+" = "+item[0])
    else:
        print("清除:"+line)

for url in urls.readlines():
    url = url.strip('\n')
    apiUrl = 'https://myssl.com/api/v1/tools/dns_query?qtype=1&host='+url+'&qmode=-1'
    page = requests.get(apiUrl)
    jsonStr = json.loads(page.text)
    hostsDict[url] = jsonStr['data']['86'][0]['answer']['records'][0]['value']
    print(jsonStr['data']['86'][0]['answer']['records'][0]['value']+" "+url)

for item in hostsDict:
    print(item)
    hosts.write(hostsDict[item]+" "+item+"\n")
urls.close()
hosts.close()
os.system('ipconfig /flushdns')
os.system('pause')