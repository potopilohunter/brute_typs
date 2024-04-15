import time

print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ \n
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌         \n
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀       ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀          \n
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                   \n
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄          \n
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌               ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌         \n
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌     ▐░▌               ▐░▌      ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌         \n
▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌               ▐░▌          ▐░▌     ▐░▌                    ▐░▌         \n
▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌               ▐░▌          ▐░▌     ▐░▌           ▄▄▄▄▄▄▄▄▄█░▌         \n
▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌               ▐░▌          ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌         \n
 ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀                 ▀            ▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀          \n """)         

liste = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

mot = input("Entrer votre mot de passe : ")
if len(mot) > 6:
    print("Le mot de passe doit faire moins de 7 lettres.")
    exit()

chaine = str()

def test(chaine, mot, compteur):
    print(chaine, end='\r')  # Affiche la chaîne en cours
    if chaine == mot:
        print("\nLe mot de passe est :", mot)
        print(f"Nombre de combinaisons testées : {compteur}")
        exit()

mot_trouve = False
compteur = 0
start_time = time.time()

for l in liste:
    chaine = l
    compteur += 1
    test(chaine, mot, compteur)
        
    for l2 in liste:
        chaine = l + l2
        compteur += 1
        test(chaine, mot, compteur)
        
        for l3 in liste:
            chaine = l + l2 + l3
            compteur += 1
            test(chaine, mot, compteur)
            
            for l4 in liste:
                chaine = l + l2 + l3 + l4
                compteur += 1
                test(chaine, mot, compteur)
                
                    

print("Le mot de passe n'a pas été trouvé.")
print(f"Nombre de combinaisons testées : {compteur}")
end_time = time.time()
print(f"Temps écoulé : {end_time - start_time} secondes")
