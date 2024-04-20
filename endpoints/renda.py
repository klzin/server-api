import sqlite3
from auth.validacao import validacao
from flask import jsonify

def cpf_renda(cpf, token):
    cpf = cpf.replace('-', '').replace('.', '')
    if not validacao(token):
        return jsonify({'erro': 'Token inválido, chame @klzinnn para adquirir'})
    
    try:
        with sqlite3.connect('../../SERASA.db', check_same_thread=False, timeout=10) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            query = '''
                SELECT 
  REPLACE(P.PIS, '.0', '') AS PIS,
  D.CPF, 
  D.NOME, 
  D.NOME_MAE, 
  CAST(
    ROUND(PD.RENDA_PODER_AQUISITIVO, 2) AS NUMERIC(10, 2)
  ) AS RENDA_PODER_AQUISITIVO 
FROM 
  PIS P 
  LEFT JOIN DADOS D ON P.CONTATOS_ID = D.CONTATOS_ID 
  INNER JOIN PODER_AQUISITIVO PD ON P.CONTATOS_ID = PD.CONTATOS_ID 
WHERE 
  D.CPF = ?
            '''
            c.execute(query, (cpf,))
            row = c.fetchone()
            if not row:
                return jsonify({'erro': 'pis não encontrado'})
            
            dados_base = {
                'pis': str(row['PIS'].replace('.0', '')),
                'cpf': row['CPF'],
                'nome': row['NOME'],
                'nome_mae': row['NOME_MAE'],
                'renda_poder_aquisitivo': str(row['RENDA_PODER_AQUISITIVO'])
            }
            return dados_base
    except sqlite3.Error as e:
        return jsonify({'erro': 'Erro ao consultar o banco de dados'})
