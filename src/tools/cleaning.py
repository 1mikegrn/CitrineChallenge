from numpy import(
    vstack, delete
)

def clean(class_object, report_values, test_values):
    """
Objective: 

The clean() function applies the class_object.apply() criterion to
the test_values array to check and see if any of the newly provided data 
points are within the constraints, as defined by the constraints from the 
<input.txt> file. The function also checks for duplication within the
report_value array. If these two criterion are satisfied, the test_value
Nx1 array is added to the report_values array and the index of the position
is noted. Once the test_values array has been traversed, the test_values 
array is shortened by deleting the transferred values.

::

    :param class_object:    <class>

class_object is the 'Constraints' class defined in src/constraints.py

::

    :param report_values:   <np.array>

report_values is the array of vectors which have passed previous clean()
implementations. New 'good' results are to be appended to the report_values
array by the function.

::

    :param test_values:     <np.array>

test_values is the array of vectors which have yet to pass through the clean()
protocol. Vectors from this array that meet the contraints are parsed from the
test_values array and appended to the report_values array.

::

    :return:                test_values, report_values

returns the cleaned arrays, maintaing len(test_values) + len(report_values) =
n_results + 1.

    """
    to_remove = list()

    for i in range(test_values.shape[0]):

        if class_object.apply(test_values[i,:]) is True and test_values[i,:] not in report_values:
            to_remove.append(i)
            report_values = vstack([report_values, test_values[i,:]])

    test_values = delete(test_values, to_remove, axis=0)

    return test_values, report_values