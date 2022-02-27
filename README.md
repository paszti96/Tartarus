# Tartarus
Simulated Environment with Unity for Robust Object Detection

## Mission Statement 👨‍🎓
This research project was my Master's Thesis @ Budapest University of Technology and Economics. 👨🏻‍🎓
The project was awarded with scholarship by the [Artificial Intelligence National Laboratory (MILAB) of Hungary](https://mi.nemzetilabor.hu/) 

The main focus of deep learning research is the development of self-supervised learning methods, where the agent completes different detection tasks by understanding his environment, and not by relying on labeled training examples. A typical usage of self-supervised learning methods is to substitute obscured details from images or to estimate the impact of actions taken by robots. The main goal of the following thesis is to create an algorithm that is able to recognize different objects and their relevant visual properties in a simulated environment and to estimate the effect of different actions on them. In this thesis, I will not only present such a robust object detection algorithm, but also create a simulated industrial environment capable of generating the data needed for training quickly and easily.

## Setting 👨🏻‍💻
The environment consists of two main part: 

### RODSIE algorithm 🤖📷
This repository contains the Object Detection Algorithm which contains combinations of a [YOLO v5](https://github.com/ultralytics/yolov5) object detector and a [U-Net](https://en.wikipedia.org/wiki/U-Net)-based segmentation layer.

### Tartarus 🌍
Thia repository contains a simulated industrial environment that can be used to generate images and metadata for the deep learning algorithm. The simulation should also be modifiable and capable of generating randomized scenarios sufficient to create diverse train dataset. 
The simulated environment is made with [Unity Engine](https://unity.com/).

## The Design:
The simulation contains different scenarios; therefore, the simulated industrial building will have three different parts:
1. A conveyor belt with different small objects on it like barrels or tools.
2. A workshop for larger items, such as cars and industrial platforms.
3. And a floor that functions as an office. 

Different robotic arms stand at the two sides of the conveyor belt and at the workshop.
In the initial setting, there are 67 different objects. First, the 3D models were downloaded from the Asset Store or other third-party providers. Then, they are
imported into the project and saved with the required features as Prefabs.

## Images of the setting

## The output
