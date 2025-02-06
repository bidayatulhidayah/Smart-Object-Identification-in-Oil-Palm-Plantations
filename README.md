# Smart-Object-Identification-in-Oil-Palm-Plantations with GUI
Project for MAD4PalmOil Hackathon 2024
OPERAI (Oil Palm Environment Recognition AI) - Object Detection GUI using YOLOv3

## Overview

OPERAi is a real-time object detection application using YOLOv3 and OpenCV, integrated with a graphical user interface (GUI) built with Tkinter. The application processes live video feed from a webcam, detects objects, and allows users to take screenshots of detected objects with a timestamp.

## Features

- Real-time Object Detection: Utilizes YOLOv3 for fast and accurate object recognition.
- Graphical User Interface: Built using Tkinter for ease of use.
- Live Camera Feed: Captures video input from the default webcam.
- Screenshot Functionality: Saves snapshots of detected objects with a timestamp.
- Customizable UI Elements: Displays logos and instructions within the GUI.
- Detection Control: Start, stop, and capture frames with buttons.

## Installation & Usage

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV
- NumPy
- Tkinter (built-in with Python)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/OPERAi.git
    cd OPERAi
    ```

2. Install required dependencies:
    ```sh
    pip install opencv-python numpy
    ```

### Running the Application

1. Execute the script:
    ```sh
    python opera_ai.py
    ```

2. Utilize the GUI controls:
    - **Start Detection**: Initiates real-time object detection.
    - **Stop Detection**: Pauses object detection.
    - **Screenshot**: Captures and saves a snapshot with detected objects.
    - **Quit**: Exits the application.

## File Structure

📂 OPERAi

| File Name        | Description                      |
|-----------------|--------------------------------|
| `opera_ai.py`   | Main application script       |
| `yolov3.weights`| YOLOv3 model weights         |
| `yolov3.cfg`    | YOLOv3 configuration file    |
| `coco.names`    | COCO class labels            |
| `logo.png`      | Primary logo for the GUI     |
| `logo2.png`     | Secondary logo               |

## Screenshot Storage

Captured images are automatically stored in a folder named OPERAi_screenshot on the user's Desktop. The filenames include timestamps and detected object names for easy reference.

## License

This project is released under the MIT License

## Acknowledgments

- YOLO (You Only Look Once): Core algorithm for object detection.
- OpenCV: Utilized for image processing.
- Tkinter: Employed for building the graphical user interface.

## Flowchart 

![image](https://github.com/user-attachments/assets/d4cc9aea-6f38-4988-a0fb-0efe8ef69022)

## Graphic User Interface (GUI)

![image](https://github.com/user-attachments/assets/934351e0-0297-4284-9c60-64079e861229)
![image](https://github.com/user-attachments/assets/a606d111-bb46-42ea-933f-a84c94237474)


## Reference
![example_with_bounding_boxes](https://github.com/user-attachments/assets/2f22bec1-b5a9-4adb-b7c8-8b2c352c1adb)

