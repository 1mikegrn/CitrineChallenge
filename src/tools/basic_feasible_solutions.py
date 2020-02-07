from numpy.random import random_sample
from scipy.optimize import root

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

    :returns:               (constraints)

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

    :returns:               (constraints)

refactored constraints which define the boundaries of the feasible space in
the hypercube.

    """
    for count, constraint in enumerate(constraints):
        temp = list(constraint)
        cmd = 'primed'

        for index, item in enumerate(temp):
            if item == '>':
                cmd = 'flip'

            if item == '<' or item == '>':
                temp[index] = '='

            # if item == '[' or item == ']':
            #     temp[index] = ''

        temp = str().join(temp).split()

        if cmd == 'flip':
            for cnt, char in enumerate(temp):
                if char not in ['-', '+', '*', '/', '**', '=', '==']:
                    temp[cnt] = '(-1*'+char+')'

        constraints[count] = str(' ').join(temp)
    
    for count, constraint in enumerate(constraints):
        temp = constraint.split()

        for index, item in enumerate(temp):
            if item == '==':
                temp[index] = '='

        constraints[count] = str(' ').join(temp)

    # constraints = hypercube_constraints(constraints, n_dim)
            
    return constraints

def slacks(constraints):
    """
Objective: add slack variables
    
    """
    for count, constraint in enumerate(constraints):
        temp = constraint.split()

        for index, item in enumerate(temp):
            if item == '=':
                temp.insert(index, '{}'.format(random_sample()))
                temp.insert(index, '+')
                break

        for index, item in enumerate(temp):
            if item == '=':
                temp[index] = '-'

        constraints[count] = str(' ').join(temp)

    constraints = quicksort(constraints)

    return constraints

def quicksort(x):
    """
Objective: Sort constraints such that two variable equations (dim and slack)
are first in the list of constraint equations.

    """

    if len(x) > 1:
        x_l = [n for n in x[1:] if len(n) <= len(x[0])]
        x_r = [n for n in x[1:] if len(n) > len(x[0])]
        
        return quicksort(x_l) + [x[0]] + quicksort(x_r)

    else: return x

def solver(constraints, n_dim):
    
    print(constraints)

    x = dict()
    res = 'dnw'

    for i in range(n_dim):
        x[i] = random_sample()

        print(x)

        for constraint in constraints:

            print(constraint)
            y = lambda x: eval(constraint)

            try:
                x[i+1] = root(y, 0.5)
            
            except: 
                print('fail')

    return x


# from sympy.solvers import solve
# from sympy.parsing.sympy_parser import parse_expr
# from sympy import Symbol

# def solver(constraints, n_dim):

#     res = 'dnw'

#     x = dict()
#     y = list()

#     for i in range(n_dim):
#         x[i] = Symbol('x{}'.format(i))
#         #y[i].append('Symbol')

#     for i in range(n_dim):

#         if type(x[i]) == type(Symbol('test')):

#             x[i] = random_sample()

#             for constraint in constraints:

#                 print(parse_expr(constraint))

#                 try:
#                     x[i+1] = solve(parse_expr(constraint), x[i+1])
                    
#                 except: pass

#     return x


