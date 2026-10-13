"""
Library of functions to predict credi card customers who are most likely to churn.

Author: Sharina V. Jones
Date: October 2026
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.environ["QT_QPA_PLATFORM"] = "offscreen"
sns.set_theme()

# constants
EDA_DIR = "./images/eda"
RESULTS_DIR = "./images/results"
MODELS_DIR = "./models"
DATA_PATH = "./data/bank_data.csv"

RESPONSE = "Attrition_Flag"


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
    perform_eda(df)


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
    Return a dataframe for the csv found at pth, with the response column added.

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
            RESPONSE 1 is 1 for cancelled customers, 0 for active customers
    """
    df = pd.read_csv(pth)
    df[RESPONSE] = (df['Attrition_Flag'] == "Attrited Customer").astype(int)
    return df


def save_figure(pth):
    """
    Save the current matplotlib figure to the pth and close it.

    input:
        pth: file pat for the image, e.g. "./images/eda/heatmap.png"
    output:
        None
    """
    plt.savefig(pth, bbox_inches="tight")
    plt.close()


def perform_eda(df):
    """
    Perform EDA on df and save figures to EDA_DIR.

    input:
            df: pandas dataframe
    output:
            None
    """
    create_output_directories()
    plt.figure(figsize=(20, 10))
    df[RESPONSE].hist()
    save_figure(os.path.join(EDA_DIR, "existing_distribution.png"))

    plt.figure(figsize=(20, 10))
    df['Customer_Age'].hist()
    save_figure(os.path.join(EDA_DIR, "customer_age_distribution.png"))

    plt.figure(figsize=(20, 10))
    df.Marital_Status.value_counts(normalize=True).plot(kind='bar')
    save_figure(os.path.join(EDA_DIR, "marital_status_distribution.png"))

    plt.figure(figsize=(20, 10))
    # Show distributions of 'Total_Trans_Ct' and add a smooth curve obtained
    # using a kernel density estimate
    sns.histplot(df['Total_Trans_Ct'], stat='density', kde=True)
    save_figure(os.path.join(EDA_DIR, "total_trans_ct_distribution.png"))

    plt.figure(figsize=(20, 10))
    numeric_df = df.drop(columns=["Unnamed: 0", "CLIENTNUM"]).select_dtypes(include="number")
    sns.heatmap(numeric_df.corr(), annot=False, cmap='coolwarm', center=0, linewidths=2)
    save_figure(os.path.join(EDA_DIR, "heatmap.png"))


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
