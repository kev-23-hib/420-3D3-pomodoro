import tkinter as tk
from observers.observer import Observateur


class BarreProgression(Observateur):

    def __init__(self, parent):
        self._canvas = tk.Canvas(parent, width=300, height=20, bg="white")
        self._canvas.pack(pady=10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant et duree_totale depuis sujet.get_donnees()
        temps_restant = self.get_donnes().get("temps_restant")
        duree_totale = self.get_donnes().get("duree_totale")
        # Calculez la largeur proportionnelle (300 * temps_restant / duree_totale)
        largeur = 300 * temps_restant / duree_totale if duree_totale > 0 else 0
        # Effacez le canvas et dessinez le rectangle
        self._canvas.delete("all")
        self._canvas.create_rectangle(0, 0, largeur, 20, fill="blue", outline="black")
