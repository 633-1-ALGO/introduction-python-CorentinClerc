# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

n_max = m_max = 0
for i in tab:
    for j in i:
        if j > tab[n_max][m_max]:
            n_max = tab.index(i)
            m_max = i.index(j)

# On peut également faire avec la longueur des tableaux

print("La valeur maximum est : " + str(tab[n_max][m_max]) + " et elle se trouve à l'indice [" + str(n_max) + "][" + str(m_max) + "]")
