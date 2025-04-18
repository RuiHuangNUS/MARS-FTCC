#ifndef CONFIG_HPP
#define CONFIG_HPP

#include <Eigen/Eigen>

#include <ros/ros.h>

#include <string>
#include <vector>
using namespace Eigen;
using namespace std;

struct Config
{
public:
   
    int threads_num{12};
    vector<double> poly_params;     
   
  

    std::vector<double> mapBound;
  
    double voxelWidth;       
    double testRate;
    double ts{-1.0};   

    double torlerance{0.005};
    int degree{4};                   
    std::string meshTopic;
    std::string edgeTopic;
    std::string vertexTopic;
    std::string inputdata; // swept volume

    double t_min{0};
    double t_max{1};
    double transparency{0.5};
    double momentum{0};//Nesterov Acceleration Momentum
    double occupancy_resolution{1.0};
    bool debug_output{true};
    int sta_threshold{1};
    double selfmapresu{0.1};
    double colli_thres{0.65};

    double weight_v;
    double weight_a;
    double weight_p;
    double weight_pr;
    double weight_ar;
    double weight_omg;
    double weight_theta;
    double safety_hor;
    double vmax;
    double omgmax;
    double thetamax;
    double rho;
    double rho_mid_end;
    double inittime{10.0};
    //lbfgs params
    int mem_size{256};
    int past{3};      
    double min_step{1.0e-32};
    double g_epsilon{0.0};
    double RelCostTol{1e-5}; 

    //flatness
    double vehicleMass;
    double gravAcc;
    double horizDrag;        
    double vertDrag;         
    double parasDrag;        
    double speedEps;         


    double smoothingEps;
    int integralIntervs; 
    double relCostTol;
    double relCostTolMidEnd;
    double eps{0.2};//swept volume mesh surface precision


 

   
    bool loadStartEnd{false};

  

    int kernel_size;//必须是奇数，对应小方块的个数
    int kernel_yaw_num;
    double front_end_safeh ;
    bool enableearlyExit{false};
    int debugpause{20};


    #define LOAD_PARAM(x) nh_priv.getParam( #x , x)
    inline void loadParameters(const ros::NodeHandle &nh_priv)
    {
       
        LOAD_PARAM(weight_v);
        LOAD_PARAM(weight_a);
        LOAD_PARAM(weight_p);
        LOAD_PARAM(weight_pr);
        LOAD_PARAM(weight_ar);
        LOAD_PARAM(weight_omg);
        LOAD_PARAM(weight_theta);
        LOAD_PARAM(safety_hor);
        LOAD_PARAM(vmax);
        LOAD_PARAM(omgmax);
        LOAD_PARAM(thetamax);
        LOAD_PARAM(rho);
        LOAD_PARAM(rho_mid_end);
        LOAD_PARAM(inittime);           
        LOAD_PARAM(mem_size);           
        LOAD_PARAM(past);               
        LOAD_PARAM(min_step);           
        LOAD_PARAM(g_epsilon);          
        LOAD_PARAM(RelCostTol);         
        LOAD_PARAM(relCostTolMidEnd);   
        LOAD_PARAM(enableearlyExit);    
        LOAD_PARAM(debugpause);         

        LOAD_PARAM(meshTopic);
        LOAD_PARAM(edgeTopic);
        LOAD_PARAM(inputdata);
        LOAD_PARAM(vertexTopic);
  
        LOAD_PARAM(testRate);

        LOAD_PARAM(ts);
     

        LOAD_PARAM(loadStartEnd);
        LOAD_PARAM(eps);
        LOAD_PARAM(t_min);
        LOAD_PARAM(t_max);
        LOAD_PARAM(momentum);
        LOAD_PARAM(torlerance);
        
        //PCSmap_manager

        LOAD_PARAM(voxelWidth);
        LOAD_PARAM(mapBound);
        LOAD_PARAM(sta_threshold);
        LOAD_PARAM(debug_output);
        LOAD_PARAM(selfmapresu);
        LOAD_PARAM(colli_thres);
        LOAD_PARAM(occupancy_resolution);
        LOAD_PARAM(kernel_size);

        nh_priv.param<std::vector<double>>("poly_params", poly_params, std::vector<double>());
     
        LOAD_PARAM( vehicleMass);
        LOAD_PARAM(gravAcc);
        LOAD_PARAM(horizDrag);
        LOAD_PARAM(vertDrag);
        LOAD_PARAM(parasDrag);
        LOAD_PARAM(speedEps);
        LOAD_PARAM(threads_num);
        LOAD_PARAM(smoothingEps);
        LOAD_PARAM(integralIntervs);
        LOAD_PARAM(relCostTol);

        LOAD_PARAM(front_end_safeh);
        LOAD_PARAM(kernel_yaw_num);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////


        ROS_WARN_STREAM("meshTopic:" << meshTopic);
        ROS_WARN_STREAM("edgeTopic:" << edgeTopic);
        ROS_WARN_STREAM("vertexTopic:" << vertexTopic);
        ROS_WARN_STREAM("inputdata:" << inputdata);

        




        ROS_WARN_STREAM("degree:" << degree);
        ROS_WARN_STREAM("threads_num:" << threads_num);
        ROS_WARN_STREAM("ts:" << ts);

    


        ROS_WARN_STREAM("eps:" << eps);
        ROS_WARN_STREAM("swept volume t_max:" << t_max);
       

        ROS_WARN_STREAM("map VoxelWidth" << voxelWidth);
        ROS_WARN_STREAM("map MapBound size" << mapBound.size());
   
        ROS_WARN_STREAM("momentum:" << momentum);
        ROS_WARN_STREAM("torlerance:" << torlerance);
     

        ROS_WARN_STREAM("selfmapresu:" << selfmapresu);
        ROS_WARN_STREAM("colli_thres:" << colli_thres);




        ROS_WARN_STREAM("weight_v:" << weight_v );
        ROS_WARN_STREAM("weight_a:" << weight_a );
        ROS_WARN_STREAM("weight_p:" << weight_p );
        ROS_WARN_STREAM("weight_omg:" << weight_omg );
        ROS_WARN_STREAM("weight_theta:" << weight_theta );
        ROS_WARN_STREAM("safety_hor:" << safety_hor );
        ROS_WARN_STREAM("vmax:" << vmax );
        ROS_WARN_STREAM("omgmax:" << omgmax );
        ROS_WARN_STREAM("thetamax:" << thetamax );
        ROS_WARN_STREAM("rho:" << rho );
        ROS_WARN_STREAM("mem_size:" << mem_size );
        ROS_WARN_STREAM("past:" << past );
        ROS_WARN_STREAM("min_step:" << min_step );
        ROS_WARN_STREAM("g_epsilon:" << g_epsilon );
        ROS_WARN_STREAM("RelCostTol:" << RelCostTol );
        ROS_WARN_STREAM("enableearlyExit:" << enableearlyExit );
        ROS_WARN_STREAM("debugpause:" << debugpause);
        ROS_WARN_STREAM("testRate:" << testRate);
        return;
    }
};

#endif