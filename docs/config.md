# How to construct proper config.yaml

## container_name:
valid container name are:

container_name | 
------------ | 
deepcluster/tensorflow:1.12-python3.6 |
deepcluster/pytorch:1.0-python3.7 | 

## dataset_name and data_path:
You may want to use any pre-cached dataset by specifying ```dataset_name```, or upload your own dataset by adding local path to ```dataset_path```.  
If ```dataset_name``` is provided, ```dataset_path``` will be ignored
> currently you may add at most one ```dataset_path```

valid dataset names are :  

dataset_name   | 
---------------|
cifar10        |

## worker_required: 
This indicates the number of GPU worker will be used for training. It is only beneficial if your code support distributed training, such as tensorflow estimator or manually assign devices in your code. Otherwise, there will be just a number of identical results.
> currently, only 1 worker is supported

## command:
command is a single command that you would like to run in shell. There are two environment variables. ```$DATASET``` is the path to dataset and ```$OUTPUT``` is the path where you can put output for download.  
For example: 
```
command: python main.py --dataset_path $DATASET --output_path $OUTPUT
```