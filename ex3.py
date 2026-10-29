from flask import Flask, jsonify, request
app = Flask(__name__)

id = 0
musicas_db = []

@app.route("/musicas", methods=["GET"])
def retornarMusicas():
    return jsonify(musicas_db)

@app.route("/musicas", methods=["POST"])
def salvarMusicas():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    artista = dados.get("artista")
    ano = dados.get("ano")

    musica = {"id": id, "nome": nome, "artista": artista, "ano": ano}

    musicas_db.append(musica)

    return jsonify(musica)

@app.route("/musicas/<int:id>", methods=["PUT"])
def editarMusicas(id):
    dados = request.get_json()
    nome = dados.get("nome")
    artista = dados.get("artista")
    ano = dados.get("ano")
    for musica in musicas_db:
        if musica["id"] == id:
            musica["nome"] = nome
            musica["artista"] = artista
            musica["ano"] = ano
            return jsonify(musica), 200
    return jsonify({"erro": "música não encontrada"}), 404

@app.route("/musicas/<int:id>", methods=["DELETE"])
def removerMusicas(id):
    for musica in musicas_db:
        if musica["id"] == id:
            musicas_db.remove(musica)
            return "", 204
    return jsonify({"erro": "música não encontrada"}), 404

app.run(debug=True)