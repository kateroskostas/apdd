# Δημιουργώ μια συνάρτηση για να αποθηκεύσω την λύση μου
def save_solution(problem_name, solution, periods):
    # Αντικαθηστώ το όνομα του αρχείου μου .stu αφαιρώντας την κατάληξη
    name_without_suffix = problem_name.replace(".stu", "")
    # Αποθηκεύω με f string ονομα αρχείου_αριθμό απο περιόδους που μας έσωσε η λύση μας .sol
    save_name = f"{name_without_suffix}_{periods}.sol"

    # Με ανοιχτό το αρχείο μας και με δικαιώματα εγγραφής αυτή την φορά
    with open(save_name, "w") as file:
        # Για κάθε κλειδί που βλέπει στο dictionary solution
        for key in solution:
            # Γράφει μια γραμμή key δηλαδή exam Tab solution key δηλαδή την περίοδο και μετά αλλάζει γραμμή
            file.write(f"{key}\t{solution[key]}\n")
