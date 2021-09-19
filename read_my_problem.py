from itertools import combinations
from networkx import Graph
from networkx.classes.function import density


def read_problem(path):
    # Δημιουργώ έναν κενό γράφο
    graph = Graph()

    # Δημιουργώ δύο μεταωλητές
    students = 0
    enrollments = 0
    # Ανοίγω ενα αρχείο με δηκαιώματα ανάγνωσης
    file = open(path, "r")

    # Χωρίζει σε λίστες το αρχείο μου
    lines = file.readlines()

    # Δημιουργώ μια for για να παίρνει καθε φορά μια μια τις γραμμές μου
    for line in lines:
        # Διαγράφω τα κενά που μπορούν να υπάρχουν μέσα σε κάθε γραμμή της λίστας μου
        line = line.strip()

        # Αν τυχόν υπάρχει κάποια γραμμή κενή θα πρέπει να την προσπεράσουμε
        if line == "":
            continue
        # Κάθε γραμμή αφορά και έναν μαθητή οπότε αυτό μας ενδιαφέρει για να βρούμε το σύνολλο των σπουδαστών
        students += 1

        # Σε κάθε γραμμή ξεχωρίζω τις εξετάσεις του κάθε μαθητή για να βρώ το σύνολο των εγραφών
        exams = line.split()
        # Και  προσθέτω καθε μια για να βρώ το μήκος της λίστας exams
        enrollments += len(exams)

        # Δημιουργώ μια συνθήκη και ελέγχω σε περίπτωση που το μήκος της λίστας μου ειναι ισο με 1 αυτομάτος
        # αυτο σημαίνει πως η γραμμή αυτή είναι και κόμβος για εμένα.
        if len(exams) == 1:
            # Εγώ θέλω την μεταβλητή μου σε integer επειδή ειναι Strings γραμμή
            # Και για την λίστα exams θα πάρω την θέση 0 που είναι και η μοναδική θέση που έχω
            exam_int = int(exams[0])
            # Δημιουργώ και τους υπόλοιπους κόμβους - κορυφές
            graph.add_node(exam_int)
            # Πάω στην επόμενη γραμμή
            continue

        # φτιάχνω ολους τους πιθανούς συνδιασμούς που εχω απο το exams παιρνοντας τα 2 2
        # Για την [1,2,3]: [(1,2),(1,3),(2,3)]
        exam_combinations = combinations(exams, 2)

        for exam_a, exam_b in exam_combinations:
            # Μετατρέπουμε τις μεταβλητές μας σε integer
            exam_a_int = int(exam_a)
            exam_b_int = int(exam_b)

            # Φτιάχνουμε τις ακμές μας στο γράφο μας
            graph.add_edge(exam_a_int, exam_b_int)

    # Βρήσκουμε την πυκνότητα
    density_of_graph = density(graph)

    # Επειδή ομως αυτο μπορεί να έχει πολλα δεκαδικά ψηφία το θέμουμε εμείς μόνο με 2 δεκαδικά
    # το κανουμε με την εντολή round
    density_rounded = round(density_of_graph, 2)

    # Τυπώνουμε τα αποτελέσματα μας
    print(f"Η πυκνότητα των συγκρούσεων για το {path} είναι {density_rounded}")
    print(f"Ο αριθμός των μαθητών είναι: {students}")
    print(f"Ο αριθμός των εγγραφών: {enrollments}")
    print(f"Ο αριθμός των εξετάσεων: {graph.number_of_nodes()}")

    return graph


if __name__ == "__main__":
    paths = [
        "car-f-92.stu",
        "car-s-91.stu",
        "ear-f-83.stu",
        "hec-s-92.stu",
        "kfu-s-93.stu",
        "lse-f-91.stu",
        "pur-s-93.stu",
        "rye-s-93.stu",
        "sta-f-83.stu",
        "tre-s-92.stu",
        "uta-s-92.stu",
        "ute-s-92.stu",
        "yor-f-83.stu",
    ]

    for path in paths:
        graph = read_problem(path)
        print()
