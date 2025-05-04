# 🎮 FURIA Challenge - Know Your Fan

## 📌 Desafio

Este projeto foi desenvolvido para o **Challenge #2: Know Your Fan [Nível Hard]**, com o objetivo de criar uma aplicação capaz de coletar informações detalhadas sobre o perfil de fãs da organização de e-sports **FURIA**, visando personalizar a experiência com base em dados reais.

---

## 🎯 Objetivos da Solução

- Coletar dados pessoais: **nome, CPF, idade, endereço completo**
- Armazenar informações sobre:
  - Interesses em e-sports
  - Participações em eventos
  - Atividades no último ano
  - Compras relacionadas a e-sports
- Associar redes sociais ao perfil do fã:
  - Nome de usuário
  - Número de seguidores
  - Nome da rede
- Registrar o consentimento para coleta de dados

---

## ✅ Funcionalidades Implementadas

- Backend funcional com **Flask** + **SQLAlchemy**
- Banco de dados **SQLite**
- CRUD completo para fãs e Nivel de fã
- Estrutura de rotas REST para integração com front-end
- Interface de testes com **Insomnia**
- Consentimento explícito para uso dos dados
- Telas para utilizar as Rotas via html+css

---

## 🚧 Funcionalidades Não Implementadas

Por questões de tempo e escopo, algumas funcionalidades **não foram implementadas**:

- Upload de documentos e validação via AI
- Leitura automática de interações em redes sociais
- Validação de perfis de sites de e-sports com inteligência artificial
- Escrever o termo de consentimento 

---

## 😓 Dificuldades e Limitações

- ⚠️ A mudança nos requisitos do desafio passou despercebida até a **véspera da entrega**, o que impactou diretamente no planejamento e na arquitetura do projeto original.
- ⚠️ O desenvolvedor (eu) possui **limitações técnicas com front-end**, o que atrasou o início da interface visual da aplicação.
- ⚠️ Devido ao tempo limitado, **as validações com AI foram descartadas**, e o foco foi manter um backend funcional, coerente e bem documentado.

---

## 🧪 Como Executar

1. Clone o repositório:

    ```
    git clone https://github.com/SeuUsuario/SeuRepositorio.git
    cd SeuRepositorio
    ```

2. Crie e ative um ambiente virtual:

    ```
    python -m venv venv
    venv\Scripts\activate  # ou source venv/bin/activate no Linux/Mac
    ```

3. Instale as dependências:

    ```
    pip install -r requirements.txt
    ```

4. Execute o servidor Flask:

    ```
    python Server/app.py
    ```

---

## 📁 Estrutura

- `BackEnd`: Arquivos do backend Flask
- `FrontEnd`: Arquivos Html das telas
- `README.md`: Este arquivo
- `requirements.txt`: Dependências do projeto

## 📊 Diagrama de Entidade e Relacionamento DER

![Diagrama de Entidade e Relacionamento](.\ReadMe_Addons\DER.png)

---

## 👤 Desenvolvido por

**Andrey Matheus Brambilla**  
Desenvolvedor backend em formação, participante do desafio da FURIA.  
Apesar das limitações e falhas de planejamento, me esforcei para entregar o máximo possível dentro do prazo e com as tecnologias que domino.

---

## 📄 Licença

Este projeto está licenciado sob os termos da **MIT License**.
