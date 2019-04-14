import cv2
import os
import numpy as np
import argparse

def keyframeDetection(video_path, threshold):

	cap = cv2.VideoCapture(video_path)
	fps = int(cap.get(5))
	if(fps==0):
	    print("Not available")

	keyframePath = 'keyframes'
	if not os.path.exists(keyframePath):
		os.makedirs(keyframePath)
		# Read the first frame.
	ret, prev_frame = cap.read()

	i = 0
	count = 0
	cv2.imwrite('keyframes/'+str(i)+'.jpg',prev_frame)
	while ret:
	    ret, curr_frame = cap.read()
	    if ret:
	        diff = cv2.absdiff(curr_frame, prev_frame)
	        non_zero_count = np.count_nonzero(diff)
	        if non_zero_count > threshold:
	        	print("Saving Frame number: {}".format(i), end='\r')
	        	cv2.imwrite('keyframes/'+str(i)+'.jpg',curr_frame)
	        	count += 1
	        prev_frame = curr_frame
	        i += 1
	print("Total Number of frames saved: {}".format(count))

parser = argparse.ArgumentParser()
parser.add_argument('-s','--source', help='source file', required=True)
parser.add_argument('-t','--Thres', help='Threshold of the image difference', default=3000000)
args = parser.parse_args()

if __name__ == "__main__":
	keyframeDetection(args.source, float(args.Thres))
