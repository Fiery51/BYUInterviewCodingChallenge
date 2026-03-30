import random

from flask import Blueprint, jsonify, request

from .get_answer import get_answer

from trivia.backend.app.get_questions import get_questions_easy, get_questions_medium, get_questions_hard

api_bp = Blueprint("api", __name__)



@api_bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "trivia-backend"})


@api_bp.get("/questions/easy")
def questions_easy():
    result = get_questions_easy()
    return jsonify(result)

@api_bp.get("/questions/medium")
def questions_medium():
    result = get_questions_medium()
    return jsonify(result)

@api_bp.get("/questions/hard")
def questions_hard():
    result = get_questions_hard()
    return jsonify(result)


@api_bp.post("/answer")
def answer():
    user_answer = request.get_json().get("answer")
    result = get_answer(user_answer)
    return jsonify(result)