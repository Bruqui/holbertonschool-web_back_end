#!/usr/bin/env python3
""" Module pour le système de mise en cache LFUCache.
Ce module définit une classe qui gère un cache basé sur la fréquence
d'utilisation la plus basse, avec une gestion LRU en cas d'égalité.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Système de cache LFU.
    Cette classe hérite de BaseCaching et implémente un algorithme
    où l'élément le moins fréquemment utilisé est supprimé en premier.
    """

    def __init__(self):
        """ Initialisation de la classe.
        Appelle le constructeur parent et initialise les dictionnaires
        de fréquences et l'ordre d'utilisation.
        """
        super().__init__()
        self.usage_counts = {}  # Stocke la fréquence {key: count}
        self.usage_order = []   # Stocke l'ordre d'utilisation pour le LRU

    def __update_meta(self, key):
        """ Méthode interne pour mettre à jour les métadonnées.
        Incrémente le compteur et déplace la clé à la fin de la liste LRU.
        """
        self.usage_counts[key] = self.usage_counts.get(key, 0) + 1
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def put(self, key, item):
        """ Ajoute un élément dans le cache.
        Si la limite est atteinte, supprime l'élément LFU (ou LRU si égalité).
        Args:
            key: La clé pour l'élément.
            item: La valeur associée.
        """
        if key is None or item is None:
            return

        # Si la clé existe déjà, on met juste à jour
        if key in self.cache_data:
            self.cache_data[key] = item
            self.__update_meta(key)
            return

        # Si le cache est plein
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Trouver la fréquence minimale
            min_freq = min(self.usage_counts.values())
            # Filtrer les clés qui ont cette fréquence minimale
            potential_discards = [k for k, v in self.usage_counts.items()
                                  if v == min_freq]

            # Si plusieurs candidats, on applique le LRU (le premier dans l'ordre)
            discard_key = None
            for k in self.usage_order:
                if k in potential_discards:
                    discard_key = k
                    break

            # Suppression
            del self.cache_data[discard_key]
            del self.usage_counts[discard_key]
            self.usage_order.remove(discard_key)
            print("DISCARD: {}".format(discard_key))

        # Insertion du nouvel élément
        self.cache_data[key] = item
        self.usage_counts[key] = 1
        self.usage_order.append(key)

    def get(self, key):
        """ Récupère un élément par sa clé.
        Met à jour la fréquence et l'ordre LRU de la clé consultée.
        Args:
            key: La clé à rechercher.
        Returns:
            La valeur associée ou None.
        """
        if key is not None and key in self.cache_data:
            self.__update_meta(key)
            return self.cache_data.get(key)
        return None
