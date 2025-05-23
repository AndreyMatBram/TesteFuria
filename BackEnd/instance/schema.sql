CREATE TABLE fan_level (
	id INTEGER NOT NULL, 
	nome VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE game (
	id INTEGER NOT NULL, 
	nome VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE fan (
	id INTEGER NOT NULL, 
	nome VARCHAR(100) NOT NULL, 
	idade INTEGER NOT NULL, 
	nivel_fa_id INTEGER NOT NULL, 
	consentimento BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(nivel_fa_id) REFERENCES fan_level (id)
);
CREATE TABLE social_network (
	id INTEGER NOT NULL, 
	nome VARCHAR(100) NOT NULL, 
	usuario INTEGER, 
	seguidores INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario) REFERENCES fan (id)
);
CREATE TABLE fan_documents (
	id INTEGER NOT NULL, 
	fan_id INTEGER NOT NULL, 
	documento VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(fan_id) REFERENCES fan (id)
);
CREATE TABLE games_list (
	fan_id INTEGER NOT NULL, 
	game_id INTEGER NOT NULL, 
	PRIMARY KEY (fan_id, game_id), 
	FOREIGN KEY(fan_id) REFERENCES fan (id), 
	FOREIGN KEY(game_id) REFERENCES game (id)
);
