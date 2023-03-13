
i did not use any datasets, i used open cv with haarcascade 
The code performs the following steps:
-It loads an input image from the specified file path using the OpenCV imread function.
-It loads a pre-trained face detection model using the OpenCV CascadeClassifier class.
-It detects faces in the input image using the detectMultiScale method of the face detection model.
-For each detected face, it crops out the region of interest (ROI) from the input image using the face's bounding box coordinates (x, y, w, h).
-It applies a Gaussian blur filter to the face ROI using the OpenCV GaussianBlur function.
-It replaces the original face ROI in the input image with the blurred face ROI.
-It displays the resulting image on the screen or saves it to a file.
