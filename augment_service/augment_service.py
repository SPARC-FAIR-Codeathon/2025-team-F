#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
augment.py

Functions to augment timeseries data
Author: Mathias Roesler
Date: 08/25
"""

import json
import pathlib
import scipy.io

import numpy as np
import pandas as pd
import tsaug as tsaug


def generate_augmented_data(data, augmenter, n):
    """Generates n datasets of augmented data

    Args:
        data (np.array(float)): data to augment
        augmenter (tsaug.AugmenterPipe): augmenter pipe
        n (int): number of datasets to generate

    Returns:
        augmented_data (np.array(float)): augmented data

    Raises:
        ValueError: if n is not positive
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n should be a positive integer")

    augmented_data = np.zeros((len(data), n))  # Allocate memory

    for i in range(n):
        augmented_data[:, i] = augmenter.augment(data)

    return augmented_data


def save_to_csv(augmented_data, Fs, save_name):
    """Saves augmented data to a csv file

    Args:
        augmented_data (np.array(float)): augmented data
        Fs (int): sampling frequency to add timestamps
        save_name (str): name of file to save data in

    Returns:

    Raises:

    """
    t = (
        np.linspace(0, augmented_data.shape[0], augmented_data.shape[0]) / Fs
    )  # Create timestamps

    # Create data frame to save to csv
    df = pd.DataFrame(augmented_data)
    df.insert(0, "Time", t)  # Add timestamps

    #root_path = pathlib.Path(__name__).resolve().parent.parents[1]
    save_path = save_name

    df.to_csv(save_path, index=False)  # Save to csv


def read_from_csv(file_path):
    """Reads the data from a csv file

    Assume that there is only one column with the data to augment

    Args:
        file_path (str): path to the csv file

    Returns:
        data (np.array[float]): data read from csv file

    Raises:
        FileNotFoundError: if the file does not exist
        ValueError: if the extension is not csv

    """
    loaded_file = pathlib.Path(file_path)

    if not loaded_file.is_file():
        raise FileNotFoundError(f"{file_path} was not found")

    if not loaded_file.suffix == ".csv":
        raise ValueError(f"{file_path} should be a csv file")

    df = pd.read_csv(file_path)  # Read file
    data = df[df.columns[0]].to_numpy()  # Get data

    return data


def read_from_mat(file_path):
    """Reads the data from a mat file

    Assume that there is only one column with the data to augment

    Args:
        file_path (str): path to the mat file

    Returns:
        data (np.array[float]): data read from mat file

    Raises:
        FileNotFoundError: if the file does not exist
        ValueError: if the extension is not csv

    """
    loaded_file = pathlib.Path(file_path)

    if not loaded_file.is_file():
        raise FileNotFoundError(f"{file_path} was not found")

    if not loaded_file.suffix == ".mat":
        raise ValueError(f"{file_path} should be a mat file")

    loaded_data = scipy.io.loadmat(file_path)  # Read file

    for key in loaded_data.keys():
        if not key[0:2] == "__":
            data = loaded_data[key]

    return data


def parse_json(json_file="input/inputs.json"):
    """Parse the information from the JSON file to get input arguments

    Args:
        json_file (str): path to json file

    Returns:
        data (dict): dict with input arguments

    Raises:
        ValueError: if the extension is not json
        FileNotFoundError: if the file is not found

    """
    args = []  # Store input arguments
    loaded_file = pathlib.Path(json_file)

    if not loaded_file.is_file():
        raise FileNotFoundError(f"{json_file} was not found")

    if not loaded_file.suffix == ".json":
        raise ValueError(f"{json_file} should be a json file")

    with open(json_file, "r") as file:
        data = json.load(file)

    return data


def setup_augmenter(input_data):
    """Sets up the augmenters based on the input data

    Args:
        input_data (dict): dict containing the user input data

    Returns:
        arr_augmenter (list[tsaug.augmenter]): list of augmentation operations

    Raises:
        KeyError: if the key is not found in input_data

    """
    arr_augmenters = []

    try:
        if input_data["drift_aug"] == True:
            arr_augmenters.append(
                create_drift(input_data["max_drift"], input_data["drift_prob"])
            )

        if input_data["noise_aug"] == True:
            arr_augmenters.append(create_noise(input_data["noise_scale"]))

        if input_data["warp_aug"] == True:
            arr_augmenters.append(
                create_warp(
                    input_data["warp_ratio"],
                    input_data["warp_speed"],
                    input_data["warp_prob"],
                )
            )

    except KeyError:
        raise

    return arr_augmenters


def create_augmenter(arr_augmenters):
    """Creates an AugmenterPipe from input arguments

    Args:
        arr_augmenter (list[tsaug.augmenter]): list of augmentation operations

    Returns:
        augmenter (tsaug._augmenter.base._AugmenterPipe): augmenter pipe

    Raises:
        ValueError: if arr_augmenters is empty.

    """
    if len(arr_augmenters) == 0:
        raise ValueError("arr_augmenters is empty")

    augmenter = arr_augmenters[0]

    for i in range(len(arr_augmenters) - 1):
        augmenter += arr_augmenters[i + 1]

    return augmenter


def create_noise(scale=0.05):
    """Creates the AddNoise augmenter

    Args:
        scale (float): scale for the noise, default 0.05

    Returns:
        noise_aug (tsaug.AddNoise): add noise augmenter

    Raises:

    """
    return tsaug.AddNoise(scale=scale)


def create_drift(max_drift=0.2, prob=0.8):
    """Creates the Drift augmenter

    Args:
        max_drift (float): maximum drift, default 0.2
        prob (float): probability of applying drift, default 0.8

    Returns:
        drift_aug (tsaug.AddNoise): drift augmenter

    Raises:

    """
    return tsaug.Drift(max_drift=max_drift) @ prob


def create_warp(max_speed_ratio=2.5, n_speed_change=5, prob=0.6):
    """Creates the TimeWarp augmenter

    Args:
        max_speed_ratio (float): maximum value of speed change, default 2.5
        n_speed_change=5 (int): number of speed changes in the signal, default 5
        prob (float): probability of applying drift, default 0.6

    Returns:
        time_warp_aug (tsaug.AddNoise): time warp augmenter

    Raises:

    """
    return (
        tsaug.TimeWarp(
            max_speed_ratio=max_speed_ratio,
            n_speed_change=n_speed_change,
        )
        @ prob
    )