# Définition des constantes
GRID_SIZE =25
CELL_SIZE = 15
NUM_FOOD = 7       # Nombre initial de nourriture
NUM_OBSTACLES = 0  # Nombre initial d'obstacles

NOMBRE_PROIE = 8
NOMBRE_CHASSEUR = 8
VITESSE_PROIE = 1
VITESSE_CHASSEUR = 1
DETECT_PROIE = 10
DETECT_CHASSEUR = 20
VITESSE_SIMU = 1  # Intervalle de mise à jour en millisecondes

# Constantes pour les Proies
ENERGIE_INITIALE_PROIE = 1500  # Energie initiale des proies
ENERGIE_DEPLACEMENT_PROIE = 4  # Energie consommée par un déplacement (proie)
ENERGIE_REPOS_PROIE = 2  # Energie consommée en restant immobile (proie)
ENERGIE_GAIN_PROIE = 5  # Energie regagnée par une proie près de la nourriture

# Constantes pour les Chasseurs
ENERGIE_INITIALE_CHASSEUR = 250  # Energie initiale des chasseurs
ENERGIE_DEPLACEMENT_CHASSEUR = 0  # Energie consommée par un déplacement (chasseur)
ENERGIE_REPOS_CHASSEUR = 3  # Energie consommée en restant immobile (chasseur)
ENERGIE_GAIN_CHASSEUR = 1  # Energie regagnée par un chasseur près de la nourriture
MUTATION_RATE = 0.01