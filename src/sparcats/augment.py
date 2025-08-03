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
