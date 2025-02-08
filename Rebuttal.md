

## Rebuttal to Reviewer G4BY  
  
We greatly appreciate Reviewer G4BY for acknowledging our novelty and providing a detailed summary of our strengths. And greatly appreciate Reviewer G4BY for providing these constructive suggestions. Below, we provide our responses to the comments, denoted by [W] for weaknesses and [Q] for questions.

**W1:** 
The proposed methodology, especially the shadow model and the reconstructor may be complex to implement and verify, with a lack of proofs and technical details. Its impact depends on the availability of local datasets for auditing, which may not be accessible.

**Response to W1:**
Thank you for your insightful comments. For existing reconstruction attacking method, it is hard to implement and verify because the attacker has no knowledge about the training data [2, 34]. However, for the auditing of unlearning, the unlearning user has an advantage, i.e., the unlearning user has access to the unlearning data and some of the data that the user previously uploaded to the server for the model training. It is because the unlearning request is uploaded by the unlearning user. Based on this advantage, we design two strategies to improve the reconstruction effect and audit effect when unlearning multiple samples. 

[2]. Balle, Borja, Giovanni Cherubin, and Jamie Hayes. "Reconstructing training data with informed adversaries." 2022 IEEE Symposium on Security and Privacy (SP). IEEE, 2022.
[34]. Salem, Ahmed, et al. "{Updates-Leak}: Data set inference and reconstruction attacks in online learning." 29th USENIX security symposium (USENIX Security 20). 2020.



**Q1:**
Should the "Figure 2: Approximate unlearning process..." result be cons of certain unlearning algorithm, as the backdoored data and the erased genuine datasets should not be awared to the model unlearning process?

**Response to Q1:**
We greatly appreciate Reviewer's insightful questions. Backdoored samples are different from genuine samples. Therefore, they perform differently during both model training and unlearning. We believe this is a common phenomenon. In Figure 2, what we want to express is that since the backdoored and genuine samples are different, it is hard to used the disappearance of backdoored samples to evaluate the unlearning effectiveness of genuine samples. This is the cons of existing backdoor-based unlearning verification methods.


**Q2:** Should Figure 3b title text be changed to "Reconstructor training to recover the erased samples".

**Response to Q2:** 
We sincerely thank your suggestion. We highlighted the title as "Reconstructor training to recover the erased samples." 



## Rebuttal to Reviewer oDpE  

We greatly thank Reviewer oDpE for acknowledging the novelty and the experimental validation of our paper. And we sincerely appreciate Reviewer oDpE for proposing these insightful comments and questions. Below, we provide our responses to the comments, denoted by [W] for weaknesses. 



**W1 and Q1:**
Despite the quality of the research, the paper diverges from the conference theme of Web. This mismatch may limit its appeal to conference participants. How does the research in this paper relate to the conference theme of Web?

**Response to W1 and Q1:** 
We sincerely appreciate the reviewer's comment and question. We believe our research is related to both the security and privacy research track and the theme of the Web conference. First, from the perspective of the security and privacy track, our paper solves the key privacy problem in machine unlearning, which is related to data privacy and the right to be forgotten. Second, from the perspective of the conference theme of Web, many web applications integrate machine learning (ML) models for recommendations or analytics, and machine unlearning becomes a critical capability if these ML model ingests data that later needs to be removed. 
In this situation, the audit of unlearning is also important for the Web. Moreover, we also noticed that there were around 4 papers that relate to machine unlearning or federated unlearning published at the Web Conference last year.

**W2:**
The work in this paper seems to be similar to that in [3], but this paper does not illustrate the difference.


**Response to W2:**
We greatly appreciated the reviewer's comment. Besides the discussion with unlearning verification methods (which is presented in Appendix A), we here supplemented the detailed discussion with [3] as follows, which we also supplemented in the Appendix in the revision.


In our first step to build the approximate unlearning shadow model, we propose the influence estimation method, which is inspired by [3]. [3] introduced a second-order influence function to effectively estimate the influence of samples.
It is well applied in existing approximate unlearning methods, which rely on calculating the Hessian matrix based on all the remaining datasets to calculate the influence of the erased samples.
Calculating second-order influence is effective in estimating the influence but is computationally expensive. 
Therefore, in our paper, we try to relax it by calculating the first-order influence estimation based only on the erased samples and several samples of the training data, which are easy to access by unlearning users as they have previously uploaded the data for model training. 
We find it is also effective and much more efficient than calculating the second-order influence, hence enabling the users to calculate it locally.

[3]. Basu, Samyadeep, Xuchen You, and Soheil Feizi. "On second-order group influence functions for black-box predictions." International Conference on Machine Learning. PMLR, 2020.


**W3:**
The source code seems to be incomplete, and main.py is irrelevant to this paper. Moreover, the source code seems to have been prepared for another conference “Experiments_for_usenix25”.


**Response to W3:**
We thank you for your feedback regarding the source code. We sincerely apologize for the oversight. We previously planned to catch up with the usenix25 deadline but have missed it.
We now update our latest code. The main introduction of our code, implementation, and main results are presented in the README.md file for your reference. 



**Q2:**
The motivation described seems inadequate. Backdoor-based approaches that only verifies that backdoor-based data has been forgotten, data that is relevant to the data the user wants to forget (line 271 to 278). Doesn't this indirectly prove that the data wanted to forget was forgotten?

**Response to Q2:**
We appreciate the reviewer's question. The backdoor-based can prove the unlearning of backdoored samples, but the key disadvantage is that the backdoor disappearance does not mean the unlearning of genuine samples, as backdoored and genuine samples are different datasets, and these two datasets perform differently during training and unlearning.
We discussed it in the Related Work Section from lines 227 to 259, and we also provided the experimental results in Figure 2.

To reduce the confusion, we also revised the introduction of lines 271 to 278 as follows.

```
Most existing backdoor-based unlearning verification methods tried to solve data removal verification but can only answer if the backdoored samples are unlearned. Since the backdoored and genuine samples are different datasets, the disappearance of backdoors is insufficient for trustworthy unlearning auditing for genuine samples. Moreover, to audit the unlearning, we should assess the unlearning effectiveness of the model, i.e., how much private information about the requested unlearning samples is removed from the model.
```

**Q3:**
The boundaries of trained model, unlearned model, reconstructor model are blurred in this paper, making it difficult to read, what model is reconstructed and is it related to unlearned model, or is it a new reconstruction?

**Response to Q3:**
We sincerely appreciate the reviewer's question. In this paper, we have three models: the trained model, the unlearned model, and the reconstructor. The trained model is denoted as $\theta_t$, which is the current model before unlearning. The unlearned model is denoted as $\theta_u$, which means the unlearning operation is conducted based on $\theta_t$. The reconstructor model is another model, denoted as $\texttt{AE}$, which is trained based on the simulated posterior difference, where the posterior difference is the output difference queried from $\theta_t$ and $\theta_u$. 
To reduce the confusion, we revised the paper and added the above description in Section 4.1 "Overview of the TAPE."

```
In this paper, we mainly have three models: the trained model, the unlearned model, and the reconstructor.
The trained model is denoted as $\theta_t$, which is the current model before unlearning. The unlearned model is denoted as $\theta_u$, which means the unlearning operation is conducted based on $\theta_t$. The reconstructor model is another model, denoted as $\texttt{AE}$, which is trained based on the simulated posterior difference, where the posterior difference is the output difference queried from $\theta_t$ and $\theta_u$.
```



## Additional Rebuttal

Comment: Thank you for your detailed answer, most of my concerns have been resolved, but I still have doubts about the relevance of the paper background. Indeed, this research can be applied to the Web, but it seems that this paper does not have any Web-related description. In other words, this paper's style of writing is designed to be submitted to security-related conferences, such as usenix25, which is also appearing in the source code.

Given that my rating is already a positive score indicating approval of the NT of this paper, I will not raise my score. However, the author should claim the Web-related background of this paper carefully, or I may consider decreasing my score.



We sincerely thank you for your response and are pleased to hear that our responses have addressed most concerns. 
We also greatly appreciate that you acknowledge the Technique and Novelty of our paper.

To solve the remaining concerns and increase the Web-related background, we revised our paper as follows.

Firstly, we revised the first sentence of our paper in the ABSTRACT as 
>With the increasing prevalence of Web-based platforms handling vast amounts of user data, machine unlearning has emerged as a crucial mechanism to uphold users' right to be forgotten, enabling individuals to request the removal of their specified data from trained models.

Secondly, in the first paragraph of Introduction, we add an example of unlearning in Web-related recommendation systems, after the sentence that introduce the unlearning concept.
>This right has sparked significant interest in the research community, giving rise to the concept of ``machine unlearning'' --- a field that explores methods for erasing the influence of user-specified samples from trained ML models. For example, in Web-based recommendation systems that collect huge amounts of sensitive user data, effective unlearning methods are essential for protecting user privacy [R1, R2].

Thirdly, we added a new subsection to supplement some discussion about Web-related unlearning studies the in Related Work section
>**Machine Unlearning in the Web-Related Studies.** Machine unlearning--the process of efficiently removing specific data influences from trained models--has been explored in diverse applications across Web-based systems, such as graph-based systems and personalized applications [R2, R3, R4, R5]. In graph-based systems, [R4] proposed an unlearning method to unlearn the graph classifiers with limited access to the original data, and [R6] introduced a general strategy leveraging influence functions to efficiently remove specific graph data while preserving model integrity. In personalized applications, [R3] introduced dynamic client selection with incentive mechanisms to enhance the federated unlearning efficiency, while [R5] extended federated unlearning to the heterogeneous knowledge graph, aiming to balance both privacy and model utility preservation. To achieve a better unlearning service, [R1] further explored the challenge of balancing privacy, utility, and efficiency and proposed a controllable unlearning framework to overcome this challenge.


[R1]. Liu, Zheyuan, et al. "Breaking the trilemma of privacy, utility, and efficiency via controllable machine unlearning." Proceedings of the ACM on Web Conference 2024.

[R2]. Chen, Chong, et al. "Recommendation unlearning." Proceedings of the ACM Web Conference 2022.

[R3]. Lin, Yijing, et al. "Incentive and Dynamic Client Selection for Federated Unlearning." Proceedings of the ACM on Web Conference 2024.

[R4]. Pan, Chao, Eli Chien, and Olgica Milenkovic. "Unlearning graph classifiers with limited data resources." Proceedings of the ACM Web Conference 2023.

[R5]. Zhu, Xiangrong, Guangyao Li, and Wei Hu. "Heterogeneous federated knowledge graph embedding learning and unlearning." Proceedings of the ACM web conference 2023.

[R6]. Wu, Jiancan, et al. "Gif: A general graph unlearning strategy via influence function." Proceedings of the ACM Web Conference 2023.


We thank you again for your insightful comments and suggestions and hope our diligent efforts can address your concerns.

Best Regards,

Authors




## Rebuttal to Reviewer oXvT  


We sincerely appreciate Reviewer oXvT for acknowledging the novelty of our paper and providing a detailed summary of our strengths. We also greatly thank Reviewer oXvT for proposing these insightful comments. Below, we provide our responses to the comments, denoted by [W] for weaknesses.

**W1:**
If no unlearning method is used, can the reconstructor reconstruct the data? The author should let people know that the reconstructor is in good performance before using it to test unlearning.

**Response to W1:**
We greatly appreciate the reviewer's comment. The reconstructor is trained based on the mimic posterior difference between the output of the trained model and the simulated shadow unlearning model. Therefore,  our reconstructor can perform well before using it to test the really unlearning. We illustrate some experimental results on MNIST that perform on the training minic posterior difference and really unlearning posterior difference as follows.

The **Table R1** of evaluation on the training mimic posterior difference and really unlearning posterior difference:

| On MNIST         |  ESS = 1|  20  | 40  | 60 | 80 |  
| --------         | --------    | -------- | -------- |  -------- |   -------- |  
| Rec. Similarity on minic       | 0.9743      | 0.9524   |  0.9403  |  0.9291   |  0.9231    |  
| Rec. Similarity on really      | 0.9650      | 0.9331   | 0.9228   |  0.9159   |  0.9033    |   
| Verifiability on minic       | 1.00     | 0.9972   |  0.9822  |  0.9880   |  0.9779    |  
| Verifiability on really      | 0.9943      | 0.9867  | 0.9583  |  0.9583   |  0.9490     |   
 
 
 

**W2:**
The author didn't show the direct connection between reconstruction, if the method cannot reconstruct the data, does it implies the model is unlearned from it?


**Response to W2:**
We sincerely appreciate the reviewer's insightful comment. The reconstructor model is used to recover the unlearned information from the posterior difference before and after unlearning. Theoretically, the posterior difference contains information about the erased data, which is also utilized to conduct privacy leakage and reconstruction attacks [2, 34]. If the reconstruction effect is comparably better, it means the unlearning posterior difference contains more information about the erased sample, which indicates a better unlearning effect of the unlearning operation.


[2]. Balle, Borja, Giovanni Cherubin, and Jamie Hayes. "Reconstructing training data with informed adversaries." 2022 IEEE Symposium on Security and Privacy (SP). IEEE, 2022.
[34]. Salem, Ahmed, et al. "{Updates-Leak}: Data set inference and reconstruction attacks in online learning." 29th USENIX security symposium (USENIX Security 20). 2020.


**W3:**
For generative models like Diffusion model, how to use this method?

**Response to W3:**
We appreciate the reviewer's insightful question. For auditing the unlearning of generative models like GAN or Diffusion model, we believe our method is also feasible. The only change is that the logic output of the classifier model and generative model is different. Therefore, we need to modify the input layer of the Reconstructor to enable it to be suitable for the generative models. Other steps are similar to the method introduced in the TAPE.




## Rebuttal to Reviewer VJZx  

We greatly thank Reviewer VJZx for acknowledging the presentation and technical quality of our paper. And we sincerely appreciate Reviewer VJZx for proposing these insightful comments. Below, we provide our responses to the comments, denoted by [W] for weaknesses. 


**W1:**
The shadow model construction relies on first-order influence estimation, which may introduce errors, particularly when the unlearned data’s impact on the model is highly nonlinear or complex. This approximation could result in inaccuracies in the shadow model, affecting audit precision. Could the authors provide evidence on more complex data?

**Response to W1:**
We greatly appreciate the reviewer's comment. Most of the experiments are conducted on the MNIST, CIFAR10 and CelebA. We also conducted experiments on a more complex dataset, STL-10, with a higher resolution of 96x96x3 pixels. Our method is also effective in auditing the unlearning of genuine samples on the complex dataset. We illustrate some results on STL-10 as follows.


The **Table R2** of Evaluation of Unlearning Audit for Genuine Samples on STL-10, ESS=2:

| On STL-10           | Original    | MIB      |   TAPE   | 
| --------             | --------    | -------- | -------- |  
| Running time (s)     | 781         | 809      |  74.90     |  
| Model Utility (Acc.) | 68.99%      | 67.26%   | 68.99%   |   
| Rec. Sim.            | -           | -        | 0.174    |  
| Unl. Verifiability  | 0.00%       | 0.00%    | 84.40%   |  


**W2:**
TAPE assumes that unlearning has a minimal impact on model parameters, making it suitable for cases requiring only limited parameter adjustments. However, if unlearning involves substantial parameter updates or retraining, the shadow model may not accurately capture these changes, limiting its usability. Could the authors provide analysis on the effects when unlearning a large number of samples?


**Response to W2:**
We sincerely appreciate the reviewer's comment and thank you for pointing out the limitations of our method. Our method achieves better effectiveness when the unlearning sample size is small. When more samples are involved in the unlearning process, the reconstruction and auditing effect will slightly decrease. This is also a problem that remained unsolved in multi-sample reconstruction attacking scenarios. We partially solve this problem through our two strategies: the customized unlearned data perturbation before unlearning and the unlearning influence-based division after unlearning. It enables us to achieve a comparable effective reconstruction and verification when the number of unlearning samples is large. We demonstrate unlearning at most 0.2% of training data in Figure 6, where unlearning 0.2% of training data is already large according to [4, 6] in practice. The results in Figure 6 demonstrate the auditing effectiveness of our method for unlearning multiple samples.



[4]. Bertram, Theo, et al. "Five years of the right to be forgotten." Proceedings of the 2019 ACM SIGSAC Conference on Computer and Communications Security. 2019.
[6]. Chen, Min, et al. "When machine unlearning jeopardizes privacy." Proceedings of the 2021 ACM SIGSAC conference on computer and communications security. 2021.


**W3:**
The paper includes limited method comparisons, primarily with backdoor-based verification methods like MIB, and lacks broader benchmarking with advanced unlearning verification techniques.


**Response to W3:**
We sincerely thank the reviewer's comment. We mainly compare our method with the backdoor-based verification methods because these methods are the mainstream verification methods from the user side. These methods are also much more oblivious compared to the membership inference methods. To reduce the concern, we additionally conduct experiments of the membership inference for unlearning verification, and the results are presented as follows. The result of membership inference does drop and indicates the unlearning effect, but it is not as effective and obvious as our method. And it cannot directly answer how much information is unlearned.


The **Table R3** of Additional Membership Inference (MI) Method for Unlearning Verification:

| On MNIST          | Original    | MIB      |   TAPE   |  MI accuracy before Unlearning   |  MI accuracy after Unlearning   | 
| --------             | --------    | -------- | -------- |  -------- |  -------- |  
| Rec. Sim.            | -           | -        | 0.174    |  -        | -   | 
| Unl. Verifiability  | 0.00%       | 0.00%    | 84.40%   |  63.86% (In training dataset)   |   57.87%  (In training dataset) |  


