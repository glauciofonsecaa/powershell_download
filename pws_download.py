import requests
from bs4 import BeautifulSoup as bs
from urllib3 import disable_warnings

disable_warnings()

url = 'https://github.com/PowerShell/PowerShell/releases/tag/v7.5.0'
target_filename = 'PowerShell-7.5.0-win-x64.exe'
agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

try:

    requisicao = requests.get(url, headers=agent, verify=False, stream=True)
    requisicao.raise_for_status()

    site = bs(requisicao.text, 'html.parser')

    for link in site.find_all('a'):
        print(link)

except requests.exceptions.RequestException as e:
    print(f'Error during request: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
    
    


  