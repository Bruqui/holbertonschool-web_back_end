#!/usr/bin/env python3
"""
Module pour l'application Flask de base.
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Route GET pour la racine (/).

    Returns:
        str: Un payload JSON contenant un message de bienvenue.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
