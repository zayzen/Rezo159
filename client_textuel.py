#!/usr/bin/python

from socket import *

#On commence par creer un socket et definir quelques options:
s = socket()
# SO_REUSEADDR autorise la reutilisation d'un port immediatement apres la fermeture du socket
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#connexion sur la machine 192.168.47.162 (uomobile.univ-orleans.fr) sur le port 6666
s.connect(('192.168.47.162', 6666))

#BONJOUR
#On envoie bonjour
s.send("bonjour\n")
#reponse
reponse = s.recv(1024).decode('utf-8')
#Traitement de la reponse.
print reponse

#On demande au joueur de saisir son nom
nom = raw_input("--- Nom du joueur: ")
#On envoie la commande joueur suivit du nom de joueur
s.send("joueur "+nom)

#On recoit le nom du joueur adverse
reponse = s.recv(1024).decode('utf-8')
#On affiche le nom du joueur adverse
l = reponse.split(' ')
print("--- L'adversaire s'appelle "+l[1])


#On demande la taille du tablier
tablier = input("--- Taille du tablier ")
s.send("tablier "+str(tablier))

#On recoit la taille du tablier choisie par l'adversaire
reponse = s.recv(1024).decode('utf-8')
print("--- L'adversaire choisi: "+reponse)

#On demande la case a jouer
joue = raw_input("--- Ou jouer : ")
s.send("joue "+joue)

#On recoit le coup de l'adversaire
reponse = s.recv(1024).decode('utf-8')
print("--- L'adversaire "+reponse)

#Au revoir
s.send("aurevoir")
print("aurevoir")

#Au revoir de l'adversaire
reponse = s.recv(1024).decode('utf-8')
print reponse
