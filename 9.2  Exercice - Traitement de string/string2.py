# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

# compte d'exemples
print(texte.lower().count("exemple"))
# remplacer est par représente
print(texte.lower().replace(" est ", " représente "))
# inverser le sens de lecture
rev_texte  = texte.split()
rev_texte.reverse()
print(*rev_texte)
