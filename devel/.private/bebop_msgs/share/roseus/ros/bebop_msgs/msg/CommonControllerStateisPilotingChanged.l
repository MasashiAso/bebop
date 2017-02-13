;; Auto-generated. Do not edit!


(when (boundp 'bebop_msgs::CommonControllerStateisPilotingChanged)
  (if (not (find-package "BEBOP_MSGS"))
    (make-package "BEBOP_MSGS"))
  (shadow 'CommonControllerStateisPilotingChanged (find-package "BEBOP_MSGS")))
(unless (find-package "BEBOP_MSGS::COMMONCONTROLLERSTATEISPILOTINGCHANGED")
  (make-package "BEBOP_MSGS::COMMONCONTROLLERSTATEISPILOTINGCHANGED"))

(in-package "ROS")
;;//! \htmlinclude CommonControllerStateisPilotingChanged.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass bebop_msgs::CommonControllerStateisPilotingChanged
  :super ros::object
  :slots (_header _piloting ))

(defmethod bebop_msgs::CommonControllerStateisPilotingChanged
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:piloting __piloting) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _piloting (round __piloting))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:piloting
   (&optional __piloting)
   (if __piloting (setq _piloting __piloting)) _piloting)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint8 _piloting
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint8 _piloting
       (write-byte _piloting s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint8 _piloting
     (setq _piloting (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get bebop_msgs::CommonControllerStateisPilotingChanged :md5sum-) "58c8cfa4c09dedbc7459b83c5d31b9fd")
(setf (get bebop_msgs::CommonControllerStateisPilotingChanged :datatype-) "bebop_msgs/CommonControllerStateisPilotingChanged")
(setf (get bebop_msgs::CommonControllerStateisPilotingChanged :definition-)
      "# CommonControllerStateisPilotingChanged
# auto-generated from up stream XML files at
#   github.com/Parrot-Developers/libARCommands/tree/master/Xml
# To check upstream commit hash, refer to last_build_info file
# Do not modify this file by hand. Check scripts/meta folder for generator files.
#
# SDK Comment: Tell the device when the controller application enters/leaves the piloting HUD.

Header header

# 0 when the application is not in the piloting HUD, 1 when it enters the HUD.
uint8 piloting

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :bebop_msgs/CommonControllerStateisPilotingChanged "58c8cfa4c09dedbc7459b83c5d31b9fd")


