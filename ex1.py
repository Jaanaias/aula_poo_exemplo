from flask import Flask, jsonify, request
app = Flask(__name__)

id = 0
filmes_db = []

@app.route("filmes", methods=["GET"])
def retornarFilmes():
    return jsonify(filmes_db)

@app.route("/filmes", methods=["POST"])
def salvarFilmes():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    diretor = dados.get("diretor")
    ano = dados.get("ano")

    filme = {"id": id, "nome":nome, "diretor": diretor, "ano": ano}

    filmes_db.append(filme)

    return jsonify(filme)

@app.route("/filmes/<int:id>", methods=["PUT"])
def editarfilmes(id):
    dados = request.get_json()
    nome = dados.get("nome")
    diretor = dados.get("diretor")
    ano = dados.get("ano")
    for filme in filmes_db:
        if filme["id"] == id:
            filme["nome"]= nome
            filme["ano"]= ano
            filme["diretor"]= diretor
            return jsonify(filme), 200
    return jsonify({"erro": "filme não encontrado"}), 404

@app.route("/filmes/<int:id>", methods=["DELETE"])
def removerFilmes(id):
    for filme in filmes_db:
        if filme["id"] == id:
            filmes_db.remove(filme)
        return "", 204
    return jsonify({"erro": "filme nao encontrado"}), 404

app.run(debug=True)