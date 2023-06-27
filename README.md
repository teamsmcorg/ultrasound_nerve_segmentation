# Ultrasound_Nerve_Segmentation
This repository contains the code and resources for an ultrasound nerve segmentation project. The project aims to develop a deep learning model that can accurately segment nerves in ultrasound images, which can be useful in medical applications such as nerve localization during surgeries or diagnostics.
# Project Structure
The project is organized as follows:

├── code.ipynb- main source code  
  
├── app.py- contains code for deployment  

├── index.html - frontend page display code

├── kaggle.json- used to upload datasets

├── model_nerve.h5 - a saved file which is further used for deployment

└── README.md
# Data:
This directory contains the ultrasound image dataset. The train folder contains the training images, the test folder contains the test images, and the masks folder contains the corresponding segmentation masks for the training images.
Dataset is taken from kaggle - https://www.kaggle.com/c/ultrasound-nerve-segmentation/data
The dataset can also be downloaded using Kaggle API
kaggle competitions download -c ultrasound-nerve-segmentation
Easy way to use Kaggle datasets in Google Colab- https://www.kaggle.com/discussions/general/51898 

![59549678-d133e080-8f7e-11e9-9c0e-3c5c73222c25](https://github.com/teamsmcorg/ultrasound_nerve_segmentation/assets/123300983/b6efd1ac-0b74-4d34-beed-107c2531a1a2)

# Training
The images are prprocessed and resized to (128 , 128).

The model is compiled using Adam optimizer , binary crossentropy as loss and accuracy as metrics.

The model is trained for 50 epochs with Early stopping , in case the validation loss doesn't lower further.

An accuracy of around 98% is achieved by the model on the test data set.

- Build a model and train it
 
 - Evaluate the model
 
 - Building a landing page using Flask
 
 - Deploy the app

# Contributing
Contributions to the project are welcome. If you have any ideas, suggestions, or bug fixes, please submit a pull request. Additionally, feel free to open an issue if you encounter any problems or have questions related to the project.




