def func(x):
    return x + 1


def select_data(data, column, value):
    mask = data[column] < value
    return data[mask]


