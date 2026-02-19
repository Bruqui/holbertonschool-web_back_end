#!/usr/bin/env python3
""" Module pour le système de mise en cache MRUCache.
Ce module définit une classe qui hérite de BaseCaching et gère
un cache avec l'algorithme de remplacement le plus récemment utilisé.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Système de cache MRU.
    Cette classe permet de stocker des éléments dans un dictionnaire.
    Si la limite est atteinte, l'élément le plus récemment accédé
    ou ajouté est supprimé (Most Recently Used).
    """

    def __init__(self):
        """ Initialisation de la classe.
        Appelle le constructeur parent et initialise une variable pour
        suivre la clé la plus récemment utilisée.
        """
        super().__init__()
        self.most_recent_key = ""

    def put(self, key, item):
        """ Ajoute un élément dans le cache.
        Si le cache dépasse MAX_ITEMS, supprime l'élément le plus
        récemment utilisé (celui dont la clé est self.most_recent_key).
        Args:
            key: La clé pour l'élément.
            item: La valeur associée à la clé.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.most_recent_key]
                print("DISCARD: {}".format(self.most_recent_key))

        self.cache_data[key] = item
        self.most_recent_key = key

    def get(self, key):
        """ Récupère un élément par sa clé.
        Si l'élément est trouvé, il est marqué comme le plus récemment utilisé.
        Args:
            key: La clé à rechercher.
        Returns:
            La valeur associée, ou None si absente.
        """
        if key is not None and key in self.cache_data:
            self.most_recent_key = key
            return self.cache_data.get(key)
        return None
