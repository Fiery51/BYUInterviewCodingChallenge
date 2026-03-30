import requests
import json
from .memory import store_answer
import random

def get_questions_easy():
    response = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")
    payload = response.json()
    status_code = payload["response_code"]
    #Correct answer is always the last one in the list of answers
    if(status_code == 0):
        questions = payload["results"]
        question = questions[0]["question"]
        correct_answer = questions[0]["correct_answer"]
        incorrect_answers = questions[0]["incorrect_answers"]
        all_answers = incorrect_answers + [correct_answer]
        #all_answers = {0: all_answers[0], 1: all_answers[1], 2: all_answers[2], 3: all_answers[3]}
        store_answer(correct_answer)
        random.shuffle(all_answers)
        return {"question": question, "answers": all_answers}
    else:
        return {"error": "Failed to fetch questions"}
    

def get_questions_medium():
    response = requests.get("https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple")
    payload = response.json()
    status_code = payload["response_code"]
    if(status_code == 0):
        questions = payload["results"]
        question = questions[0]["question"]
        correct_answer = questions[0]["correct_answer"]
        incorrect_answers = questions[0]["incorrect_answers"]
        all_answers = incorrect_answers + [correct_answer]
        all_answers = {0: all_answers[0], 1: all_answers[1], 2: all_answers[2], 3: all_answers[3]}
        store_answer(correct_answer)
        return {"question": question, "answers": all_answers}
    else:
        return {"error": "Failed to fetch questions"}
    

def get_questions_hard():
    response = requests.get("https://opentdb.com/api.php?amount=1&difficulty=hard&type=multiple")
    payload = response.json()
    status_code = payload["response_code"]
    if(status_code == 0):
        questions = payload["results"]
        question = questions[0]["question"]
        correct_answer = questions[0]["correct_answer"]
        incorrect_answers = questions[0]["incorrect_answers"]
        all_answers = incorrect_answers + [correct_answer]
        all_answers = {0: all_answers[0], 1: all_answers[1], 2: all_answers[2], 3: all_answers[3]}
        store_answer(correct_answer)
        return {"question": question, "answers": all_answers}
    else:
        return {"error": "Failed to fetch questions"}