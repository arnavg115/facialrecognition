# Face Detection using tensorflow
This is a project I have worked on using code from many sources and some of my own.
## Disclaimer: NOT ALL OF THE CODE IS MINE
A lot of collect.py was from <a href ="https://github.com/SouravJohar/rock-paper-scissors ">Sourav Johar's rock-paper-scissors project</a>. However I added the face detection algorithm to collect the data on the face. For the face detection algorithm I used <a href="https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81"> Adarsh Menon's post</a>. I would check both of them out. In addition I do not own the haarcascade_frontalface_default.xml. This is from the opencv github page and was made by Rainer Lienhart. Make sure to read the copyright below as downloading this file means you agree to it. To see this go to file and also check out the <a href ="https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml">opencv github.</a>
---

## The code:
1. Get all of the files
Clone this repository
```shell
git clone https://github.com/arnavg115/facialrecognition.git
```
Get the 
2. Install all of the nescessary packages
Install tensorflow.
Quick note: If you are on windows I would recommend following <a href= "https://www.tensorflow.org/install/pip"> this guide</a> as there are some other files you may have to install.
```shell
pip install tensorflow
```
Install opencv
```shell
pip install opencv-python
```
3. Gather the nescessary data
In the terminal type
```shell
python collect.py /name of person/ /number of images/
```
For the /name of person/ put in the name of the person you are collecting data for. For the /number of images/ put in the number of images you wish to capture. I recommend 300 images as sometimes the face detection algoorithm can wrongly detect an object and the save it. After hitting enter the program should launch a window where you can see your webcam's stream. I would make sure it is able to see your face and puts a box around it. Once this is done hit A on your keyboard for it to start capturing images. It should create a folder under the name "image_data" and the images will be saved to "/name of person/". Now I would go through the pictures and delete all of the pictures where there is no face and delete them. Repeat this for as many faces you want the model to recognize.
4. Train the model
Once you have captured the needed data, run the training script.
```shell
python train.py
```
It might take a while depending on your hardware. It should start with each of the epochs. Then it should save the model to a file called 'model.h5'. 
Note: Delete this file before retraining as it might lead to errors in the program. 
5. Use the AI to detect faces
So now that you have done all of the prep work you can start the program with
```shell
python detect.py
```
For now it is able to detect one face at a time. I am working on making it able to do many faces. When run it should open the same webcam window used to get the training data. Just like before it should box your face automaticaly and also recognize it.
---
## Other stuff
Feel free to modify the code that I wrote and also checkout the projects of both Sourav Johar and Adarsh Menon as they are very interesting as well and really well made.
### Some errors
<<<<<<< HEAD
Make sure tensorflow and keras are updated to the latest versions. I have only tested it with two people so there might errors with more than two people. If for some reason opencv(cv2) or numpy is giving errors please downgrade them using pip. One basic issue you may have is with pip shown below.
#### Example:
Downgrade numpy.
```shell
pip install numpy==1.19.3
```
Downgrade opencv
```shell
pip install opencv-python==4.4.0.44
```
#### pip error
If you try for example
```shell
pip install tenorflow
```
and it gives an error
```shell
-bash: pip: command not found
```
Instead of pip for all of the pip commands use pip3. So type
```shell
pip3 install tensorflow
```
=======
Make sure tensorflow and keras are updated to the latest versions. I have only tested it with two people so there might errors with more than two people.  

