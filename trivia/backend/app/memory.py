current_score = 0
answer_key = ""


def store_answer(answer):
    global answer_key
    answer_key = answer


def validate_answer(selected_option):
    return selected_option == answer_key


def update_score(num):
    global current_score
    current_score += num
    return current_score


def get_score():
    return current_score

