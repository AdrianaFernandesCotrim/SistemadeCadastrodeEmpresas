import requests as biblioteca
import json

def consulta_cnpj(cnpj):
    def consulta_cnpj(cnpj):
        url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
        querystring = {'token':'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX','cnpj':'06990590000123','plugin':'RF'}
        response = requests.request('GET', url, params=querystring)

        resp = json.loads(response.text)
        listaChaves = ['nome', 'logradouro','numero','complemento','bairro','municipio','uf','cep','telefone','email']
        listaValores = []
        for chave in listaChaves:
            listaValores.append(resp[chave])
        return listaValores
    print(consulta_cnpj('06990590000123'))
