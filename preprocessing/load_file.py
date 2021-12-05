from pathlib import Path
import pandas as pd

################################################################################
''' File usage: loading and reading the churn dataset. 
    '''
################################################################################


def read_dataset() -> pd.DataFrame:
    # Since there is only one dataset, we are directly reading the csv file here.
    return pd.read_csv(Path('..', 'WA_Fn-UseC_-Telco-Customer-Churn.csv'))


if __name__ == "__main__":
    dataset = read_dataset()
    assert type(dataset) == pd.DataFrame
    print("Dataset - reading - Done")
