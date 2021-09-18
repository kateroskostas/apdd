def save_solution(problem_name, solution, periods):
    name_without_suffix = problem_name.replace(".stu", "")
    save_name = f"{name_without_suffix}_{periods}.sol"
    with open(save_name, "w") as file:
        for key in solution:
            file.write(f"{key}\t{(solution[key])}\n")