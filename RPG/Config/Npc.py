class NPC:
    def __init__(self, nome):
        self.nome = nome
        self.Falas = []
    
    def add_fala(self, fala):
        self.Falas.append(fala)
    
    def __repr__(self):
        return self.nome
    