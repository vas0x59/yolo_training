#!/bin/bash

echo "Hello Training"

work_dir="./work_416"


~/darknet/darknet detector train $work_dir"/obj.data" $work_dir"/yolov3_tiny_cfg.cfg" darknet53.conv.74