# Emare Intranet — Flask Giriş Noktası

from flask import Flask, render_template, jsonify
import os


def create_app():
    app = Flask(__name__)

# === Emare Feedback ===
from feedback_bp import feedback_bp, FeedbackMsg
app.register_blueprint(feedback_bp)
# FeedbackMsg tablosunu oluşturmak için: with app.app_context(): db.create_all()
# ======================

    app.secret_key = os.environ.get("SECRET_KEY", "emare-dev-key")

    @app.route("/")
    def index():
        return render_template("index.html", title="Emare Intranet")

    @app.route("/health")
    def health():
        return jsonify({"status": "ok", "app": "Emare Intranet"})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200, debug=True)
