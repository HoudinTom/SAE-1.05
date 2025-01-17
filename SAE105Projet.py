import csv
import os
import numpy
from pylab import *
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

liste_fichier_pluie = []
liste_fichier_tempmax = []
liste_fichier_tempmin = []
dico_pluie = {}
dico_temp_max = {}
dico_temp_min = {}
liste_annee = [ 1951 + i for i in range(72)]
dico_pluie_moy_an = {}
dico_temp_max_an = {}
dico_temp_min_an = {}
liste_pluie = []
liste_temp_max = []
liste_temp_min = []

#modifier le chemin  et le remplacer par l'emplacement ou vous avez télécherger les fichier du github
emplacement_ou_vous_avez_télécharger_le_github = "/home/Etudiants/RT/BUT-RT-1/th157449/python/SAE105Projet"
# Pour moi c'étais /home/Etudiants/RT/BUT-RT-1/th157449/python/SAE105Projet

#ici on récupère les données de chaque fichier csv pour avoir le nom de chacun des fichiers csv qui a les températures et pluviométrie pour une commune de France 

with open(emplacement_ou_vous_avez_télécharger_le_github + "/fichier_donne/Liste_hauteur_pluie.csv",newline = "") as csvfile:
	data1 = csv.reader(csvfile,delimiter = ';')
	t = csvfile.readline()
	for val1 in data1:
		liste_fichier_pluie.append(val1[0])
		
with open(emplacement_ou_vous_avez_télécharger_le_github + "/fichier_donne/Liste_temp_max.csv",newline = "") as csvfile:
	data2 = csv.reader(csvfile,delimiter = ';')
	t = csvfile.readline()
	for val2 in data2:
		liste_fichier_tempmax.append(val2[0])
		
with open(emplacement_ou_vous_avez_télécharger_le_github + "/fichier_donne/Liste_temp_min.csv",newline = "") as csvfile:
	data3 = csv.reader(csvfile,delimiter = ';')
	t = csvfile.readline()
	for val3 in data3:
		liste_fichier_tempmin.append(val3[0])

#Après avec les données récupéré précédemment on peux parcourir chaque fichier et stocké toutes les données de températures et pluviométries par mois

for nfic1 in liste_fichier_pluie:
	with open(((emplacement_ou_vous_avez_télécharger_le_github + "/SH_RR_metropole/" + str(nfic1))),newline = "") as csvfile:
		datatemp1 = csv.reader(csvfile,delimiter = ';')
		for valtemp1 in datatemp1:
			if valtemp1[0][0] != "#":
				if  valtemp1[1] != 'VALEUR':
					if valtemp1[1] != "":
						float_temp1 = float(valtemp1[1])
						if valtemp1[0] not in dico_pluie:
							dico_pluie[valtemp1[0]] = float_temp1
						else:
							dico_pluie[valtemp1[0]] += float_temp1
	
for nfic2 in liste_fichier_tempmax:
	with open(((emplacement_ou_vous_avez_télécharger_le_github + "/SH_TN_metropole/" + str(nfic2))),newline = "") as csvfile:
		datatemp2 = csv.reader(csvfile,delimiter = ';')
		for valtemp2 in datatemp2:
			if valtemp2[0][0] != "#":
				if  valtemp2[1] != "VALEUR":
					if valtemp2[1] != "":
						float_temp2 = float(valtemp2[1])
					if valtemp2[0] not in dico_temp_max:
						dico_temp_max[valtemp2[0]] = float_temp2
					else:
						dico_temp_max[valtemp2[0]] += float_temp2
				
for nfic3 in liste_fichier_tempmin:
	with open(((emplacement_ou_vous_avez_télécharger_le_github + "/SH_TX_metropole/" + str(nfic3))),newline = "") as csvfile:
		datatemp3 = csv.reader(csvfile,delimiter = ';')
		for valtemp3 in datatemp3:
			if valtemp3[0][0] != "#":
				if  valtemp3[1] != "VALEUR":
					if valtemp3[1] != "":
						float_temp3 = float(valtemp3[1])
						if valtemp3[0] not in dico_temp_min:
							dico_temp_min[valtemp3[0]] = float_temp3
						else:
							dico_temp_min[valtemp3[0]] += float_temp3
							
#On fait la moyenne des données précédemment stocké

longueur1 = len(liste_fichier_pluie)					
for v1 in dico_pluie:
	moy = dico_pluie[v1] / longueur1
	dico_pluie[v1] = moy
	
longueur2 = len(liste_fichier_tempmax)	
for v2 in dico_temp_max:
	moy = dico_temp_max[v2] / longueur2
	dico_temp_max[v2] = moy

longueur3 = len(liste_fichier_tempmin)	
for v3 in dico_temp_min:
	moy = dico_temp_min[v3] / longueur3
	dico_temp_min[v3] = moy
	
#On met toutes les données stocké en années

for v4 in dico_pluie:
	if v4[:4] not in dico_pluie_moy_an:
		dico_pluie_moy_an[v4[:4]] = dico_pluie[v4]
	else:
		dico_pluie_moy_an[v4[:4]] += dico_pluie[v4]
		
for v5 in dico_temp_max:
	if v5[:4] not in dico_temp_max_an:
		dico_temp_max_an[v5[:4]] = dico_temp_max[v5]
	else:
		dico_temp_max_an[v5[:4]] += dico_temp_max[v5]
		
for v6 in dico_temp_min:
	if v6[:4] not in dico_temp_min_an:
		dico_temp_min_an[v6[:4]] = dico_temp_min[v6]
	else:
		dico_temp_min_an[v6[:4]] = dico_temp_min[v6]
		
#Et on fait la moyenne des données stocké par année
		
for v7 in dico_pluie_moy_an:
	if int(v7) >= 1951:
		moy = dico_pluie_moy_an[v7] / 12
		dico_pluie_moy_an[v7] = moy
		liste_pluie.append(moy)
	
for v8 in dico_temp_max_an:
	moy = dico_temp_max_an[v8] / 12
	dico_temp_max_an[v8] = moy
	liste_temp_max.append(moy)
	
for v9 in dico_temp_min_an:
	moy = dico_temp_min_an[v9] / 12
	dico_temp_min_an[v9] = moy
	liste_temp_min.append(moy)

print(liste_pluie)
print(liste_temp_max)
print(liste_temp_min)

#On définie les fonction pour afficher les données traité

def activation1():
	plt.figure(figsize=(8, 6))

	x = liste_annee
	y = liste_pluie

    # Tracé de la courbe
	plt.plot(x, y, label="Courbe quadratique", color='blue', marker='o')

    # Ajout des titres et des labels
	plt.title("Evolution de la pluviométrie en fonction des années en France")
	plt.xlabel("Année")
	plt.ylabel("Hauteur de pluie en milimètre")

    # Ajout d'une légende
	plt.legend()
	plt.show()

def activation2():
	plt.figure(figsize=(8, 6))

	x = liste_annee
	y = liste_temp_max

    # Tracé de la courbe
	plt.plot(x, y, label="Courbe quadratique", color='blue', marker='o')

    # Ajout des titres et des labels
	plt.title("Evolution des température maximal en fonction des années en France")
	plt.xlabel("Annee")
	plt.ylabel("Température maximal en degré Celsius")

    # Ajout d'une légende
	plt.legend()
	plt.show()
	
def activation3():
	plt.figure(figsize=(8, 6))

	x = liste_annee
	y = liste_temp_min

    # Tracé de la courbe
	plt.plot(x, y, label="Courbe quadratique", color='blue', marker='o')

    # Ajout des titres et des labels
	plt.title("Evolution des température minimal en fonction des années en France")
	plt.xlabel("Année")
	plt.ylabel("Température minimal en degré Celsius")

    # Ajout d'une légende
	plt.legend()
	plt.show()
	
#On fait une fenêtre Tkinter pour regrouper les fonction faites précédemment et pour pouvoir les lancer

fenetre= tk.Tk()

fenetre.geometry("1200x500")
fenetre.title("Saé traitée les donnée Gui")

#on donne un nom a la fenêtre

texte= tk.Label(fenetre,text="Choisissez une courbe a afficher pour connaître l'avancer du rechauffement climatique",font=('Arial',18))
texte.pack(padx=20, pady=20)

#on crée 3 boutons

bouttonframe= tk.Frame(fenetre)
bouttonframe.columnconfigure(0,weight=10)
bouttonframe.columnconfigure(1,weight=10)
bouttonframe.columnconfigure(2,weight=10)

#on attribue la fonction de afficher les courbe on les nommes on leur donnes des couleurs.

btn1=tk.Button(bouttonframe,text="avancer des temperatures maximal",font=('Arial'),bg='red',fg='white',command=activation2)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2=tk.Button(bouttonframe,text="Pluviometrie",font=('Arial'),fg='blue',command=activation1)
btn2.grid(row=1, column=0, sticky=tk.W+tk.E)

btn3=tk.Button(bouttonframe,text="avancer des temperatures minimal",font=('Arial'),bg='blue',fg='white',command=activation3)
btn3.grid(row=2, column=0, sticky=tk.W+tk.E)

#pour afficher la fenêtre et les boutons

bouttonframe.pack()

fenetre.mainloop()
