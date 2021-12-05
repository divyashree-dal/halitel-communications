from typing import List

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


##############################################
'''
    File Usage: Data encoding purpose (label encoder + one hot encoder). Used later in the code.
'''
##############################################


# To generate label encoding of categorical columns
def generate_label_encoder(df_column: pd.Series) -> LabelEncoder:
    label_encoder = LabelEncoder()
    label_encoder.fit(np.ravel(df_column.values.reshape(-1, 1)))
    return label_encoder


# To generate one hot encoding of categorical columns
def generate_one_hot_encoder(df_column: pd.Series) -> OneHotEncoder:
    onehotencoder = OneHotEncoder(handle_unknown='ignore')
    df_column_onehotencoder = onehotencoder.fit(df_column.values.reshape(-1, 1))
    return df_column_onehotencoder


# To replace those columns with labelled encoded values.
def replace_with_label_encoder(df: pd.DataFrame, column: str, le: LabelEncoder) -> pd.DataFrame:
    df = df.copy()
    df[column] = le.fit_transform(df[column])
    return df


# To replace those columns with one hot encoded values.
def replace_with_one_hot_encoder(df: pd.DataFrame, column: str, ohe: OneHotEncoder,
                                 ohe_column_names: List[str]) -> pd.DataFrame:
    df_copy = df.copy(deep=True)
    encoded_column = ohe.transform(df_copy[column].values.reshape(-1, 1)).toarray()
    join_data = pd.DataFrame(encoded_column,
                             columns=ohe_column_names)  # creating new data frame which has encoded columns
    df_copy = df_copy.drop([column], axis=1)  # Dropping the original column
    df_copy = pd.concat([df_copy, join_data], axis=1)  # concatenating the encoded column with original data frame
    return df_copy


if __name__ == "__main__":
    df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [True, True, False, False], 'c': ['one', 'two', 'three', 'four']})
    le = generate_label_encoder(df.loc[:, 'c'])
    assert le is not None
    ohe = generate_one_hot_encoder(df.loc[:, 'c'])
    assert ohe is not None
    assert replace_with_label_encoder(df, 'c', le) is not None
    assert replace_with_one_hot_encoder(df, 'c', ohe, list(ohe.get_feature_names())) is not None
    print("Data Encoding - Done")
