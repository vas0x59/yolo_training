import argparse

import glob
import os
parser = argparse.ArgumentParser(
    description="Sample TensorFlow XML-to-CSV converter")
parser.add_argument("-c",
                    "--classes",
                    help="",
                    type=str)
parser.add_argument("-t",
                    "--datasetPaths",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
parser.add_argument("-bs",
                    "--bathSize",
                    help="Path to the folder where the input .xml files are stored",
                    type=int)
parser.add_argument("-b",
                    "--backupDir",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
parser.add_argument("-o",
                    "--outputFile",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
parser.add_argument("-cf",
                    "--cfgFile",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
parser.add_argument("-co",
                    "--cfgFileOut",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
args = parser.parse_args()

file_classes = open(args.classes, "r")
CLASSES = file_classes.read().split('\n')[:-1]

file_out = open(args.outputFile, 'w')
file_out.write("classes = " + str(len(CLASSES)) + "\n")
# print(CLASSES)
file_out.write("train = " + args.datasetPaths + '/train.txt' + "\n")
file_out.write("test = " + args.datasetPaths + '/test.txt' + "\n")
file_out.write("names = " + args.classes + "\n")
file_out.write("backup = " + args.backupDir+'/' + "\n")

cfg_file = open(args.cfgFile, 'r')
cfg = cfg_file.readlines()

cfg[2] = "batch=" + str(args.bathSize) + "\n"
cfg[3] = "subdivisions=" + str(24) + "\n"

cfg[126] = "filters=" + str((len(CLASSES) + 5)*3) + "\n"
cfg[170] = "filters=" + str((len(CLASSES) + 5)*3) + "\n"

cfg[134] = "classes=" + str(len(CLASSES)) + "\n"
cfg[176] = "classes=" + str(len(CLASSES)) + "\n"

cfg_out = open(args.cfgFileOut, 'w+')
cfg_out.writelines(cfg)
# cfg_str = ""
# for i in cfg:
#     cfg_str+=i

# cfg_str = cfg_str.replace("batch=1", "batch="+str(args.bathSize))
# cfg_str = cfg_str.replace("classes=80", "classes="+str(len(CLASSES)))
# cfg = cfg.replace("classes=80", "classes="+str(len(CLASSES)))
