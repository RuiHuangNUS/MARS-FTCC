# MARS-FTCC: Robust Fault-Tolerant Control and Agile Trajectory Planning for Modular Aerial Robotic Systems

## Project Overview
The project **MARS-FTCC** consists of two folders, which correspond to the **Algorithm** and **Simulation** in the paper that show the following two advantages of our method.
1. We propose a novel fault-tolerant control reallocation method that adapts to arbitrary number of modular robots and their assembly formations.
2. We propose an agile trajectory planning method for MARS of arbitrary configurations, which is collision-avoiding and dynamically feasible. 

Please find out more details in our paper: ["Robust Fault-Tolerant Control and Agile Trajectory Planning for Modular Aerial Robotic Systems"](https://arxiv.org/pdf/2503.09351)

|                     A video  of this project             |
:----------------------------------------------------------------------------------------------------------------------------------:
[![NetFlix on UWP](https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/MARS_FTCC.png?raw=true)](https://youtu.be/H8Fmif7PbdM "NetFlix on UWP")
Youtube: https://youtu.be/H8Fmif7PbdM Bilibili: xxx (Coming soon)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Motivation: Dynamics Aware Planning and Control](#1-motivation-dynamics-aware-planning-and-control)
3. [Fault-Tolerant Control](#2-fault-tolerant-control)  
   - [Fault-Tolerant via Control Reallocation](#21-fault-tolerant-via-control-reallocation)  
   - [Fault-Tolerant Control During Flight](#22-fault-tolerant-control-during-flight)
4. [Comparison with the Baseline Method](#3-comparison-with-the-baseline-method)  
   - [Self-Reconfiguration Fault-Tolerant Control](#31-self-reconfiguration-fault-tolerant-control)  
   - [Collision-Free Trajectory Planning](#32-collision-free-trajectory-planning)
5. [How to Use](#4-how-to-use)  
   - [Dependency Packages](#41-dependency-packages)  
   - [Algorithm 1](#42-algorithm-1)
   - [Simulation](#43-simulation)
6. [Contact Us](#5-contact-us)
7. [Cite](#cite)
8. [References](#references)

## 1 Motivation​: Dynamics Aware Planning and Control​

MARS is tasked with tracking a collision-free trajectory with one faulty unit. The faulty propellers are marked in red. (a) MARS cannot accurately follow the planned trajectory using an existing collision-free trajectory generation method [[2]](#2) under a simple PID control. (b) MARS fails to track the trajectory planned with [[2]](#2) under our proposed fault-tolerant control. (c) MARS can track the trajectory planned with our proposed dynamics-aware planning method relatively accurately under our proposed fault-tolerant control.

<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/why_agile.gif?raw=true" alt="diagram", width="900"/>
</div>

Advantages:
1. Dynamics Aware PnC ​Enhance dynamic feasibility​
2. Collision-free flying and reduced tracking errors ​
3. Less yaw motion ​(enhancing safety)

## 2 Fault-tolerant control
### 2.1 Fault-tolerant via Control Reallocation​
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/FT.gif?raw=true" alt="diagram", width="900"/>
</div>

Advantages:
1. No need for optimization with an objective function (Less time consumption)
2. The optimal configuration ensures controllability and is theoretically guaranteed

### 2.2 ​Fault-Tolerant Control During Flight​
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/FT_flight.gif?raw=true" alt="diagram", width="900"/>
</div>

## 3 Comparison with the baseline method

### 3.1 Self-Reconfiguration Fault-Tolerant Control ​ [[1]](#1)
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/3x3_plus_self_reconfiguration.gif?raw=true" alt="diagram", width="900"/>

  3x3 Plus Assembly
</div>

<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/3x1_self_reconfiguration.gif?raw=true" alt="diagram", width="350"/>

  3x1 Assembly
</div>

Advantages:
1. No oscillation (control robustness): significantly reduces oscillations during docking and separation compared to previous work [[1]](#1).

### 3.2 Collision-Free Trajectory Planning​  [[2]](#2)
(a) Normal assembly (Dynamics Agnostic Planning  [[1]](#1)) |   (b) Normal assembly with Dynamics Aware Planning (Ours)  | (c) Post-failure assembly with fault-tolerance (Dynamics Agnostic Planning  [[1]](#1)) |   (d) Post-failure assembly with fault-tolerance (Ours Dynamics Aware Planning)
:---------------------------------------------------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------------:
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/collision_free_4x1_3.gif?raw=true" alt="diagram", width="900"/>
  Fault in No.3 of 4×1 Assembly (4X)
</div>

<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/collision_free_4x1_4.gif?raw=true" alt="diagram", width="900"/>
  Fault in No.4 of 4×1 Assembly (4X)
</div>

<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/collision_free_3x2_2.gif?raw=true" alt="diagram", width="900"/>
  Fault in No.2 of 3×2 Assembly (4X)
</div>

Advantages:
1. Enhanced stability (control robustness) and better guarantee of collision avoidance compared to  [[1]](#1).
2. Reduced tracking errors

## 4 How to Use
To reproduce the simulation results presented in the paper, simply follow the steps outlined below, sequentially, after downloading and decompressing all the necessary folders. The self-reconfiguration is based on our previous work [[3]](#3), and the control methods of different configurations are based on previous works [[4]](#4).

### 4.1 Dependency Packages
Please make sure that the following packages have already been installed before running the source code.
* CoppeliaSim: version 4.6.0 Info: https://www.coppeliarobotics.com/

### 4.2 Dynamical trajectory
```sh
sudo apt-get install gcc g++ make gfortran cmake libomp-dev
/usr/bin/python3 -m pip3 install pygame==2.0.0.dev12 
/usr/bin/python3 -m pip3 install catkin_pkg
/usr/bin/python3 -m pip3 uninstall em
/usr/bin/python3 -m pip3 install empy==3.3.4
```

```sh
cd Dynamical_Trajectory
./build.sh
source devel/setup.bash
roslaunch plan_manager run_MARS3x2.launch 
```

### 4.3 Simulation
#### a. Fault-tolerant via Control Reallocation​
1. Simulation: 3×2 assembly (faults in No.2, No.3, No.2 and 4, No.2 and 5, No.3 and 4), Open the file '**3X2_Mod_independent_No.X.ttt**' in the folder '**Simulation/FTC_Reallocation**'

#### b. Self-Reconfiguration Fault-Tolerant Control
1. Simulation 1: Full disassembly in a 3×1 assembly, Open the file '**3x1_full_disassembly_iros.ttt**' in the folder '**Simulation**'

#### c. Collision-Free Trajectory Planning
Remember to modify the reference path before use, the corresponding data can be found in the folder '**Simulation/trajectory_planning/x_trajectory_data**'

1. Simulation 1: 4×1 assembly (fault in No.3), Open the file '**4X1_3_fault_path_planning_obs.ttt**' in the folder '**Simulation/trajectory_planning**'

2. Simulation 1: 4×1 assembly (fault in No.4), Open the file '**4X1_4_fault_path_planning_obs.ttt**' in the folder '**Simulation/trajectory_planning**'

3. Simulation 1: 3×2 assembly (fault in No.2), Open the file '**3X2_2_fault_path_planning_obs.ttt**' in the folder '**Simulation/trajectory_planning**'

## 5 Contact Us
If you encounter a bug in your implementation of the code, please do not hesitate to inform me.
* Name: Mr. Rui Huang
* Email: ruihuang@u.nus.edu

## Cite
If you find this work helpful, please consider citing our paper.

```
@misc{huang2025robust,
      
      title={Robust Fault-Tolerant Control and Agile Trajectory Planning for Modular Aerial Robotic Systems}, 
      author={Rui Huang and Zhenyu Zhang and Siyu Tang and Zhiqian Cai and Lin Zhao},
      year={2025},
      eprint={2503.09351},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2503.09351}, 
}
```
## References
<a id="1">[1]</a> N. Gandhi, D. Saldana, V. Kumar, and L. T. X. Phan, “Self-reconfiguration in response to faults in modular aerial systems,” IEEE Robotics and Automation Letters, vol. 5, no. 2, pp. 2522–2529, 2020.

<a id="2">[2]</a> J. Wang, T. Zhang, Q. Zhang, C. Zeng, J. Yu, C. Xu, L. Xu, and F. Gao, “Implicit swept volume sdf: Enabling continuous collision-free trajectory generation for arbitrary shapes,” ACM Transactions on Graphics (TOG), vol. 43, no. 4, pp. 1–14, 2024. https://github.com/ZJU-FAST-Lab/Implicit-SVSDF-Planner

<a id="3">[3]</a> Rui Huang, Siyu Tang, Zhiqian Cai, and Lin Zhao, “Robust Self-Reconfiguration for Fault-Tolerant Control of Modular Aerial Robot Systems,” IEEE International Conference on Robotics & Automation (ICRA), 2025. Available: https://github.com/RuiHuangNUS/MARS-Reconfig https://arxiv.org/pdf/2503.09376

<a id="4">[4]</a> R. HUANG, H. SHENG, C. Qian, R. Ziting, X. Zhen, L. Jiacheng, and L. Tong, “Adaptive configuration control of combined uavs based on leader-wingman mode,” Chinese Journal of Aeronautics, 2024.