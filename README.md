# JB Embodied AI Robot Platform

## Objective

Build an intelligent robot system based on:

- ROS2 Humble
- RDK S100
- Computer Vision
- LLM Agent

## Current Status

### Environment

- Ubuntu 22.04.5 LTS
- Python 3.10.12
- ROS2 Humble

### Completed

- [x] Ubuntu robotics workstation
- [x] ROS2 installation
- [x] ROS2 communication test

## Architecture

User
|
LLM Agent
|
ROS2
|
RDK S100
|
Robot Controller
|
Actuators


JB_Embodied_AI_Robot

│

├── README.md                 # Project introduction

│

├── docs/                     # Engineering documents

│

├── src/                      # ROS2 source code

│   │

│   ├── jb_robot_driver       # Hardware interface

│   │

│   ├── jb_control            # Control algorithms

│   │

│   ├── jb_navigation         # Navigation

│   │

│   └── jb_robot_demo         # ROS2 learning package

│

├── vision/                   # Computer Vision

│

├── llm_agent/                # LLM interaction layer

│

├── hardware/                 # Robot hardware analysis

│

└── scripts/                  # Utility scripts


