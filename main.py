# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:00:52 2023

"""
from datetime import datetime
from datetime import timedelta

class Tache: 
    def __init__(self, index, description, duree, status):
        self.index = index
        self.description = description
        self.attribue_a = None
        self.duree = duree #jours
        self.date_creation = datetime.now().strftime("%m/%d/%Y")
        self.status = status
        
    def __str__(self):
        return f"Tache {self.index}: {self.description} créée le {self.date_creation} terminée le " 
    
    def get_date_fin(self):
        date = datetime.strptime(self.date_creation, "%m/%d/%Y")
        date_fin = date + timedelta(days=self.duree)
        return date_fin.strftime("%m/%d/%Y")


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
                #if self.taches[i][j] != None:
                txt += str(self.taches[i][j]) + "  "
            txt += "\n"
        return txt
    
    def ajout_tache(self, description_tache):
        self.taches.append([Tache(self.nombre_taches + 1, 
                                  description_tache, 2, 
                                  self.noms_colonnes[0])])
        
        

colonnes = ["To Do", "In Progress", "Done"]
kanban = Kanban(colonnes)
            
print(kanban)

kanban.ajout_tache("Nouvelle tache")
kanban.ajout_tache("Nouvelle tache 2")
print(kanban)
            