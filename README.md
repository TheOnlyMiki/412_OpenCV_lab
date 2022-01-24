# Introduction
The goals of this lab are to:
* Intertacting with ROS camera topic to get real-time pictures
* Knowing how to filter color through build in functions in opencv
* Knowing how to match and compare images by feature detecture and matcher

This lab will use the ROS noetic environment and requires gazebo and turtlebot3 (see below for installation instructions)

### Installing lab package
```
cd ~/catkin_ws/src

git clone <repo-url>

cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
```


# Instructions and Potentailly Helpfur Resources (non-exhaustive)

First of all, we have to know that ROS store images which get from it's sensor by it own message formate - `senor_msg/Image`. However we can not using these meesages directly to work with Computer Vision algorithm. Therefore, we need to use `CvBridge`, which is a ROS library that provides an interface between ROS and OpenCV, to make conncetion and convert ROS images to OpenCV formate. After you make the package, in the `src` folder, there is a simple python file whcih shows how to use CvBridge and open the camera of robot, called `camera.py`. If you want to know more infromation about this, you can go to http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython.

In this lab, you also need to know the how to detect colors in images. In order to descibe a color, We need to know the properties that make up this color. there are many way to define a color, a well knowed approach is RGB which describe all the colors by mixing red, green, and blue(Note: in Pyhton, ordering change to BGR). However, OpenCV uses HSV(Hue Saturation Value) model to describe color. If you want to know more about HSV model, please visit https://en.wikipedia.org/wiki/HSL_and_HSV . Therefore, in order to get color information in an image for specific model from other model, we need to use a function which include in `cv2` library called `cvtColor(src, code)`. Forexample, if you we want to convert a RGB image to HSV image in python, it should be like `cvtColor(image, cv2.COLOR_BGR2HSV)`. OpenCV also enable us to make other converting, such as RGB to Gray, etc. If you want to learn more about color converting 
function, you can visit these two link https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html ,and https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/. 

After we know how to describe color, we need to know how to handle color. Now, consider a question. If we only want to see the specific color in an image, what should we do?  The asnwer is let just watch this specific color. I know this sounds like crap, but it indeed what we will do in the program. We already know the properties of the color we want, and then we can set a window or bound so that our camera can only look for colors within this range. In order to do this, we need to use another funcion inlcude in `cv2` libray called `inRange(src, lower_bound, upper_bound)`. If you want to know more information about this function, please visit https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html.  After you make the package, in the `src` folder, there is a simple python file whcih shows how to convert an image from RGB to HSV and fliter color, called `fliter.py`.


# Task 

In this lab you need to let your robot move along with the track on the ground. track is split in differents color.

Whtie track is normal track. 

Blue track is accelertation belt which required you to increase your robot's speed to 1.5 times. 

Green tracks is a shortcut, you should let your robot change track from white to green and back to whtie when you pass green track. 

Red track is the final position where used to stop your robot.


# Grading
40%, can completely follow the entire path, which is the turtlebot able to follow the WHITE line perfectly. (shortcut is special)

20%, the GREEN line (shortcut) can be filtering, and passed completely. (Hardest part, because incorrect timing of switching color filters will cause the robot to walk back along the white line)

10%, the BLUE line (acceleration band) can be filtering, and passed completely by increasing half speed (1.5x).

10%, the Red floor tiles (speed bumps) can be filtering, and slowed down by a half speed (0.5x), then start matching Stop-Sign icon.

20%, Turtlebot can effectively match the Stop-Sign icon, and should stopeed before passed red area.


### Launching world and turtlebot
`roslaunch lab_2 main.launch`


### Turtlebot3 install
```
mkdir -p ~/catkin_ws/src/
cd ~/catkin_ws/src/
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git

cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
```
