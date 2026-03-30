import random

import requests

API_URL = "https://opentdb.com/api.php"


def _format_questions(raw_questions):
    formatted_questions = []
    for raw_question in raw_questions:
        correct_answer = raw_question.get("correct_answer")
        incorrect_answers = raw_question.get("incorrect_answers", [])

        if correct_answer is None:
            return None

        all_answers = list(incorrect_answers) + [correct_answer]
        random.shuffle(all_answers)

        formatted_questions.append(
            {
                "question": raw_question.get("question", ""),
                "answers": all_answers,
                "correct_answer": correct_answer,
            }
        )

    return formatted_questions


def _get_questions_by_difficulty(difficulty, amount=10):
    try:
        response = requests.get(
            API_URL,
            params={"amount": amount, "difficulty": difficulty, "type": "multiple"},
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()
    except (requests.RequestException, ValueError):
        return {"error": "Failed to fetch questions"}

    if payload.get("response_code") != 0:
        return {"error": "Failed to fetch questions"}

    raw_questions = payload.get("results") or []
    if len(raw_questions) != amount:
        return {"error": "Failed to fetch questions"}

    questions = _format_questions(raw_questions)
    if questions is None:
        return {"error": "Failed to fetch questions"}

    return {"difficulty": difficulty, "questions": questions}


def get_questions_easy():
    return _get_questions_by_difficulty("easy")


def get_questions_medium():
    return _get_questions_by_difficulty("medium")


def get_questions_hard():
    return _get_questions_by_difficulty("hard")
