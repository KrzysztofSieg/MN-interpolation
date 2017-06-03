import numpy as np


def spline(x_basic_points, y_basic_points, x_all_points):
    size_x = x_basic_points.size
    delta = np.zeros([size_x])
    mi = np.zeros([size_x])
    sigma = np.zeros([size_x])
    h = np.zeros([size_x])
    for j in range(1, size_x):
        h[j] = x_basic_points[j] - x_basic_points[j - 1]
    for j in range(1, size_x - 1):
        mi[j] = h[j] / (h[j] + h[j + 1])
        sigma[j] = h[j + 1] / (h[j] + h[j + 1])
        delta[j] = (6 / (h[j] + h[j + 1])) * \
                   (((y_basic_points[j + 1] - y_basic_points[j]) / h[j + 1]) - ((y_basic_points[j] - y_basic_points[j - 1]) / h[j]))
    matrix_m = np.zeros([size_x, size_x])
    matrix_m[0, 0] = 2
    matrix_m[0, 1] = sigma[0]
    matrix_m[-1, -1] = 2
    matrix_m[1, -2] = mi[-1]
    for j in range(1, size_x - 1):
        matrix_m[j, j] = 2
        matrix_m[j, j - 1] = mi[j]
        matrix_m[j, j + 1] = sigma[j]
    m_constants = np.linalg.solve(matrix_m, delta)
    a = np.zeros([size_x - 1])
    b = np.zeros([size_x - 1])
    c = np.zeros([size_x - 1])
    d = np.zeros([size_x - 1])
    for j in range(size_x - 1):
        a[j] = y_basic_points[j]
        b[j] = ((y_basic_points[j + 1] - y_basic_points[j]) / h[j + 1]) - ((((2 * m_constants[j]) + m_constants[j + 1]) / 6) * h[j + 1])
        c[j] = m_constants[j] / 2
        d[j] = (m_constants[j + 1] - m_constants[j]) / (6 * h[j + 1])
    function_count = 0
    result = np.array([])
    for x in x_all_points:
        y_result = 0.
        while x > x_basic_points[function_count + 1]:
            function_count += 1
        y_result += a[function_count] + b[function_count] * (x - x_basic_points[function_count]) + \
                   c[function_count] * np.power(x - x_basic_points[function_count], 2) + \
                   d[function_count] * np.power(x - x_basic_points[function_count], 3)
        result = np.append(result, y_result)
    return result