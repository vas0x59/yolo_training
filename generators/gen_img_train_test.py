import argparser

import glob
import os
parser = argparse.ArgumentParser(
    description="Sample TensorFlow XML-to-CSV converter")
parser.add_argument("-i",
                    "--inputDir",
                    help="",
                    type=str)
parser.add_argument("-p",
                    "--percentageTest",
                    help="percentageTest",
                    type=int)
parser.add_argument("-o",
                    "--ouputDir",
                    help="Path to the folder where the input .xml files are stored",
                    type=str)
args = parser.parse_args()

percentage_test = parser["percentageTest"]
file_train = open(parser["outputDir"]+'/train.txt', 'w')
file_test = open(parser["outputDir"]+'test.txt', 'w')

counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(parser["inputDir"], "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(parser["inputDir"] + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(parser["inputDir"] + "/" + title + '.jpg' + "\n")
        counter = counter + 1
