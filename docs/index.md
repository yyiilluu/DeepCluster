# DeepCluster.io
dccli is a command line interface to train deep learning model using GPU cluster.  
[Read more about the platform](./intro.md)

## Installation
---------------
Install latest cli with pip
```
pip install dccli
```
> Warning: dccli<=0.0.11 will no longer work due to updates that are not backward compatible
<br/>

## Prepare your workspace and code
---------------
To use DeepCluster, your project is required to be a git repository. The easitest way is to start with the [template git repository](https://github.com/githublu/DeepClusterTemplate). 


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
```config.yaml``` looks like the following. You can choose our known dataset by providing ```dataset_name```,   deep learning framework type with ```container_name```, number of worker you want to use with ```worker_required```, and the entry command with ```command```.  
There are two environment variables. $DATASET is the path to dataset and $OUTPUT is the path where you can put output for download.    
You can find more detailed information about each field [here](./config.md)
```
# speficy your container name, such as deepcluster/tensorflow:1.12-python3.6 or deepcluster/pytorch:1.0-python3.7
container_image:

# provide known dataset name or local datasets
dataset_name: 
dataset_path:

# number of GPU used to train, default it 1
worker_required: 1

# command to run
# use the environment variable $DATASET to access dataset
# and write output to $OUTPUT
command: 

# other custom configs
```

You can also provide other configs that are specific to your model here and access ```config.yaml``` in the main function of ```main.py``` at ```"./configs.yaml"```

### Step 2: List python packages you need in ```requirements.txt```
If model requires other python packages from Pypi, you can list them in ```requirements.txt```  

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

### Step 2: Invoke your code inside the main function from main.py
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

### Step 3 Download and locate dataset
To test locally, download or locate the dataset on your computer. For this example, suppose you download the dataset to ```/MyDataset/dataset.json```  

### Step 4: Test locally by running ```main.py```
Before submit to DeepCluster, it is strongly recommended to run your code locally:  

```
python main.py --dataset_dir /MyDataset --output_dir /MyOutput
```

<br />
That is it! You have completed all the required preparation steps.

 <br />  

## Submit your training job  
---------------

### Step 1: Register to DeepCluster, If this is your first time  
```
dccli register
```
you will be asked for email and password to register for the service:  

```
===========================================
         Register with DeepCluster
===========================================
Please enter your email address: <your email>
Password must be 8 - 20 characters and can contain alphanumeric and @#$%^&+=
Please enter your password: <your password>
Please re-enter your password: <your password>
Registered successfully
Login successfully
```

Once you successfully registered with DeepCluster, you are already logged in. Skip to *Step 3: Submit your training job*  
<br>
### Step 2: Login to DeepCluster
If your log in is expired, log in with the following command

```
dccli login
```
you will be asked for email and password to login to the service:  

```
===========================================
           Login to DeepCluster
===========================================
Please enter your email: <your email>
Please enter your password: <your password>
Login successfully
```

### Step 3: Submit your training job  
dccli will package and submit the entire git repository by default. Use ```-c``` flag to submit current directory instead.  

```
dccli submit
```
you should see something like below if it is successful
```
===========================================
                Submit Job
===========================================
Code package includes uncommitted changes
zip source code...
Upload code...
Submit job successfully
 >  job type: tensorflow
 >  job uuid: 7040d88f-d02f-4529-84e2-d1991b90afc0
```
> job uuid is the identifier to track training progress, stream log and download artifacts

congratulations! Now you have successfully submit a training job to DeepCluster.

## Manage training jobs
You can check the progress using:
```
dccli progress
```
Optionally, you can provide ```--job_uuid <job uuid>``` to comnand line if you have more than one job:

```
===========================================
            Check Job Progress
===========================================
Job 7040d88f-d02f-4529-84e2-d1991b90afc0
 >  job type:  tensorflow
 >  job state: waiting for worker to join
 >  duration:  00:00:58
 >  job local history:
        [2019-03-10 12:42:13] pending upload
        [2019-03-10 12:42:19] job data uploaded
        [2019-03-10 12:42:20] job is ready
```

```job state``` indicate the current status of the job  
```job local history``` captures the events from the earliest to latest 

To stream console logs:
```
dccli stream
```

output will be something like

```
===========================================
Query for logs
===========================================
first line of log  ## if there is any console log of your code
second line of log
```

Once your job is completed, you can download code outputs, such as model artifacts or plots, to ```output_dir```
```
dccli download --dest=<local path where you want model outputs downloaded to>
```
output will look like below

```
===========================================
Download Job Output
===========================================
Output downloaded to: <local path where you want model outputs downloaded to>
```

## Demo here
[![Video demo](http://img.youtube.com/vi/M5DD6QmcdIM/0.jpg)](http://www.youtube.com/watch?v=M5DD6QmcdIM&feature=youtu.be)