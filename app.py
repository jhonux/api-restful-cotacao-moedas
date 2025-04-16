from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

historico_cache = []


@app.route('/cotacao', methods=['GET'])
def get_cotacao():
    base = request.args.get('base', 'EUR')
    symbols = request.args.get('symbols', 'BRL')
    url = f'https://api.frankfurter.app/latest?from={base}&to={symbols}'

    try:
        response = requests.get(url)
        print(f"Requisição para: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Resposta: {response.text}")

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Falha ao consultar API externa'}), 500
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return jsonify({'error': 'Erro interno ao consultar cotação.'}), 500
    

@app.route('/cotacao', methods=['POST'])
def post_cotacao():
    dados = request.get_json()
    
    if not dados:
        return jsonify({'error': 'Dados JSON são obrigatórios'}), 400
  
    historico_cache.append(dados)
    
    return jsonify({'mensagem': 'Cotação registrada com sucesso', 'dados': dados}), 201


@app.route('/historico', methods=['GET'])
def get_historico():
    return jsonify(historico_cache)


if __name__ == '__main__':
    app.run(debug=True)