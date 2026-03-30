import random

from flask import Blueprint, jsonify

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


@api_bp.get("/trivia/question")
def random_question():
    question = random.choice(TRIVIA_PROMPTS)
    return jsonify({"question": question})
