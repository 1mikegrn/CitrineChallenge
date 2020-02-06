def hypercube_constraints(constraints, n_dim):
    """
Objective: Add hypercube constraints to the constraints list. For each
dimension, as the search is to be bound by the hypercube, there is an enforced
upper bound at x[dim] = 1.

::

    :param constraints:     list()

constraints are the list of constraints provided through the constraints input
file. 

::

    :param n_dim:           int()

dimensionality of the problem, provided through the constraints input file.

::

    :returns:               constraints

refactored constraints which include the bounds of the hypercube.
    """

    for i in range(n_dim):
        constraints.append('x[{}] = 1'.format(i))

    return constraints

def boundaries(constraints, n_dim):
    """
Objective: This function refactors the extracted constraints into equations 
which define the bounds of the 'feasible region' (region within the hypercube
where valid solutions will be found inside).

::

    :param constraints:     list()

constraints are the list of constraints provided through the constraints input
file. 

::

    :param n_dim:           int()

dimensionality of the problem, provided through the constraints input file.

::

    :returns:               constraints

refactored constraints which define the boundaries of the feasible space in
the hypercube.

    """
    for count, constraint in enumerate(constraints):
        temp = list(constraint)

        for index, item in enumerate(temp):
            if item == '<' or item == '>':
                temp[index] = '='
        
        constraints[count] = str().join(temp)
    
    for count, constraint in enumerate(constraints):
        temp = constraint.split()

        for index, item in enumerate(temp):
            if item == '==':
                temp[index] = '='

        constraints[count] = str(' ').join(temp)

    constraints = hypercube_constraints(constraints, n_dim)
            
    return constraints

def slacks(constraints):
    """
    Objective: add slack variables
    
    """
    for count, constraint in enumerate(constraints):
        temp = constraint.split()

        for index, item in enumerate(temp):
            if item == '=':
                temp.insert(index, 's{}'.format(count))
                temp.insert(index, '+')
                break

        constraints[count] = str(' ').join(temp)
    
    return constraints


