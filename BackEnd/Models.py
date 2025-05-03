from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#tabela de nivel de fã, para mapear o nivel de fã
class FanLevel(db.Model):
    __tablename__ = 'fan_level'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

#Tabela de rede sociais, slava o @ do usuario e id do fã respectivo e o numero de seguidores
class SocialNetwork(db.Model):
    __tablename__ = 'social_network'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.Integer,db.ForeignKey('fan.id'), nullable=True)
    seguidores = db.Column(db.Integer, nullable=True)


#Tabela de jogos, para mapear os jogos favoritos dos fãs e o id do fã respectivo
class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

#tabela de documentos para armazenar os documentos dos fãs, como RG, CPF e etc..
class FanDocuments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fan_id = db.Column(db.Integer, db.ForeignKey('fan.id'), nullable=False)
    documento = db.Column(db.String(100), nullable=False)


#tabela de fãs, onde são armazenados os dados dos fãs, como nome, idade, nivel de fã e etc..
#Tabela principal do banco de dados, onde são armazenados os dados dos fãs e relacina com as outras tabelas
class Fan(db.Model):
    __tablename__ = 'fan'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    nivel_fa_id = db.Column(db.Integer, db.ForeignKey('fan_level.id'), nullable=False)
    consentimento = db.Column(db.Boolean, nullable=False, default=False)

    ## Relacionamento um-para-muitos entre fã e documentos
    documents = db.relationship('FanDocuments', backref=db.backref('fan', lazy=True))
    ## Relacionamento muitos-para-um entre Rede social e fã
    social_network = db.relationship('SocialNetwork', backref=db.backref('fans', lazy=True))
    ## Relacionamento muitos-para-muitos entre fãs e jogos
    games_list = db.relationship('Game', secondary='games_list', backref=db.backref('fans', lazy=True))

games_list = db.Table('games_list',
    db.Column('fan_id', db.Integer, db.ForeignKey('fan.id'), primary_key=True),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True)
)
    


