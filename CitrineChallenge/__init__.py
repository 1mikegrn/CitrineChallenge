"""
CitrineChallenge is the Python library built by Michael Green as a submission 
for the technical challenge provided by Citrine Informatics.

Objective: build an array of vectors in an n-dimensional hypercube, whos vectors
satisfy a system of non-linear constraints.

Solution: The current method is an iterative process which, from a set of random
vectors within the hypercube, linearly interpolates between good vectors and bad 
vectors, until there are no more bad vectors. An initial set of random vectors 
is generated as an array called test_values. test_values is then passed through 
a cleaning function to extract vectors which satisfy the constraints provided,
and place these vectors in a separate array called report_values to be reported.

Now that we have two arrays, the arrays are passed through a generator function.
For each vector in the test_values array, the generator function pairs this 
vector with a random vector from the report_values array. Linear interpolation
is then used to replace the vector in the test_values array with a new vector
which is between the good vector and bad vector. These new vectors are then 
passed back to the cleaning function for evaluation. This process of cleaning 
and generating is repeated until there are no bad vectors.

To note, this is what I would consider a 'minimally viable product'. The library
is built modularly so to allow pieces of it to be optimized as desired by a 
teamleader. Values tend to cluster a tad near the center of the hypercube, and
future optimization would inclue the integration of methods which would better 
correct for this tendency. It's not a hard problem per se, as there are methods
which could be implemented to build an array of the corners of the feasible 
region (see simplex method and introducing slack variables) and then apply the
switch function to those corner points; but in an effort to stay below the time 
constraint, we save this for a future version.

This library includes the following functions:

::

    src.tools.cmd_reader.reader(

    )

the reader function parses the command-line interface arguments for calculation.
see 

the cleaning function separates 
"""