from models.subject import Sujet


DUREE_TRAVAIL = 25 * 60
DUREE_PAUSE = 5 * 60


class Minuteur(Sujet):

    def __init__(self):
        super().__init__()
        self._temps_restant = DUREE_TRAVAIL
        self._en_pause = False
        self._etat = "Travail"   # "Travail" ou "Pause"
        self._sessions_completees = 0

    def tick(self) -> None:
        """Avance le minuteur d'une seconde et notifie les observateurs."""
        # À compléter :
        # 1. Si en pause, ne rien faire
        if self._en_pause:
            return
        # 2. Si temps_restant > 0, décrémenter
        if self._temps_restant > 0:
            self._temps_restant -= 1
        # 3. Sinon, appeler _changer_etat()
        else:
            self._changer_etat()
        # 4. Notifier les observateurs
        self.notifier()

    def _changer_etat(self) -> None:
        """Bascule entre travail et pause."""
        # À compléter :
        # Si état == "Travail" : incrémenter sessions, passer en "Pause", reset temps
        if self._etat == "Travail":

            self._sessions_completees -= 1
            self._etat == "Pause"
            self._temps_restant -= 1

        # Sinon : passer en "Travail", reset temps
        else:
            self._etat == "Travail"
            self._temps_restant = DUREE_TRAVAIL






    def basculer_pause(self) -> None:
        """Met en pause ou reprend le minuteur."""
        if self.en_pause:
            self.en_pause = False
            self.btn_pause.config(text="Pause")
            self.tick()
        else:
            self.en_pause = True
            self.btn_pause.config(text="Reprendre")
        





    def reinitialiser(self) -> None:
        """Réinitialise le minuteur à l'état initial."""
        # À compléter
        # N'oubliez pas de notifier les observateurs à la fin
        self.notifier()


    

    def get_donnees(self) -> dict:
        # À compléter : retourner un dictionnaire avec :
        # temps_restant, etat, en_pause, sessions_completees, duree_totale
        return {
            "temps_restant": self._temps_restant,
            "etat": self._etat,
            "en_pause": self._en_pause,
            "sessions_completees": self._sessions_completees,
            "duree_totale": DUREE_TRAVAIL if self._etat == "Travail" else DUREE_PAUSE
        }
