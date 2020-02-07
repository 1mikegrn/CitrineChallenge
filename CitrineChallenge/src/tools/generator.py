
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

    :param test_values:     <numpy.array>

test_values are values which were rejected by the cleaner() function located
in src.cleaning. These values are passed through the switch() function and
replaced in position.

::

    :param report_values:   <numpy.array>

array of values previously accepted by the cleaner function. A set of random 
vectors are sefected from this array and utilized by the switch() function 
for replacing the rejected test_values with a new test_values for cleaning.

::

    :returns:               <numpy.array>

function returns a numpy array containing a new set of test values for 
cleaning.

    """

    report_values = [
        report_values[randint(report_values.shape[0]), :] 
        for _ in test_values[:,0]
    ]
    
    report_values = array(report_values)

    test_values = switch(report_values, test_values)

    return test_values


def switch(report_values, test_values):
    """
Objective:

Replace the 'rejected' points from the test_values array with new test points
to be examined by the clean() function. The logic is rather simple - between
every accepted vector and rejected vector there is a space that is guarenteed 
to be part 'feasible' and part 'infeasible'. The switch function uses linear 
interpolation to pick a random vector between the accepted vector and rejected
vector, and replaces the rejected vector with this new vector to be tested. 
Switch() makes use of broadcasting over numpy arrays for increased 
performance.

::

    :param report_values:       <numpy.array>

the vector provided from the generate() function located in src.generate which
picks random accepted points from the array of accepted vectors.

::

    :param test_values:         <numpy.array>

the vector provided from the generate() function located in src.generate which
provides the rejected vectors from the test_values array.

 ::

    :returns:                   <numpy.array>

a numpy array of new vectors for subsequent cleaning.
   
    """

    pct = random_sample()
    new_point = (1-pct)*report_values + pct*test_values

    return new_point