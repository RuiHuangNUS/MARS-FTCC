import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def visualize_robots_coordinate(y_position_list_new, x_position_list_new, theta_z, w):
    """
    可视化机器人位置和旋转后的坐标系，初始的x轴朝上，y轴朝右。
    
    参数：
    x_position_list : np.array
        机器人在x轴的坐标。
    y_position_list : np.array
        机器人在y轴的坐标。
    theta_z : float
        旋转角度，弧度制。
    w : float
        机器人正方形轮廓的尺寸。
    """
    # 绘制机器人的位置分布（位置保持不变）
    robot_size = w
    figure_size = (10, 10)
    plt.figure(figsize=figure_size)

    # 绘制固定的机器人位置
    plt.scatter(x_position_list_new, y_position_list_new, color='blue', label='individual units', s=100)
    for i in range(len(x_position_list_new)):
        plt.text(x_position_list_new[i], y_position_list_new[i], f"unit {i+1}\n({x_position_list_new[i]:.1f}, {y_position_list_new[i]:.1f})", fontsize=12, color='blue')

        # 为每个机器人添加一个正方形轮廓
        robot = Rectangle((x_position_list_new[i] - robot_size / 2, y_position_list_new[i] - robot_size / 2), 
                          robot_size, robot_size, fill=False, edgecolor='blue', linewidth=2)
        plt.gca().add_patch(robot)

    # 绘制坐标系，x轴朝上，y轴朝右
    plt.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='black', label="x-axis (before)")  # x朝上
    plt.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='black', label="y-axis (before)")  # y朝右

    # 在图中标注 x 和 y 坐标轴
    plt.text(0, 1.2, 'x', fontsize=15, color='black', ha='center', va='center')  # x轴朝上
    plt.text(1.2, 0, 'y', fontsize=15, color='black', ha='center', va='center')  # y轴朝右

    # 绘制旋转后的坐标系
    plt.quiver(0, 0, -np.sin(theta_z), np.cos(theta_z), angles='xy', scale_units='xy', scale=1, color='red', label=f"virtual x'-axis (after, θz={np.degrees(theta_z):.2f}°)")  # x'轴旋转
    plt.quiver(0, 0, np.cos(theta_z), np.sin(theta_z), angles='xy', scale_units='xy', scale=1, color='red', label="virtual y'-axis (after)")  # y'轴旋转

    # 在图中标注旋转后的 x' 和 y' 坐标轴
    plt.text(-np.sin(theta_z), np.cos(theta_z) + 0.2, "x'", fontsize=15, color='red', ha='center', va='center')
    plt.text(np.cos(theta_z) + 0.2, np.sin(theta_z), "y'", fontsize=15, color='red', ha='center', va='center')

    # 设置图形属性
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('Y Position')  # 原来的x轴成为y
    plt.ylabel('X Position')  # 原来的y轴成为x
    plt.title('Optimal virtual quadcopter coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()

# # 示例调用
# x_u_adjusted = np.array([1, 1, -1, -1])
# y_u_adjusted = np.array([-1, 1, -1, 1])
# optimal_theta_z = np.pi / 6  # 例如 30 度
# w = 2  # 机器人正方形的边长

# # 调用函数进行可视化
# visualize_robots(x_u_adjusted, y_u_adjusted, optimal_theta_z, w)
