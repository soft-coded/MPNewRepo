## iiest and all that jazz for header

### department of cst

**date** // try right aligning this once. If it looks good, keep it

**center align {**

### Mini project on
// title is provisional ofc
# Object recognition to keep social distancing norms in check

*By:*
* Name 1
* Name 2
* Name 3
* Name 4
* Name 5

**} center align**

**right or left align (whichever looks better) {**

* Prof. Samit Biswas
* Madam's name if required

**} right or left align**

--------------------New Page-------------------

# CERTIFICATE

**content {**

It is certified hereby that this report, titled *whatever the tile is*, and all the attached 
documents herewith are authentic records of *names and enrol id of all* from the prestigious department of Comp sc and tech of the distinguished and respected IIEST Shibpur under my guidance.

The works of these students are satisfies all the requirements for which it is submitted.
To the extent of my knowledge, it has not been submitted to any different institutions for
the awards of degree/diploma.

**} content**

**right align {**

*Prof name*
*Prof post*
IIEST, Shibpur

**} right align**

--------------------New Page-------------------

# ACKNOWLEDGEMENT

**content {**

We, as the students of IIEST, consider ourselves honoured to be working with *prof*.
The success of this project would not have been possible without his useful insights,
appropriate guidance and necessary criticism. 

We would pass our token of token of gratitude to the department of cst as well for providing
us with the opportunity to be able to tackle real world problems while improving
our problem solving ability and thinking capacity by organizing this project. We all have
learnt quite a handful of new skills and are eager to use them henceforth as well.

**} content**

**right align {**

* Name 1
* Name 2
* Name 3
* Name 4
* Name 5

**} right align**

--------------------New Page-------------------

# CONTENTS (make sure to hyperlink all these later)

1. INTRODUCTION
    1. Motivation..................................pg no whatever
    1. Idea behind the workings....................pg

1. PREREQUISITES
    1. Outdoor requirements
    1. Indoor requirements

1. THE PROJECT
    1. Software used

1. SHORTCOMINGS
    *will see later what to put in here*

1. HENCEFORTH
1. REFERENCES

--------------------New Page-------------------

# INTRODUCTION

## Motivation

Coronaviruses are a group of related RNA viruses that cause diseases in mammals
and birds. In humans and birds, they cause respiratory tract infections that can
range from mild to lethal. Mild illnesses in humans include some cases of the
common cold (which is also caused by other viruses, predominantly rhinoviruses),
while more lethal varieties can cause SARS, MERS, and COVID-19.

With the increase in the spread of the dangerous and highly contagious **Novel**
**Coronavirus** and the underlying disease caused by it, **COVID-19**,
it is a requirement now more than ever to follow the social distancing
norms set in place by the scientists and researchers.

But as we all know, India is a country with a not-so-small population,
so it is pretty understandable and obvious that the law enforcement will
not be able to actually enforce it on every single person. Therefore,
new means of automata in place of actual individuals is a no brainier.
That is where we come in.

## Idea behind.......

The idea behind the working of this software was simple. The software just needed
to be able to look at a live feed (or recorded footage) of a camera and know
which of the people present in the footage are actually following the social 
distancing norms and which of them are not, and mark either one appropriately.
That is where out journey to build a social distance checker started.

// will add more later probably lul

--------------------New Page-------------------

# KNOWLEDGE REFINEMENT

Before we settled on the topic of object detection and started building this project, we got some practice, which was necessary since we were going to dip our toes in image processing.

## Histogram

* We made histograms for grey-level images. This was done using both the OpenCV's ``ravel()`` function and our own implementation of it, called ``compute_histogram()``.

// insert the compute_histogram vs ravel image here from the 2nd ppt

* Once that was over, we moved onto some Image Enhancement skills. Here we implemented noise reduction functions using mean, mode and median filters.

// I leave it upto you what images to insert here from ppt 3.

* Then we implemented Otsu's thresholding algorithm using minimization of within class variance approach. 

// insert otsu's code here

// I think this much useless information should be enough. Really dont want to spend time on this

# PREREQUISITES

## Outdoor requirements

It is important to mention here that this is not a portable software that can
be fed any footage and just be expected to work. There need to be some
calibration measures taken to actually get this software working:

* Actually knowing the local social distancing norms
    * The minimum distance set for social distancing by the local gov

* Finding a good position for the camera
    * The footage needs to be taken from a high enough place

* Knowing the required distance in pixels
    * This will depend on the position and angle of the camera's view

## Indoor requirements

The tools used to build this software are platform independent. However,
there are a few requirements needed to be fulfilled to get the program
working. These are:

* Python
    * Python - 3.5 or above
    * OpenCV - version 2 or above
    * numPy

* Hardware acceleration
    * A GPU is optional yet recommended to get the best performance
    * If a GPU is not being used, the CPU need to be good enough

--------------------New Page-------------------

# THE PROJECT

## Software used

The softwares used to build this *checker* are:

1. An Integrated Development Environment (IDE)

    An integrated development environment (IDE) is a software application that 
provides comprehensive facilities to computer programmers for software 
development. An IDE normally consists of at least a source code editor, build 
automation tools and a debugger. Some IDEs contain the necessary compiler, 
interpreter, or both; others, do not.

1. Python

    Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of 
significant whitespace. Its language constructs and object-oriented approach aim 
to help programmers write clear, logical code for small and large-scale projects.

    **Why did we choose Python?:**
    * Python has an upper hand when it comes to software based on
    image recognition and object detection. Since it is the main
    objective of the project, choosing python was a given.

    * Python is unbeaten when it comes to Machine Learning. Python has
    support for myriad machine learning libraries, such as OpenCV, the
    one being used here.

    * Python is comparatively easier to understand and learn. The syntax
    is clear and simple to read and write.

    * And just our overall experience of using python for years.

1. Google Colab

    After working on the project for quite some time, we realised that we did
not have enough hardware resources at out disposal to actually make the
*checker* work smoothly. So we decided on shifting to Google Colab.
Google colab is an online iPython development environment similar to 
Jupyter Notebook. It uses CUDA acceleration to speed up processes, so we
switched to it rather than continuing development locally.

1. LaTeX

    LaTeX was used to write this report. LaTeX is a software system for document 
preparation. When writing, the writer uses plain text as opposed to the formatted 
text found in "What You See Is What You Get" word processors like Microsoft Word 
or LibreOffice Writer.

// we can insert a photo of each of these

## The Program

### Outline 

The blueprint of this *checker* that we thought of initially:

1. Video Input
    * Need some way to handle video input coming through the camera feed

1. Processing
    * The input needs to be processed somehow

1. Detecting people
    * Need to identify people in the video feed

1. Measuring distance between each couple
    * Need to calculate the distance between every two persons

1. Mark the violations
    * Need to mark the ones that violate social distancing norms

### Proceedings

How we proceeded with the outlines of the blueprint:

1. Video Input
    * This was easier than we expected it to be. We just had to get our hands
    on some recorded footage of somewhat populated areas. We refrained from using live
    footage because:
        * It is tough to get our hands on the light footage of a security camera or the equivalent.
        * If the checker worked on recorded footage, it would work on live footage as well.
    * The videos we ended up choosing:
    // insert a frame from the videos here

1. Processing
    * We used the OpenCV library for our video/image processing. It is a really handy library that can be used for image processing, object detection and many other purposes. 
    // insert some of the opencv code here 

1. Detecting people
    * For this we decided to go with the You Only Look Once (YOLO) algorithm for object detection. The algorithm itself is discussed a bit later in the report. 
    * We did not train the object detection neural network model ourselves. We used the *insert model name* model because of time constraints.
    // insert some yolo code here lul

1. Measuring distance between each couple
    * This was undeniably the toughest part of the project and took the longest time. First we decided to go with measuring the distance between the centroids of every two detections. But that may not work in every condition since it depends on the placement of camera and the view angle from the ground and perpendicular to the ground.
    * A conversion of the 3-dimensional footage being fed to the algorithm to 2-dimensions was more than necessary to get the top view of every frame to avoid the *viewing angle problem*.
    * Enter **Bird's Eye View (BEV)**. This is what we called the top view of every frame. This was made possible by OpenCV's ``getPerspectiveTransform()`` and ``warpPerspective()`` functions.

    // insert the bird's eye view function here
    * This piece of code essentially calculates what is called a *transformation matrix* for the supplied image (frame) which can then be used to get the centroids of the points as seen from a vertical position directly above the center of the rectangle passed to the function.
    * We used this to get a two dimensional view of every frame and calculate distance between every pair of detections (people).

1. Mark the violations
    * This was again a fairly easy step. We just needed the coordinates of the people in the *violation zone* and make their detection rectangle red as opposed to green.

## The YOLO Algorithm

* **What is the YOLO algorithm?**

    * **YOLO (“You Only Look Once”)** is an effective real-time **object recognition** algorithm, first described in the seminal 2015 paper by Joseph Redmon et al.
    * **Image classification** done by YOLO algorithm aims at assigning an image to one of a number of different categories (e.g. car, dog, cat, human, etc.), essentially answering the question “What is in this picture?”. One image has only one category assigned to it. 
    * **Object localization** then allows us to locate our object in the image, so our question changes to “Where is it?”. 
    * **Object detection** provides the tools for doing just that –  finding all the objects in an image and drawing the so-called bounding boxes around them.

    // insert a picture of YOLO working here

* **Where does YOLO stand in the *object detection algorithms* chart?**

    There are a few different algorithms for object detection and they can be split into two groups:

    1. **Algorithms based on classification**: They are implemented in two stages. First, they select regions of interest in an image. Second, they classify these regions using convolutional neural networks. This solution can be slow because we have to run predictions for every selected region. A widely known example of this type of algorithm is the Region-based convolutional neural network (RCNN) and its cousins Fast-RCNN, Faster-RCNN and the latest addition to the family: Mask-RCNN. Another example is RetinaNet.

    1. **Algorithms based on regression**: Instead of selecting interesting parts of an image, these predict classes and bounding boxes for the whole image in one run of the algorithm. The two best known examples from this group are the **YOLO *(it stands here)*** family algorithms and SSD (Single Shot Multibox Detector). They are commonly used for real-time object detection as, in general, they trade a bit of accuracy for large improvements in speed. 

* **How does YOLO work?**

    [reference to the article](https://appsilon.com/object-detection-yolo-algorithm/)

    * To understand the YOLO algorithm, it is necessary to establish what is actually being predicted. Ultimately, we aim to predict a class of an object and the bounding box specifying object location. Each bounding box can be described using four descriptors:
        1. Center of a bounding box (b<sub>x</sub>,b<sub>y</sub>)
        1. Width of the bounding box (b<sub>w</sub>)
        1. Height of the bounding box (b<sub>h</sub>)
        1. Value corresponding to the class of an object (car,person,traffic lights etc)
        1. The probability (confidence value) that there is an object bounding the box (p<sub>c</sub>)

    // insert yoloWorks1.png here from the Real Deal/Pictures folder

    * Then, the image is split into cells, typically using a 19×19 grid. Each cell is responsible for predicting 5 bounding boxes (in case there are multiple objects in this cell). Therefore, we arrive at a large number of 1805 bounding boxes for one image.

    // insert yoloWorks2.png here

    * Most of these cells and bounding boxes will not contain an object. Therefore, the value pc is predicted, which serves to remove boxes with low object probability and bounding boxes with the highest shared area in a process called **non-maxima suppression**.

    // insert yoloWorks3.png here

* **Darknet implementation of YOLO**

    * There are a few different implementations of the YOLO algorithm on the web. Darknet is one such open source neural network framework. Darknet was written in the C Language and CUDAtechnology, which makes it really fast and provides for making computations on a GPU, which is essential for real-time predictions.

    * The Darknet YOLO model that we used here is pre-trained on the COCO (Common Objects in COntext) dataset. // insert a reference to the model's website here

----------------New page-----------------
# SHORTCOMINGS

Like every other piece of software, this *checker* is not perfect. It has its own limitations and shortcomings.

* **The camera that will record the feed needs to be placed at a position high enough** so that the *viewing angle problem* can be avoided. Placing the camera at a horizontal level will not allow the checker to work correctly. For the lowest error margin, the camera needs to pe place perpendicular to the ground, which is not always possible.

* **Enormous amount of computing power will be needed to make the algorithm work for a live footage**. Even for recorded footage, we were not able to get more than 5-7 frames per second with a decent GPU. This is due to the object detection algorithm taking time in detecting objects. It is not practical to use this *checker* on a live feed.

* **The minimum social distance needs to be known in pixels beforehand**. This is a lot more difficult than it sounds since a small change in viewing angle can bring a large change in the distance measurements. Plus it is not easy to calculate any distance in pixels. We ourselves have taken arbitrary values using trial and error here to make things work as they should.

* **The algorithm will completely fail in overly populated areas**. This is due to how YOLO works. It sacrifices accuracy for speed, therefore it really struggles with multiple objects in a single *cell*. // may want to include a bad frame from shibuya.mp4 here

// will insert more later, cant think of any rn

## Solutions 

A few of these limitations can be solved by adopting the following means:

* Recording via a drone can completely eliminate the *viewing angle problem*, since a drone can be stabilized at exactly 90 degrees to the ground. Indoors, a camera at the center of the ceiling will work wonders.

* The *checker* can work in densely populated areas as well if we use RCNN or any classification based algorithm. But that will further slow down the *checker* since RCNN is a much slower algorithm than YOLO.

* **Non-Maxima Suppression Analysis**

    * To make the algorithm work in relatively dense and overpopulated areas, we were suggested to adjust the Non-Maxima Suppression (NMS) threshold by Prof. Samit Biswas. 

    * So we decided to try various different values of the NMS threshold. A few of the terms that we used in our NMS analysis are:
        * **Bad Frame**: This is a frame in which the algorithm fails to correctly identify people and instead gives a horrible big box as the output.
        // may want to include a bad frame here
        * **Total Frames**: This is the number of total frames in the entire video or the length of the video to be analysed.
        * **Performance Ratio**: This is simply (Number of Bad Frames)/(Total Frames).
        * **Object threshold**: This is the confidence value for which a detection is actually considered. Any detection with confidence (p<sub>c</sub>) equal to or above this value is taken into consideration.
    * From this it was clear that the threshold value for which the Performance Ratio will be the lowest would be the best value. We also tinkered with the Object Threshold to get the best possible outcome. The script that we wrote for this was:
    // insert the "Main" part from performance_analysis.ipynb here
    * After running the test for a number of threshold values, we got this graph:
    // insert the graph here 
    * From this, we can see that the algorithm gives the best results for NMS threshold around 0.010 to 0.014 and for the Object threshold greater than 0.9.
    * Of course, this is not ideal since **it will ignore most of the detections**.

------------New page------------

# HENCEFORTH

While keeping the limitations in mind, this app does serve well as a starting point for an automated social distance checker. The tedious process that needed to be done manually can now be done by a software. This is undoubtedly music to the ears of any software developer and enthusiast.

With that being said, here is how we can improve the *checker*:

* We can make the entire thing command line based so that an average consumer will not have to dig around the code to calibrate the algorithm to his or her needs.

* We can (and will) train our own model of YOLO that will only be used to detect people. This can tremendously increase the speed and bring down the processing power requirements.

* We can add a help panel for first time users.

// will add more later, suggest something to add

# REFERENCES

// will fill this up at the very end

## -------------finish------------------

// additional material:
// histogram shit is added before "PREREQUISITES" section
// NMS analysis has been added to Solutions section
// changes have been made to "how yolo works" section's first paragraph