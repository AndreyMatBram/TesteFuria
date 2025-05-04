from flask import Flask, request, jsonify
from Models import db, Fan, FanLevel, Game, SocialNetwork
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  #Nome do arquivo.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False # Para suportar caracteres especiais / evitar erros de unicode
CORS(app)# Permite requisições de qualquer origem (CORS)

# Inicializa o banco de dados com o app
db.init_app(app)

# Cria o banco de dados apenas uma vez na inicialização do app
with app.app_context():
    db.create_all()

#============================== ROTAS ==============================#
@app.route('/')
def index():
    return "API Funcionando!"

@app.route('/fan/add', methods=['POST'])
def add_fan():
    data = request.json

    #coleta de dados do fã
    new_fan = Fan(
        nome = data.get('nome', None),
        idade = data.get('idade', None),
        nivel_fa_id = data.get('nivel_fa_id', 0),
        consentimento = data.get('consentimento', False)
    )

    #verificando o consentimento para salvar
    if not new_fan.consentimento:
        return jsonify({"msg":"É nescessario o consentimento para o cadastro!"}), 400
    if not new_fan.nome:
        return jsonify({"msg":"É nescessario o nome para o cadastro!"}), 400
    
    
    db.session.add(new_fan)
    db.session.commit()
    return jsonify({"message": "Fã adicionado com sucesso!"}), 201

@app.route('/fan/busca', methods = ['GET'])
def fanList():

    fans= Fan.query.all()
    if not fans :
        return jsonify({"msg":"Nenhum fã registrado!"}), 202 #Não ha fans porem o contato com o banco ocorreu, 204 não permite atrelar uma mensagem

    
    saida = []
    for fan in fans:
        nivel_fa = FanLevel.query.get(fan.nivel_fa_id)
        fan_data = {
        'id': fan.id,
        'nome': fan.nome,
        'idade': fan.idade,
        'nivel_fa_id': nivel_fa.nome if nivel_fa else fan.nivel_fa_id,
        'consentimento': fan.consentimento
        }
        saida.append(fan_data)
    return jsonify(saida), 200

@app.route('/fan/busca/<int:id>', methods = ['GET'])
def fanBusca(id):
    fan = Fan.query.get(id)
    if not fan:
        return jsonify({"msg":"Fã não encontrado!"}), 202
    
    nivel_fa = FanLevel.query.get(fan.nivel_fa_id)

    fan_data = {
        'id': fan.id,
        'nome': fan.nome,
        'idade': fan.idade,
        'nivel_fa_id': nivel_fa.nome if nivel_fa else fan.nivel_fa_id,
        'consentimento': fan.consentimento
    }
    return jsonify(fan_data), 200

@app.route('/fan/busca/<string:nome>', methods = ['GET'])
def fanBuscaNome(nome):
    fan = Fan.query.filter_by(nome=nome).first()
    if not fan:
        return jsonify({"msg":"Fã não encontrado!"}), 202

    nivel_fa = FanLevel.query.get(fan.nivel_fa_id)

    fan_data = {
        'id': fan.id,
        'nome': fan.nome,
        'idade': fan.idade,
        'nivel_fa_id': nivel_fa.nome if nivel_fa else fan.nivel_fa_id,
        'consentimento': fan.consentimento
    }

    return jsonify(fan_data), 200

@app.route('/fan/update/<int:id>', methods=['PUT'])
def update_fan(id):
    data = request.json
    fan = Fan.query.get(id)

    if not fan:
        return jsonify({"msg":"Fã não encontrado!"}), 202

    # Atualiza os dados do fã
    fan.nome = data.get('nome', fan.nome)
    fan.idade = data.get('idade', fan.idade)
    fan.nivel_fa_id = data.get('nivel_fa_id', fan.nivel_fa_id)
    fan.consentimento = data.get('consentimento', fan.consentimento)

    db.session.commit()
    return jsonify({"message": "Fã atualizado com sucesso!"}), 200

@app.route('/fan/update/<string:nome>', methods=['PUT'])
def update_fan_nome(nome):
    data = request.json
    fan = Fan.query.filter_by(nome=nome).first()

    if not fan:
        return jsonify({"msg":"Fã não encontrado!"}), 202

    # Atualiza os dados do fã
    fan.nome = data.get('nome', fan.nome)
    fan.idade = data.get('idade', fan.idade)
    fan.nivel_fa_id = data.get('nivel_fa_id', fan.nivel_fa_id)
    fan.consentimento = data.get('consentimento', fan.consentimento)

    db.session.commit()
    return jsonify({"message": "Fã atualizado com sucesso!"}), 200

@app.route('/fan/delete/<int:id>', methods=['DELETE'])
def delete_fan(id):
    fan = Fan.query.get(id)
    if not fan:
        return jsonify({"msg":"Fã não encontrado!"}), 202

    db.session.delete(fan)
    db.session.commit()
    return jsonify({"message": "Fã deletado com sucesso!"}), 200

@app.route('/fan/delete/<string:nome>', methods=['DELETE'])
def delete_fan_nome(nome):
    fan = Fan.query.filter_by(nome=nome).first()
    if not fan:
        return jsonify({"msg":"Fã não encontrado!"}), 202

    db.session.delete(fan)
    db.session.commit()
    return jsonify({"message": "Fã deletado com sucesso!"}), 200

@app.route('/nivelFa/add', methods=['POST'])
def add_nivel_fa():
    data = request.json

    if FanLevel.query.get(data['id']):
        return jsonify({"msg":"Nivel de fã já cadastrado!"}), 400

    #coleta de dados do fã
    new_nivel_fa = FanLevel(
        id = data['id'],
        nome = data['nome']
    )

    

    db.session.add(new_nivel_fa)
    db.session.commit()
    return jsonify({"message": "Nivel de fã adicionado com sucesso!"}), 201

@app.route('/nivelFa/busca', methods = ['GET'])
def nivelFaList():

    niveis= FanLevel.query.all()
    if not niveis :
        return jsonify({"msg":"Nenhum nível de fã registrado!"}), 202 #Não ha fans porem o contato com o banco ocorreu, 204 não permite atrelar uma mensagem
    
    saida = []
    for nivel in niveis:
        nivel_data = {
        'id': nivel.id,
        'nome': nivel.nome
        }
        saida.append(nivel_data)
    return jsonify(saida), 200

@app.route('/nivelFa/busca/<int:id>', methods = ['GET'])
def nivelFaBusca(id):
    nivel = FanLevel.query.get(id)
    if not nivel:
        return jsonify({"msg":"Nivel de fã não encontrado!"}), 202

    nivel_data = {
        'id': nivel.id,
        'nome': nivel.nome
    }
    return jsonify(nivel_data), 200

@app.route('/nivelFa/busca/<string:nome>', methods = ['GET'])
def nivelFaBuscaNome(nome):
    nivel = FanLevel.query.filter_by(nome=nome).first()
    if not nivel:
        return jsonify({"msg":"Nivel de fã não encontrado!"}), 202

    nivel_data = {
        'id': nivel.id,
        'nome': nivel.nome
    }

    return jsonify(nivel_data), 200

@app.route('/nivelFa/update/<int:id>', methods=['PUT'])
def update_nivel_fa(id):
    data = request.json
    nivel = FanLevel.query.get(id)

    if not nivel:
        return jsonify({"msg":"Nivel de fã não encontrado!"}), 202

    # Atualiza os dados do fã
    nivel.nome = data.get('nome', nivel.nome)
    nivel.id = data.get('id', nivel.id)
    
    db.session.commit()
    return jsonify({"message": "Nivel de fã atualizado com sucesso!"}), 200

@app.route('/nivelFa/update/<string:nome>', methods=['PUT'])
def update_nivel_fa_nome(nome):
    data = request.json
    nivel = FanLevel.query.filter_by(nome=nome).first()

    if not nivel:
        return jsonify({"msg":"Nivel de fã não encontrado!"}), 202

    # Atualiza os dados do fã
    nivel.nome = data.get('nome', nivel.nome)
    nivel.id = data.get('id', nivel.id)

    db.session.commit()
    return jsonify({"message": "Nivel de fã atualizado com sucesso!"}), 200

@app.route('/nivelFa/delete/<int:id>', methods=['DELETE'])
def delete_nivel_fa(id):
    nivel = FanLevel.query.get(id)
    if not nivel:
        return jsonify({"msg":"Nivel de fã não encontrado!"}), 202

    db.session.delete(nivel)
    db.session.commit()
    return jsonify({"message": "Nivel de fã deletado com sucesso!"}), 200

@app.route('/nivelFa/delete/<string:nome>', methods=['DELETE'])
def delete_nivel_fa_nome(nome):
    nivel = FanLevel.query.filter_by(nome=nome).first()
    if not nivel:
        return jsonify({"msg":"Nivel de fã não encontrado!"}), 202

    db.session.delete(nivel)
    db.session.commit()
    return jsonify({"message": "Nivel de fã deletado com sucesso!"}), 200

@app.route('/fake-twitter/<username>', methods=['GET'])
def fake_twitter(username):
    # Dados fictícios simulando uma resposta da API do X
    from random import randint
    mock_data = {
        "username": username,
        "seguidores": randint(1, 10000),
        "tweets": [
            {"texto": "Vamos FURIA!", "data": "2025-05-01"},
            {"texto": "Assistindo o Major com a camisa da FURIA 🔥", "data": "2025-04-28"},
            {"texto": "FURIA TOP 1 DO MUNDO!", "data": "2025-04-20"}
        ],
        "interacoes_com_furia": True,
        "seguindo_furia": True,
        "temas_esports_frequentes": ["Counter-Strike", "FURIA", "Major", "e-sports"]
    }

    return jsonify(mock_data)


if __name__ == '__main__':
    app.run(debug=True)