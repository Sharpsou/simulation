import tkinter as tk
import random
from config import *
import math

class Radar:
    def __init__(self, agent, detection_range, known_obstacles):
        self.agent = agent
        self.detection_range = detection_range
        self.known_obstacles = known_obstacles

    def scan(self, env, num_sectors=4):
        # Fonction de scan vide, à remplir plus tard
        return [random.random() for _ in range(17)]  # Données aléatoires pour simuler le radar


class Agent:
    def __init__(self, x, y, agent_type, env, detection_range, vitesse, energie_init, energie_deplacement, energie_repos, energie_gain):
        self.x = x
        self.y = y
        self.agent_type = agent_type
        self.env = env
        self.radar = Radar(self, detection_range, env.obstacles)
        self.vitesse = vitesse
        self.energie = energie_init
        self.energie_deplacement = energie_deplacement
        self.energie_repos = energie_repos
        self.energie_gain = energie_gain
        self.energie_init = energie_init
        self.tours_pres_nourriture = 0

    def decide(self, radar_data):
        # Décision aléatoire
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        return dx, dy

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            target = self.env.grid[new_x][new_y]
            if isinstance(self, Chasseur) and isinstance(target, Proie):
                target.energie = 0
                self.env.remove_agent(target)
                self.energie = self.energie_init
                return True
            elif target == ' ':
                self.env.grid[self.x][self.y] = ' '
                self.x, self.y = new_x, new_y
                self.env.grid[self.x][self.y] = self
                return True
        return False

    def check_nourriture(self):
        # Vérifier nourriture à proximité, comportement simplifié
        pass

    def update(self):
        if self.energie == 0:
            self.env.remove_agent(self)
            return
        radar_data = self.radar.scan(self.env)
        dx, dy = self.decide(radar_data)
        if self.move(dx, dy):
            self.energie -= self.energie_deplacement
        else:
            self.energie -= self.energie_repos
        if self.energie < 0:
            self.energie = 0
        self.check_nourriture()

class Chasseur(Agent):
    def __init__(self, x, y, env):
        super().__init__(x, y, 'C', env, detection_range=DETECT_CHASSEUR, vitesse=VITESSE_CHASSEUR,
                         energie_init=ENERGIE_INITIALE_CHASSEUR, energie_deplacement=ENERGIE_DEPLACEMENT_CHASSEUR,
                         energie_repos=ENERGIE_REPOS_CHASSEUR, energie_gain=ENERGIE_GAIN_CHASSEUR)

class Proie(Agent):
    def __init__(self, x, y, env):
        super().__init__(x, y, 'P', env, detection_range=DETECT_PROIE, vitesse=VITESSE_PROIE,
                         energie_init=ENERGIE_INITIALE_PROIE, energie_deplacement=ENERGIE_DEPLACEMENT_PROIE,
                         energie_repos=ENERGIE_REPOS_PROIE, energie_gain=ENERGIE_GAIN_PROIE)

class Environnement:
    def __init__(self):
        self.grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.agents = []
        self.obstacles = []
        self.reproduction_counter_proie = 0
        self.reproduction_counter_chasseur = 0
        self.place_items('N', NUM_FOOD)
        self.place_items('O', NUM_OBSTACLES)

    def place_items(self, item_type, count):
        for _ in range(count):
            while True:
                x = random.randint(0, GRID_SIZE - 1)
                y = random.randint(0, GRID_SIZE - 1)
                if self.grid[x][y] == ' ':
                    self.grid[x][y] = item_type
                    if item_type == 'O':
                        self.obstacles.append((x, y))
                    break

    def add_agent(self, agent):
        self.agents.append(agent)
        self.grid[agent.x][agent.y] = agent

    def remove_agent(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)
            self.grid[agent.x][agent.y] = ' '

    def update(self):
        for agent in self.agents[:]:
            agent.update()

    def reproduction(self, agent_type):
        # Fonction de reproduction vide, à remplir plus tard
        pass

    def max_energie(self, agent_type):
        """
        Retourne l'énergie maximale d'un agent en fonction de son type.
        """
        if agent_type == 'C':
            return ENERGIE_INITIALE_CHASSEUR
        elif agent_type == 'P':
            return ENERGIE_INITIALE_PROIE
        return 0

