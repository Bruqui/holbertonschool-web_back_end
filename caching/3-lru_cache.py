#!/usr/bin/env python3
""" Module pour le système de mise en cache LRUCache.
Ce module définit une classe qui hérite de BaseCaching et gère
un cache avec l'algorithme de remplacement le moins récemment utilisé.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Système de cache LRU.
    Cette classe permet de stocker des éléments dans un dictionnaire.
    Si la limite est atteinte, l'élément le moins récemment accédé
    ou ajouté est supprimé (Least Recently Used).
    """

    def __init__(self):
        """ Initialisation de la classe.
        Appelle le constructeur parent et initialise une liste pour
        suivre l'ordre d'utilisation des clés.
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Ajoute un élément dans le cache.
        Si la clé existe déjà, elle est mise à jour et marquée comme récente.
        Si le cache est plein, l'élément le moins utilisé est supprimé.
        Args:
            key: La clé pour l'élément.
            item: La valeur associée à la clé.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        # Insertion/Mise à jour
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Récupère un élément par sa clé.
        Si l'élément est trouvé, il est marqué comme récemment utilisé.
        Args:
            key: La clé à rechercher.
        Returns:
            La valeur associée, ou None si absente.
        """
        if key is not None and key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data.get(key)
        return None
