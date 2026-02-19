#!/usr/bin/env python3
""" Module pour le système de mise en cache FIFOCache.
Ce module définit une classe qui hérite de BaseCaching et gère
un cache avec l'algorithme de remplacement Premier Entré, Premier Sorti.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Système de cache FIFO.
    Cette classe permet de stocker des éléments dans un dictionnaire.
    Lorsque la limite est atteinte, l'élément le plus ancien est supprimé.
    """

    def __init__(self):
        """ Initialisation de la classe.
        Appelle le constructeur parent et initialise une liste pour
        suivre l'ordre d'insertion des clés.
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Ajoute un élément dans le cache.
        Si le cache dépasse MAX_ITEMS, supprime le premier élément inséré.
        Args:
            key: La clé pour l'élément.
            item: La valeur associée à la clé.
        """
        if key is None or item is None:
            return

        # Si la clé existe déjà, on la supprime de l'ordre pour la réinsérer
        # (optionnel selon l'interprétation, mais plus propre pour le suivi)
        if key in self.cache_data:
            self.keys_order.remove(key)

        self.cache_data[key] = item
        self.keys_order.append(key)

        # Vérification de la limite
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Récupération de la première clé insérée
            first_key = self.keys_order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Récupère un élément par sa clé.
        Args:
            key: La clé à rechercher.
        Returns:
            La valeur associée, ou None si la clé est absente ou None.
        """
        return self.cache_data.get(key)
