import cv2
if __name__ == '__main__':
	cap = cv2.VideoCapture(1)

	while True:
		ret, frame = cap.read()
		if ret == False:
			continue
		cv2.imshow('frame', frame)
		k=cv2.waitKey(10)
		if cv2.waitKey(10) == 27:
			break

		cap.release()
		cv2.destroyAllWindows()



