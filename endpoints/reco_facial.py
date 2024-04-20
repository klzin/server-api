import sqlite3
from auth.validacao import validacao
from flask import jsonify

def reconhecimento(token):
    
    try:
        with sqlite3.connect('data.db', check_same_thread=False, timeout=10) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            query = '''SELECT dominant_emotion, cpf, nome, foto FROM dados WHERE TOKEN = ?'''
            c.execute(query, (token,))
            row = c.fetchone()
            if not row:
                return jsonify({'erro': 'facial não encontrado'})
            
            dados_base = {
                'emocao': row['dominant_emotion'],
                'cpf': row['cpf'],
                'nome': row['nome'],
                'foto': row['foto'],
            }
            return dados_base
    except sqlite3.Error as e:
        return jsonify({'erro': 'Erro ao consultar o banco de dados '+str(e)})
