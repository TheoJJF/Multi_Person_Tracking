# Multi_Person_Tracking

This repository contains 3 YOLOv8 models, 2 of which are fine tuned further to enhance performace. Using the latest version of the popular "You Only Look Once" (YOLO) algorithm and non-max suppression, yielding highly accurate pedestrian tracking.

![fine_tuned2_model](https://github.com/user-attachments/assets/b7f582cb-2186-4b7a-b1c1-13a584b09b6c)

Due to the nature

## 🚀 Getting Started

### Cloning the repository

```
git clone https://github.com/TheoJJF/Multi_Person_Tracking.git
cd Multi_Person_Tracking
```

### Setting up environment [Optional] 

```
conda create -n myEnvironment
conda activate myEnvironment
```

### Installing dependencies

```
pip3 install -r requirements.txt
```

### Downloading `sample.mp4` video

```
python3 src/setup/video_installer.py
```

## ⌨️ Running the script

```
python3 src/core/tracker.py --input_video_path path/to/video --output_video_output path/to/output  
```

This is the bare minimum of arguments needed to run the script. Further adjustments can be made using the list of script arguments below.

## 🛠️ Script Arguments
There are a few places for potential adjustments. Below contains a list of possible arguments. 

- `--input_video_path`
    - REQUIRED
    - The relative path of the video file that will be annotated.

- `--output_video_path`
    - REQUIRED
    - The relative path of the annotated output video file.

- `--model_path`
    - OPTIONAL
    - The relative path of the model file that the script will use for annotations. 
        - Default value: `models/default.pt` 

- `--confidence_threshold`
    - OPTIONAL
    - The threshold used to measure how confident the model at detecting the object.
        - Default value: `0.3`

- `--iou_threshold`
    - OPTIONAL
    - The threshold used to determine whether multiple bounding boxes belong to the same or different object.
        - Default value: `0.7`
