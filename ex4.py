from flask import Flask, jsonify, request
app = Flask(__name__)

id = 0
funcionarios_db = []

@app.route("/funcionarios", methods=["GET"])
def retornarFuncionarios():
    return jsonify(funcionarios_db)

@app.route("/funcionarios", methods=["POST"])
def salvarFuncionarios():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    cargo = dados.get("cargo")
    salario = dados.get("salario")

    funcionario = {"id": id, "nome": nome, "cargo": cargo, "salario": salario}

    funcionarios_db.append(funcionario)

    return jsonify(funcionario)

@app.route("/funcionarios/<int:id>", methods=["PUT"])
def editarFuncionarios(id):
    dados = request.get_json()
    nome = dados.get("nome")
    cargo = dados.get("cargo")
    salario = dados.get("salario")
    for funcionario in funcionarios_db:
        if funcionario["id"] == id:
            funcionario["nome"] = nome
            funcionario["cargo"] = cargo
            funcionario["salario"] = salario
            return jsonify(funcionario), 200
    return jsonify({"erro": "funcionário não encontrado"}), 404

@app.route("/funcionarios/<int:id>", methods=["DELETE"])
def removerFuncionarios(id):
    for funcionario in funcionarios_db:
        if funcionario["id"] == id:
            funcionarios_db.remove(funcionario)
            return "", 204
    return jsonify({"erro": "funcionário não encontrado"}), 404

app.run(debug=True)