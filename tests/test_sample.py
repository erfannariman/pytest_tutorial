from main import func, select_data, drop_column
import pandas as pd
import pandas.testing as tm


def test_answer():
    assert func(3) == 4


def test_select_data():
    df = pd.DataFrame({'Col': range(5)})
    expected = pd.DataFrame({'Col': [0, 1, 2]})
    result = select_data(df, 'Col', 3)

    tm.assert_frame_equal(expected, result)


def test_drop_column():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]

    })

    expected = pd.DatFrame({'A': [1, 2, 3]})
    result = drop_column(df, 'B')

    tm.assert_frame_equal(expected, result)
