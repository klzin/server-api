import requests
import json
import random
from colorama import Fore
from flask import jsonify


def login():

    req = requests.session()
    
    cookies = {
    'JSESSIONID': '865a8aa5ff40e6c9d435d7cd009b',
}

    headers = {
        'Host': 'portal.sisp.es.gov.br',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://portal.sisp.es.gov.br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'https://portal.sisp.es.gov.br/xhtml/pesquisa.jsf',
    }

    data = {
        'j_username': '08456633720',
        'j_password': 'pcdp1979',
        'j_idt19': 'j_idt19',
        'j_idt19:j_idt20.x': '171',
        'j_idt19:j_idt20.y': '18',
        'javax.faces.ViewState': '-5003044710522587294:5398876124454036473',
    }

    response = req.post('https://portal.sisp.es.gov.br/xhtml/j_security_check', cookies=cookies, headers=headers, data=data, allow_redirects=False, verify=False)

    cookies = response.cookies
    
    for cookie in cookies:
        print(f'Nome do Cookie: {cookie.name}')
        print(f'Valor do Cookie: {cookie.value}')

    cookies = {'JSESSIONID': f'{cookie.value}',}

    headers = {
    'Host': 'portal.sisp.es.gov.br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
    'Origin': 'https://portal.sisp.es.gov.br',
    'Referer': 'https://portal.sisp.es.gov.br/sispes-frontend/xhtml/pesquisa.jsf',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

    data = 'javax.faces.partial.ajax=true&javax.faces.source=pesquisaform%3AtblPessoas%3A0%3Aimgs&javax.faces.partial.execute=%40all&javax.faces.partial.render=pesquisaform%3AdlgImagens&pesquisaform%3AtblPessoas%3A0%3Aimgs=pesquisaform%3AtblPessoas%3A0%3Aimgs&pesquisaform=pesquisaform&pesquisaform%3AtxtNm=&pesquisaform%3AtxtNmmae=&pesquisaform%3AtxtNmpai=&pesquisaform%3AtxtCpf=120.806.317-05&pesquisaform%3AtxtRg=&pesquisaform%3AtxtAp=&pesquisaform%3AtxtIdaini=&pesquisaform%3AtxtIdafin=&pesquisaform%3AselSexo_input=&pesquisaform%3AselSexo_focus=&pesquisaform%3AtxtProf=&pesquisaform%3AaccParametrosOpcionais%3AmnuTipoFiltro_input=C&pesquisaform%3AaccParametrosOpcionais%3AmnuTipoFiltro_focus=&pesquisaform%3AaccParametrosOpcionais%3AcbxVinculoImagem_input=on&pesquisaform%3AaccParametrosOpcionais%3AselCutis_input=&pesquisaform%3AaccParametrosOpcionais%3AselCutis_focus=&pesquisaform%3AaccParametrosOpcionais%3AselTpecul_input=&pesquisaform%3AaccParametrosOpcionais%3AselTpecul_focus=&pesquisaform%3AaccParametrosOpcionais%3AselPcorpo_input=&pesquisaform%3AaccParametrosOpcionais%3AselPcorpo_focus=&pesquisaform%3AaccParametrosOpcionais%3AtxtDesc=&pesquisaform%3AaccParametrosOpcionais_active=0&pesquisaform%3AtblPessoas_selection=3873364&pesquisaform%3ApnlSiarhes_active=0&javax.faces.ViewState=-8316733986558793550%3A4578716167394684902'

    response = requests.post('https://portal.sisp.es.gov.br/sispes-frontend/xhtml/pesquisa.jsf', cookies=cookies, headers=headers, data=data, allow_redirects=True, verify=False).text

    print(response)

    if 'sispes-frontend/image?param=1031584' in response:
        print("Deu bom")


login()