import random

from flask import Blueprint, app, jsonify

api_bp = Blueprint("api", __name__)

TRIVIA_PROMPTS = [
    "What planet is known as the Red Planet?",
    "Which ocean is the largest on Earth?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the capital of Japan?",
]


@api_bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "trivia-backend"})


#returns question, along with all possible answers
@app.route("/api/questions/easy", methods=["GET"])
def get_questions_easy():
    result = get_questions_easy()
    return jsonify(result)