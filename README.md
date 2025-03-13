# MARS-FTCC: Robust Fault-Tolerant Control and Agile Trajectory Planning for Modular Aerial Robotic Systems (Coming soon)

## Project Overview
The project **MARS-FTCC** consists of two folders, which correspond to the **Algorithm** and **Simulation** in the paper that show the following two advantages of our method.
1. We propose a novel fault-tolerant control reallocation method that adapts to arbitrary number of modular robots and their assembly formations.
2. We propose an agile trajectory planning method for MARS of arbitrary configurations, which is collision-avoiding and dynamically feasible. 

Please find out more details in our paper: "Robust Fault-Tolerant Control and Agile Trajectory Planning for Modular Aerial Robotic Systems" 

|                     A video  of this project             |
:----------------------------------------------------------------------------------------------------------------------------------:
[![NetFlix on UWP](https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/movie_cover.png?raw=true)](https://youtu.be/SB0hwK33088 "NetFlix on UWP")
https://youtu.be/SB0hwK33088
|                     A diagram of the Agile Trajectory Planning             |
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/Fig1.png?raw=true" alt="diagram" width="400"/>
</div>
MARS is tasked with tracking a collision-free trajectory with one faulty unit. The faulty propellers are marked in red. (a) MARS cannot accurately follow the planned trajectory using an existing collision-free trajectory generation method~\cite{wang2024implicit} under a simple PID control. (b) MARS fails to track the trajectory planned with~\cite{wang2024implicit} under our proposed fault-tolerant control. (c) MARS can track the trajectory planned with our proposed dynamics-aware planning method relatively accurately under our proposed fault-tolerant control.

Todo:
<!-- ## Table of contents
1. [Project Overview](#project-Overview)
2. [Dependency Packages](#Dependency-Packages)
3. [How to Use](#How-to-Use)
      1. [A: Distributed Learning of Adaptive Weightings](#A-Distributed-Learning-of-Adaptive-Weightings)
      2. [B: Distributed Learning of Adaptive References](#B-Distributed-Learning-of-Adaptive-References)
4. [Contact Us](#Contact-Us) -->

## 1 Motivation​: Dynamics Aware Planning and Control​

We Calculate the optimal configuration with maximum remaining control authority using controllability margin (CM)
  (a) Dynamics Agnostic PnC [1]​ (No Fault)     |   (b) Dynamics Aware PnC (Ours)​ (No Fault)​
:---------------------------------------------------------------:|:--------------------------------------------------------------:
![cl_training](https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/robot_configuration_3x2.gif) | ![ol_training](https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/robot_configuration_3x3.gif)

Advantages:
1. Dynamics Aware PnC ​Enhance dynamic feasibility​
2. Collision-free flying and reduced tracking errors ​
3. Less yaw motion ​(enhancing safety)

## 2 Methods
### 2.1 Fault-tolerant via Control Re-allocation​

We Calculate the optimal configuration with maximum remaining control authority using controllability margin (CM)
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/FT.gif?raw=true" alt="diagram"/>
</div>

Advantages:
1. No need for optimization with an objective function (Less time consumption)
2. The optimal configuration ensures controllability and is theoretically guaranteed

### 2.2 ​Fault-Tolerant Control During Flight​
We designed the Minimum Controllable Subassembly to enable the transfer of faulty units.
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/self_reconfiguration_flow.png?raw=true" alt="diagram" width="400"/>
</div>

Advantages:
The minimum controllable subassembly ensures the safety of faulty units

### 2.3 Agile Trajectory Planning

### 2.4 Collision-free Trajectory Planning​

 (a) 3×2 assembly: full disassembly  |   (b) 3×2 assembly: partial disassembly 
:---------------------------------------------------------------:|:--------------------------------------------------------------:
![cl_training](https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/full_self_reconfiguration_3x2.gif) | ![ol_training](https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/partial_self_reconfiguration_3x2.gif)
 (c) 3×3 assembly: full disassembly  |   (d) 3×3 assembly: partial disassembly 
![cl_training](https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/full_self_reconfiguration_3x3.gif) | ![ol_training](https://github.com/RuiHuangNUS/MARS-Reconfig/blob/main/Picture/partial_self_reconfiguration_3x3.gif)

Advantages:
Each step of disassembly and assembly is ensured to be theoretically optimal

## 3 Comparison with the baseline method

### 3.1 Self-Reconfiguration Fault-Tolerant Control ​ [[1]](#1)

3x1 Assembly

<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/3x3_plus_combined.gif?raw=true" alt="diagram"/>
</div>

3x3 Plus Assembly

<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/3x1_combined.gif?raw=true" alt="diagram"/>
</div>

Advantages:
1. No oscillation (control robustness): significantly reduces oscillations during docking and separation compared to previous work [[1]](#1).

### 3.1 Collision-Free Trajectory Planning​  [[2]](#2)
 (a) Normal assembly (Dynamics Agnostic Planning [1]) |   (b) Normal assembly with Dynamics Aware Planning (Ours)  | (c) Post-failure assembly with fault-tolerance (Dynamics Agnostic Planning [1]) |   (d) Post-failure assembly with fault-tolerance (Ours Dynamics Aware Planning)
:---------------------------------------------------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------------:

Fault in No.3 of 4×1 Assembly
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/collision_free_4x1_3.gif?raw=true" alt="diagram"/>
</div>

Fault in No.4 of 4×1 Assembly
<div align="center">
  <img src="https://github.com/RuiHuangNUS/MARS-FTCC/blob/main/Picture/collision_free_4x1_4.gif?raw=true" alt="diagram"/>
</div>

Fault in No.2 of 3×2 Assembly



Advantages:
1. Enhanced stability (control robustness) and better guarantee of collision avoidance compared to [1].
2. Reduced tracking errors

## 5 How to Use
First and foremost, the implementation for MARS-Reconfig is straightforward to setup. The source code has been comprehensively annotated to facilitate ease of use. To reproduce the simulation results presented in the paper, simply follow the steps outlined below, sequentially, after downloading and decompressing all the necessary folders. All self-reconfiguration is based on our previous work [[3]](#3), and the control methods of different configurations are based on previous works [[4]](#4).

### 5.1 Dependency Packages
Please make sure that the following packages have already been installed before running the source code.
* CoppeliaSim: version 4.6.0 Info: https://www.coppeliarobotics.com/
* imageio: version 2.9.0 Info: https://imageio.readthedocs.io/

### 5.2 Algorithm 1 Find Optimal Reconfiguration

1. Open the Python file '**Algorithm1_Find_Optimal_Reconfiguration.py**' in the folder '**Algorithm**'
2. Before running, please do the following settings:
   * Set the number of quadrotors on line 225 and 226.
   * Set the Fault status of four rotors on line 229 (the default value is rotor_faults = [True, True, True, True]).
   * Set non-symmetric positions on line 231 (We provided examples of 3x2 and 3x3 assemblies for demonstration).

### 5.3 Algorithm 3 Plan Disassembly and Assembly Sequence

1. Open the Python file '**Algorithm3_Plan_Disassembly_Assembly_Sequence.py**' in the folder '**Algorithm**'
2. Before running, please do the following settings:
   * Set the configuration on line 14.

### 5.4 Simulation
1. Simulation 1: Full disassembly in a 3×2 assembly, Open the file '**3x2_full_disassembly.ttt**' in the folder '**Simulation**'

## 6 Contact Us
If you encounter a bug in your implementation of the code, please do not hesitate to inform me.
* Name: Mr. Rui Huang
* Email: ruihuang@nus.edu.sg

## Cite
@misc{huang2025robust,
      title={Robust Fault-Tolerant Control and Agile Trajectory Planning for Modular Aerial Robotic Systems}, 
      author={Rui Huang and Zhenyu Zhang and Siyu Tang and Zhiqian Cai and Lin Zhao},
      year={2025},
      eprint={2503.09351},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2503.09351}, 
}

## References
<a id="1">[1]</a> N. Gandhi, D. Saldana, V. Kumar, and L. T. X. Phan, “Self-reconfiguration in response to faults in modular aerial systems,” IEEE Robotics and Automation Letters, vol. 5, no. 2, pp. 2522–2529, 2020.

<a id="2">[2]</a> J. Wang, T. Zhang, Q. Zhang, C. Zeng, J. Yu, C. Xu, L. Xu, and F. Gao, “Implicit swept volume sdf: Enabling continuous collision-free trajectory generation for arbitrary shapes,” ACM Transactions on Graphics (TOG), vol. 43, no. 4, pp. 1–14, 2024.

<a id="3">[3]</a> Rui Huang, Siyu Tang, Zhiqian Cai, and Lin Zhao, “Robust Self-Reconfiguration for Fault-Tolerant Control of Modular Aerial Robot Systems,” IEEE International Conference on Robotics & Automation (ICRA), 2025. Available: https://github.com/RuiHuangNUS/MARS-Reconfig https://arxiv.org/abs/2503.09376

<a id="4">[4]</a> R. HUANG, H. SHENG, C. Qian, R. Ziting, X. Zhen, L. Jiacheng, and L. Tong, “Adaptive configuration control of combined uavs based on leader-wingman mode,” Chinese Journal of Aeronautics, 2024.