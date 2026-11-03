
from flask import Flask, request, jsonify, render_template
from agent import agent
from database import init_db
from memory import save_message, get_history, clear_history

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    session_id = data.get("session_id")
    user_message = data.get("message", "").strip()

    if not session_id or not user_message:
        return jsonify({"error": "Session ID and message are required"}), 400

    try:
        history = get_history(session_id)

        save_message(session_id, "user", user_message)

        response = agent.invoke({
            "messages": history + [
                {"role": "user", "content": user_message}
            ]
        })

        bot_reply = response["messages"][-1].content

        save_message(session_id, "assistant", bot_reply)

        return jsonify({
            "reply": bot_reply,
            "session_id": session_id
        })

    except Exception:
        app.logger.exception("Chat request failed")
        return jsonify({"error": "Something went wrong. Please try again."}), 500


@app.route("/history", methods=["GET"])
def history():
    session_id = request.args.get("session_id")

    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    return jsonify({"messages": get_history(session_id)})


@app.route("/reset", methods=["POST"])
def reset():
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id")

    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    clear_history(session_id)

    return jsonify({"message": "Conversation history cleared"})


if __name__ == "__main__":
    app.run(debug=True)
