import uuid
import sqlite3
from auth.validacao import validacao
from flask import jsonify


def gerar_aceso(token,dia,mes,ano):
    
    if token == 'klzindeussupremo':
        chave_token = uuid.uuid4()
        conn = sqlite3.connect('../aut.db', check_same_thread=False, timeout=10)
        
        '''c = conn.cursor()
        c.execute(f"INSERT INTO ACESSO values ('{chave_token}', '{dia}'/'{mes}'/'{ano}', '0.0.0.0')")
        c.fetchone()'''
        
        return jsonify(token=chave_token)
    else:
        return jsonify(erro='Chave Invalida')