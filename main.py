from read_my_problem import read_problem
from read_my_solutions import read_solution, evaluate
from save_my_solutions import save_solution
from dsatur import color_dsatur

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

    while True:
        print("Επιλέξτε:")
        print("0. Έξοδος")
        print("1. Ανάγνωση προβλήματος")
        print("2. Ανάγνωση λύσης")
        print("3. Επίλυση προβλήματος")
        print("4. Μαζική επίλυση")

        select = input("Επιλογή: ")
        select_int = int(select)

        if select_int == 0:
            break

        elif select_int == 1:

            print("Επιλέξτε αρχείο προβλήματος:")
            for index, path in enumerate(paths):
                print(index, path)
            i = input("Εισήγαγε πρόβλημα:")
            problem = paths[int(i)]
            graph = read_problem(problem)

        elif select_int == 2:
            solution_name = input("Δώστε όνομα λύσης: ")
            solution_dict = read_solution(solution_name)
            used_periods, valid = evaluate(graph, solution_dict)
            if valid == True:
                print(f"Χρησιμοποιεί {used_periods} περιοόδους.")
            else:
                print("Άκυρη λύση")

        elif select_int == 3:
            solution = color_dsatur(graph)
            periods, feasible = evaluate(graph, solution)
            if feasible == True:
                save_solution(problem, solution, periods)
                print(f"Η λύση χρησιμοποιεί {periods} περιόδους")

        elif select_int == 4:
            for problem in paths:
                print()
                graph = read_problem(problem)

                solution = color_dsatur(graph)
                periods, feasible = evaluate(graph, solution)
                if feasible == True:
                    save_solution(problem, solution, periods)
                    print(f"Χρησιμοποιεί {periods} περιόδους")
                else:
                    print("Άκυρη λύση")
