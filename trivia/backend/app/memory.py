current_score = 0
answer_key = []
game_questions = []
current_question_index = 0
answered_indices = set()
answered_results = {}


def start_game(questions):
    global game_questions
    global answer_key
    global current_score
    global current_question_index
    global answered_indices
    global answered_results

    game_questions = list(questions)
    answer_key = [str(question["correct_answer"]) for question in game_questions]
    current_score = 0
    current_question_index = 0
    answered_indices = set()
    answered_results = {}


def has_active_game():
    return len(game_questions) > 0


def get_total_questions():
    return len(game_questions)


def get_score():
    return current_score


def get_percentage():
    total = get_total_questions()
    if total == 0:
        return 0.0
    return round((current_score / total) * 100, 1)


def is_game_complete():
    return current_question_index >= get_total_questions()


def get_current_question():
    if not has_active_game() or is_game_complete():
        return None

    question_data = game_questions[current_question_index]
    return {
        "questionNumber": current_question_index + 1,
        "question": question_data["question"],
        "answers": question_data["answers"],
    }


def validate_answer(selected_option):
    if is_game_complete() or selected_option is None:
        return False

    return str(selected_option) == answer_key[current_question_index]


def submit_answer(selected_option):
    global current_score

    if not has_active_game() or is_game_complete():
        return {"error": "No active question"}

    question_index = current_question_index
    already_answered = current_question_index in answered_indices
    if already_answered:
        is_correct = answered_results[question_index]
    else:
        is_correct = validate_answer(selected_option)

    if not already_answered:
        answered_indices.add(question_index)
        answered_results[question_index] = is_correct
        if is_correct:
            current_score += 1

    return {
        "result": "correct" if is_correct else "incorrect",
        "alreadyAnswered": already_answered,
        "score": current_score,
        "totalQuestions": get_total_questions(),
        "percentage": get_percentage(),
        "questionNumber": current_question_index + 1,
    }


def advance_question():
    global current_question_index

    if not has_active_game():
        return None

    if current_question_index < get_total_questions():
        current_question_index += 1

    return get_current_question()
