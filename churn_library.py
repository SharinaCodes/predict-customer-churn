""" 
Library of functions to predict credi card customers who are most likely to churn.

Author: Sharina V. Jones
Date: October 2026
"""

import os
import pandas as pd

os.environ["QT_QPA_PLATFORM"] = "offscreen"

EDA_DIR = "./images/eda"
RESULTS_DIR = "./images/results"
MODELS_DIR = "./models"
DATA_PATH = "./data/bank_data.csv"

def main():
    """
    Run the churn pipeline end to end.

    input:
        None

    output:
        None
    """
    create_output_directories()
    df = import_data(DATA_PATH)
    print(df.shape)


def create_output_directories():
    """
    Create output directories used by the project.

    input:
            None
    output:
            None
    """
    os.makedirs(EDA_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(MODELS_DIR, exist_ok=True)


def import_data(pth):
    """
    Return a dataframe for the csv found at pth.

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    """
    return pd.read_csv(pth)


def perform_eda(df):
    """
    Perform EDA on df and save figures.

    input:
            df: pandas dataframe
    output:
            None
    """
    create_output_directories()

    # TODO: implement
    # Suggested steps:
    # 1. Create a binary churn column if needed
    # 2. Plot key distributions
    # 3. Plot a correlation heatmap
    # 4. Save figures into EDA_DIR
    pass


def encoder_helper(df, category_lst, response):
    """
    Encode categorical features.

    input:
            df: pandas dataframe
            category_lst: list of categorical columns
            response: response column name
    output:
            df: updated dataframe
    """
    # TODO: implement
    pass


def perform_feature_engineering(df, response):
    """
    Split dataset into train and test sets.

    input:
              df: pandas dataframe
              response: response column name
    output:
              x_train, x_test, y_train, y_test
    """
    # TODO: implement
    pass


def classification_report_image(
    y_train,
    y_test,
    y_train_preds_lr,
    y_train_preds_rf,
    y_test_preds_lr,
    y_test_preds_rf,
):
    """
    Save classification reports as images.

    input:
            predictions and labels
    output:
            None
    """
    create_output_directories()

    # TODO: implement
    pass


def feature_importance_plot(model, x_data, output_pth):
    """
    Save feature importance plot.

    input:
            model, x_data, output path
    output:
            None
    """
    # TODO: implement
    pass


def train_models(x_train, x_test, y_train, y_test):
    """
    Train models and save outputs.

    input:
            train/test data
    output:
            None
    """
    create_output_directories()

    # TODO: implement
    pass


if __name__ == "__main__":
    main()

