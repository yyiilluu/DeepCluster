# Distributed Deep Learning doc
DDL is a platform that trains tensorflow models with GPUs provided by other people

## Installation
Install latest cli with pip
```
pip install ddlcli
```
you may also install a specific version:
```
pip install ddlcli==0.0.3
```

## Prepare your TF model

**Step 1:** Create a ```main.py``` file at root of your project  

```main.py``` is the entry point when the training task is started. Place it at the root of the project
```
/example_pkg
    /example_lib
    /main.py
```
```main.py``` is required to implement a main function  
for example:
```
from example_lib import train
def main(dataset_dir, model_output_dir)
    train(dataset_dir, model_output_dir)
```
where the ```train(dataset_dir, model_output_dir)``` invokes the training job that you submit  
```dateset_dir``` is the location where your model can access all the dateset  
```model_output_dir``` is the location where your model should output all the training results. Otherwise you will not be able to access the training results  

**Step 2:** Create a training config yaml  
The condig yaml will contains your login information and training specifications.  
Sample yaml file looks like the following:  
```
email: <your_email>
password: <your_password>
job_data:
  model_location: <your_path>/example_pkg
  dataset:
    dataset_location: <your_path>/dataset
  worker_required: 1
```
> dataset directory hierarchy will be maintained, so that ```dataset_dir``` is equivalent to ```<your_path>/dataset``` specified in the yaml to your training task

## Submit your training task  
 
**Step 1:** Register to ddl, If this is your first time  
```
ddlcli register
```

**Step 2:** Submit your training task
```
ddlcli submit --task_config=<path to your config yaml>
```
you should see something like below if it is successful
```
===========================================
Step 1: User login
===========================================
===========================================
Step 2: Submit task
===========================================
uploading file ...
...
Status: 200
job_uuid: 99047c5e-380f-4a58-86c0-788517acf3df
job_type: tensorflow
```


## Check task progress
```
ddlcli progress --job_uuid=<uuid>
```
**Once your task is completed**  
you can download model outputs with 
```
ddlcli download --job_uuid=<uuid> --dest=<path where you want model outputs downloaded to>
```