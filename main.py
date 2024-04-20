import logging
from flask import Flask
from endpoints.cpf import consulta_cpf
from endpoints.cpf_email import consulta_email_cpf
from endpoints.email import consulta_email
from endpoints.reco_facial import reconhecimento
from endpoints.telefone import telefone_consulta
from endpoints.poder_social import consulta_podersocial
from endpoints.cpf_basico import cpf_dados_basico
from endpoints.politica import dados_urna_eletronixa
from endpoints.renda import cpf_renda
from endpoints.cpf_medico import consultar_medico
from endpoints.conf.dump import dados_base_dump
from endpoints.cpf2 import consulta_cpf_2
from src.cnh import consulta_cpf_cnh
from src.cnh2 import consulta_cpf_cnh_reds
from admin.gerar_user import gerar_aceso
#======================================
#from foto.app import cpf_uf
#======================================
app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def endpoint_cpf(valor, token):
    return consulta_cpf(valor, token)
    
def endpoint_email(valor, token):
    return consulta_email(valor, token)

def endpoint_email_cpf(valor, token):
    return consulta_email_cpf(valor, token)

def consultar_medico_cpf(valor, token):
    return consultar_medico(valor, token)

def endpoint_telefone(valor, token):
    return telefone_consulta(valor, token)

def endpoint_cnh(valor, token):
    return consulta_cpf_cnh(valor, token)

def endpoint_cnh2(valor, token):
    return consulta_cpf_cnh_reds(valor, token)

def endpoint_poder_social(valor, token):
    return consulta_podersocial(valor, token)

def endpoint_cpf_basico(valor, token):
    return cpf_dados_basico(valor, token)

def endpoint_cpf_renda(valor, token):
    return cpf_renda(valor, token)

def dados_eleicao(valor, token):
    return dados_urna_eletronixa(valor, token)

def getids(valor):
    return dados_base_dump(valor)

def gerartoken(token,dia,mes,ano):
    return gerar_aceso(token,dia,mes,ano)

def consulta_cpf_22(valor,token):
    return consulta_cpf_2(valor,token)

def reco_face(token):
    return reconhecimento(token)

'''def cpf_uf_rota(valor, token):
    return cpf_uf(valor, token)'''


# Define as rotas para cada endpoint separadamente
app.route('/token/<token>/cpf/<valor>')(endpoint_cpf)
app.route('/token/<token>/email/<valor>')(endpoint_email)
app.route('/token/<token>/email_cpf/<valor>')(endpoint_email_cpf)
app.route('/token/<token>/telefone/<valor>')(endpoint_telefone)
app.route('/token/<token>/cnh/<valor>')(endpoint_cnh)
app.route('/token/<token>/cnh_modulo2/<valor>')(endpoint_cnh2)
app.route('/token/<token>/poder_social/<valor>')(endpoint_poder_social)
app.route('/token/<token>/basiccpf/<valor>')(endpoint_cpf_basico)
app.route('/token/<token>/medico_cpf/<valor>')(consultar_medico_cpf)
app.route('/token/<token>/eleicao/<valor>')(dados_eleicao)
app.route('/token/<token>/renda/<valor>')(endpoint_cpf_renda)
app.route('/token/<token>/cpf2/<valor>') (consulta_cpf_22)
#======================================
#app.route('/token/<token>/foto/<valor>') (cpf_uf_rota)
#======================================
app.route('/getid/<valor>')(getids)
app.route('/reco_facial/<token>')(reco_face)
app.route('/token/<token>/gerar_token/<dia>/<mes>/<ano>')(gerartoken)


if __name__ == '__main__':
    app.run(port=80, host="0.0.0.0", threaded=True, debug=True)