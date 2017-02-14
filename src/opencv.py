
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist



#size = (640, 480)
#lower_color = np.array([0,100,100])
#upper_color = np.array([10,255,255])
#lower_color = np.array([30,0,50])
#upper_color = np.array([50,90,160])
lower_color = np.array([10,130,130])
upper_color = np.array([30,255,255])
cv2.namedWindow('frame')
#cv2.namedWindow('trackbar')
cap = cv2.VideoCapture(1) # 0はカメラのデバイス番号
___, frame = cap.read()
pre_mask = np.zeros((np.shape(frame)[0],np.shape(frame)[1]),dtype='uint8')
pre_mask1 = np.zeros((np.shape(frame)[0],np.shape(frame)[1]),dtype='uint8')
pre_mask2 = np.zeros((np.shape(frame)[0],np.shape(frame)[1]),dtype='uint8')
pre_mask3 = np.zeros((np.shape(frame)[0],np.shape(frame)[1]),dtype='uint8')
pre_mask4 = np.zeros((np.shape(frame)[0],np.shape(frame)[1]),dtype='uint8')
pre_mask5 = np.zeros((np.shape(frame)[0],np.shape(frame)[1]),dtype='uint8')
callnum=0
pub_takeoff = rospy.Publisher('bebop/takeoff',Empty, queue_size=10)
pub_land = rospy.Publisher('bebop/land',Empty,queue_size=10)
pub_piloting = rospy.Publisher('bebop/cmd_vel',Twist,queue_size=10)
rospy.init_node('talker')
rate = rospy.Rate(4)

obj_beb = np.array([75,320,200])

def get_square():
	global callnum, pre_mask, pre_mask1, pre_mask2,pre_mask3, pre_mask4, pre_mask5
	# カメラをキャプチャする
	# retは画像を取得成功フラグ
	for i in range(6):
		ret, frame = cap.read()
	if ret == False:
		return -1,-1,-1
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_color, upper_color)
	kernel = np.ones((40,40),np.uint8)
	mask = cv2.dilate(mask, kernel, iterations = 2)
#		mask=255-mask
	area = 7000
	if callnum > 5:
		mask1 = mask * (pre_mask != 0) * (pre_mask1 != 0) * (pre_mask2 != 0)*(pre_mask3 != 0) * (pre_mask4 != 0) * (pre_mask5 != 0)
		cv2.imshow('mask1', mask1)
		contours, hierarchy = cv2.findContours(mask1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contours:
			M = cv2.moments(cnt)
			if M['m00'] > area:
				area = M['m00']
				x = int(M['m10'] / M['m00'])
				y = int(M['m01'] / M['m00'])
				cv2.circle(frame, (x, y), 10, (0,255,0), -1)
				cv2.circle(frame, (obj_beb[1],obj_beb[2]), 10, (0,0,255),-1)
		cv2.imshow('frame', frame)
	pre_mask = mask
	pre_mask1 = pre_mask
	pre_mask2 = pre_mask1
	pre_mask3 = pre_mask2
	pre_mask4 = pre_mask3
	pre_mask5 = pre_mask4
	callnum += 1
	if area > 7000:
		print "--------"
		return x, y, area
	else:
		return -1,-1,-1

def onMouse(event, x,y,flags,param):
	global obj_beb, frame
	if event == cv2.EVENT_LBUTTONDOWN:
		obj_beb[1] = x
		obj_beb[2] = y

def onChange1(pos):
	lower_color[0] = pos
	print lower_color
def onChange2(pos):
	upper_color[0] = pos
	print lower_color
def onChange3(pos):
	lower_color[1] = pos
	print lower_color
def onChange4(pos):
	upper_color[1] = pos
	print lower_color
def onChange5(pos):
	lower_color[2] = pos
	print lower_color
def onChange6(pos):
	upper_color[2] = pos
	print lower_color
if __name__ == '__main__':
	for iterations in range(10):  
		pub_takeoff.publish()
		rate.sleep()
	cv2.cv.SetMouseCallback('frame',onMouse)
#	cv2.cv.CreateTrackbar('hmin','trackbar',0,180,onChange1)
#	cv2.cv.CreateTrackbar('hmax','trackbar',180,180,onChange2)
#	cv2.cv.CreateTrackbar('smin','trackbar',0,255,onChange3)
#	cv2.cv.CreateTrackbar('smax','trackbar',255,255,onChange4)
#	cv2.cv.CreateTrackbar('vmin','trackbar',0,255,onChange5)
#	cv2.cv.CreateTrackbar('vmax','trackbar',255,255,onChange6)
	while not rospy.is_shutdown():
		if cv2.waitKey(1) == 27:
			break
		x_beb, y_beb, area = get_square()
		msg = Twist()
		print x_beb, y_beb
		if x_beb > 0:
			msg.linear.y = -(x_beb - obj_beb[1])/8000.0
			msg.linear.z = (y_beb - obj_beb[2])/2000.0
		print msg.linear.y, msg.linear.z
		pub_piloting.publish(msg)
		rate.sleep()
	for iterations in range(10):
		pub_land.publish()
		rate.sleep()
	# キャプチャを解放する
	cap.release()
	cv2.destroyAllWindows()
