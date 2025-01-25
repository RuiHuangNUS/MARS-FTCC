import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

def rotate_point_around_center(x, y, cx, cy, theta_z):
    """绕中心点 (cx, cy) 旋转 (x, y) 角 theta_z"""
    x_new = (x - cx) * np.cos(theta_z) - (y - cy) * np.sin(theta_z) + cx
    y_new = (x - cx) * np.sin(theta_z) + (y - cy) * np.cos(theta_z) + cy
    return x_new, y_new

def visualize_robots(x_position_list, y_position_list, x_sol, y_sol, F_values, w, theta_z, scale_factor=0.5):
    """
    可视化原始和优化后的机器人位置和力大小，x轴朝上，y轴朝右，并绘制旋转后的坐标系。
    
    参数：
    x_position_list : np.array
        机器人原始的x轴的坐标（朝上）。
    y_position_list : np.array
        机器人原始的y轴的坐标（朝右）。
    x_sol : np.array
        机器人优化后的x坐标。
    y_sol : np.array
        机器人优化后的y坐标。
    F_values : np.array
        作用在每个机器人的力的大小。
    w : float
        机器人正方形轮廓的尺寸。
    theta_z : float
        旋转角度，弧度制。
    scale_factor : float
        缩放因子，用来调整圆圈大小。
    """
    # 绘制机器人的初始位置分布（原始坐标）
    robot_size = w
    figure_size = (10, 10)
    plt.figure(figsize=figure_size)

    # 绘制旋转后的机器人框
    for i in range(len(x_position_list)):
        cx, cy = x_position_list[i], y_position_list[i]  # 中心点

        # 矩形四个顶点的初始位置（未旋转）
        rect_corners = np.array([
            [cx - robot_size / 2, cy - robot_size / 2],
            [cx + robot_size / 2, cy - robot_size / 2],
            [cx + robot_size / 2, cy + robot_size / 2],
            [cx - robot_size / 2, cy + robot_size / 2]
        ])

        # 旋转每个框的顶点
        rotated_corners = np.array([rotate_point_around_center(x, y, cx, cy, theta_z) for x, y in rect_corners])
        # 绘制旋转后的矩形框
        robot_polygon = Polygon(rotated_corners, fill=False, edgecolor='blue', linewidth=2)
        plt.gca().add_patch(robot_polygon)
        
        # 绘制中心点
        plt.scatter(cx, cy, color='blue', label='Initial units' if i == 0 else "", s=100)

    # 连接优化后的机器人位置之间的任意两点
    for i in range(len(x_sol)):
        for j in range(i+1, len(x_sol)):
            plt.plot([x_sol[i], x_sol[j]], [y_sol[i], y_sol[j]], color='orange', linestyle='-', linewidth=1)

    # 绘制优化后的机器人位置并显示力大小
    max_force = max(F_values)
    for i in range(len(x_sol)):
        plt.scatter(x_sol[i], y_sol[i], color='orange', label='virtual multirotor' if i == 0 else "", s=100)

        # 添加机器人力大小的圆圈，圆圈大小与力成正比，使用缩放因子调整大小
        circle_radius = (F_values[i] / max_force) * scale_factor  # 使用最大力值进行归一化并乘以缩放因子
        circle = Circle((x_sol[i], y_sol[i]), circle_radius, color='green', alpha=0.5)
        plt.gca().add_patch(circle)
        plt.scatter(x_sol[i], y_sol[i], color='green', label='virtual propeller' if i == 0 else "", s=200)
        # 在圆圈旁边显示力的大小
        plt.text(x_sol[i], y_sol[i], f"{F_values[i]:.2f}", fontsize=12, color='black')

    # 绘制 PX4 坐标系，x轴朝上，y轴朝右
    plt.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1.1, color='black', label="x-axis")  # x朝上
    plt.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1.1, color='black', label="y-axis")  # y朝右

    # 绘制旋转后的坐标系 x' 和 y'
    plt.quiver(0, 0, -np.sin(theta_z), np.cos(theta_z), angles='xy', scale_units='xy', scale=1.1, color='red', label="virtual x'-axis (optimal theta)")  # 绘制x'轴
    plt.quiver(0, 0, np.cos(theta_z), np.sin(theta_z), angles='xy', scale_units='xy',  scale=1.1, color='red', label="virtual y'-axis (optimal theta)")  # 绘制y'轴

    # 在图中标注原始的 x 和 y 坐标轴
    plt.text(0, 1.2, 'original x', fontsize=12, color='black', ha='center', va='center')  # x轴朝上
    plt.text(1.2, 0, 'original y', fontsize=12, color='black', ha='center', va='center')  # y轴朝右

    # 在图中标注旋转后的 x' 和 y' 坐标轴
    plt.text(-np.sin(theta_z), np.cos(theta_z), "virtual x'", fontsize=12, color='red', ha='center', va='center')
    plt.text(np.cos(theta_z),  np.sin(theta_z), "virtual y'", fontsize=12, color='red', ha='center', va='center')

    # 设置图形属性
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    # plt.xlim(-8, 8)
    # plt.ylim(-8, 8)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('Y Position')  # 原来的x轴，现在是y轴方向
    plt.ylabel('X Position')  # 原来的y轴，现在是x轴方向
    plt.title('Initial units and virtual multirotor')
    plt.legend()
    plt.grid(True)
    plt.show()



# # 示例参数
# w = 1  # 定义宽度
# x_position_list = np.array([w, w, 0, 0])  # 输入的 x 坐标列表
# y_position_list = np.array([-w, 0, -w, 0])  # 输入的 y 坐标列表

# # 优化后的坐标和力
# x_sol = [0.18386493044579885, -0.1904072435489806, 0.18782872282247878, -0.1881533539099044]
# y_sol = [0.3656991380104493, -0.3787408846901053, -0.39340019649653774, 0.363326141159753]
# F_sol = [41.80029145627925, 38.76074895936324, 38.94182002020051, 40.497139564157024]

# # 定义旋转角度
# theta_z = np.pi / 4  # 45度角

# # 调用函数进行可视化，缩小圆圈至原来的50%
# visualize_robots(x_position_list, y_position_list, x_sol, y_sol, F_sol, w, theta_z, scale_factor=0.3)
