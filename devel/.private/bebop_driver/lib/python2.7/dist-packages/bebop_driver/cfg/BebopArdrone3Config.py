## *********************************************************
## 
## File autogenerated for the bebop_driver package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 235, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'PILOTINGSETTINGS', 'lower': 'pilotingsettings', 'srcline': 109, 'name': 'pilotingsettings', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::PILOTINGSETTINGS', 'field': 'DEFAULT::pilotingsettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 16, 'description': 'Current altitude max in m', 'max': 160.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsMaxAltitudeCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 18, 'description': 'Current tilt max in degree', 'max': 180.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsMaxTiltCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -180.0, 'type': 'double'}, {'srcline': 24, 'description': '1 to enable, 0 to disable', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsAbsolutControlOn', 'edit_method': "{'enum_description': '1 to enable, 0 to disable', 'enum': [{'srcline': 21, 'description': 'Disabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsAbsolutControlOn_OFF'}, {'srcline': 22, 'description': 'Enabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsAbsolutControlOn_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 26, 'description': 'Current max distance in meter', 'max': 160.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsMaxDistanceValue', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 32, 'description': '1 if the drone cant fly further than max distance, 0 if no limitation on the drone should be done', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover', 'edit_method': "{'enum_description': '1 if the drone cant fly further than max distance, 0 if no limitation on the drone should be done', 'enum': [{'srcline': 29, 'description': 'Disabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_OFF'}, {'srcline': 30, 'description': 'Enabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 1}, {'upper': 'SPEEDSETTINGS', 'lower': 'speedsettings', 'srcline': 109, 'name': 'speedsettings', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::SPEEDSETTINGS', 'field': 'DEFAULT::speedsettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 37, 'description': 'Current max vertical speed in m/s', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsMaxVerticalSpeedCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 39, 'description': 'Current max rotation speed in degree/s', 'max': 900.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsMaxRotationSpeedCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 45, 'description': '1 if present, 0 if not present', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsHullProtectionPresent', 'edit_method': "{'enum_description': '1 if present, 0 if not present', 'enum': [{'srcline': 42, 'description': 'Disabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsHullProtectionPresent_OFF'}, {'srcline': 43, 'description': 'Enabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsHullProtectionPresent_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 51, 'description': '1 if outdoor flight, 0 if indoor flight', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsOutdoorOutdoor', 'edit_method': "{'enum_description': '1 if outdoor flight, 0 if indoor flight', 'enum': [{'srcline': 48, 'description': 'Disabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsOutdoorOutdoor_OFF'}, {'srcline': 49, 'description': 'Enabled', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsOutdoorOutdoor_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 2}, {'upper': 'NETWORKSETTINGS', 'lower': 'networksettings', 'srcline': 109, 'name': 'networksettings', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::NETWORKSETTINGS', 'field': 'DEFAULT::networksettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 60, 'description': 'The type of wifi selection (auto, manual)', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'NetworkSettingsWifiSelectionType', 'edit_method': "{'enum_description': 'The type of wifi selection (auto, manual)', 'enum': [{'srcline': 57, 'description': 'Auto selection', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionType_auto'}, {'srcline': 58, 'description': 'Manual selection', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionType_manual'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 66, 'description': 'The allowed band(s) : 2.4 Ghz, 5 Ghz, or all', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'NetworkSettingsWifiSelectionBand', 'edit_method': "{'enum_description': 'The allowed band(s) : 2.4 Ghz, 5 Ghz, or all', 'enum': [{'srcline': 62, 'description': '2.4 GHz band', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionBand_2_4ghz'}, {'srcline': 63, 'description': '5 GHz band', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionBand_5ghz'}, {'srcline': 64, 'description': 'Both 2.4 and 5 GHz bands', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionBand_all'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 67, 'description': 'The channel (not used in auto mode)', 'max': 50, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'NetworkSettingsWifiSelectionChannel', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 3}, {'upper': 'SETTINGS', 'lower': 'settings', 'srcline': 109, 'name': 'settings', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::SETTINGS', 'field': 'DEFAULT::settings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [], 'type': '', 'id': 4}, {'upper': 'PICTURESETTINGS', 'lower': 'picturesettings', 'srcline': 109, 'name': 'picturesettings', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::PICTURESETTINGS', 'field': 'DEFAULT::picturesettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [], 'type': '', 'id': 5}, {'upper': 'GPSSETTINGS', 'lower': 'gpssettings', 'srcline': 109, 'name': 'gpssettings', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::GPSSETTINGS', 'field': 'DEFAULT::gpssettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 82, 'description': 'The type of the home position', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'GPSSettingsHomeTypeType', 'edit_method': "{'enum_description': 'The type of the home position', 'enum': [{'srcline': 79, 'description': 'The drone will try to return to the take off position', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'GPSSettingsHomeTypeType_TAKEOFF'}, {'srcline': 80, 'description': 'The drone will try to return to the pilot position', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'GPSSettingsHomeTypeType_PILOT'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 84, 'description': 'Delay in second', 'max': 120, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/mech-user/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'GPSSettingsReturnHomeDelayDelay', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 6}], 'parameters': [], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

BebopArdrone3_PilotingSettingsAbsolutControlOn_OFF = 0
BebopArdrone3_PilotingSettingsAbsolutControlOn_ON = 1
BebopArdrone3_PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_OFF = 0
BebopArdrone3_PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_ON = 1
BebopArdrone3_SpeedSettingsHullProtectionPresent_OFF = 0
BebopArdrone3_SpeedSettingsHullProtectionPresent_ON = 1
BebopArdrone3_SpeedSettingsOutdoorOutdoor_OFF = 0
BebopArdrone3_SpeedSettingsOutdoorOutdoor_ON = 1
BebopArdrone3_NetworkSettingsWifiSelectionType_auto = 0
BebopArdrone3_NetworkSettingsWifiSelectionType_manual = 1
BebopArdrone3_NetworkSettingsWifiSelectionBand_2_4ghz = 0
BebopArdrone3_NetworkSettingsWifiSelectionBand_5ghz = 1
BebopArdrone3_NetworkSettingsWifiSelectionBand_all = 2
BebopArdrone3_GPSSettingsHomeTypeType_TAKEOFF = 0
BebopArdrone3_GPSSettingsHomeTypeType_PILOT = 1
