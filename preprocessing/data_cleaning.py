from preprocessing.data_profile import *

##############################################
'''
    File Usage: Common cleaning methods. Used later in the code.
    Picked from the Assignments. 
'''
##############################################


def fix_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:

    df = df.copy()
    numeric_data = get_numeric_columns(df)
    categorical_data = get_text_categorical_columns(df)
    binary_data = get_binary_columns(df)

    if column in numeric_data:

        # considering the inter-quartile-range case for dealing with numeric outliers
        quartile3 = df[column].quantile(0.75)
        quartile1 = df[column].quantile(0.25)

        inter_quartile_range = quartile3 - quartile1

        lower_limit = quartile1 - (1.5 * inter_quartile_range)
        upper_limit = quartile3 + (1.5 * inter_quartile_range)

        df[column] = df[column].apply(lambda value: np.nan if value < lower_limit or value > upper_limit else value)

    elif column in categorical_data or column in binary_data:

        list_unique_val = df[column].unique().tolist()
        dict_count = df[column].value_counts(ascending=True).to_dict()
        dict_less_than_percent_outlier = {}

        # Considering the percentage condition for categorical and binary outliers
        for key, value in dict_count.items():
            if (value * len(list_unique_val) / df.shape[0]) * 100 < 4:
                dict_less_than_percent_outlier[key] = True
        df[column] = df[column].apply(lambda x: np.nan if x in dict_less_than_percent_outlier else x)

    return df


def fix_nans(df: pd.DataFrame, column: str) -> pd.DataFrame:

    df = df.copy()
    numeric_data = get_numeric_columns(df)
    categorical_data = get_text_categorical_columns(df)
    binary_data = get_binary_columns(df)
    if column in numeric_data:
        mean_column = get_column_mean(df, column)
        df[column] = df[column].fillna(mean_column)

    elif column in categorical_data or binary_data:
        df[column] = df[column].fillna(df[column].value_counts().index[0])

    return df


if __name__ == "__main__":
    df = pd.DataFrame({'a': [1, 2, 3, None], 'b': [True, True, False, None], 'c': ['one', 'two', np.nan, None]})
    assert fix_outliers(df, 'c') is not None
    assert fix_nans(df, 'c') is not None
    print(" Data Cleaning - ok")
