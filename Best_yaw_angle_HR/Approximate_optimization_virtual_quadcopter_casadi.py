import casadi as ca
import numpy as np
import matplotlib.pyplot as plt
from visualize_robots_rotor_position import visualize_robots
from visualize_robots_coordinate import visualize_robots_coordinate

# 定义函数计算质心
def calculate_center_of_mass(x_position_list, y_position_list):
    """Calculate the center of mass for the given position lists"""
    x_center_of_mass = np.mean(x_position_list)
    y_center_of_mass = np.mean(y_position_list)
    return x_center_of_mass, y_center_of_mass

# 定义函数调整位置相对于质心
def adjust_relative_positions(x_position_list, y_position_list, x_center_of_mass, y_center_of_mass):
    """Adjust position lists relative to the center of mass"""
    x_position_list_adjusted = x_position_list - x_center_of_mass
    y_position_list_adjusted = y_position_list - y_center_of_mass
    return x_position_list_adjusted, y_position_list_adjusted

# 参数定义
w = 1  # 定义宽度 w
# x_i = np.array([0.22, -0.22,  0.22, -0.22])
# y_i = np.array([-0.22, 0.22,  0.22, -0.22])
x_i = np.array([0.22, -0.22, 0.22, -0.22])
y_i = np.array([0.22, -0.22, -0.22, 0.22])

#x↑
#  y→
#demo 1
#01
# objective -17.6
# Optimal theta_z (degrees): 0.0
# initial_theta_z = 0
# x_position_list = np.array([0])
# y_position_list = np.array([0])

#demo 3
#01-02
# objective -57.6
# Optimal theta_z (degrees): 4.4174370576069283e-16
# initial_theta_z = 0
# x_position_list = np.array([w, w])
# y_position_list = np.array([0, w])

#demo 4 20.69
#01-02
#03
# objective -103 ~ -106.75746135776906
# Optimal theta_z (degrees): 20.698425901051184
# initial_theta_z = 15
# x_position_list = np.array([w, w, 0])
# y_position_list = np.array([0, w, 0])

# demo 3
# 01-02
#   03
# objective  -102.13333333333333
# initial_theta_z = 0
# x_position_list = np.array([w, w, 0])
# y_position_list = np.array([0, w, 0.5*w])

#demo 5
#01-02
#03-04
#Optimal theta_z (degrees): 0.0
#objective -160.0
# initial_theta_z = 0
# x_position_list = np.array([w, w, 0, 0])
# y_position_list = np.array([-w, 0, -w, 0])

#demo 6
#01-02-03
#04
#objective -187.83929301400173
#Optimal theta_z (degrees): 71.56505117707799
# initial_theta_z = 65
# x_position_list = np.array([w, w, w, 0])
# y_position_list = np.array([0, w, 2*w, 0])

#demo 6
#01-02-03
#   04
#objective -157~-175.07963902178915
#Optimal theta_z (degrees): 44.999999999999595
# initial_theta_z = 30
# x_position_list = np.array([w, w, w, 0])
# y_position_list = np.array([0, w, 2*w, w])

#demo 11
# 01-02-03-04
# objective -226.27416997969522
# initial_theta_z = 45
# x_position_list = np.array([w, w, w,   w])
# y_position_list = np.array([0, w, 2*w, 3*w])

#demo 7
#01-02-03
#04
#05
#objective -288.0
# initial_theta_z = 0
# x_position_list = np.array([w, w, w, 0,-w])
# y_position_list = np.array([0, w, 2*w, 0,0])

#demo 8
#01-02-03
#04-05
#objective -231.83994478950345 69.81419699053515
# initial_theta_z = 60 
# x_position_list = np.array([w, w, w, 0, 0])
# y_position_list = np.array([0, w, 2*w, 0,w])

#demo 9
#01-02-03
#04-05-06
# -297.6
initial_theta_z = 0
x_position_list = np.array([w, w, w, 0, 0,0])
y_position_list = np.array([-w, 0, w,-w, 0, w])

#demo 9
#01-02-03
#04    05
# -297.6
initial_theta_z = 0
x_position_list = np.array([w, w, w, 0 ,0])
y_position_list = np.array([-w, 0, w,-w, w])


#demo 10
#01-02-03-04
#   05-06
# objective -317.1609615882061
# initial_theta_z = 45
# x_position_list = np.array([w, w, w,   w,  0, 0])
# y_position_list = np.array([0, w, 2*w, 3*w, w,2*w])

n=len(x_position_list)  # 模块数
x_center_of_mass, y_center_of_mass = calculate_center_of_mass(x_position_list, y_position_list) # 计算质心偏差
x_u_adjusted, y_u_adjusted = adjust_relative_positions(x_position_list, y_position_list, x_center_of_mass, y_center_of_mass) # 调整相对质心的位置
x_center_of_mass, y_center_of_mass = calculate_center_of_mass(x_u_adjusted, y_u_adjusted) # 计算质心

# 计算 x_u 和 y_u
x_u = np.zeros((1, 4 * n))
y_u = np.zeros((1, 4 * n))
# 通过遍历模块的坐标来计算新的位置
for i in range(n):
    x_u[0, i * 4:(i + 1) * 4] = x_i + x_u_adjusted[i]
    y_u[0, i * 4:(i + 1) * 4] = y_i + y_u_adjusted[i]
# 输出 x_u 和 y_u
print("x_u:", x_u)
print("y_u:", y_u)

theta_z_max = np.radians(90) #2*np.pi    
print(theta_z_max)
u_u_max_i = np.array([10, 10, 10, 10])  # 单元模块的最大推力
u_u_max_i = u_u_max_i.reshape(4,1)
u_u_max = np.tile(u_u_max_i, (n, 1))
print("u_u_max_i",u_u_max_i.shape)
print("u_u_max",u_u_max.shape)

v = np.array([1, 1, -1, -1])  # 权重向量
v_1x4 = v.reshape(1,4)
C_x = np.array([
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
])
C_y = np.array([
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 1]
])

# 创建优化器对象
opti = ca.Opti()
# 变量定义
theta_z = opti.variable(1,1)  # 旋转角度符号变量,弧度
opti.set_initial(theta_z, np.radians(initial_theta_z))
# theta_z = np.degrees(initial_theta_z)
x_a = opti.variable(4, 1)  # 虚拟四旋翼的 x 坐标
y_a = opti.variable(4, 1)  # 虚拟四旋翼的 y 坐标
x_a_1x4 = ca.reshape(x_a, 1, 4)
y_a_1x4 = ca.reshape(y_a, 1, 4)

x_y_a = ca.vertcat(x_a_1x4,y_a_1x4)
print("xy_a",x_y_a.shape)
# 旋转矩阵 R(theta_z)
R_theta = ca.vertcat(
    ca.horzcat(ca.cos(theta_z), -ca.sin(theta_z)),
    ca.horzcat(ca.sin(theta_z), ca.cos(theta_z))
)

# print("R_theta",R_theta.shape)
# x_y_a_theta = ca.mtimes(R_theta,x_y_a)
# print("x_y_a_theta",x_y_a_theta.shape)
# x_a_theta = x_y_a_theta[0, :]
# y_a_theta = x_y_a_theta[1, :]
x_a_theta = x_a
y_a_theta = y_a

x_a_4x1 = ca.reshape(x_a_theta, 4, 1)
y_a_4x1 = ca.reshape(y_a_theta, 4, 1)
xy_a_1x8 = ca.horzcat(x_a_theta, y_a_theta)  # 垂直堆叠 x 和 y 坐标，得到 (8, 1)
diag_x_a = ca.diag(x_a_4x1)
diag_y_a = ca.diag(y_a_4x1)
xy_a_8x1 = ca.reshape(xy_a_1x8, 8, 1)
print("diag_y_a",diag_y_a.shape)
u_a_max = np.array([10 * n, 10 * n, 10 * n, 10 * n])  # 虚拟四旋翼的最大推力
u_a_max_4x1 = u_a_max.reshape(4, 1)

# 构建扩展矩阵 R_extended
zero_2x2 = ca.DM.zeros((2, 2))
R_extended = ca.vertcat(
    ca.horzcat(R_theta, zero_2x2),
    ca.horzcat(zero_2x2, R_theta)
)
print("R_extended",R_extended.shape)

x_y_u_vector = ca.vertcat(
    x_u,
    y_u,
    x_u,
    y_u
)
min_x_u_origin = ca.fmin(x_y_u_vector[0, :], 0)
min_y_u_origin = ca.fmin(x_y_u_vector[1, :], 0)
max_x_u_origin = ca.fmax(x_y_u_vector[2, :], 0)
max_y_u_origin = ca.fmax(x_y_u_vector[3, :], 0)

input_vector_origin = ca.vertcat(
    min_x_u_origin,
    min_y_u_origin,
    max_x_u_origin,
    max_y_u_origin
)

x_y_u_vector = ca.mtimes(R_extended,x_y_u_vector)

min_x_u = ca.fmin(x_y_u_vector[0, :], 0)
min_y_u = ca.fmin(x_y_u_vector[1, :], 0)
max_x_u = ca.fmax(x_y_u_vector[2, :], 0)
max_y_u = ca.fmax(x_y_u_vector[3, :], 0)

input_vector_theta = ca.vertcat(
    min_x_u,
    min_y_u,
    max_x_u,
    max_y_u
)

# 计算 tau_pm_max
tau_pm_max_origin = ca.mtimes(input_vector_origin, u_u_max)
tau_pm_max = ca.mtimes(input_vector_theta, u_u_max)

# 计算 M_pm_expr
M_pm_expr = ca.mtimes(C_x, ca.mtimes(diag_x_a, u_a_max_4x1)) + ca.mtimes(C_y, ca.mtimes(diag_y_a, u_a_max_4x1))
print("M_pm_expr",M_pm_expr.shape)
# 目标函数
# print(u_u_max)
print(v_1x4)
# objective = ca.mtimes(v_1x4, M_pm_expr) 
objective = ca.mtimes(v_1x4, tau_pm_max) 
# 设置优化目标
opti.minimize(objective)
# 添加约束条件
# opti.subject_to(M_pm_expr == tau_pm_max)
opti.subject_to(M_pm_expr - tau_pm_max <= 1e-1)
opti.subject_to(M_pm_expr - tau_pm_max >= -1e-1)
# opti.subject_to(M_pm_expr - tau_pm_max_origin <= 1e-1)
# opti.subject_to(M_pm_expr - tau_pm_max_origin >= -1e-1)
# TODO:
# opti.subject_to((x_a_4x1[0] - x_a_4x1[1]) / (y_a_4x1[0] - y_a_4x1[1] + 1e-4) - ca.tan(theta_z) <= 1e-1)
# opti.subject_to((x_a_4x1[0] - x_a_4x1[1]) / (y_a_4x1[0] - y_a_4x1[1] + 1e-4) - ca.tan(theta_z) >= -1e-1)

# opti.subject_to((x_a_4x1[0] - x_a_4x1[2]) / (y_a_4x1[0] - y_a_4x1[2] + 1e-4) * (x_a_4x1[1] - x_a_4x1[3]) / (y_a_4x1[1] - y_a_4x1[3] + 1e-4)
#                 <= -1 + 1e-2)
# opti.subject_to((x_a_4x1[0] - x_a_4x1[2]) / (y_a_4x1[0] - y_a_4x1[2] + 1e-4) * (x_a_4x1[1] - x_a_4x1[3]) / (y_a_4x1[1] - y_a_4x1[3] + 1e-4)
#                 >= -1 - 1e-2)

# 设置求解器
opti.solver('ipopt')
# opti.solver('knitro')
# opti.solver('osqp')
# opti.solver('qpoases')
# opti.solver('snopt')
# opti.solver('gurobi')
# opti.solver('scipy')
# opti.solver('sqpmethod')


plt.figure(figsize=(8, 8))  # 增大图形尺寸
# 绘制所有点，交换 x 和 y 轴
plt.scatter(y_u, x_u, color='b', s= 1500, label='Module Points')
plt.scatter(y_u_adjusted, x_u_adjusted, color='r',s= 100, marker='x', label='Module Centers')
plt.scatter(y_center_of_mass, x_center_of_mass, color='g', s= 100, marker='o', label='Center of Mass')

# 设置坐标范围，确保所有点都在视图内
plt.xlim(-2, 2)
plt.ylim(-2, 2) 
# 设置图表属性
plt.xlabel('Y-axis')
plt.ylabel('X-axis')
plt.title('Module Positions and Points (Swapped Axes)')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.grid(True)
plt.legend()
# plt.axis('equal')
# 显示图表
plt.show()

# 求解优化问题
try:
    sol = opti.solve()
    # 输出最优解并将 theta_z 转换为角度
    theta_z_deg = np.degrees(sol.value(theta_z))
    print("Optimal theta_z :", sol.value(theta_z))
    print("Optimal theta_z (degrees):", theta_z_deg)
    print("Optimal x_a:", sol.value(x_a))
    print("Optimal y_a:", sol.value(y_a))
    print("objective",sol.value(objective))

    x_u_prime = [x_u_adjusted[i] * ca.cos(sol.value(theta_z)) - y_u_adjusted[i] * ca.sin(sol.value(theta_z)) for i in range(n)]
    y_u_prime = [x_u_adjusted[i] * ca.sin(sol.value(theta_z)) + y_u_adjusted[i] * ca.cos(sol.value(theta_z)) for i in range(n)]
    print(x_u_prime,x_u_adjusted)
    print(y_u_prime,y_u_adjusted)
    # x_a_prime = [sol.value(x_a)[i] * ca.cos(sol.value(-2*theta_z)) - sol.value(y_a)[i] * ca.sin(sol.value(-2*theta_z)) for i in range(4)]
    # y_a_prime = [sol.value(x_a)[i] * ca.sin(sol.value(-2*theta_z)) + sol.value(y_a)[i] * ca.cos(sol.value(-2*theta_z)) for i in range(4)]
    print(sol.value(theta_z))
    visualize_robots_coordinate(x_u_adjusted , y_u_adjusted, sol.value(-theta_z),w)
    # visualize_robots(y_u_prime, x_u_prime, y_a_prime, x_a_prime, u_a_max, w, sol.value(-theta_z), scale_factor=0.5/4*n)
    #optimal virtual quadrotor
    visualize_robots(y_u_prime, x_u_prime, sol.value(y_a), sol.value(x_a), u_a_max, w, sol.value(-theta_z), scale_factor=0.5/4*n)

except RuntimeError as e:
    print(f"Solver failed: {e}")
    # 使用 opti.debug.value() 检查当前的变量值
    # theta_z_deg = np.degrees(opti.debug.value(theta_z))
    # print("Debug theta_z (degrees):", theta_z_deg)
    # print("Debug x_a:", opti.debug.value(x_a))
    # print("Debug y_a:", opti.debug.value(y_a))

# 计算 theta 和目标函数之间的关系曲线
theta_values = np.linspace(0, float(theta_z_max), 100)
objective_values = []
# 计算每个 theta 对应的目标函数值
for theta in theta_values:
    current_objective = ca.Function('obj', [theta_z], [objective])(theta)
    objective_values.append(float(current_objective.full().item()))  # 转换为标量

# 绘制目标函数与 theta 的关系曲线
plt.figure(figsize=(10, 6))
plt.plot(np.degrees(theta_values), objective_values, color='b', label='Objective Function')
plt.xlabel('Theta (degrees)')
plt.ylabel('Objective Function Value')
plt.title('Relationship Between Theta and Objective Function')
plt.grid(True)
plt.legend()
plt.show()