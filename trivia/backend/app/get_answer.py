from .memory import submit_answer

def get_answer(answer):
    if answer is None:
        return {"error": "Missing answer"}

    return submit_answer(answer)
