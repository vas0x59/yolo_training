import argparser

import glob
import os
parser = argparse.ArgumentParser(
    description="Sample TensorFlow XML-to-CSV converter")
parser.add_argument("-i",
                    "--inputDir",
                    help="",
                    type=str)
parser.add_argument("-o",
                    "--ouputFile",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
args = parser.parse_args()
file_train = open(args["outputFile"], 'w')

for pathAndFilename in glob.iglob(os.path.join(parser["inputDir"], "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_train.write(parser["inputDir"] + "/" + title + '.jpg' + "\n")
