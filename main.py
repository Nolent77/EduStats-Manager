# Pour executer cette tâche executer la ligne de commande suivante : py main.py

def make_student_list_note():
    Note_Student = 0
    Nb_Student = 0
    Note_Liste = []

    # demande à taper le nombre d'élève
    while True :
        try:
            Nb_Student = int(input("Combien d'élève : "))

            if Nb_Student < 1 :
                print("il faut au moin un élève")
            else :
                break
        except ValueError :
            print(ValueError)

    print(Nb_Student)
    for i in range(Nb_Student):
        while True :
            try :
                Note_Student = float(input("La note de l'élève " + str(i + 1) +  " est : "))
                if Note_Student > 0 :
                    Note_Liste.append(Note_Student)
                    print("j'ai ajouter la nb à la liste")
                    break
                else:
                    print("la note de l'élève ne peux pas être négative")
            except ValueError :
                print("Taper uniquement un nombre")
    return Note_Liste

print(make_student_list_note())

