from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada para almacenar conocimiento
knowledge_base = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "Como estas?": "Estoy bien, gracias. ¿Y tú?",
    "de que te gustaría hablar?": "Puedo hablar de muchos temas. ¿Tienes alguna preferencia?",
}

# Pregunta predeterminada para adquirir nuevo conocimiento
default_question = "No entiendo. ¿Puedes proporcionarme más información sobre eso?"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    # Buscar respuesta en la base de conocimientos
    response = knowledge_base.get(message, default_question)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
