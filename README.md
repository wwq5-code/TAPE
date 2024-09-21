# TAPE

# TAPE: Tailored Posterior Difference for Auditing of Machine Unlearning
## Overview
This repository is the official implementation of TAPE, and the corresponding paper is under review.


## Prerequisites

```
python = 3.10.10
torch==2.0.0
torchvision==0.15.1
matplotlib==3.7.1
numpy==1.23.5
```

We also show the requirements packages in requirements.txt

Here, we demonstrate the overall evaluations, which are also the main achievement claimed in the paper. We will explain the results and demonstrate how to achieve these results using the script and corresponding parameters.

Evaluated on NVIDIA Quadro RTX 6000 GPUs,
### TABLE I: General Evaluation Results on MNIST, CIFAR10, STL-10, and CelebA:

On MNIST, ESS=20

| On MNIST             | Original    | MIB      |   TAPE   | 
| --------             | --------    | -------- | -------- |  
| Running time (s)     | 613         | 638      |  113     |  
| Model Utility (Acc.) | 99.05%      | 98.73%   | 99.05%   |   
| Rec. Sim.            | -           | -        |   0.933  |  
| Unl. Verifiability  | 0.00%       | 0.00%    | 98.67%   |  
 
On CIFAR10, ESS=20

| On CIFAR10           | Original    | MIB      |   TAPE   | 
| --------             | --------    | -------- | -------- |  
| Running time (s)     | 644         | 673      |  113     |  
| Model Utility (Acc.) | 81.62%      | 79.13%   | 81.62%   |   
| Rec. Sim.            | -           | -        | 0.973    |  
| Unl. Verifiability  | 0.00%       | 0.00%    | 97.44%   |  

In this table, we can achieve these metric values by running corresponding python files.


1. To run the TAPE on MNIST, we can run
```
python /MUV_Reconstruciton/On_MNIST/Our_method/MUV_on_MNIST_unl_multi.py
```

2. To run the TAPE on CIFAR10, we can run

```
python /MUV_Reconstruciton/On_CIFAR10/Our_method/MUV_on_CIFAR10_unl_multi.py
```

3. To run the TAPE on STL-10, we can run

```
python /MUV_Reconstruciton/On_STL10/Our_method/MUV_on_STL10_unl_multi.py
```

4. To run the TAPE on CelebA, we can run

```
python /MUV_Reconstruciton/On_CelebA/Our_method/MUV_on_CelebA_unl_multi.py
```
Note that, to sucessfully run the program on CelebA, we need first prepare the CelebA dataset, which can be downloaded from: 
(https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg)