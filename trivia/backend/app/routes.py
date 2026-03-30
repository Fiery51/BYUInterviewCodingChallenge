from flask import Blueprint, jsonify, request

from .get_answer import get_answer
from .get_questions import get_questions_easy, get_questions_medium, get_questions_hard
from .memory import (
    advance_question,
    get_current_question,
    get_percentage,
    get_score,
    get_total_questions,
    has_active_game,
    is_game_complete,
    start_game,
)

api_bp = Blueprint("api", __name__)



@api_bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "trivia-backend"})


@api_bp.get("/questions/easy")
def questions_easy():
    result = get_questions_easy()
    return _start_game_response(result)

@api_bp.get("/questions/medium")
def questions_medium():
    result = get_questions_medium()
    return _start_game_response(result)

@api_bp.get("/questions/hard")
def questions_hard():
    result = get_questions_hard()
    return _start_game_response(result)


@api_bp.post("/answer")
def answer():
    payload = request.get_json(silent=True) or {}
    user_answer = payload.get("answer")
    if user_answer is None:
        return jsonify({"error": "Missing answer"}), 400

    result = get_answer(user_answer)
    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)


@api_bp.post("/next")
def next_question():
    if not has_active_game():
        return jsonify({"error": "No active game"}), 400

    next_item = advance_question()
    if next_item is None:
        return jsonify(
            {
                "gameOver": True,
                "score": get_score(),
                "totalQuestions": get_total_questions(),
                "percentage": get_percentage(),
            }
        )

    return jsonify(
        {
            "gameOver": is_game_complete(),
            "score": get_score(),
            "totalQuestions": get_total_questions(),
            "percentage": get_percentage(),
            "question": next_item,
        }
    )


def _start_game_response(result):
    if "error" in result:
        return jsonify(result), 502

    start_game(result["questions"])
    first_question = get_current_question()
    return jsonify(
        {
            "difficulty": result["difficulty"],
            "gameOver": False,
            "score": get_score(),
            "totalQuestions": get_total_questions(),
            "percentage": get_percentage(),
            "question": first_question,
        }
    )
