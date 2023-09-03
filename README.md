# sourcegraph-ros
Tools for creating search contexts to search ROS code on sourcegraph.com

## Plan

I want to search released ROS source code.

ros/rosdistro --> ?magic here? --> sourcegraph search context

* `ROS-Rolling-development`: All source entries in ROS Rolling

It's a JSON list of repositories and revisions

```json
[
  {
    "repository": "github.com/ros2/rclcpp",
    "revisions": ["rolling"]
  },
  ...
]
```

Reading ros/rosdistro - could use https://github.com/ros-infrastructure/rosdistro , but it takes me a while to relearn it's API :(


Testing:
```
pipenv install --dev .
pipenv shell
```

## Issues

Lots of repositories aren't indexed in the public sourcegraph instance :(
Some of these are caused by repository renaming (Fast-RTPS -> Fast-DDS is one example).

```
    Cannot find github.com/robosoft-ai/SMACC2 repository.
    Cannot find gitlab.com/autowarefoundation/autoware.auto/acado_vendor repository.
    Cannot find github.com/rudislabs/actuator_msgs repository.
    Cannot find github.com/ros-acceleration/ament_acceleration repository.
    Cannot find github.com/ubuntu-robotics/ament_nodl repository.
    Cannot find github.com/ros-acceleration/ament_vitis repository.
    Cannot find gitlab.com/ApexAI/apex_containers repository.
    Cannot find github.com/fictionlab/ros_aruco_opencv repository.
    Cannot find github.com/hatchbed/asyncapi_gencpp repository.
    Cannot find github.com/wep21/aws_sdk_cpp_vendor repository.
    Cannot find github.com/wep21/bag2_to_image repository.
    Cannot find github.com/OUXT-Polaris/boost_geometry_util repository.
    Cannot find github.com/tesseract-robotics/boost_plugin_loader repository.
    Cannot find github.com/ngmor/catch_ros2 repository.
    Cannot find github.com/OUXT-Polaris/color_names-release repository.
    Cannot find github.com/MetroRobots/color_util repository.
    Cannot find github.com/tier4/cudnn_cmake_module repository.
    Cannot find github.com/ros2/domain_bridge repository.
    Cannot find github.com/dynamixel-community/dynamixel_hardware repository.
    Cannot find github.com/ros-event-camera/event_camera_codecs repository.
    Cannot find github.com/ros-event-camera/event_camera_renderer repository.
    Cannot find github.com/flexbe/flexbe_behavior_engine repository.
    Cannot find github.com/ForteFibre/FluentRviz repository.
    Cannot find github.com/boschresearch/fmilibrary_vendor repository.
    Cannot find github.com/ros-simulation/gazebo_ros2_control repository.
    Cannot find github.com/ros-sports/gc_spl repository.
    Cannot find github.com/flynneva/grbl_msgs repository.
    Cannot find github.com/flynneva/grbl_ros repository.
    Cannot find github.com/ros-controls/gz_ros2_control repository.
    Cannot find github.com/hatchbed/hatchbed_common repository.
    Cannot find github.com/tier4/heaphook repository.
    Cannot find github.com/ros2-gbp/ifm3d-release repository.
    Cannot find github.com/ignitionrobotics/ign-rviz repository.
    Cannot find github.com/ignition-release/ignition_cmake2_vendor repository.
    Cannot find github.com/ignition-release/ignition_math6_vendor repository.
    Cannot find github.com/iRobotEducation/irobot_create_msgs repository.
    Cannot find github.com/joshnewans/joy_tester repository.
    Cannot find github.com/ros-tooling/keyboard_handler repository.
    Cannot find github.com/ros-controls/kinematics_interface repository.
    Cannot find github.com/fzi-forschungszentrum-informatik/lanelet2 repository.
    Cannot find github.com/PickNikRobotics/launch_param_builder repository.
    Cannot find github.com/ros2-gbp/libg2o-release repository.
    Cannot find github.com/boschglobal/locator_ros_bridge repository.
    Cannot find github.com/hatchbed/log_view repository.
    Cannot find github.com/open-rmf/menge_vendor repository.
    Cannot find github.com/ijnek/nao_button_sim repository.
    Cannot find github.com/ijnek/nao_interfaces repository.
    Cannot find github.com/ros-sports/nao_lola repository.
    Cannot find github.com/neobotix/neo_simulation2 repository.
    Cannot find github.com/open-rmf/nlohmann_json_schema_validator_vendor repository.
    Cannot find github.com/OUXT-Polaris/nmea_hardware_interface repository.
    Cannot find github.com/osrf/nodl_to_policy repository.
    Cannot find github.com/LORD-MicroStrain/ntrip_client repository.
    Cannot find github.com/octomap/octomap repository.
    Cannot find github.com/octomap/octomap_msgs repository.
    Cannot find github.com/gstavrinos/odom_to_tf_ros2 repository.
    Cannot find github.com/ros2-gbp/ompl-release repository.
    Cannot find github.com/hatchbed/opensw_ros repository.
    Cannot find github.com/OUXT-Polaris/ouxt_common repository.
    Cannot find github.com/ros-perception/perception_open3d repository.
    Cannot find github.com/ros2-gbp/picknik_ament_copyright-release repository.
    Cannot find github.com/facontidavide/plotjuggler_msgs repository.
    Cannot find github.com/PlotJuggler/plotjuggler-ros-plugins repository.
    Cannot find github.com/splintered-reality/py_trees_ros_interfaces repository.
    Cannot find github.com/open-rmf/pybind11_json_vendor repository.
    Cannot find github.com/Autoware-AI/qpoases_vendor repository.
    Cannot find github.com/ros2-gbp/radar_msgs-release repository.
    Cannot find github.com/roboception/rc_common_msgs_ros2 repository.
    Cannot find github.com/roboception/rc_dynamics_api repository.
    Cannot find github.com/roboception/rc_reason_clients_ros2 repository.
    Cannot find github.com/ros-sports/rcss3d_agent repository.
    Cannot find github.com/ros-industrial/reach_ros2 repository.
    Cannot find github.com/open-rmf/rmf_building_map_msgs repository.
    Cannot find github.com/open-rmf/rmf_cmake_uncrustify repository.
    Cannot find github.com/open-rmf/rmf_demos repository.
    Cannot find github.com/open-rmf/rmf_ros2 repository.
    Cannot find github.com/open-rmf/rmf_traffic repository.
    Cannot find github.com/open-rmf/rmf_variants repository.
    Cannot find github.com/ros2/rmw_connextdds repository.
    Cannot find github.com/Kinovarobotics/ros2_kortex repository.
    Cannot find github.com/SteveMacenski/ros2_ouster_drivers repository.
    Cannot find github.com/PickNikRobotics/ros2_robotiq_gripper repository.
    Cannot find github.com/autowarefoundation/ros2_socketcan repository.
    Cannot find github.com/ros-sports/ros_image_to_qimage repository.
    Cannot find github.com/ros2-gbp/ros_industrial_cmake_boilerplate-release repository.
    Cannot find github.com/ros2/rosidl_core repository.
    Cannot find github.com/ros2/rosidl_dynamic_typesupport repository.
    Cannot find github.com/ros2/rpyutils repository.
    Cannot find github.com/ros-visualization/rqt_action repository.
    Cannot find github.com/ros-visualization/rqt_console repository.
    Cannot find github.com/ros-sports/rqt_image_overlay repository.
    Cannot find github.com/ros-visualization/rqt_moveit repository.
    Cannot find github.com/ros-visualization/rqt_msg repository.
    Cannot find github.com/ros-visualization/rqt_srv repository.
    Cannot find github.com/PickNikRobotics/RSL repository.
    Cannot find github.com/rt-net/rt_manipulators_cpp repository.
    Cannot find github.com/pantor/ruckig repository.
    Cannot find github.com/teamspatzenhirn/rviz_2d_overlay_plugins repository.
    Cannot find github.com/septentrio-gnss/septentrio_gnss_driver repository.
    Cannot find github.com/oKermorgant/simple_launch repository.
    Cannot find github.com/PickNikRobotics/snowbot_operating_system repository.
    Cannot find github.com/ros-sports/soccer_interfaces repository.
    Cannot find github.com/ijnek/soccer_object_msgs repository.
    Cannot find github.com/ros-sports/soccer_vision_3d_rviz_markers repository.
    Cannot find github.com/ijnek/soccer_visualization repository.
    Cannot find github.com/OUXT-Polaris/sol_vendor repository.
    Cannot find github.com/open-rmf/stubborn_buddies repository.
    Cannot find github.com/ros-visualization/tango_icons_vendor repository.
    Cannot find github.com/ros2/test_interface_files repository.
    Cannot find github.com/DLu/tf_transformations repository.
    Cannot find github.com/wep21/tinyspline_vendor repository.
    Cannot find github.com/PickNikRobotics/topic_based_ros2_control-release repository.
    Cannot find github.com/ros-tooling/topic_tools repository.
    Cannot find github.com/ros-acceleration/tracetools_acceleration repository.
    Cannot find github.com/wep21/turbojpeg_compressed_image_transport repository.
    Cannot find github.com/ros-teleop/twist_mux_msgs repository.
    Cannot find github.com/joshnewans/twist_stamper repository.
    Cannot find github.com/aussierobots/ublox_dgnss repository.
    Cannot find github.com/ament/uncrustify_vendor repository.
    Cannot find github.com/UniversalRobots/Universal_Robots_Client_Library repository.
    Cannot find github.com/UniversalRobots/Universal_Robots_ROS2_Driver repository.
    Cannot find github.com/MetroRobots/urdf_launch repository.
    Cannot find github.com/ros-drivers/urg_node_msgs repository.
    Cannot find gitlab.com/boldhearts/ros2_v4l2_camera repository.
    Cannot find bitbucket.org/DataspeedInc/velodyne_simulator repository.
    Cannot find github.com/ros-sports/vision_msgs_layers repository.
    Cannot find github.com/ros-acceleration/vitis_common repository.
    Cannot find github.com/alvinsunyixiao/vrpn_mocap repository.
    Cannot find github.com/ros-planning/warehouse_ros_sqlite repository.
    Cannot find github.com/eclipse-zenoh/zenoh-plugin-dds repository.
    Cannot find github.com/tier4/zmqpp_vendor repository.
```