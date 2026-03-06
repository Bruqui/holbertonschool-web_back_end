#!/usr/bin/env python3
"""
Module pour l'application Flask de base.
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    Route POST pour connecter un utilisateur et créer une session.

    Attend les champs de formulaire 'email' et 'password'.

    Returns:
        str: Un payload JSON de confirmation avec un cookie de session,
             ou une erreur 401 si les identifiants sont incorrects.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = jsonify({"email": email, "message": "logged in"})

    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """
    Route DELETE pour déconnecter un utilisateur.

    Attend le cookie 'session_id'.
    Redirige vers '/' en cas de succès, sinon renvoie une erreur 403.
    """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
