class Pokemon:
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense

    def attaquer(self, adversaire):
        degats = self.attaque - adversaire.defense
        if degats > 0:
            adversaire.pv -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} dégâts.")
        
    def se_defendre(self):
        self.defense += 5
        print(f"{self.nom} se défend et sa défense augmente de 5.")


class Type:
    def __init__(self, nom, faiblesses, resistances):
        self.faiblesses = faiblesses
        self.resistances = resistances


class Normal(Type, Pokemon):
    def __init__(self):
        super().__init__("Normal", ["Combat"], [])
        

class Feu(Type, Pokemon):
    def __init__(self):
        super().__init__("Feu", ["Eau", "Roche", "Sol"], ["Feu", "Herbe", "Glace"])



class Eau(Type, Pokemon):
    def __init__(self):
        super().__init__("Eau", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])


class Electrik(Type, Pokemon):
    def __init__(self):
        super().__init__("Electrik", ["Eau", "Sol"], ["Feu", "Electrik", "Glace"])

class Herbe(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Glace(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Combat(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Poison(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Sol(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Volant(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Psychique(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class coccinelle(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Roche(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class Fantome(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class dragon(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class obscur(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class fer(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

class fee(Type, Pokemon):
    def __init__(self):
        super().__init__("Herbe", ["Electrik", "Herbe"], ["Feu", "Eau", "Glace"])

pikachu = Pokemon("Pikachu", pv=90, niveau=5, attaque=25, defense=10, type=Electrik())
charmander = Pokemon("Charmander", pv=80, niveau=5, attaque=30, defense=5, type=Feu())

print(pikachu.type.nom)  # Output : Electrik
print(charmander.type.faiblesses)  # Output : ['Eau', 'Roche', 'Sol']