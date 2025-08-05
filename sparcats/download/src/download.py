import os
import shutil

import pandas as pd
from sparc_me import Dataset_Api

from sparcats.download.src.util import convert_cols_lower, save_csv_file, save_mat_file, save_xlsx_file

dp = Dataset_Api()  # SPARC-ME object


def download_dataset(datasetID, versionID=None):
    if versionID is None:
        versionID = dp.get_dataset_latest_version_number(datasetID)
    out_path = f"../../../validation/output/{datasetID}/{versionID}/"
    if os.path.exists(f"{out_path}"):
        print(f"[Warning] Dataset already exists at file path [validation/output/{datasetID}/{versionID}/]")
    else:
        dp.download_dataset(datasetID, versionID)
        os.makedirs(f"{out_path}", exist_ok=True)
        shutil.move("dataset", out_path)

        print(f"[Info] Dataset downloaded. Dataset Path: [{os.path.abspath(out_path)}]")


# Get absolute file path of timeseries data. This function returns a key-value pair,
# where the key is the subject-id and the value is the comma-seperated list (string) of paths.
def download_timeseries_files(datasetID, versionID=None, sex=None, out_path=None, primary_files_only=True,
                              num_subjects=1, num_files_per_subject=1):
    chk_sub_gender = False
    subject_files, subject_list, output = {}, [], ""

    if versionID is None:
        versionID = dp.get_dataset_latest_version_number(datasetID)
    if out_path is None:
        out_path = f"../outputs/"
    if sex is not None and sex.lower() in ["Male", "Female"]:
        chk_sub_gender = True  # Check for separating out on the basis of sex.

    all_dataset_files = dp.get_all_files_path(datasetID, versionID)

    # Assumption: The subject & manifest file will always follow this trend.
    subjects_sheet = list(filter(lambda s: "subjects.xlsx" in s, all_dataset_files))[
        0]  # Assumption: Only one master subjects file.

    response = dp._download_file(datasetID, subjects_sheet)
    if response.status_code == 200:
        save_xlsx_file(response.content, os.path.abspath(f"{out_path}{subjects_sheet.split('/')[1]}"))

        df = convert_cols_lower(pd.read_excel(os.path.abspath(f"{out_path}{subjects_sheet.split('/')[1]}"), sheet_name="Sheet1"))
        os.remove(f"{out_path}{subjects_sheet.split('/')[1]}")

        if chk_sub_gender:
            if "sex" in df.columns:
                subject_list = df.loc[df['sex'] == sex, "subject id"].tolist()
            elif "gender" in df.columns:
                subject_list = df.loc[df['gender'] == sex, "subject id"].tolist()
        else:
            subject_list = df['subject id'].tolist()

        for i in subject_list:
            if primary_files_only:
                subject_files[i] = list(filter(lambda s: f"primary/{i}" in s, all_dataset_files))
            else:
                subject_files[i] = list(filter(lambda s: f"{i}" in s, all_dataset_files))

        if num_subjects < 0 and num_files_per_subject < 0:
            for i in subject_files:
                print(f"Downloading all files for subject [{i}]")
                for j in subject_list[i]:
                    response = dp._download_file(datasetID, j)
                    #TODO: Feature to be added.
        else:
            print(f"Downloading first [{num_files_per_subject}] for first [{num_subjects}] subject(s).")
            for i in list(subject_files.keys())[0:num_subjects]:
                for j in range(0, num_files_per_subject):
                    response = dp._download_file(datasetID, subject_files[i][j])

                    if response.status_code == 200:
                        filename = subject_files[i][j].split("/")[-1]
                        if filename.endswith(".xlsx"):
                            save_xlsx_file(response.content, f"{out_path}{filename}")

                            if output == "":
                                output = os.path.abspath(f"{out_path}{filename}")
                            else:
                                output = output + "," + os.path.abspath(f"{out_path}{filename}")

                        elif filename.endswith(".csv"):
                            save_csv_file(response.content, f"{out_path}{filename}")

                            if output == "":
                                output = os.path.abspath(f"{out_path}{filename}")
                            else:
                                output = output + "," + os.path.abspath(f"{out_path}{filename}")

                        elif filename.endswith(".mat"):
                            save_mat_file(response, f"{out_path}{filename}")

                            if output == "":
                                output = os.path.abspath(f"{out_path}{filename}")
                            else:
                                output = output + "," + os.path.abspath(f"{out_path}{filename}")

                        else:
                            print(f"[Warning] Unsupported file type [{filename}].")
                    else:
                        print(
                            f"[Warning] Downloading failed. Couldn't file from the server. Response code [{response.status_code}].")

    else:
        print(f"[Warning] Skipping subject-based separation. Downloading first [{num_files_per_subject}] primary files.")

        subject_files = list(filter(lambda s: f"primary/" in s, all_dataset_files))

        for i in range(0, num_files_per_subject):
            response = dp._download_file(datasetID, subject_files[i])
            if response.status_code == 200:
                filename = subject_files[i].split("/")[-1]
                if filename.endswith(".xlsx"):
                    save_xlsx_file(response.content, f"{out_path}{filename}")

                    if output == "":
                        output = os.path.abspath(f"{out_path}{filename}")
                    else:
                        output = output + "," + os.path.abspath(f"{out_path}{filename}")

                elif filename.endswith(".csv"):
                    save_csv_file(response.content, f"{out_path}{filename}")

                    if output == "":
                        output = os.path.abspath(f"{out_path}{filename}")
                    else:
                        output = output + "," + os.path.abspath(f"{out_path}{filename}")

                elif filename.endswith(".mat"):
                    save_mat_file(response, f"{out_path}{filename}")

                    if output == "":
                        output = os.path.abspath(f"{out_path}{filename}")
                    else:
                        output = output + "," + os.path.abspath(f"{out_path}{filename}")

                else:
                    print(f"[Warning] Unsupported file type [{filename}].")
            else:
                print(
                    f"[Warning] Downloading failed. Couldn't file from the server. Response code [{response.status_code}].")

    return output


if __name__ == "__main__":
    download_timeseries_files(375, out_path="../outputs/")
