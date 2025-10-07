import random

def jeu_devinette():
    noooooooooooooon
    print("Je pense à un nombre entre 1 et 100...")
    
    nombre_secret = random.randint(1, 100)
    essais = 0
    trouve = False

    while not trouve:
        try:
            choix = int(input("Devine le nombre : "))
            essais += 1
            
            if choix < nombre_secret:
                print("C’est plus grand ! 🔼")
            elif choix > nombre_secret:
                print("C’est plus petit ! 🔽")
            else:
                print(f"Bravo ! 🎉 Tu as trouvé le nombre {nombre_secret} en {essais} essais.")
                trouve = True
        except ValueError:
            print("⚠️ Merci d’entrer un nombre valide.")

if __name__ == "__main__":
    jeu_devinette()