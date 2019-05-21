import argparser

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
parser.add_argument("-b",
                    "--backupDir",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
parser.add_argument("-o",
                    "--outputFile",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
args = parser.parse_args()

file_classes = open(args["classes"], "r")
CLASSES = file_classes.read().split('\n')

file_out = open(args["outputFile"], 'w')
file_out.write("classes = " + str(len(CLASSES)))
file_out.write("train = " + args["datasetPaths"] + '/train.txt')
file_out.write("test = " + args["datasetPaths"] + '/test.txt')
file_out.write("names = " + args["classes"])
file_out.write("backup = " + args["backupDir"]+'/')