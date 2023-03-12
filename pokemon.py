import random

class Pokemon:
    
    def __init__(self, pokemon_nom, pokemon_adversaire, pv, niveau, attaque, defense, type=None, faiblesses=None, resistances=None):
        
        self.pokemon_adversaire = pokemon_adversaire
        self.pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense
        self.type = type
        self.faiblesses = faiblesses or []
        self.resistances = resistances or []
        self.pokemon_nom = pokemon_nom

    

class Normal(Pokemon):
    def __init__(self, pokemon_nom):
        super().__init__(pokemon_nom, pv=100, niveau=1, attaque=1, defense=1, type="Normal")

class Feu(Pokemon):
    def __init__(self, pokemon_nom):
        super().__init__(pokemon_nom, pv=100, niveau=1, attaque=1.5, defense=1.5, type="Feu")

class Eau(Pokemon):
    def __init__(self, pokemon_nom):
        super().__init__(pokemon_nom, pv=100, niveau=1, attaque=1.5, defense=1.5, type="Eau")

class Electrik(Pokemon):
    def __init__(self, pokemon_nom):
        super().__init__(pokemon_nom, pv=100, niveau=1, attaque=2, defense=1.5, type="Electrik")

class Herbe(Pokemon):
    def __init__(self, pokemon_nom):
        super().__init__(pokemon_nom, pv=100, niveau=1, attaque=1, defense=1, type="Herbe")

class Glace(Pokemon):
    def __init__(self, pokemon_nom):
        super().__init__(pokemon_nom, pv=100, niveau=1, attaque=1.2, defense=1.5, type="Glace")

class Poison(Pokemon):
    def __init__(self, pokemon_nom, pokemon_adversaire):
        super().__init__(pokemon_nom, pokemon_adversaire, pv=100, niveau=1, attaque=1.2, defense=1)
        self.type = "Poison"

class Terre(Pokemon):
    def __init__(self, pokemon_nom, pokemon_adversaire):
        super().__init__(pokemon_nom, pokemon_adversaire, pv=100, niveau=1, attaque=1.3, defense=1.3)
        self.type = "Terre"

class Volant(Pokemon):
    def __init__(self, pokemon_nom, pokemon_adversaire):
        super().__init__(pokemon_nom, pokemon_adversaire, pv=120, niveau=3, attaque=2, defense=1)
        self.type = "Volant"

class Psychique(Pokemon):
    def __init__(self, pokemon_nom, pokemon_adversaire):
        super().__init__(pokemon_nom, pokemon_adversaire, pv=120, niveau=2, attaque=1.7, defense=1.7)
        self.type = "Psychique"

class Joueur:
    def __init__(self, nom_joueur, niveau, pokemon):
        self.nom_joueur = nom_joueur
        self.niveau = niveau
        self.pokemon = pokemon

class Combat:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.degats = 0  # initialiser la valeur de degats à 0

    def attaque(self, attaquant, defenseur):
        # Calcul des dégâts
        if attaquant.type in defenseur.faiblesses:
            self.degats = 2 * attaquant.attaque - defenseur.defense
        elif attaquant.type in defenseur.resistances:
            self.degats = 0.5 * attaquant.attaque - defenseur.defense
        else:
            self.degats = attaquant.attaque - defenseur.defense
        self.degats = max(1, self.degats)  # Les dégâts infligés sont toujours d'au moins 1 PV

        # Réduction des PV du défenseur
        defenseur.pv -= self.degats

        # Affichage du résultat de l'attaque
        print(f"{attaquant.pokemon_nom} attaque {defenseur.pokemon_nom} et lui inflige {self.degats} PV de dégâts.")
        if defenseur.pv <= 0:
            print(f"{defenseur.pokemon_nom} est K.O. !")

    def tour(self):
        # Le joueur 1 attaque le joueur 2
        print(f"{self.joueur1.nom_joueur} envoie {self.joueur1.pokemon.pokemon_nom} en combat !")
        self.attaque(self.joueur1.pokemon, self.joueur2.pokemon)
        if self.joueur2.pokemon.pv <= 0:
            print(f"{self.joueur2.nom_joueur} perd le combat.")
            return

        print(f"{self.joueur2.nom_joueur} envoie {self.joueur2.pokemon.pokemon_nom} en combat !")
        self.attaque(self.joueur2.pokemon, self.joueur1.pokemon)
        if self.joueur1.pokemon.pv <= 0:
            print(f"{self.joueur1.nom_joueur} perd le combat.")
            return

        # Le combat continue si les deux Pokémon sont encore en vie
        print(f"Il reste {self.joueur1.pokemon.pv} PV à {self.joueur1.pokemon.pokemon_nom} et {self.joueur2.pokemon.pv} PV à {self.joueur2.pokemon.pokemon_nom}.")

class Joueur:
    def __init__(self, joueur_ennemi, joueur_nom):
        self.pokemon = None
        self.joueur_nom = joueur_nom
        self.joueur_ennemi = joueur_ennemi
        joueur_ennemi = random.choice(["Jean", "Marie", "Lucie", "Pierre", "Sophie", "Bob", "Charlie"])

    
    def choisir_pokemon(self, pokemon):
        self.pokemon = pokemon
        print(f"{self.nom} a choisi {pokemon.nom} !")
    
    def attaquer(self, joueur, adversaire):

        combat = Combat(self, adversaire)
        combat.tour()


liste_pokemon = ['Pikachu', 'Salameche', 'Bulbizarre', 'Carapuce', 'Rondoudou', 'Aspicot', 'Rattata', 'Piafabec', 'Abo', 'Papilusion', 'Dracaufeu', 'Tortank', 'Florizarre']
print(*liste_pokemon)
pokemon_nom = input("Choisissez un Pokemon dans la liste: ")
joueur = Joueur()
pokemon = Pokemon()

if pokemon_nom in liste_pokemon:
    #pokemon_nom = Pokemon(pokemon_nom)

    print(f"Vous avez choisi {pokemon_nom}!")
    print(f"Vouler vous combatre {joueur.joueur_ennemi()} avec votre {pokemon_nom}?")
else:
    print("Ce Pokemon n'est pas dans la liste.")


def se_defendre(self):
    print(f"{pokemon_nom} se défend.")

print("Le combat commence !")

while True:
    joueur.joueur_nom().attaquer(joueur.joueur_ennemi())
    print(f"{pokemon.pokemon_nom} attaque {pokemon.pokemon_adversaire} !")
    joueur.pokemon.pv -= combat.degats
    print(f"Il reste {pokemon.pokemon_adversaire.pv} points de vie à {pokemon.pokemon_adversaire()} !")
    if joueur.pokemon.points_de_vie <= 0:
        print(f"{joueur.pokemon.nom} est K.O. !")

    if joueur.joueur_ennemi().pokemon.pv <= 0:
        print(f"{joueur.joueur_ennemi()} n'a plus de Pokémon ! {joueur.joueur_nom()} a gagné le combat !")
        break
    
    joueur.joueur_ennemi().attaquer(joueur.joueur_nom())
    if joueur.joueur_nom.pokemon.pv <= 0:
        print(f"{joueur.joueur_nom()} n'a plus de Pokémon ! {joueur.joueur_ennemi()} a gagné le combat !")
        break
