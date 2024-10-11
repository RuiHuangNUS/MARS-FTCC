function x = calculate_f()
    % 设定初始点
    x0 = [1, 0, 1, 1]; 
    
    % 用fmincon进行优化
    options = optimoptions(@fmincon, 'Algorithm', 'interior-point');
    x = fmincon(@objective, x0, [], [], [], [], [], [], @nonlinear_constraints, options);
    
    % 定义一个目标函数，这个函数返回x的标准差
    function std_dev = objective(x)
        std_dev = std(x([1, 2, 3, 4]));
    end

    % 创建一个用于fmincon的非线性约束函数
    function [c, ceq] = nonlinear_constraints(x)
        c = [];
        
        % 约束条件
        ceq(1) = x(1) + x(2) + x(3) + x(4) - 4;    % f1+f2+f3+f4=4  
        ceq(2) = x(1) - x(3) - x(4);               % f1-f3-f4=0
        ceq(3) = x(1) + x(3) - x(4);               % f1+f3-f4=0
        ceq(4) = x(2);                             % f2=0
    end
end
