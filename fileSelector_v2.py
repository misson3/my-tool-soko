# Dec17, 2022, ms
# fileSelector_v2.py
# create out dir with count

import sys
import glob
import random
import shutil
import os


def randomlySelectFiles(file_dir, count):
    """
    rondomly select files and return their paths
    """
    files = glob.glob(file_dir + '/*.wav')
    selected_files = random.sample(files, count)
    # normpath
    selected_files = [os.path.normpath(p) for p in selected_files]
    return selected_files


def createOutDir(file_dir, count):
    """
    construct out dir path and create that dir under current dir
    """
    # remove the last '/' if there is
    # otherwise, basename will be ''
    file_dir = file_dir.rstrip('/')
    out_dir = './' + os.path.basename(file_dir) + '-selected-' + str(count)
    # create out_dir
    os.mkdir(out_dir)

    return out_dir


def copyFiles(paths, out_dir):
    """
    copy file in given pnaths to out_dir
    """
    # copy files into out_dir
    for p in paths:
        print(p)
        shutil.copy(p, out_dir)


if __name__ == '__main__':
    # copy specified number of files from in_dir into out_dir
    in_dir = sys.argv[1]
    count_to_select = int(sys.argv[2])
    selected_files = randomlySelectFiles(in_dir, count_to_select)
    out_dir = createOutDir(in_dir, count_to_select)
    copyFiles(selected_files, out_dir)
