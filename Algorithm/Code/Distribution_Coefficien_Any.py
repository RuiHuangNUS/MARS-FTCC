# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:06:25 2023

@author: RuiHuang
"""
def I_assembly(X_position_list,Y_position_list,n):
    Ixx_assembly = Ixx*n + m*(sum(y**2 for y in Y_position_list))
    Iyy_assembly = Iyy*n + m*(sum(x**2 for x in X_position_list))
    Izz_assembly = Izz*n + m*(sum(y**2 for y in Y_position_list) + sum(x**2 for x in X_position_list))
    print(Ixx_assembly,Iyy_assembly,Izz_assembly)
    return Ixx_assembly,Iyy_assembly,Izz_assembly
    
def I_Unit(x_position_center,y_position_center):
    Ixx_Unit = Ixx + m*(y_position_center**2)
    Iyy_Unit = Iyy + m*(x_position_center**2)
    Izz_Unit = Izz + m*(y_position_center**2+x_position_center**2)
    return Ixx_Unit,Iyy_Unit,Izz_Unit

def Distribution(X_position,Y_position,n):
    #average
    Ixx_assembly,Iyy_assembly,Izz_assembly = I_assembly(X_position,Y_position,n)
    K_Ixx = Ixx_assembly/Ixx
    K_Iyy = Iyy_assembly/Iyy
    K_Izz = Izz_assembly/Izz
    # K_Ixx = Ixx/Ixx_assembly
    # K_Iyy = Iyy/Iyy_assembly
    # K_Izz = Izz/Izz_assembly
    print(K_Ixx,K_Iyy,K_Izz)
    X_abs_sum = sum(abs(x+0.000001) for x in X_position)
    Y_abs_sum = sum(abs(y+0.000001) for y in Y_position)
    n_normal = len(X_position)
    print('n_normal=',n_normal)
    for i in range(n_normal):
        K_distribution_y = abs(Y_position[i]+0.000001)/(Y_abs_sum)
        K_distribution_x = abs(X_position[i]+0.000001)/(X_abs_sum)
        # K_distribution_y = (Y_abs_sum)/abs(Y_position[i]+0.000001)
        # K_distribution_x = (X_abs_sum)/abs(X_position[i]+0.000001)
#        print(K_distribution_y,K_distribution_x)
        #True
        #print('Mod %s='%(i+1), K_distribution_y*K_distribution_y, K_distribution_x*K_distribution_x, K_Izz/n_normal,'\n')
        #Test
        print('Mod %s='%(i+1),K_Ixx*K_distribution_y,K_Iyy*K_distribution_x,K_Izz/n_normal,'\n')    


def calculate_center_of_mass(x_positions, y_positions):
    # 计算机器人的重心位置
    # x_positions: 机器人的x坐标列表
    # y_positions: 机器人的y坐标列表

    # 计算机器人的质量
    mass = [0.925] * len(x_positions)

    # 计算机器人的质心位置
    x_center_of_mass = sum([x * m for x, m in zip(x_positions, mass)]) / sum(mass)
    y_center_of_mass = sum([y * m for y, m in zip(y_positions, mass)]) / sum(mass)
    
    return x_center_of_mass, y_center_of_mass

def adjust_relative_positions(x_positions, y_positions, x_center_of_mass, y_center_of_mass):
    # 根据重心位置调整机器人的相对坐标
    # x_positions: 机器人的相对x坐标列表
    # y_positions: 机器人的相对y坐标列表
    # x_center_of_mass: 重心的x坐标
    # y_center_of_mass: 重心的y坐标

    new_x_positions = [x - x_center_of_mass for x in x_positions]
    new_y_positions = [y - y_center_of_mass for y in y_positions]

    return new_x_positions, new_y_positions

        
#def Distribution_test(X_position,Y_position,n):
#    #independent
#    Ixx_assembly,Iyy_assembly,Izz_assembly = I_assembly(X_position,Y_position,n)
#    X_abs_sum = sum(abs(x) for x in X_position)
#    Y_abs_sum = sum(abs(y) for y in Y_position)
#    for i in range(n):
#        Ixx_Unit,Iyy_Unit,Izz_Unit = I_Unit(X_position[i],Y_position[i])
#        # K_Ixx = Ixx_assembly/Ixx_Unit
#        # K_Iyy = Iyy_assembly/Iyy_Unit
#        # K_Izz = Izz_assembly/Izz_Unit
#        
#        K_Ixx = Ixx_Unit/Ixx
#        K_Iyy = Iyy_Unit/Iyy
#        K_Izz = Izz_Unit/Izz
#        # K_Ixx = Ixx_Unit/Ixx_assembly
#        # K_Iyy = Iyy_Unit/Iyy_assembly
#        # K_Izz = Izz_Unit/Izz_assembly
##        print(K_Ixx,K_Iyy,K_Izz)
#        K_distribution_y = Y_abs_sum/(abs(Y_position[i])+0.001)
#        K_distribution_x = X_abs_sum/(abs(X_position[i])+0.001)
#       # print(K_distribution_y,K_distribution_x)
#        # K_distribution_y = abs(Y_position[i])/(Y_abs_sum+0.001)
#        # K_distribution_x = abs(X_position[i])/(X_abs_sum+0.001)
#        #print(K_distribution_y,K_distribution_x)
#        print('Mod_test %s='%(i+1),K_Ixx*K_distribution_y,K_Iyy*K_distribution_x,K_Izz/n,'\n')
        
#def Distribution_test2(X_position,Y_position,n):
#    #independent
#    Ixx_assembly,Iyy_assembly,Izz_assembly = I_assembly(X_position,Y_position,n)
#    X_abs_sum = sum(abs(x) for x in X_position)
#    Y_abs_sum = sum(abs(y) for y in Y_position)
#    for i in range(n):
#        Ixx_Unit,Iyy_Unit,Izz_Unit = I_Unit(X_position[i],Y_position[i])
#
##        K_Ixx1 = Ixx_Unit/Ixx_assembly
##        K_Iyy1 = Iyy_Unit/Iyy_assembly
##        K_Izz1 = Izz_Unit/Izz_assembly
#        
#        K_Ixx2 = Ixx_Unit/Ixx
#        K_Iyy2 = Iyy_Unit/Iyy
#        K_Izz2 = Izz_Unit/Izz
#
##        K_distribution_y = Y_abs_sum/(abs(Y_position[i])+0.001)
##        K_distribution_x = X_abs_sum/(abs(X_position[i])+0.001)
#
#        print('Mod_test2 %s='%(i+1),K_Ixx2,K_Iyy2,K_Izz2,'\n')

    

if __name__=='__main__':
    # import numpy as np
    #Unite parameters
    m=1.200e-01
    Ixx=6.667e-05*m
    Iyy=7.533e-03*m
    Izz=7.533e-03*m
    d=0.35
    
    #Assembly parameters (Assembly Coordinate)
    #↑Y
    #  →X
    #01-02
#    n=2
#    X_position = [-0.5*d,0.5*d]
#    Y_position = [ 0,0]
    #01-XX
    #XX-02
    n=2
    X_position = [-0.5*d,0.5*d]
    Y_position = [0.5*d,-0.5*d]
    #01
    #02
    # n=2
    # X_position = [0,0]
    # Y_position = [0.5*d,-0.5*d]
    #010203
#    n=3
#    X_position = [-d, 0, d]
#    Y_position = [ 0,0,0]
    
    #test 3L success
    #01
    #02-03
    # n=3
    # X_position = [-0.5*d,-0.5*d,0.5*d]
    # Y_position = [0.5*d,-0.5*d,-0.5*d]
    #03
    #02-01
    # n=3
    # X_position_3=[0.35,0.35,-0.35]
    # Y_position_3=[0.35,0.35,-0.35]
    # x_3_1=X_position_3[0]*2/3
    # x_3_2=X_position_3[1]*1/3
    # x_3_3=X_position_3[2]*1/3
    
    # y_3_1=Y_position_3[0]*1/3
    # y_3_2=Y_position_3[1]*1/3
    # y_3_3=Y_position_3[2]*2/3
    # X_position = [x_3_1,x_3_2,x_3_3]
    # Y_position = [y_3_1,y_3_2,y_3_3]

#    n=4
#    X_position = [-1.5*d,-0.5*d,0.5*d,1.5*d]
#    Y_position = [ 0,0,0,0]
    #01-02
    #03-04
#    n=4
#    X_position = [-0.5*d,0.5*d,-0.5*d, 0.5*d]
#    Y_position = [ 0.5*d,0.5*d,-0.5*d,-0.5*d]
    
    #6Mod
    #01-02-03
    #04-05-06
    # n=6
    # X_position = [-d, 0, d,
    #               -d, 0, d]
    # Y_position = [ 0.5*d, 0.5*d, 0.5*d,
    #               -0.5*d,-0.5*d,-0.5*d]
    #error_2
    # n = 5
    # X_position = [-d,   d,
    #                 -d, 0, d]
    # Y_position = [ 0.5*d,   0.5*d,
    #                 -0.5*d,-0.5*d,-0.5*d]
    #error_3
#    n=5
#    X_position = [-d, 0, 
#                  -d, 0, d]
#    Y_position = [ 0.5*d, 0.5*d,
#                  -0.5*d,-0.5*d,-0.5*d]
#    error_34
#    n=6
#    X_position = [-d, 0, 
#                      0, d]
#    Y_position = [ 0.5*d, 0.5*d,
#                         -0.5*d,-0.5*d]

    # n=6
    # X_position = [  0, d,
    #               -d, 0 ]
    # Y_position = [   0.5*d, 0.5*d,
    #               -0.5*d,-0.5*d ]
    
    #error_25
#    n=6
#    X_position = [-d,   d,
#                  -d,   d]
#    Y_position = [ 0.5*d,   0.5*d,
#                  -0.5*d,  -0.5*d]
    
    #error_24
#    n=6
#    X_position = [-d,    d,
#                      0, d]
#    Y_position = [ 0.5*d,       0.5*d,
#                        -0.5*d,-0.5*d]
    #error_23
#    n=6
#    X_position = [-d,     
#                  -d, 0, d]
#    Y_position = [ 0.5*d,   
#                  -0.5*d,-0.5*d,-0.5*d]
    #error_36
#    n=6
#    X_position = [-d, 0,  
#                  -d, 0 ]
#    Y_position = [ 0.5*d, 0.5*d,  
#                  -0.5*d,-0.5*d]
    
    #8Mod
#    n=8
#    X_position = [-1.5*d,-0.5*d, 0.5*d, 1.5*d,
#                  -1.5*d,-0.5*d, 0.5*d, 1.5*d]
#    
#    Y_position = [0.5*d, 0.5*d, 0.5*d, 0.5*d,
#                 -0.5*d,-0.5*d,-0.5*d,-0.5*d]
    
    ###NX3
    #1X3
    #01
    #02
    #03
#    n=3
#    X_position = [0,0,0]
#    Y_position = [d,0,d]
    
#    n=6
#    X_position = [-0.5*d,0.5*d,-0.5*d,0.5*d,-0.5*d,0.5*d]
#    Y_position = [     d,    d,     0,    0,  -1*d, -1*d]
    
    # n=9
    # X_position = [-1*d, 0, d,-1*d, 0, d, -1*d,   0,   d]
    # Y_position = [   d, d, d,   0, 0, 0, -1*d,-1*d,-1*d]
    
    # n=12
    # X_position = [-1.5*d, -0.5*d, 0.5*d, 1.5*d, 
    #               -1.5*d, -0.5*d, 0.5*d, 1.5*d,
    #               -1.5*d, -0.5*d, 0.5*d, 1.5*d]
    # Y_position = [  d,   d,   d,   d,
    #                 0,   0,   0,   0,
    #              -1*d,-1*d,-1*d,-1*d]
    #01-02-03
    #04    05
    #06-07-08
    # n=8
    # X_position = [-d, 0, d,
    #                 -d,    d,
    #                 -d, 0, d]
    # Y_position = [d, d, d,
    #                 0,    0,
    #                 -d,-d,-d]
#     X_position_8 = [-d, 0, d,
#                     -d,    d,
#                     -d, 0, d]
#     Y_position_8 = [0, 0, 0,
#                     -d,    -d,
#                    -2*d,-2*d,-2*d]
    #11
    #   01    02
    #03-04-05-06-07
    #   08-09-10
    #      11
#    n=11
#    X_position = [-d, d,
#                  -2*d,-d,0,d,2*d,
#                  -d,0,d,
#                   0]
#    Y_position = [ 1.5*d, 1.5*d,
#                  0.5*d,0.5*d,0.5*d,0.5*d,0.5*d,
#                  -0.5*d,-0.5*d,-0.5*d,
#                  -1.5*d]
    #21Mod 
    #05-04-03-02-01
    #08    07    06 
    #13-12-11-10-09
    #16    15    14
    #21-20-19-18-17
    # n=21
    # X_position_21 = [-2*d,-d,0,d,2*d,
    #                  -2*d,   0,  2*d,
    #                  -2*d,-d,0,d,2*d,
    #                  -2*d,   0,  2*d,
    #                  -2*d,-d,0,d,2*d]
    
    # Y_position_21 = [2*d, 2*d, 2*d, 2*d, 2*d,
    #                   d,         d,        d,
    #                   0,    0,   0,   0,   0,
    #                  -d,        -d,       -d,
    #                 -2*d,-2*d,-2*d,-2*d,-2*d]
    #21Mod 
    #07-06-05-04-03-02-01
    #14-13-12-11-10-09-08
    #21-20-19-18-17-16-15
#    Ixx_center,Iyy_center,Izz_center = I_Unit(0,0)
    x_center_of_mass, y_center_of_mass = calculate_center_of_mass(X_position, Y_position)
    #print(x_center_of_mass,y_center_of_mass)
    x_center_of_mass = 0
    y_center_of_mass = 0
    x_positions,y_positions = adjust_relative_positions(X_position, Y_position, x_center_of_mass, y_center_of_mass)
    Distribution(x_positions,y_positions,n)
    #Distribution_test(X_position,Y_position,n)
    #Distribution_test2(X_position,Y_position,n)
    