import requests

url = 'https://github.com/PowerShell/PowerShell/releases/download/v7.5.0/PowerShell-7.5.0-win-x64.msi'
arquivo = 'PowerShell-7.5.0-win-x64.msi'

try:
    resposta =  requests.get(url, stream=True)
    resposta.raise_for_status()

    with open(arquivo, 'wb') as file:
        for chunk in resposta.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f'Arquivo {arquivo} baixado com sucesso!')

except requests.exceptions.RequestException as e:
    print(f'Erro ao baixar o arquivo: {e}')
except IOError as e:
    print(f'Erro ao salvar o arquivo: {e}')