# Get timeseries specific files.
# Download - dataset from SPARC-ME
# Get all file paths using SPARC-Me
# Separate out required files
# File to path pairing.
# "filename": "absolute path"
import os
import shutil

from sparc_me import Dataset_Api

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
