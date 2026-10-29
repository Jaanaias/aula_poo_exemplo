from flask import Flask, jsonify, request
app = Flask(__name__)

id = 0
cidades_db = []

@app.route("/cidades", methods=["GET"])
def retornarCidades():
    return jsonify(cidades_db)

@app.route("/cidades", methods=["POST"])
def salvarCidades():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    cidade = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}

    cidades_db.append(cidade)

    return jsonify(cidade)

@app.route("/cidades/<int:id>", methods=["PUT"])
def editarCidades(id):
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    for cidade in cidades_db:
        if cidade["id"] == id:
            cidade["nome"] = nome
            cidade["preco"] = preco
            cidade["categoria"] = categoria
            return jsonify(cidade), 200

    return jsonify({"erro": "cidade não encontrada"}), 404

@app.route("/cidades/<int:id>", methods=["DELETE"])
def removerCidades(id):
    for cidade in cidades_db:
        if cidade["id"] == id:
            cidades_db.remove(cidade)
            return "", 204

    return jsonify({"erro": "cidade não encontrada"}), 404

app.run(debug=True)