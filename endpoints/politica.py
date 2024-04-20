import sqlite3
from auth.validacao import validacao
from flask import jsonify

def dados_urna_eletronixa(cpf, token):
    cpf = cpf.replace('-', '').replace('.', '')
    with sqlite3.connect('../../SERASA.db', check_same_thread=False, timeout=10) as conn:
        if not validacao(token):
            return jsonify({'erro': 'Token invalido, chame @klzinnn para adquirir'})
        
        try:
            c = conn.cursor()
            c.execute("SELECT C.NOME, C.SEXO,C.RENDA, d.TITULO_ELEITOR FROM DADOS C INNER JOIN tse d on c.CONTATOS_ID = d.CONTATOS_ID WHERE CPF = ?", (cpf,))
            row = c.fetchone()
            if not row:
                return jsonify({'erro': 'CPF nao encontrado'})
            
            dados_base = {'nome': row[0], 'sexo': row[1], 'renda': row[2], 'titulo': str(row[3]).replace('.0', '')}  # Use integer indices to access row elements
            return dados_base
        except sqlite3.Error as e:
            return jsonify({'erro': 'Erro ao consultar o banco de dados'})