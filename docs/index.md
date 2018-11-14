# DDL doc
DDL is a platform that trains tensorflow models with GPUs provided by other people

## Installation
Install latest cli with pip
```
pip install ddlcli
```
you may also install a specific version:
```
pip install ddlcli==0.0.5
```

## Prepare your TF model

To submit a training job, you need to follow a general project structure.

[Required] ```main.py``` is the entry point when the training task is started. Place it at the root of the project  
[Optional] ```requirements.txt``` contains all the python package that your code depends on  
[Optional] ```config.yaml``` contains all the configrations that you can read from  
```
/example_project
    /example_objects
        /example.py
    /main.py
    /requirements.txt
    /config.yaml

/dataset
    /my_data.tfrecord
```
> PYTHON_PATH will be set at ./example_project, so please make sure it is the same when test locally  
Also relative location inside /example_project will be same when running the job

```main.py``` is required to implement a main function that takes two parameters as input  
for example:  

```
from example_lib import train
def main(dataset_dir, model_output_dir)
    your_train_fn(dataset_dir, model_output_dir)
```  

where the ```your_train_fn(dataset_dir, model_output_dir)``` invokes the training job that you submit  

```dateset_dir``` parameter is the location where your model can access all the dateset  
 In your code, please retrieve your dataset using something like ```os.path.join(dateset_dir, 'my_data.tfrecord')``` 

```model_output_dir``` parameter is the location where your model should output all the training results. Otherwise, you will not be able to download the training outputs.  

> Implement the main function is sufficient. Don't need to invoke it in your code

## Submit your training task  
**Before you start**  
1. Make sure your project is within a git repository.
2. Navigate to your project, such as ```cd ./example_project``` and then start ddlcli

**Step 1:** Register to ddl, If this is your first time  
```
ddlcli register
```
you will be asked for email and password to register for the service  
something like below
```
Please enter your email address: <your_email_address>
Please enter your password: <password>
Please re-enter your password: <password>
Status: 201
Successfully registered
```

**Step 2:** Login to ddl
```
ddlcli login
```
you will be asked for email and password to register for the service  
something like below
```
Please enter your email address: <your_email_address>
Please enter your password: <password>
Status: 200
Successfully logged in
```
> Once you are logged in, you are able to interact with your account using ddlcli for 10 mins  
After 10 mins, you might be prompted for login again when running other ddlcli commands

**Step 3:** Create a training task.yaml  
after register successfully, you can create a ```task.yaml``` that contains your login information and training specifications.  
Sample yaml file looks like the following:  
```
job_data:
  dataset:
    dataset_location: <your_path>/dataset/
  worker_required: 1
```
> dataset directory hierarchy will be maintained, so that ```dataset_dir``` parameter in the main function of ```main.py``` is equivalent to ```<your_path>/dataset/``` specified in the yaml to your training task  

**Step 4:** Submit your training task  
Once you have your model prepared and completed registeration, navigate to your project directory, such as ```./example_project``` and run the following command. ddlcli will package current direcories and their sub-directorys up to the latest commit.  
Make sure you run this command at where you put ```main.py```
> You will not be able to submit a job if you have any uncommit change in the working diretory  
ddlcli will not package any parent directory from the location you run the command
```
ddlcli submit --task_config=<path_to_your_task_yaml>
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

congratulations! Now you have successfully submit a training task with DDL, and just wait for the artifact to be produced

## Check task progress and download artifact

```
ddlcli progress --job_uuid=<uuid> --task_config=<path to your task yaml>
```
**Once your task is completed**  
you can download model outputs with 
```
ddlcli download --job_uuid=<uuid> --dest=<local path where you want model outputs downloaded to> --task_config=<path_to_your_task_yaml>
```
