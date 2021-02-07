#***IMPORTING ALL THE NECCESSARY DEPENDENCIES***********************
import dlib
import cv2
#********LOADING THE DETECTOTR*************************************
detector= dlib.simple_object_detector("SteeringWheelDetector.svm")
#*********OPENING THE CAMERA FEED***********************************
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    #Applying the operations of the  detecting bounding box overhere
    dets = detector(frame)
    if len(dets)>1 :
       #hence initialising two trackers for the same
       Tracker_LeftFist = dlib.correlation_tracker()
       Tracker_RightFist = dlib.correlation_tracker()
       #starting the two trackers
       Tracker_LeftFist.start_track(frame, dets[0])
       Tracker_RightFist.start_track(frame, dets[1])
       #after initialisation update the tracker with every frame
       Tracker_LeftFist.update(frame)
       Tracker_RightFist.update(frame)
       #finding the new position of the image detected
       LeftFist = Tracker_LeftFist .get_position()
       RightFist = Tracker_RightFist .get_position()
       #now displaying new points
       Left_pt1 = (int(LeftFist.left()), int(LeftFist.top()))
       Left_pt2 = (int(LeftFist.right()), int(LeftFist.bottom()))
       #for 2nd bounding box
       Right_pt1 = (int(RightFist.left()), int(RightFist.top()))
       Right_pt2 = (int(RightFist.right()), int(RightFist.bottom()))

       cv2.rectangle(frame, Left_pt1 , Left_pt2 , (255, 255, 255), 3)
       cv2.rectangle(frame,  Right_pt1 ,  Right_pt2, (255, 255, 255), 3)

#       print "Object {} tracked at [{}, {}] \r".format(pt1, pt2),
      # if dispLoc:
       loc = (int(LeftFist.left()), int(LeftFist.top()-20))
       loc1 = (int(RightFist.left()), int(RightFist.top()-20))

       txt1 = "Left Fist "
       txt2 = "Right Fist"
       cv2.putText(frame, txt1, loc , cv2.FONT_HERSHEY_SIMPLEX, .5, (255,0,0), 1)
       cv2.putText(frame, txt2, loc1 , cv2.FONT_HERSHEY_SIMPLEX, .5, (255,0,0), 1)
       a = (LeftFist.top() + LeftFist.bottom())/2
       b = (RightFist.top() +RightFist.bottom())/2
       if a<b:
          print ("Steering Left")
       if a>b:
          print("Steering Right")

    cv2.imshow("Image", frame)
        # Continue until the user presses ESC key
    if cv2.waitKey(1) == 27:
            break
