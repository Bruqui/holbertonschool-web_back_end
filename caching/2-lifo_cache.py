#!/usr/bin/env python3
""" Module pour le système de mise en cache LIFOCache.
Ce module définit une classe qui hérite de BaseCaching et gère
un cache avec l'algorithme de remplacement Dernier Entré, Premier Sorti.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Système de cache LIFO.
    Cette classe permet de stocker des éléments dans un dictionnaire.
    Lorsque la limite est atteinte, l'élément le plus récemment ajouté
    est supprimé (Last-In, First-Out).
    """

    def __init__(self):
        """ Initialisation de la classe.
        Appelle le constructeur parent et initialise une liste pour
        suivre l'ordre des clés insérées.
        """
        super().__init__()
        self.last_key = ""

    def put(self, key, item):
        """ Ajoute un élément dans le cache.
        Si le cache dépasse MAX_ITEMS, supprime le dernier élément inséré.
        Args:
            key: La clé pour l'élément.
            item: La valeur associée à la clé.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.last_key]
                print("DISCARD: {}".format(self.last_key))

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """ Récupère un élément par sa clé.
        Args:
            key: La clé à rechercher.
        Returns:
            La valeur associée, ou None si la clé est absente ou None.
        """
        return self.cache_data.get(key)
