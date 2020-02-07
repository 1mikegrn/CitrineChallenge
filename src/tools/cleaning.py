from numpy import(
    vstack, delete
)

def clean(class_object, report_values, test_values):

    x = list()

    for i in range(test_values.shape[0]):

        if class_object.apply(test_values[i,:]) is True and test_values[i,:] not in report_values:
            x.append(i)
            report_values = vstack([report_values, test_values[i,:]])

    test_values = delete(test_values, x, axis=0)

    return test_values, report_values