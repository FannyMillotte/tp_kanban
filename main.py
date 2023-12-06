# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:00:52 2023

"""
import locale
from datetime import datetime
from datetime import timedelta

locale.setlocale(locale.LC_TIME, 'fr-FR.utf8')

class Tache: 
    def __init__(self, index, description, duree, status):
        self.index = index
        self.description = description
        self.attribue_a = None
        self.duree = duree #jours
        self.date_creation = datetime.now().strftime("%d/%m/%Y")
        self.date_fin = self.get_date_fin()
        self.status = status
        
    def __str__(self):
        return f"Tache {self.index}: {self.description} créée le {self.date_creation} terminée le {self.date_fin} attribué à {self.attribue_a}" 
    
    def get_date_fin(self):
        date = datetime.strptime(self.date_creation, "%d/%m/%Y")
        date_fin = date + timedelta(days=self.duree)
        return date_fin.strftime("%d/%m/%Y")


class Kanban:
    
    def __init__(self, noms_colonnes):
        self.noms_colonnes = noms_colonnes
        self.taches = []
        self.color = (255,255,255)
        self.nombre_taches = 0
    
        
    def __str__(self):
        txt = str(self.noms_colonnes) + "\n\n"
        
        for i in range(0, len(self.taches)):
            for j in range(0, len(self.taches[i])):
                txt += str(self.taches[i][j]) + "  "
            txt += "\n"
        return txt
    
    def ajout_tache(self, description_tache):
        self.taches.append([Tache(self.nombre_taches + 1, 
                                  description_tache, 2, 
                                  self.noms_colonnes[0])])
        self.nombre_taches += 1
        
    def supprimer_tache(self, index_tache):
        for i in range(0, len(self.taches)):
            for j in range(0, len(self.taches[i])):
                if self.taches[i][j].index == index_tache:
                    self.taches[i].remove(self.taches[i][j])
                    return True
        return False
    
    def attribuer_tache(self, index_tache, utilisateur):
        for i in range(0, len(self.taches)):
            for j in range(0, len(self.taches[i])):
                if self.taches[i][j].index == index_tache:
                    self.taches[i][j].attribue_a = utilisateur
        

colonnes = ["To Do", "In Progress", "Done"]
kanban = Kanban(colonnes)

kanban.ajout_tache("Nouvelle tache")
kanban.ajout_tache("Nouvelle tache 2")
print(kanban)

kanban.supprimer_tache(2)
print(kanban)

kanban.attribuer_tache(1, "Toto")
print(kanban)

            