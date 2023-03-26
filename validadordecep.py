import requests

cep = input('Informe o número do CEP: ')
url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    print ('CONSULTA DE CEP')

    print(f'CEP: {dados["cep"]}')
    print(f'Logradouro: {dados["logradouro"]}')
    print(f'Complemento: {dados["complemento"]}')
    print(f'Bairro: {dados["bairro"]}')
    print(f'Cidade: {dados["localidade"]}')
    print(f'Estado: {dados["uf"]}')
    print(f'IBGE: {dados["ibge"]}')
    print(f'DDD: {dados["ddd"]}')
    print(f'Siafi: {dados["siafi"]}')

else:

    print('CEP inválido.')
