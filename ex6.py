from flask import Flask, jsonify, request
app = Flask(__name__)

id = 0
carros_db = []

@app.route("/carros", methods=["GET"])
def retornarCarros():
    return jsonify(carros_db)

@app.route("/carros", methods=["POST"])
def salvarCarros():
    global id
    id = id + 1
    dados = request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")

    carro = {"id": id, "modelo": modelo, "marca": marca, "ano": ano}

    carros_db.append(carro)

    return jsonify(carro)

@app.route("/carros/<int:id>", methods=["PUT"])
def editarCarros(id):
    dados = request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")

    for carro in carros_db:
        if carro["id"] == id:
            carro["modelo"] = modelo
            carro["marca"] = marca
            carro["ano"] = ano
            return jsonify(carro), 200

    return jsonify({"erro": "carro não encontrado"}), 404

@app.route("/carros/<int:id>", methods=["DELETE"])
def removerCarros(id):
    for carro in carros_db:
        if carro["id"] == id:
            carros_db.remove(carro)
            return "", 204

    return jsonify({"erro": "carro não encontrado"}), 404

app.run(debug=True)