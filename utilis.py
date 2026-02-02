import math

list_student_note = [55, 60, 65, 75, 80, 85]
mean_class = 70.0

def calculate_mean(result_list : list[float]) :
    somme_total = sum(result_list)
    moyenne = somme_total/len(result_list)
    print (result_list)
    max(result_list)
    min(result_list)
    return "le maximum : " + str(max(result_list)) + " et le minimum : " + str(min(result_list)) + " pour une moyenne de : " + str(moyenne)

def calculate_standard_deviation (mean_class : float , list_student_note : list) :
    student_counter_above_equal_average = 0
    relative_average_list = []
    nb_student_note = len(list_student_note)
    for i in range(nb_student_note) :
        if list_student_note[i] > mean_class :
            student_counter_above_equal_average += 1
        relative_average_val = (list_student_note[i] - mean_class)**2
        relative_average_list.append(relative_average_val)
    if nb_student_note > 1 :
        variance = sum(relative_average_list) / (nb_student_note - 1)
    else :
        print("il n'y a pas de variance")
    standard_deviation = math.sqrt(variance)
    return standard_deviation , student_counter_above_equal_average


print(calculate_standard_deviation(mean_class,list_student_note))














