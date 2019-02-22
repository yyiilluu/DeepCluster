# DeepCluster.io
dccli is a command line interface to train deep learning model using GPU cluster.  
[Read more about the platform](./intro.md)

## Installation
---------------
Install latest cli with pip
```
pip install dccli
```
you may also install a specific version:
```
pip install dccli==0.0.3
```

<br/>

## Prepare your workspace and code
---------------
To use DeepCluster, your project is required to be a git repository. The easitest way is to start with the [template git repository](https://github.com/githublu/DeepClusterTemplate). dccli needs to run at the root of a git repo.  


 Template repo has the following structure:
```
/DeepClusterTemplate
    /main.py
    /requirements.txt
    /config.yaml
    /README.md
    /.gitignore
```
> You may rename the repo but make sure you **DO NOT** rename/move ```main.py```

### Step 1: Choose datasets and define configs using ```config.yaml```
```config.yaml``` looks like the following. You could choose existing dataset by providing ```dataset_name```.
```
dataset:
  dataset_name: cifar10
```

You can also provide other configs that are specific to your model here and access ```config.yaml``` in the main function of ```main.py``` at ```"./configs.yaml"```

### Step 2: List python packages you need in ```requirements.txt```
If model requires other python packages from Pypi, you could list them in ```requirements.txt```  

<br/>

## Develop with DeepCluster and test locally
---------------
### Suppose your project looks like the following
You may start with the [template git repository](https://github.com/githublu/DeepClusterTemplate)
```
/MyDataset
    /dataset.json

/MyProject
    /my_model.py
    /main.py
    /requirements.txt
    /config.yaml
    /README.md
    /.gitignore
```


### Step 1: Install packages in the requirements.txt
> You may want to start with a virtualenv by following [this](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)   

Navigate to the root of your project
```
pip install -r requirements.txt
```

### Step 2: Download your dataset
To test locally, locate the dataset on your computer. For this example, suppose you download the dataset to ```/MyDataset/dataset.json```

### Step 3: Invoke your code inside the main function from main.py
The template repo includes a ```main.py``` which contains a main function which looks like:  
```
# import your packages

# do not rename the functions
def main(dataset_dir, output_dir):
    config_path = "./config.yaml"
    
    # invoke your training function
```  

Modify the main function to invoke your training code.  
For example:
```
# import your packages
from my_model import my_train_fn

# do not rename the functions
def main(dataset_dir, output_dir):
    config_path = "./config.yaml"
    
    # invoke your training function
    my_train_fn(dataset_dir, output_dir, config_path)
```  

### Step 4: Run ``main.py``
```
python main.py --dataset_dir /MyDataset --output_dir /MyOutput
```
> ```--dataset_dir``` expects the directory path where dataset resides, instead of the path to dataset itself  

That is it! You have completed all the required steps.

 <br />  

## Submit your training job  
---------------
**Before you start**  
1. Make sure your project is within a git repository.
2. Navigate to the root your project, such as ```cd ./example_project``` and then start dccli

**Step 1:** Register to DeepCluster, If this is your first time  
```
dccli register
```
you will be asked for email and password to register for the service  
something like below
```
Please enter your email address: <your_email_address>
Please enter your password: <password>
Please re-enter your password: <password>
Successfully registered
```

**Step 2:** Login to DeepCluster
```
dccli login
```
you will be asked for email and password to register for the service  
something like below
```
Please enter your email address: <your_email_address>
Please enter your password: <password>
Successfully logged in
```

**Step 3:** Submit your training job  
At the root of your repository, where you have your main.py file
```
dccli submit
```
you should see something like below if it is successful
```
===========================================
Submit Job
===========================================
uploading file ...
...
job_uuid: 99047c5e-380f-4a58-86c0-788517acf3df
job_type: pytorch
```
> Please save your job_uuid somewhere, you will need to use it for tracking progress and download logs/artifacts

congratulations! Now you have successfully submit a training job with DeepCluster.

## Check job progress and download artifact
You can check the progress of the training using job_uuid you got when submit the training job
```
dccli progress --job_uuid=<uuid>
```
You will see something like this if it is successful
```
===========================================
Check Job Progress
===========================================
job_uuid: 99047c5e-380f-4a58-86c0-788517acf3df
job_state: finished
```

To stream console logs, you can use the stream function 
```
dccli stream --job_uuid=<uuid>
```

output will be something like

```
===========================================
Query for logs
===========================================
No log is found... ## if there is no log yet
first line of log  ## if there is any log, it will be output to your console directly
second line of log
```

Once your job is completed, you can download everything output to ```output_dir``` in your code, such as model artifacts or plots using
```
dccli download --job_uuid=<uuid> --dest=<local path where you want model outputs downloaded to>
```

## Demo here
[![Video demo](http://img.youtube.com/vi/M5DD6QmcdIM/0.jpg)](http://www.youtube.com/watch?v=M5DD6QmcdIM&feature=youtu.be)