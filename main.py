#créé par Mikolai Szychowski
#créé le 19 septembre 2023
#TP2
import random
def jeu():
    bornes=str(input('Voulez vous choisir les limites du nombres mystere? (y/n)'))
    if bornes == ('y'):
        borne_minimale=int(input('Quelle sera le minimum?'))
        borne_maximale=int(input('Quelle sera le maximum?'))
    chiffre_aléatoire = random.randint(borne_minimale,borne_maximale)
    print('Lordinateur a choisi un nombre, essayez de le deviner.')
    nb_essai=1
    boucle_jeu=True
    while True:
        essai=int(input('Entrez votre premier essai:'))
        if essai>chiffre_aléatoire:
            print('Le nombre est plus petit')
            nb_essai=nb_essai+1
            boucle_jeu + True
        elif essai < chiffre_aléatoire:
            print('le nombre est plus grand')
            nb_essai=nb_essai+1
            boucle_jeu = True
        elif essai == chiffre_aléatoire:
            print('Bravo! Vous avez trouvez en',nb_essai,'essais,Bravo!')
            rejouer=str(input('Voulez vous réssayer? (y/n)'))
            if quit==('y'):
                break
            else:
                if quit==('n'):
                    print('A la prochaine!')
            boucle_jeu=False
        else:
            print('Erreur')
            boucle_jeu = True

jeu()