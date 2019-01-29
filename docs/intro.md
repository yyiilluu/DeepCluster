# Distributed GPU cluster
## Easy to use and Cheap GPU cluster for deep learning powered by distributed GPUs

It is a fully managed platform allows students and researchers to simply submit their training task to our GPU cluster with only very minimal changes  
Our GPU cluster is powered by people who would like to share their spare GPU with others  
Designed specifically for students and researchers who wants to learn deep learning but do not have convenient access to powerful GPU or GPU cluster.

![submit task demo](../assets/submit_task_demo.gif)

## Use our known datasets or upload your own dataset for training
There are a large number of open source dataset can be used for training. We provide a list popular dataset that you can choose from to train your model.  
You can also upload your own dataset and consume it in similar fashion. With one caveat, [We secure your code but use nonsensitive dataset](#We-secure-your-code-but-use-nonsensitive-dataset)  

![add dataset demo](../assets/add_dataset_demo.gif)

## We secure your code but use nonsensitive dataset
Each training job is preprocessed so that GPU host cannot steal our code, however, data has to be unencrypted at the time of computation due to performance considerations. So, please use public or nonsensitive dataset since GPU host could be curious about what data you are using
