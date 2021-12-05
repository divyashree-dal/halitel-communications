from typing import List
import pandas as pd
import numpy as np

from preprocessing.load_file import read_dataset

################################################################################
''' File usage: Common Profiling of churn dataset.
    These methods will be used for later analytics in other files. 
    Picked from Assignments
    '''
################################################################################


# To retrieve the maximum value of the specified column
def get_column_max(df: pd.DataFrame, column_name: str) -> float:
    return df[column_name].max()


# To retrieve the minimum value of the specified column
def get_column_min(df: pd.DataFrame, column_name: str) -> float:
    return df[column_name].min()


# To retrieve the mean of the specified column
def get_column_mean(df: pd.DataFrame, column_name: str) -> float:
    return df[column_name].mean(axis=0)


# To retrieve the count of Nan(Missing) Values of the specified column
def get_column_count_of_nan(df: pd.DataFrame, column_name: str) -> float:
    return df[column_name].isnull().sum()


# To retrieve the count of duplicates of the specified column
def get_column_number_of_duplicates(df: pd.DataFrame, column_name: str) -> float:
    return df[df.duplicated(subset=[column_name]) == True].shape[0]


# To retrieve the numeric columns of a dataframe
def get_numeric_columns(df: pd.DataFrame) -> List[str]:
    return df.select_dtypes(include=np.number).columns.tolist()


# To retrieve the binary columns of the dataframe
def get_binary_columns(df: pd.DataFrame) -> List[str]:
    binary_column_values = []
    for column in df:
        if np.isin(df[column].dropna().unique(), [0, 1]).all():
            binary_column_values.append(column)
    return binary_column_values


# To retrieve the categorical columns of the dataframe
def get_text_categorical_columns(df: pd.DataFrame) -> List[str]:
    return df.select_dtypes(include=['object']).columns.tolist()


# To retrieve the correlation between columns of the dataframe
def get_correlation_between_columns(df: pd.DataFrame, col1: str, col2: str) -> float:
    return df[[col1, col2]].corr(method="pearson")


if __name__ == "__main__":
    df = read_dataset()

    assert get_column_max(df, df.columns[19]) is not None
    assert get_column_min(df, df.columns[19]) is not None
    assert get_column_mean(df, df.columns[5]) is not None
    assert get_column_count_of_nan(df, df.columns[5]) is not None
    assert get_column_number_of_duplicates(df, df.columns[5]) is not None
    assert get_numeric_columns(df) is not None
    assert get_binary_columns(df) is not None
    assert get_text_categorical_columns(df) is not None
    assert get_correlation_between_columns(df, df.columns[19], df.columns[20]) is not None

    print(" Data profiling - Done")
