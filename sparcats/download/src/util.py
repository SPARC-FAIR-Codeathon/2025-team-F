import io
import os

import pandas as pd


# Convert all column names of a dataset to lower case.
def convert_cols_lower(df):
    df.rename(columns=str.lower)
    return df


def save_xlsx_file(content, out_path):
    output_directory = os.path.dirname(out_path)
    os.makedirs(output_directory, exist_ok=True)

    with io.BytesIO(content) as buffer:
        df = pd.io.excel.read_excel(buffer, engine='openpyxl')

    df.dropna(axis=0, how='all', inplace=True)
    writer = pd.ExcelWriter(out_path)
    df.to_excel(writer)
    writer.close()


def save_csv_file(content, out_path):
    output_directory = os.path.dirname(out_path)
    os.makedirs(output_directory, exist_ok=True)

    with io.BytesIO(content) as writer:
        df = pd.read_csv(writer)
    df.to_csv(out_path, sep=',', header=False, index=False)


def save_mat_file(response, out_path):
    output_directory = os.path.dirname(out_path)
    os.makedirs(output_directory, exist_ok=True)

    with open(out_path, 'wb') as writer:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                writer.write(chunk)
