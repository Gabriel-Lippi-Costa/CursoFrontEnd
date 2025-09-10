from flask import Flask, request, jsonify
import statistics

app = Flask(__name__)

@app.route("/estatistica", methods=["POST"])
def estatistica():
    dados = request.json.get("valores", [])
    if not dados:
        return jsonify({"erro": "Nenhum valor enviado"}), 400

    media = statistics.mean(dados)
    variancia = statistics.pvariance(dados)
    desvio = statistics.pstdev(dados)

    return jsonify({
        "media": media,
        "variancia": variancia,
        "desvio_padrao": desvio
    })

if __name__ == "__main__":
    app.run(debug=True)
