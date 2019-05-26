#!/bin/bash

echo "Hello Training"

work_dir="./danon"


~/darknet/darknet detector train $work_dir"/obj.data" $work_dir"/yolov3_cfg.cfg" darknet53.conv.74