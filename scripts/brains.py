#!/usr/bin/env python
# coding: utf-8

#    +"Brats18_TCIA08_469_1/Brats18_TCIA08_469_1_flair.nii.gz"

from nilearn import plotting
import nibabel as nib
import gzip
import os

hgg_data_dir = "/home/cddunca2/data/miccai-brats-2018-data-training/HGG/" 
f_pos = ".nii.gz" 

modes = ["_flair", "_t1ce", "_t2", "_seg", "_t1"]
dir_lst = os.listdir(hgg_data_dir)

for data_dir in dir_lst:
    out_dir="images/"+data_dir
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    for mode in modes:
        fname = data_dir+mode
        full_fname = hgg_data_dir+data_dir+"/"+fname+f_pos
        img = nib.load(full_fname)
        display = plotting.plot_img(img, display_mode='z', cut_coords=[65])
        display.savefig(out_dir+"/"+fname+'.png')
        display.close()

