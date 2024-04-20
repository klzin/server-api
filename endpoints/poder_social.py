import sqlite3
from auth.validacao import validacao
from flask import jsonify

conn = sqlite3.connect('../../SERASA.db', check_same_thread=False, timeout=10)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

def consulta_podersocial(cpf, token):
    try:
        auth = validacao(token)
        if auth != 1:
            return jsonify({'mensagem': 'Token inválido, chame @klzinnn para adquirir'})
        
        c = conn.cursor()
        c.execute("""
            SELECT D.CBO,
       D.CD_MOSAIC,
       D.RENDA,
       S.CSBA,
       P.PODER_AQUISITIVO,
       P.FX_PODER_AQUISITIVO,
       S.CSB8
  FROM DADOS D
       INNER JOIN
       SCORE S ON D.CONTATOS_ID = S.CONTATOS_ID
       LEFT JOIN
       poder_aquisitivo P ON D.CONTATOS_ID = P.CONTATOS_ID
 WHERE CPF = ?
        """, (cpf,))
        row = c.fetchone()
        fxpoder_aquisitivo = row['FX_PODER_AQUISITIVO'].replace('at�', 'ate')
        if not row:
            return jsonify({'erro': 'CPF não encontrado'})
        
        dados_base = {'mosaic': row['CD_MOSAIC'], 'fx_poder_aquisitivo': fxpoder_aquisitivo, 'cbo': row['CBO'], 'poder_aquisitivo': row['PODER_AQUISITIVO'], 'renda': row['RENDA'], 'score_csba': str(row['CSBA']), 'score_csb8': row['CSB8']}
        
        return dados_base
    except:
        return jsonify({'erro': 'Ocorreu um erro ao processar a requisição / cpf nao encontrado'})