
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:35:24 2022

@author: antoine
"""


import time
start_time = time.time()


import random as rd
import pandas as pd
import os
import math
import numpy as np

#%% Récupération des données

def lecture_fichier() :
    data = pd.read_csv("position_sample.csv",sep = ';',names = ['t','x','y'])
    list_x = data['x'].tolist()
    list_x_test = list_x[1:] # Liste prise à partir de 1 pour éviter la première ligne "x, y, t"
    print(list_x_test,"\n")
    
    list_y_test = data['y'].tolist()
    list_y_test = list_y_test[1:]
    print(list_y_test,"\n")
    
    list_t_test = data['t'].tolist()
    list_t_test = list_t_test[1:]
    print(list_t_test,"\n")
    

    return list_x_test,list_y_test,list_t_test


#%% Calcul de la Fitness


def fitness(p1,p2,p3,x2,list_t_test):
    total = 0
    for i in range(len(list_t_test)) : 
        x = p1 * math.sin(p2*float(list_t_test[i]) + p3) # Recherche de la valeur théorique
        total += abs(x-float(x2[i])) # Différence entre les valeurs théoriques et pratiques
    return total 

#%% Initialisation aléatoire

def init_gen1() :
    p1 = [0,0,0,0,0,0,0,0,0,0]
    for i in range (10):
         p1[i] = rd.randint(-100000,100000)/1000 # Créatoin de 10 nombre aléatoire entrte [-100, 100] avec une précision au millième
         
    p2 = [0,0,0,0,0,0,0,0,0,0]
    for i in range (10):
         p2[i] = rd.randint(-100000,100000)/1000
         
    p3 = [0,0,0,0,0,0,0,0,0,0]
    for i in range (10):
         p3[i] = rd.randint(-100000,100000)/1000
         
    p4 = [0,0,0,0,0,0,0,0,0,0]
    for i in range (10):
         p4[i] = rd.randint(-100000,100000)/1000
         
    p5 = [0,0,0,0,0,0,0,0,0,0]
    for i in range (10):
         p5[i] = rd.randint(-100000,100000)/1000
         
    p6 = [0,0,0,0,0,0,0,0,0,0]
    for i in range (10):
         p6[i] = rd.randint(-100000,100000)/1000
    print("FIRST GENERATION CREATED :\n\np1 = ", p1, "\np2 = ",p2, "\np3 = ",p3,"\np4 = ",p4,"\np5 = ", p5, "\np6 = ",p6,"\n")
    return p1,p2,p3,p4,p5,p6
     
#%% Tri de la génération (Recherche du meilleur)

def tri_gen(p1,p2,p3,p4,p5,p6) :
    tab_correspondance = [None] * 1000
    fitness_x = [None] * 1000
    fitness_y = [None] * 1000
    tab_correspondance_x = [None] * 1000
    tab_correspondance_y = [None] * 1000
    compteur = 0
    for i in p1 : 
        for j in p2 :
            for k in p3 :
                fitness_x[compteur] = round(fitness(i,j,k,list_x_test,list_t_test),4) #Création d'une liste avec toutes les fitness pour x
                tab_correspondance_x[compteur] = [i,j,k] #Création d'une liste avec toutes les combinaisons de p1, p2, p3
                compteur += 1
    compteur = 0
    for l in p4 : 
        for m in p5 : 
            for n in p6 :   
                fitness_y[compteur] = round(fitness(l,m,n,list_y_test,list_t_test),4)#Création d'une liste avec toutes les fitness pour y
                tab_correspondance_y[compteur] = [l,m,n] #Création d'une liste avec toutes les combinaisons de p4, p5, p6
                compteur += 1
    
    sorted_tab1 = np.sort(fitness_x)
    sorted_tab1 = sorted_tab1[0:3] # Tri et récupération des meilleurs fitness en x
    sorted_tab2 = np.sort(fitness_y)
    sorted_tab2 = sorted_tab2[0:3] # Tri et récupération des meilleurs fitness en y
    sorted_tab = list(map(lambda x,y : round(x+y,4),sorted_tab1,sorted_tab2)) # Addition triée des meilleures fitness en x et en y 
    index_x = fitness_x.index(sorted_tab1[0]) #Recherche de l'indice de la meilleure combinaison en x
    index_y = fitness_y.index(sorted_tab2[0]) #Recherche de l'indice de la meilleure combinaison en y
    tab_correspondance = tab_correspondance_x[index_x] + tab_correspondance_y[index_y] # Concaténation de la meilleure combinaison en x et en y
                            
    print ("BEST FITNESS VALUES : ",sorted_tab)
    return sorted_tab,tab_correspondance


#%% Création d'une nouvelle génération (avec croisement et mutation)
        
def new_generation(compt,tab_correspondance,sorted_tab,p1,p2,p3,p4,p5,p6):
    fils1 = tab_correspondance
    f1, f2, f3, f4, f5, f6 = [],[],[],[],[],[]
    
    f1.append(fils1[0]) #Ajout du p1 correspondant au meilleur fils (Croisement)
    for i in range (2):
        f1.append(round(rd.uniform(fils1[0]-5 if fils1[0]-5 > -100 else -100,fils1[0] + 5 if fils1[0] + 5 < 100 else 100),4)) # Ajout de 2 valeurs qui seront proches du meilleur fils (Mutation)
    for i in range(7) :
        f1.append(rd.randint(-100000,100000)/1000) # Autres valeurs aléatoires
    
    f2.append(fils1[1])    
    for i in range (2):
        f2.append(round(rd.uniform(fils1[1]-5 if fils1[1]-5 > -100 else -100,fils1[1] + 5 if fils1[1] + 5 < 100 else 100),4))
    for i in range(7) :
        f2.append(rd.randint(-100000,100000)/1000)
  
    f3.append(fils1[2])
    for i in range (2):
        f3.append(round(rd.uniform(fils1[2]-5 if fils1[2]-5 > -100 else -100,fils1[2] + 5 if fils1[2] + 5 < 100 else 100),4))
    for i in range(7) :
        f3.append(rd.randint(-100000,100000)/1000)


    f4.append(fils1[3])
    for i in range (2):
        f4.append(round(rd.uniform(fils1[3]-5 if fils1[3]-5 > -100 else -100,fils1[3] + 5 if fils1[3] + 5 < 100 else 100),4))
    for i in range(7) :
        f4.append(rd.randint(-100000,100000)/1000)


    f5.append(fils1[4])
    for i in range (2):
        f5.append(round(rd.uniform(fils1[4]-5 if fils1[4]-5 > -100 else -100,fils1[4] + 5 if fils1[4] + 5 < 100 else 100),4))
    for i in range(7) :
        f5.append(rd.randint(-100000,100000)/1000)


    f6.append(fils1[5])
    for i in range (2):
        f6.append(round(rd.uniform(fils1[5]-5 if fils1[5]-5 > -100 else -100,fils1[5] + 5 if fils1[5] + 5 < 100 else 100),4))
    for i in range(7) :
        f6.append(rd.randint(-100000,100000)/1000)
        
    print("\n\nGENERATION n°",compt,"CREATED :\n\np1 = ", f1, "\np2 = ",f2, "\np3 = ",f3,"\np4 = ",f4,"\np5 = ", f5, "\np6 = ",f6,"\n")
    return f1,f2,f3,f4,f5,f6





#%% PROGRAMME PRINCIPAL :

os.chdir(r"") #The path where you uploaded your files
list_x_test,list_y_test,list_t_test = lecture_fichier()
p1,p2,p3,p4,p5,p6 = init_gen1()
i = 2   
for j in range (59):#while True :
    sorted_tab,tab_correspondance = tri_gen(p1, p2, p3, p4, p5, p6)
    p1, p2, p3, p4, p5, p6 = new_generation(i,tab_correspondance,sorted_tab, p1, p2, p3, p4, p5, p6)
    i += 1
sorted_tab = tri_gen(p1, p2, p3, p4, p5, p6)
print("\nMeilleure combinaison trouvée sur",i-1,"générations :\nx(t) =",p1[0],"* sin (",p2[0],"* t +",p3[0],")\ny(t) =",p4[0],"* sin (",p5[0],"* t +",p6[0],")\n\n--- Temps d'execution : %s secondes ---" % round((time.time() - start_time),3))


#Best Value : -13.1989, 21.0983, -45.116, -22.9041, -41.101, 78.694 Fitness = 5.2973



