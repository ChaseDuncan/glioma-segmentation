#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: config.py

import numpy as np

# unet model
DATA_SAMPLING = 'random' # all_positive, random, one_positive
###
# random: complete random sampling within entire volume.
# one_positive: at least one batch contain tumor label (label > 0)
# all_positive: all batch must contain tumor label (label > 0)
###
RESIDUAL = True
DEPTH = 5
DEEP_SUPERVISION = True
FILTER_GROW = True
INSTANCE_NORM = True
# Use multi-view fusion 3 models for 3 view must be trained
DIRECTION = 'axial' # axial, sagittal, coronal
MULTI_VIEW = False

# training config
BASE_LR = 0.001

CROSS_VALIDATION = False
CROSS_VALIDATION_PATH = "./5fold.pkl"
FOLD = 0
###
# Use when 5 fold cross validation
# 1. First run generate_5fold.py to save 5fold.pkl
# 2. Set CROSS_VALIDATION to True
# 3. CROSS_VALIDATION_PATH to /path/to/5fold.pkl
# 4. Set FOLD to {0~4}
###
#NO_CACHE = True
NO_CACHE = False
###
# if NO_CACHE = False, we load pre-processed volume into memory to accelerate training.
# set True when system memory loading is too high
###
TEST_FLIP = False
# Test time augmentation
DYNAMIC_SHAPE_PRED = False
# change PATCH_SIZE in inference if cropped brain region > PATCH_SIZE
ADVANCE_POSTPROCESSING = True
BATCH_SIZE = 2
PATCH_SIZE = [128, 128, 128]
INFERENCE_PATCH_SIZE = [128, 128, 128]
INTENSITY_NORM = 'modality' # different norm method
STEP_PER_EPOCH = 500
EVAL_EPOCH = 5

# data path
# BASEDIR = "/data/dataset/BRATS2018/" #'/data/dataset/BRATS2018/'

import argparse
# brats2018 = BRATS_SEG("/data/dataset/BRATS2018/", "training")

training_dir = 'training_t2'
testing_dir = 'val_t2'

BASEDIR = "/home/nfs/zpy/testing_dic/544proj/data/"

# TRAIN_DATASET = ['training']
# VAL_DATASET = 'val'   # val or val17 
# TEST_DATASET = 'val'

TRAIN_DATASET = [training_dir]
VAL_DATASET = testing_dir  
TEST_DATASET = testing_dir 

NUM_CLASS = 4
