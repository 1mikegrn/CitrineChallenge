class Constraint():
    """Constraints loaded from a file."""

    def __init__(self, fname, **kwargs):
        """
        Construct a Constraint object from a constraints file

        :param fname: Name of the file to read the Constraint from (string)
        """

        if 'google' in kwargs and kwargs['google'] is True:
            lines = fname.decode().split('\n')
        
        else:
            with open(fname, "r") as f:
                lines = f.readlines()

        print(lines)

        # Parse the dimension from the first line
        self.n_dim = int(lines[0])
        # Parse the example from the second line
        self.example = [float(x) for x in lines[1].split(" ")[0:self.n_dim]]

        # Run through the rest of the lines and compile the constraints
        self.exprs = list()
        self.raw_exprs = list()

        for i in range(2, len(lines)):
            # support comments in the first line
            if lines[i][0] == "#":
                continue
            self.raw_exprs.append(lines[i])
            self.exprs.append(compile(lines[i], "<string>", "eval"))
        return

    def get_constraints(self):
        """Get the raw string of the constraints"""
        return self.raw_exprs

    def get_example(self):
        """Get the example feasible vector"""
        return self.example

    def get_ndim(self):
        """
        Get the dimension of the space on which the constraints are defined
        """
        return self.n_dim

    def apply(self, x):
        """
        Apply the constraints to a vector, returning True only if all are 
        satisfied

        :param x: list or array on which to evaluate the constraints
        """
        for expr in self.exprs:
            if not eval(expr):
                return False
        return True   


