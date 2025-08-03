#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
augment.py

Functions to augment timeseries data
Author: Mathias Roesler
Date: 08/25
"""

import tsaug as tsaug


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
