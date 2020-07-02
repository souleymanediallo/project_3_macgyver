# Projet 3 : Aidez MacGyver à s'échapper !

Créer un jeu de labyrinthe en python dans lequel MacGyver aurait été enfermé. La sortie est surveillée par un garde du 
corps. MacGyver doit ramasser trois objets puis endormir le gardien et trouver la sortie.

## Fonctionnalités
- Dessiner le labyrinthe (départ, emplacement des murs, arrivée)
- Contrôler MacGyver par les touches directionnelles du clavier
- Répartir aléatoirement les objets dans le labyrinthe 
- Changer d’emplacement si l'utilisateur ferme le jeu et le relance.
- Afficher 15 sprites sur la longueur.
- Arrête le programme si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe
- Exécuté le programme sur n'importe quel ordinateur

## Programme
Les deux classes utilisées dans le programme sont stockées dans des fichiers différents. La class Labyrinth est la 
structure de mon jeu. La class MacGyver et ses méthodes permet de gérer le personnage principale.

Le fichier main.py contient le coeur de mon projet pour lancer mon jeu. On peut également retrouver le module pygame, 
l’import de mon fichier Labyrinth et les constantes. Ce fichier me permet de gérer les évenements de pygame.

## Contraintes
* Versionner le code en utilisant Git et le publier sur Github.
* Respecter les bonnes pratiques de la PEP 8 et développer dans un environnement virtuel utilisant Python 3
* Ecrire en anglais : nom des variables, commentaires, fonctions...

#### Plus d'info
* /usr/bin/venv python3
* coding : utf-8