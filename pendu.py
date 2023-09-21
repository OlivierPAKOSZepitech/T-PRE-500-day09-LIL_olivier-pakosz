from random import choice
from unidecode import unidecode
import datetime


#Choisit un mot aléatoire dans la liste txt

def word_to_guess():
    f = open('mots.txt', 'r', encoding= 'utf8')
    contenu = f.readlines()
    return unidecode(choice(contenu).upper().replace('\n', '').strip())

word = word_to_guess()

mot_devine = ["_"] * len(word)

# Permet d'afficher le résultat

def afficher_underscore(lettre:str, word:str):
    for i in range(len(word)):
        if word[i] == lettre:
            mot_devine[i] = lettre
    print(" ".join(mot_devine))

# Recupère lettre utilisateur
def letter():
    return input("Choisissez une lettre à deviner ").upper() 


# Défini si une lettre est présente dans le mot
def presence_lettre(lettre, word):
    if lettre in word:
        return True
    return False

def play():
    isfinish = False
    nombre_essai_maximal = 10
    score = 0
    while not isfinish and nombre_essai_maximal > 0:
        lettre = letter()
        estPresent = presence_lettre(lettre, word)
        if estPresent and lettre.isalpha(): 
            score += +1
            if "_" not in mot_devine and lettre == word: #S'il n'y a plus de _ dans le mot, le jeu sea
                isfinish = True
                score += 5
                print('Bravo ! tu as trouvé ', word)
                print(afficher_score(score))
                meilleur_score(score)
                break 
        else: 
            nombre_essai_maximal -= 1
            score -= 1
            print("\n" f"Il vous reste {nombre_essai_maximal} essais")
        afficher_underscore(lettre, word)
        print(afficher_score(score))
    if not isfinish: print(f"Vous avez perdu. Le mot était {word}")

#Affiche le score de l'utilisateur
def afficher_score(score):
    return f"Vous avez un score de {score}!"

# Permet de trouver le meilleur score dans le fichier score.txt et de le remplacer dans le cas ou score > record
def meilleur_score(score):
    with open('score.txt', 'r', encoding='utf8') as g:
            contenu = g.read()
            record = int(contenu.strip())
    if score > record: 
        with open('score.txt', 'w', encoding= 'utf8') as g:
            g.write(str(score))
            nom_utilisateur = input(f"Best ever!!! You’ve guessed {word} in {10-nombre_essai} attempts. Quel est ton nom ? ")
            date_actuelle = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('score.txt', 'w', encoding='utf8') as score_file:
            score_file.write(f"Nom de l'utilisateur : {nom_utilisateur}\n")
            score_file.write(f"Score : {score}\n")
            score_file.write(f"Date : {date_actuelle}\n")

play()