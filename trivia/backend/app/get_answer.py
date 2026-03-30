from .memory import validate_answer

def get_answer(answer):
    if validate_answer(answer):
        return {"result": "correct"}
    else:
        return {"result": "incorrect"}