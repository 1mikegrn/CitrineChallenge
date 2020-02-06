from src.tools import(
    cmd_reader, basic_feasible_solutions
) 
from src.constraints import Constraint

def main():

    input_file, output_file, dim = cmd_reader.reader()

    class_object = Constraint(input_file)

    example = class_object.get_example()
    n_dim = class_object.get_ndim()
    constraints = class_object.get_constraints()

    edges = basic_feasible_solutions.boundaries(
        constraints=constraints,
        n_dim=n_dim
    )

    slacks = basic_feasible_solutions.slacks(
        constraints=edges
    )

    print(slacks)



if __name__ == "__main__":
    main()