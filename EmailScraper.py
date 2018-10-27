import urllib
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time
import re

linkRegex=re.compile(r'''
[a-zA-Z0-9_.+]+ #name part
\.com/ #domain
[:/a-zA-Z0-9_.+]+
#####following
''', re.VERBOSE)

url=[
#insert urls here seperated by commas
]

compoundfinal=''

for i in url:
    try:
        page=urllib.request.urlopen(i)
        text=BeautifulSoup(page,'html.parser')
        extractedLink=linkRegex.findall(text.text)
        extractedLink=list(set(extractedLink))
        nodelessLink1=[n for n in extractedLink if '.js' not in n]
        nodelessLink2=[n for n in nodelessLink1 if 'node.' not in n]
        nodelessLink3=[n for n in nodelessLink2 if 'dev.' not in n]
        nodelessLink4=[n for n in nodelessLink2 if 'admin' not in n]
        finalLink=[n for n in nodelessLink4 if '.com' in n]
        extractedLinkS= ";".join(finalLink)
        final=i+';'+extractedLinkS+'\n'
        compoundfinal=compoundfinal+final
    except:
        compoundfinal=compoundfinal+i+';N/A\n'
        pass

print('url;'+'Link'+'\n'+compoundfinal)
