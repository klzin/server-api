import sqlite3
from auth.validacao import validacao
from flask import jsonify

conn = sqlite3.connect('../../SERASA.db', check_same_thread=False, timeout=10)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

def telefone_consulta(telefone, token):
    telefone = telefone.replace('-', '').replace('.', '').replace('%20', '')
    try:
        auth = validacao(token)
        if auth != 1:
            return jsonify({'mensagem': 'Token inválido, chame @klzinnn para adquirir'})

        ddd = telefone[:2]
        telefone = telefone[2:]
        
        c = conn.cursor()
        c.execute("""
            SELECT CONTATOS_ID
            FROM TELEFONE
            WHERE DDD = ? AND TELEFONE = ?
        """, (ddd, telefone,))
        row = c.fetchall()
        if not row:
            return jsonify({'erro': 'Telefone não encontrado'})

        dados_bases = []

        for contatos_id in row:
            c.execute("""
                SELECT cpf, nome, sexo,renda,nasc,nome_mae,nome_pai
                FROM DADOS
                WHERE contatos_id = ?
            """, (contatos_id['CONTATOS_ID'],))
            result = c.fetchone()
            
            dados_base = {'nome': result['nome'], 'cpf': result['cpf'], 'sexo': result['sexo'], 'renda': result['renda'], 'nascimento': result['nasc'], 'mae': result['nome_mae'], 'pai': result['nome_pai']}
            dados_bases.append(dados_base)

        return jsonify(dados_bases)
    
    except Exception as e:
        return jsonify({'erro': 'Ocorreu um erro ao processar a requisição '+e})