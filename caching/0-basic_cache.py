#!/usr/bin/env python3
""" Module pour le système de mise en cache BasicCache.
Ce module définit une classe qui permet de stocker et de récupérer
des données dans un dictionnaire sans limite de taille.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Système de cache basique.
    Cette classe hérite de BaseCaching et permet d'ajouter des éléments
    dans un dictionnaire sans aucune restriction de limite (MAX_ITEMS).
    """

    def put(self, key, item):
        """ Ajoute un élément dans le cache.
        Si la clé ou l'item est None, la méthode ne fait rien.
        Args:
            key: La clé pour l'élément.
            item: La valeur associée à la clé.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Récupère un élément par sa clé.
        Args:
            key: La clé à rechercher.
        Returns:
            La valeur associée à la clé, ou None si la clé n'existe pas.
        """
        return self.cache_data.get(key)
