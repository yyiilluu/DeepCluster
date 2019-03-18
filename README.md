# DeepCluster.io

## Installation
---------------
Install latest cli with pip
```
pip install dccli
```
<br/>

## Qucik start with mnist example
---------------
under ```/examples```, there are a couple examples that you can try, one of them is tensorflow mnist

### Submit mnist with tensorflow example
Navigate to /examples/tensorflow_example/mnist
```
# Register with dccli
dccli register

# submit mnist training example
# make sure you run this command under /examples/tensorflow_example/mnist
dccli submit -c
```

### Check out log and progress
Check out progress 
```
dccli progress
```

Check out console log
```
dccli stream
```

## Get more details from full instruction [here](./docs/index.md)
