# Graphic editor

## Introduction

Un éditeur graphique permet de maninupler des objets, que ce soit des images importées, des objets dessinés, ou du text écrit. Nous pouvons ainsi dessiner des formes aux épaisseurs et aux couleurs diverses et les supprimer; importer des images, manipuler leur position et leur rotation; placer du text pré-choisi aux coordonnées voulues. 


## Description

Notre editeur graphique:

- a une fenêtre aux dimensions réglables avec la souris
- jouer de la musique en arrière plan grace au module mixer
- permet d'importer des formes (rectangles, ellipses, et lignes) 
- permet à l'utilisateur la modification de l'épaisseur et de la couleur de celles-ci 
- permet à l'utilisateur de modifier la couleur de l'arrière plan
- permet d'importer des images
- permet à l'utilisateur de faire le déplacement et la rotation de celles-ci
- permet de créer du text à des coordonnées choisies
- permet la sauvegarde de l'éditeur si elle est voulue par l'utilisateur


## Interface

Voici l'interface par défaut, sans aucune modification

![](img/screenshot1.png)

A l'aide de notre éditeur, nous pouvons faire des images simples

![](img/screenshot2.png)

Ou des images plus complexes comme celle-ci

![](img/screenshot3.png)

ou bien même...

<img width="1414" alt="screenshot5" src="https://user-images.githubusercontent.com/77754959/111219230-1237a980-85d8-11eb-8782-f7890daf1e2e.png">


## Raccourcis claviers


#### Arrière-plan
- X change la couleur de l'arrière plan en Or
- C change la couleur de l'arrière plan en Cyan
- V change la couleur de l'arrière plan en Magenta
- N change la couleur de l'arrière plan en Noir
- W change la couleur de l'arrière plan en Blanc
- B change la couleur de l'arrière plan en Bleu


#### Formes
- R pour dessiner des rectangles
- E pour dessiner des ellipses
- L pour placer des points pour faire un polygone
- 1 pour une épaisseur de 1 sur la prochaine forme dessinée
- 2 pour une épaisseur de 3 sur la prochaine forme dessinée
- 7 couleur rouge 
- G couleur verte
- 8 couleur bleu

- ESC supprime la dernière forme déssinée

#### Image
- I pour importer une image (en précisant son emplacement et son extension)
- Y rotation à gauche (10 degrés)
- H rotation à droite (10 degrés)
- D déplace l'image
- Z agrandi l'image
- P diminue l'image
- F flip l'image de 180 degrés 
- ALT + F mirroire de l'image
- S arrête tous les mouvements
- ESC supprime la dernière image

#### Texte
- T demande le texte voulu et sa position (à écrire dans le terminal)

#### Sauvegarde 
- La sauvegarde se fait par l'écriture de "oui" ou de "non" à la fermeture du fichier

### il est évident que la mémorisation de tous ces raccourcis n'est pas possible lorsque le programme est en exécution, une page de menu est donc disponible pour tous les afficher dans le programme-même avec la touche M

![](img/screenshot4.png)




## Conclusion

L'éditeur graphique que nous avons créé est le fruit de nombreuses heures de travail en collaboration proche, et le résultat cherché a été obtenu: nous avons fait un programme qui nous permet de dessiner plus ou moins ce que nous voulions.

