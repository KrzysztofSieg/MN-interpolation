import numpy as np


def lagrange(x_basic_points, y_basic_points, x_all_points):
    negative_x = np.ma.array(np.negative(x_basic_points), mask=False)

    result = np.array([])
    for x in x_all_points:
        y_result = 0.
        for x_enum in enumerate(x_basic_points):
            upper_side = np.ma.array(negative_x + x, mask=False)
            upper_side.mask[x_enum[0]] = True
            result_upper = upper_side.prod()
            upper_side.mask[x_enum[0]] = False
            lower_side = np.ma.array(negative_x + x_basic_points[x_enum[0]], mask=False)
            lower_side.mask[x_enum[0]] = True
            result_lower = lower_side.prod()
            lower_side.mask[x_enum[0]] = False
            lnk = result_upper / result_lower
            y_result += y_basic_points[x_enum[0]] * lnk

        result = np.append(result, y_result)
    return result
