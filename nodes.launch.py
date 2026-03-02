import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a5141e1d8112d38000375c",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a5141e1d8112d38000375c",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a5142b1d8112d380003777","source_node_id":"69a514281d8112d380003773","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a514211d8112d380003766",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a514211d8112d380003766",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a5142f1d8112d38000377d","source_node_id":"69a514281d8112d380003773","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a5141f1d8112d380003761",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a5141f1d8112d380003761",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a5142d1d8112d38000377a","source_node_id":"69a514281d8112d380003773","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a514231d8112d38000376b",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a514231d8112d38000376b",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a514311d8112d380003780","source_node_id":"69a514281d8112d380003773","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_69a514281d8112d380003773",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a514281d8112d380003773",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_left","name":"encoder_left","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_right","name":"encoder_right","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:odometry","name":"odometry","direction":"output","msg_type":"nav_msgs/Odometry"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a5143e1d8112d380003788","source_node_id":"69a5143b1d8112d380003785","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a514431d8112d380003791","source_node_id":"69a514401d8112d38000378d","source_pin_id":"encoder_state","target_pin_id":"encoder_left"},{"connection_id":"69a514481d8112d38000379a","source_node_id":"69a514451d8112d380003796","source_pin_id":"encoder_state","target_pin_id":"encoder_right"},{"connection_id":"69a514501d8112d3800037a3","source_node_id":"69a5144a1d8112d38000379f","source_pin_id":"mode","target_pin_id":"mode"},{"connection_id":"69a514581d8112d3800037ab","source_node_id":"69a514521d8112d3800037a8","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a5142b1d8112d380003777","target_node_id":"69a5141e1d8112d38000375c","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69a5142d1d8112d38000377a","target_node_id":"69a5141f1d8112d380003761","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69a5142f1d8112d38000377d","target_node_id":"69a514211d8112d380003766","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69a514311d8112d380003780","target_node_id":"69a514231d8112d38000376b","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_69a5143b1d8112d380003785",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a5143b1d8112d380003785",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c77bb3f393789aad6f62:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3c77bb3f393789aad6f62:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3c77bb3f393789aad6f62:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a5143e1d8112d380003788","target_node_id":"69a514281d8112d380003773","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a514401d8112d38000378d",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a514401d8112d38000378d",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a514431d8112d380003791","target_node_id":"69a514281d8112d380003773","source_pin_id":"encoder_state","target_pin_id":"encoder_left"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a514451d8112d380003796",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a514451d8112d380003796",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a514481d8112d38000379a","target_node_id":"69a514281d8112d380003773","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_69a5144a1d8112d38000379f",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a5144a1d8112d38000379f",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"stopped","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd36b3f393789aad7079:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3cd36b3f393789aad7079:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a514501d8112d3800037a3","target_node_id":"69a514281d8112d380003773","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
        Node(
            package="mission_runner",
            executable="mission_runner_node",
            name="mission_runner_69a514521d8112d3800037a8",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a514521d8112d3800037a8",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"mission":[],"linear_speed":0.5,"angular_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":10,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a477bcc85549d8e55e27db:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a477bcc85549d8e55e27db:status","name":"status","direction":"output","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a514581d8112d3800037ab","target_node_id":"69a514281d8112d380003773","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="logger",
            executable="logger_node",
            name="logger_69a5145b1d8112d3800037b0",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a5145b1d8112d3800037b0",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"log_file":"","log_to_stdout":true}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
    ])