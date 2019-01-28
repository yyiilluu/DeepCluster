# ddlcli doc
ddlcli is a command line interface to train deep learning model using GPU cluster.

## Installation
Install latest cli with pip
```
pip install ddlcli
```
you may also install a specific version:
```
pip install ddlcli==0.0.5
```

## Prepare your workspace and code

To submit a training job, the easitest way is building from the sample git template repository. ddlcli assumes you are running the commnad at the root of a git repository.

The template repo looks like the following
```
/DDLTemplate
    /main.py
    /requirements.txt
    /config.yaml
    /README.md
    /.gitignore
```
> You may rename the repo but make sure you have do **NOT** rename/move ```main.py```

### Step 1: Choose datasets and define configs
```config.yaml``` looks like the following. You could choose existing dataset by providing ```dataset_name``` or input the local path to your dataset under ```dataset_path```.
```
dataset:
  dataset_name:
  dataset_path: eg. ~/dataset/my_data.tfrecords
```

You can also provide other configs that are specific to your model in there and read this ```config.yaml``` in the main function of ```main.py``` at ```"./configs.yaml"```

### Step 2: List python packages that you may need in requirements.txt
In the case where model requires other python packages from Pypi, you could list all the depended python packages under ```requirements.txt```

### Step 3: Prepare main.py and invoke training
```main.py``` is required to implement a main function that takes two parameters as input. It is the entry point of your training code and where you should invoke your functions
for example:  

```
from example_lib import your_train_fn
def main(dataset_dir, output_dir)
    your_train_fn(dataset_dir, model_output_dir)
```  

where the ```your_train_fn(dataset_dir, output_dir)``` invokes the training job that you submit  

```dateset_dir``` parameter is the location where your model can access all the dateset  
 In your code, please retrieve your dataset using something like ```os.path.join(dateset_dir, 'my_data.tfrecords')``` 

```output_dir``` parameter is the location where your model should output all the training results or plots to. Otherwise, you will not be able to download the outputs.  

Suppose you have additional configs in ```configs.yaml```, you could access them with something like 
```
from example_lib import your_train_fn
def main(dataset_dir, output_dir)
    import yaml
    with open('./config.yaml', 'r') as f:
        configs = yaml.load(f)

    your_train_fn(dataset_dir, model_output_dir, configs)
```  

> You don't need to invoke the main function in your code. Assume the main function will be invoked after you submit you task

That is it! You have completed all the required steps.

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
Successfully logged in
```
> Once you are logged in, you are able to interact with your account using ddlcli for 10 mins  
After 10 mins, you might be prompted for login again when running other ddlcli commands

**Step 3:** Submit your training task  
At the root of your repository, where you have your main.py file
```
ddlcli submit
```
you should see something like below if it is successful
```
===========================================
Submit task
===========================================
uploading file ...
...
job_uuid: 99047c5e-380f-4a58-86c0-788517acf3df
job_type: tensorflow
```
> Please save your job_uuid somewhere, you will need to use it for tracking progress and download logs/artifacts

If you have uncommitted change in your repo and you want to include everything in your current working directory without a new commit, please use
```
ddlcli submit -d
or 
ddlcli submit --dirty
```

congratulations! Now you have successfully submit a training task with DDL.

## Check task progress and download artifact
You can check the progress of the training using job_uuid you got when submit the training task
```
ddlcli progress --job_uuid=<uuid>
```
You will see something like this if it is successful
```
===========================================
Check Job Progress
===========================================
job_uuid: 99047c5e-380f-4a58-86c0-788517acf3df
job_state: finished
tensorboard_location: https://192.46.115.25:6006
```

To see console logs, you could download it with
```
ddlcli log --job_uuid=<uuid> --dest=<local path console logs will be downloaded to>
```

You should see something like below
```
===========================================
Query for logs
===========================================
No log is found... ## if there is no log yet
Download log files: ## if there is any console log
...
```
Once your task is completed, you can download everything output to ```output_dir``` in your code, such as model artifacts or plots using
```
ddlcli download --job_uuid=<uuid> --dest=<local path where you want model outputs downloaded to>
```

<!-- ![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif) -->