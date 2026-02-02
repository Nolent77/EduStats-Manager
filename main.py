# Pour executer cette tâche executer la ligne de commande suivante : py main.py
from utilis import *

def make_student_list_note():
    note_list = []

    # Pour enregistré le nombre d'élève
    while True :
        try:
            nb_student = int(input("Combien d'élève : "))

            if nb_student < 1 :
                print("il faut au moin un élève")
            else :
                break
        except ValueError :
            print(ValueError)

    # Pour enregistré les notes d'élève suivant les nb_student
    note_student = 0
    for i in range(nb_student):
        if note_student != -1 :
            while True :
                try :
                    note_student = float(input("La note de l'élève " + str(i + 1) +  " est : "))
                    if note_student >= 0 :
                        note_list.append(note_student)
                        break
                    elif note_student == -1:
                        print("Processus stopper")
                        break
                    else:
                        print("la note de l'élève ne peux pas être négative")
                except ValueError :
                    print("Taper uniquement un nombre")
    return note_list

### Initialization ###

result_list = make_student_list_note()

### Call & Display ###

print(result_list)
print(calculate_mean(result_list))
