def func(x):
    return x + 1


def select_data(data, column, value):
    mask = data[column] < value
    return data[mask]


def drop_column(data, column):
    return data.drop(columns=column, axis=1)
