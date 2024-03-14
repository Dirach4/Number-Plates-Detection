# License Plate Detection using OpenCV
This project demonstrates license plate detection using OpenCV, a popular computer vision library, and Python. The project utilizes a pre-trained Haar cascade classifier for detecting license plates in Real Time using Webcam.

## Source
1. YouTube [Real Time Car Number Plates Extraction in 30 Minutes 🔥| OpenCV Python | Computer Vision | EasyOCR](https://www.youtube.com/watch?v=ltpnWBBT7NI&t=344s)

2. GitHub[Car-Number-Plates-Detection](https://github.com/entbappy/Car-Number-Plates-Detection)

## Requirements

Install Python versi 3.11
Install [Conda Conda Documentation — conda 24.1.2 documentation](https://docs.conda.io/projects/conda/en/stable/)
Setup environment [Python for AI #1: Dev Environment Setup - YouTube](https://www.youtube.com/watch?v=yTJxDzqo4fQ)

## How to Install

1. Clone or Download Repository
2. ```bash
   pip install -r requirements.txt
   ```
3. if you encounter error :
   OpenCV(4.9.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:1272: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'
   Go to Error Handling down below

## Usage
Run Script number_plate.py
Press 's' to save the plate and look at the output at terminal
Press 'Ctrl+c' at terminal to exit the application.

## Eror Handling
Re install opencv-python if it has error with opencv

```bash
   pip uninstall opencv-python
   ```
   and
```bash
   pip install opencv-python
   ```
