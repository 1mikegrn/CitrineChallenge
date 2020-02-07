from numpy import array
from numpy.random import randint, random_sample

def generate(test_values, report_values):
    """
Objective:

the generate() function uses the 'accepted' points in tandem with the 
'rejected' points to replace the rejected points with a new data set for 
cleaning. Each rejected point is paired with at random an accepted point
in the 'report_values' array. These two points are then passed through the
switch() function in src.generator so to replace the rejected value with a
new test value. The new test values are returned for cleaning.

::

    :param test_values:     <np.array>

test_values are values which were rejected by the cleaner() function located
in src.cleaning. These values are passed through the switch() function and
replaced in position.

::

    :param report_values:   <np.array>

array of values previously accepted by the cleaner function. A random vector
from this array is utilized by the switch() function for replacing the 
rejected test array with a new untested array for testing.

::

    :returns:               test_values

function returns a new set of test values for subsequent cleaning.

    """
 
    for i in range(test_values.shape[0]):

        try:
            choice = randint(report_values.shape[0]-1)
        except:
            choice = 0
        
        test_values[i] = switch(
            report_values[choice,:], 
            test_values[i, :]
        )

    return test_values


def switch(accepted, rejected):
    """
Objective:

Replace a 'rejected' point from the test_values array with a new test point
to be examined by the clean() function. The logic is rather simple - between
every accepted point and rejected point there is a space that is guarenteed to
be part 'feasible' and part 'infeasible'. The switch function uses linear 
interpolation to pick a random point between the accepted point and rejected
point, and replaces the rejected point with this new point to be tested.

::

    :param accepted:        <float>

the vector provided from the generate() function located in src.generate which
picks a random accepted point from the array of accepted vectors.

::

    :param rejected:        <float>

the vector provided from the generate() function located in src.generate which
is a rejected point from the array of rejected vectors.

 ::

    :returns:               new_point

a new point for subsequent cleaning.
   
    """
    pct = random_sample()
    new_point = (1-pct)*accepted + pct*rejected

    return new_point
