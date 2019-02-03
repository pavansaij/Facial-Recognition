# Facial-Recognition
Python/Tensorflow based facial recognition system.

Dependencies:
Tensorflow (1.4.0)
Scipy (0.17.0)
Scikit-learn (0.19.1)
Opencv (2.4.9.1)

Process:

1.Database_Generator/Data Collection: To add new users for training thier images which can be done either by directly adding user's photos to test_images by creating a sub-folder with the user's name,
or execute the following script: python .\Facial_Recognition\source_files\facial_dataset_generator_camera.py -n "user_name" which captures user's images.

2.Pre-Process: For pre-processing run .\Facial_Recognition\source_files\pre_process.py script. This file will crop the face of each face and label each face image with the folder name. And generate a text file “bounding_boxes_433.txt” where you see labelling of data. 
This type of labelling can be accomplished with image labelling data. All the work will be done by the program automatically you only have to run this file.

3.Training: For training the model run .\Facial_Recognition\source_files\training.py script. After preprocessing of data we have to train model with a predefined model. It will train model and also pkl file will be saved inside directory “class”

4.Identification/Recognition: Indentification can be done in three ways,
	i)   Real-time via camera: Run identify_face_camera.py script.
	ii)  Via Input Image: Run .\Facial_Recognition\source_files\identify_face_image.py -p "path_to_image".
	iii) Via Input_Video: .\Facial_Recognition\source_files\identify_face_video.py -p "path_to_video".
	
	
