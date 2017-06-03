import numpy as np
import csv
import matplotlib.pyplot as plt
import lagrange_interpolation as li
import spline_interpolation as si


def interpolation_read_csv(filename):
    with open(filename, newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        read_data_x = np.array([])
        read_data_y = np.array([])
        for row in csv_data:
            read_data_x = np.append(read_data_x, row[0])
            read_data_y = np.append(read_data_y, row[1])
    return read_data_x, read_data_y


def interpolation_basic_points(acq_x, acq_y, mod):
    read_basic_x = np.array([])
    read_basic_y = np.array([])
    read_basic_x = np.append(read_basic_x, acq_x[0])
    read_basic_y = np.append(read_basic_y, acq_y[0])
    for x_enum in range(1, acq_x.size-1):
        if x_enum % mod == 2:
            read_basic_x = np.append(read_basic_x, acq_x[x_enum])
            read_basic_y = np.append(read_basic_y, acq_y[x_enum])
    read_basic_x = np.append(read_basic_x, acq_x[-1])
    read_basic_y = np.append(read_basic_y, acq_y[-1])
    return read_basic_x, read_basic_y


def interpolation_basic_points_rand(acq_x, acq_y, mod):
    read_basic_x = np.array([])
    read_basic_y = np.array([])
    read_basic_x = np.append(read_basic_x, acq_x[0])
    read_basic_y = np.append(read_basic_y, acq_y[0])
    for x_enum in range(1, acq_x.size-1):
        if x_enum % mod == np.random.randint(0, mod-1):
            read_basic_x = np.append(read_basic_x, acq_x[x_enum])
            read_basic_y = np.append(read_basic_y, acq_y[x_enum])
    read_basic_x = np.append(read_basic_x, acq_x[-1])
    read_basic_y = np.append(read_basic_y, acq_y[-1])
    return read_basic_x, read_basic_y


def interpolation_plot(x_points, true_y, lagrange_y, spline_y):
    true_plot, = plt.plot(x_points, true_y, 'r', label='True data')
    lagrange_plot, = plt.plot(x_points, lagrange_y, 'g', label='Lagrange interpolation')
    spline_plot, = plt.plot(x_points, spline_y, 'b', label='Spline interpolation')
    plt.ylabel('height(m)')
    plt.xlabel('length(m)')
    plt.legend(handles=[true_plot, spline_plot, lagrange_plot])
    plt.title('Interpolation comparison')
    plt.show()


def interpolation_plot_no_lagrange(x_points, true_y, spline_y):
    true_plot, = plt.plot(x_points, true_y, 'r', label='True data')
    spline_plot, = plt.plot(x_points, spline_y, 'b', label='Spline interpolation')
    plt.ylabel('height(m)')
    plt.xlabel('length(m)')
    plt.legend(handles=[true_plot, spline_plot])
    plt.title('Interpolation comparison')
    plt.show()


def main():
    data_x, data_y = interpolation_read_csv('data.csv')
    basic_x, basic_y = interpolation_basic_points(acq_x=data_x, acq_y=data_y, mod=50)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data2.csv')
    basic_x, basic_y = interpolation_basic_points(acq_x=data_x, acq_y=data_y, mod=50)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data3.csv')
    basic_x, basic_y = interpolation_basic_points(acq_x=data_x, acq_y=data_y, mod=50)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data.csv')
    basic_x, basic_y = interpolation_basic_points(acq_x=data_x, acq_y=data_y, mod=25)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data2.csv')
    basic_x, basic_y = interpolation_basic_points(acq_x=data_x, acq_y=data_y, mod=25)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data3.csv')
    basic_x, basic_y = interpolation_basic_points(acq_x=data_x, acq_y=data_y, mod=25)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)


def main_rand():
    data_x, data_y = interpolation_read_csv('data.csv')
    basic_x, basic_y = interpolation_basic_points_rand(acq_x=data_x, acq_y=data_y, mod=50)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data2.csv')
    basic_x, basic_y = interpolation_basic_points_rand(acq_x=data_x, acq_y=data_y, mod=50)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data3.csv')
    basic_x, basic_y = interpolation_basic_points_rand(acq_x=data_x, acq_y=data_y, mod=50)
    y_lagrange = li.lagrange(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot(x_points=data_x, true_y=data_y, lagrange_y=y_lagrange, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data.csv')
    basic_x, basic_y = interpolation_basic_points_rand(acq_x=data_x, acq_y=data_y, mod=25)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot_no_lagrange(x_points=data_x, true_y=data_y, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data2.csv')
    basic_x, basic_y = interpolation_basic_points_rand(acq_x=data_x, acq_y=data_y, mod=25)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot_no_lagrange(x_points=data_x, true_y=data_y, spline_y=y_spline)

    data_x, data_y = interpolation_read_csv('data3.csv')
    basic_x, basic_y = interpolation_basic_points_rand(acq_x=data_x, acq_y=data_y, mod=25)
    y_spline = si.spline(x_basic_points=basic_x, y_basic_points=basic_y, x_all_points=data_x)
    interpolation_plot_no_lagrange(x_points=data_x, true_y=data_y, spline_y=y_spline)


if __name__ == "__main__":
    #main()
    main_rand()
