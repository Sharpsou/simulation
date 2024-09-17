import numpy as np
import random
import math

# Classe pour la couche Fully-Connected
class CoucheCachee:
    def __init__(self, nombre_neurones: int, nombre_entrees: int):
        """
        Initialise une couche fully-connected avec un certain nombre de neurones et de connexions en entrée.
        """
        self.neurones = [Neurone() for _ in range(nombre_neurones)]
        self.poids = [[random.uniform(-1, 1) for _ in range(nombre_entrees)] for _ in range(nombre_neurones)]
    
    def calculer_sorties(self, entrees):
        """
        Calcule les sorties de la couche Fully-Connected. 
        Fonction actuellement vide, à compléter plus tard.
        """
        return [random.random() for _ in self.neurones]  # Sorties aléatoires pour simuler un comportement


# Classe pour les neurones classiques
class Neurone:
    def __init__(self, activation: str = "tanh"):
        self.activation = activation
    
    def activation_function(self, x: float) -> float:
        """
        Fonction d'activation vide pour l'instant.
        """
        return random.random()  # Valeur aléatoire pour simuler une activation


# Classe pour une couche GRU (non utilisée actuellement)
class GRU:
    def __init__(self, nombre_neurones: int, nombre_entrees: int):
        """
        Initialisation du GRU avec le nombre de neurones et le nombre d'entrées.
        Actuellement, cette classe est vide.
        """
        self.h_t = np.zeros((nombre_neurones,))

    def calculer_sorties(self, x_t):
        """
        Calcule les sorties de la couche GRU.
        Fonction vide à remplir plus tard.
        """
        return np.random.rand(self.h_t.shape[0])  # Retourne des valeurs aléatoires


# Classe du réseau neuronal général
class IA:
    def __init__(self, nombre_entrees: int, configuration_couches_cachees, nombre_sorties: int):
        """
        Initialise le réseau neuronal avec une entrée, des couches cachées et une sortie.
        Actuellement, la logique de création des couches est vide.
        """
        self.couches_cachees = []
        self.weights = []  # Ajout d'un attribut pour stocker les poids
        nombre_entrees_actuel = nombre_entrees

        # Création des couches cachées
        for nombre_neurones in configuration_couches_cachees:
            if nombre_neurones < 0:
                couche = GRU(abs(nombre_neurones), nombre_entrees_actuel)
            else:
                couche = CoucheCachee(nombre_neurones, nombre_entrees_actuel)
                self.weights.append(couche.poids)
            
            self.couches_cachees.append(couche)
            nombre_entrees_actuel = abs(nombre_neurones)
        
        # Création de la couche de sortie
        self.couche_sortie = CoucheCachee(nombre_sorties, nombre_entrees_actuel)
        self.weights.append(self.couche_sortie.poids)

    def forward(self, entrees):
        """
        Effectue la propagation avant à travers toutes les couches du réseau.
        Actuellement, retourne des sorties aléatoires.
        """
        activations = entrees  # Les entrées deviennent les premières activations

        for couche in self.couches_cachees:
            activations = couche.calculer_sorties(activations)

        sorties = self.couche_sortie.calculer_sorties(activations)
        return sorties  # Valeurs aléatoires pour simuler les sorties du réseau
