from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'pagina.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    try:
        data = request.get_json()
        nome = data.get('nome', '').strip()
        cpf = data.get('cpf', '').strip()
        
        if not nome or not cpf:
            return jsonify({'message': 'Nome e CPF são obrigatórios!'}), 400
        
        # Salvar no arquivo texto.txt
        with open('texto.txt', 'a', encoding='utf-8') as f:
            f.write(f"{nome},{cpf}\n")
        
        return jsonify({'message': 'Pessoa cadastrada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': f'Erro: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)