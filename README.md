# Keyframe Detection
The script is used to detect the keyframes in a video

## Description
 keyframeDetector.py is an Python based script for extracting keyframes from a video. Video will be given as input and output will be the key frame images saved into the folder "keyframes"

## Requirements
 - python3
 - numpy
 - opencv3

## How to run
```
python keyframe.py --source path/to/video [--Thres (required threshold between frames)]
```
 A higher threshold will mean that there should be more difference between the frames for them to be key. It will have values anywhere from 1000000 to 5000000
