#!/bin/bash

echo "Hello world"

# Configs
in_dir="/home/vasily/Projects/datasets/arduino_raspberry_metro/train"
classes="/home/vasily/Projects/datasets/arduino_raspberry_metro/names.names"
work_dir="./work"
per=10

echo "gen_img_train_test"
python ./generators/gen_img_train_test.py -i $in_dir -p $per -o $work_dir
python ./generators/gen_training_config.py -c $classes -t $work_dir -b $work_dir"/backup" -o $work_dir"/obj.data"
