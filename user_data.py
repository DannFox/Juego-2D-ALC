# user_data.py

import json

def get_username(player):
    username = input(f"Jugador {player}, por favor ingresa tu nombre de usuario: ")
    return username

def load_scores():
    try:
        with open('scores.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_scores(scores):
    with open('scores.json', 'w') as f:
        json.dump(scores, f)

def get_score(username, scores):
    return scores.get(username, 0)

def update_score(username, score, scores):
    scores[username] = score
    save_scores(scores)
