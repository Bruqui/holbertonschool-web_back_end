#!/usr/bin/env python3
"""
Module pour l'application Flask de base.
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Route GET pour la racine (/).

    Returns:
        str: Un payload JSON contenant un message de bienvenue.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """
    Route POST pour enregistrer un nouvel utilisateur.

    Attend les champs de formulaire 'email' et 'password'.

    Returns:
        str: Un payload JSON indiquant le succès ou l'échec de la création.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
