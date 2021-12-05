from preprocessing.data_cleaning import *
from preprocessing.data_encoding import *
from preprocessing.data_profile import *

##############################################
'''
    File Usage: Implementing previous file methods. 
    Main functionality is to preprocess the dataset, fixing nans, outliers of numeric columns 
    and encoding categorical columns.
'''


##############################################


# To preprocess the churn dataset
def process_churn_dataset() -> pd.DataFrame:
    """
        In the dataset, there are totally 21 columns where numeric columns are three in count
        and 18 columns are of categorical type. We have dropped off the customer ID and converted
        the TotalCharges column from object to float.
    """

    # 1. Load the dataset
    churn_df = read_dataset()

    # 2. Work on the copy of the dataframe
    churn_df = churn_df.copy()

    # 2. To perform exploratory data analysis using pandas profiling
    # pandas_churn = pandas_profile(churn_df)

    # 3. Drop the customer ID columns since all are unique, and not helpful for visualization
    churn_df.drop(labels='customerID', inplace=True, axis=1)

    # 4. Convert the TotalCharges column from object type to float type.
    # Convert Senior citizen yes and no to 1 and 0 resp
    churn_df['TotalCharges'] = churn_df['TotalCharges'].apply(lambda x: float(x) if x.strip() else 0.0)
    churn_df['SeniorCitizen'] = churn_df['SeniorCitizen'].apply(lambda x: 'No' if x == 0 else 'Yes')

    # 5. Obtain the different columns
    numerical_columns = get_numeric_columns(churn_df)

    # 6. Fix NaNs and Outliers among the numerical columns
    for numerical in numerical_columns:
        churn_df = fix_outliers(churn_df, numerical)
        churn_df = fix_nans(churn_df, numerical)

    return churn_df


def process_churn_dataset_again():
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    # 1. get categorical columns
    categorical_columns = get_text_categorical_columns(churn_df)

    # 2. Label encode the categorical columns
    for categorical in categorical_columns:
        label_encoder = generate_label_encoder(churn_df.loc[:, categorical])
        churn_df = replace_with_label_encoder(churn_df, categorical, label_encoder)

    return churn_df


def getLabelEncoderForCategorical():
    churn_df = process_churn_dataset()
    categorical_columns = get_text_categorical_columns(churn_df)

    categorical_label_encoder = {}

    for categorical in categorical_columns:
        label_encoder = generate_label_encoder(churn_df.loc[:, categorical])
        categorical_label_encoder[categorical] = label_encoder
        churn_df = replace_with_label_encoder(churn_df, categorical, label_encoder)
    return churn_df, categorical_label_encoder


if __name__ == "__main__":
    assert process_churn_dataset() is not None
    assert process_churn_dataset_again() is not None
    print("Data Experimentation - Done")
