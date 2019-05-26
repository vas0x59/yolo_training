#!/bin/bash

echo "Hello world"

# Configs
in_dir="/home/vasily/Projects/datasets/small_danon/small_yolo"
classes="/home/vasily/Projects/datasets/small_danon/names.names"
work_dir="./danon"
cfg="./cfgs/yolov3_tiny.cfg"
bs=5
per=10
mkdir $work_dir
mkdir $work_dir"/backup"
echo "gen_img_train_test"
python ./generators/gen_img_train_test.py -i $in_dir -p $per -o $work_dir

echo "gen_training_config"
python ./generators/gen_training_config_yolov3_tiny.py -c $classes -t $work_dir -b $work_dir"/backup" -o $work_dir"/obj.data" -bs $bs -cf $cfg -co $work_dir"/yolov3_cfg.cfg"
