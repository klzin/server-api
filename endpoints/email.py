import sqlite3
from auth.validacao import validacao
from flask import jsonify

def consulta_email(email, token):
    conn = sqlite3.connect('../SERASA.db', check_same_thread=False, timeout=10)
    auth = validacao(token)

    if auth == 1:
        try:
            c = conn.cursor()
            c.execute("SELECT contatos_id FROM EMAIL WHERE email = ?", (email,))
            contatos_id = c.fetchone()[0]
            c = conn.cursor()
            c.execute("SELECT cpf FROM DADOS WHERE contatos_id = ?", (contatos_id,))
            email_response = c.fetchall()
            
            email_list = []
            for email_lista_alls in email_response:
                email_dict = {
                            'cpf': str(email_lista_alls[0])
                        }
                email_list.append(email_dict)
            
            return jsonify({'cpf_cadastrado': email_list})
        except Exception as e:
            return jsonify({'erro': 'email nao encontrado'})
        finally:
            conn.close()
    else:
        return jsonify({'erro': 'Token invalido, chame @klzinnn para adquirir'})