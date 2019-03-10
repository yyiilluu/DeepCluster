# How to construct proper config.yaml

### job_type:
valid job types are:
job_type      |
------------- |
tensorflow    |
pytorch       |

### dataset_name and data_path:
You may want to use any pre-cached dataset by specifying ```dataset_name```, or upload your own dataset by adding local path to ```dataset_path```.
> currently you may add at most one ```dataset_path```

valid dataset names are :
dataset_name    |
--------------- |
cifar10         |
squad           |

### worker_required: 
This indicates the number of GPU worker used to train your code. It is only beneficial if your code support distributed training, such as tensorflow estimator or manually assign devices in your code. Otherwise, there will be just a number of identical results.

