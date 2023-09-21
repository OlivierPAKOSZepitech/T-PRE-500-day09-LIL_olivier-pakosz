from random import choice
from unidecode import unidecode
import datetime

# permet de selectionner un mot dans la base de données mots.txt
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
    while True:
        user_input = input("Choisissez une lettre à deviner ").strip().upper()
        if user_input and len(user_input) == 1 and user_input.isalpha():
            return user_input
        elif user_input == word:
            return user_input
        else:
            print("Veuillez entrer une lettre valide.")



# Défini si une lettre est présente dans le mot
def presence_lettre(lettre, word):
    if lettre in word:
        return True
    return False

# Permet d'afficher le score de l'utilisateur
def afficher_score(score):
    return print(f"Vous avez un score de {score}!")

def play():
    jeuFini = False
    nombre_essai_maximal = 10
    score = 0

    while not jeuFini and nombre_essai_maximal > 0:
        lettre = letter()
        lettrePresenteDansLeMot = presence_lettre(lettre, word)
        if lettre == word:
            jeuFini = True
            score = int(len(word)) - score + 10
            print(f"Wow ! Tu as trouvé {word}! Tu es vraiment fort")
            afficher_score(score)
            break

        if lettrePresenteDansLeMot:
            score +=1
            afficher_score(score)
        else: 
            nombre_essai_maximal -= 1
            if score == 0:
                score == 0
            else: score -= 1
            afficher_score(score)
            print("\n" f"Il vous reste {nombre_essai_maximal} essais")
        afficher_underscore(lettre, word)

        if "_" not in mot_devine or lettre == word:
                jeuFini = True
                print('Bravo ! tu as trouvé ', word)
                afficher_score(score)
                meilleur_score(score)
                break 
    if not jeuFini: print(f"Vous avez perdu. Le mot était {word}")
        

        
play()

