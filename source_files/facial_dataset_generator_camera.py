import cv2
import sys, os
import argparse

def get_path_for_classifier():
    source_pathname = os.path.dirname(sys.argv[0])       
    if "/" in source_pathname:
        components = list(source_pathname.split('/'))
    else:
        components = list(source_pathname.split('\\'))
    components.pop(-1)
    images_path = "\\".join(components)+"\\test_images"
    components.append("haar_files")
    components.append("frontal_face_detector.xml")
    classifier_path = "\\".join(components)
    return images_path,classifier_path

def create_image_database():
    count = 0
    new_path = images_path+r"\\"+face_id.lower() 
    try:
        os.mkdir(new_path)
    except:
        print("data already captured")

    while(True):
        _, image_frame = vid_cam.read()
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1
            cv2.imwrite(new_path + "\\" + "capture" + '_' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('frame', image_frame)

        if count>5:
            break

    vid_cam.release()
    cv2.destroyAllWindows()

images_path,classifier_path = get_path_for_classifier()
vid_cam = cv2.VideoCapture(0)
face_detector=cv2.CascadeClassifier(classifier_path)
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="face_id to create folder name")
args = vars(ap.parse_args())
face_id = args["name"]
create_image_database()