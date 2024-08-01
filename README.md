# MUA-PD

# Turning Your Weakness into a Strength: Machine Unlearning Audit Based on Tailored Posterior Difference
## Overview
This repository is the official implementation of MUA-PD, and the corresponding paper is under review.


## Prerequisites

```
python = 3.10.10
torch==2.0.0
torchvision==0.15.1
matplotlib==3.7.1
numpy==1.23.5
```

We also show the requirements packages in requirements.txt


1. To run the MUA-PD on MNIST, we can run
```
python /MUV_Reconstruciton/On_MNIST/Our_method/MUV_on_MNIST_unl_multi.py
```

2. To run the MUA-PD on CIFAR10, we can run

```
python /MUV_Reconstruciton/On_CIFAR10/Our_method/MUV_on_CIFAR10_unl_multi.py
```

3. To run the MUA-PD on CelebA, we can run

```
python /MUV_Reconstruciton/On_CelebA/Our_method/MUV_on_CelebA_unl_multi.py
```
Note that, to sucessfully run the program on CelebA, we need first prepare the CelebA dataset, which can be downloaded from: 
(https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg)