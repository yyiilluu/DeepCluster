# cifar_nn.py
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import random
import time

# To fully utilize the service, train network with GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Net(nn.Module):
  def __init__(self):
    super(Net, self).__init__()
    self.conv1 = nn.Conv2d(3, 6, 5)
    self.pool = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(6, 16, 5)
    self.fc1 = nn.Linear(16 * 5 * 5, 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 10)

  def forward(self, x):
    x = self.pool(F.relu(self.conv1(x)))
    x = self.pool(F.relu(self.conv2(x)))
    x = x.view(-1, 16 * 5 * 5)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.fc3(x)
    return x

def train_model(dataset_dir, output_dir, config):
  np.random.seed(1)
  random.seed(2)
  torch.manual_seed(3)

  transform = transforms.Compose([transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

  # For known dataset, if you are using pytorch dataset, put dataset_dir
  # to the root folder, where pytorch usually download dataset to
  #
  trainset = torchvision.datasets.CIFAR10(root=dataset_dir, train=True,
    download=True, transform=transform)
  trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
    shuffle=True, num_workers=2)

  testset = torchvision.datasets.CIFAR10(root=dataset_dir,
    train=False, download=True, transform=transform)
  testloader = torch.utils.data.DataLoader(testset, batch_size=4,
    shuffle=False, num_workers=2)

  classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog',
    'horse', 'ship', 'truck')

  # get some random training images
  dataiter = iter(trainloader)
  images, labels = dataiter.next()

  # print labels
  print(' '.join('%5s' % classes[labels[j]] for j in range(4)))

  net = Net()
  net.to(device)

  criterion = nn.CrossEntropyLoss()
  optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

  start_time = time.time()
  for epoch in range(3):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
      # get the inputs
      inputs, labels = data
      inputs, labels = inputs.to(device), labels.to(device)

      # zero the parameter gradients
      optimizer.zero_grad()

      # forward + backward + optimize
      outputs = net(inputs)
      loss = criterion(outputs, labels)
      loss.backward()
      optimizer.step()

      # print statistics
      running_loss += loss.item()

      if i % 5000 == 4999:
        print('[%d, %5d] loss: %.3f' %(epoch + 1, i + 1,\
 running_loss / 2000))
        running_loss = 0.0
        print(f"time elapsed: {time.time() - start_time}")

  print('Finished Training')

  _, predicted = torch.max(outputs, 1)

  print('Predicted: ', ' '.join('%5s' % classes[predicted[j]] \
for j in range(4)))

  correct = 0
  total = 0
  with torch.no_grad():
    for data in testloader:
      images, labels = data
      outputs = net(images)
      _, predicted = torch.max(outputs.data, 1)
      total += labels.size(0)
      correct += (predicted == labels).sum().item()

  print('Accuracy of the network on the 10000 test images: \
%d %%' % (100 * correct / total))

  class_correct = list(0. for i in range(10))
  class_total = list(0. for i in range(10))
  with torch.no_grad():
    for data in testloader:
      images, labels = data
      outputs = net(images)
      _, predicted = torch.max(outputs, 1)
      c = (predicted == labels).squeeze()
      for i in range(4):
        label = labels[i]
        class_correct[label] += c[i].item()
        class_total[label] += 1

  for i in range(10):
    print('Accuracy of %5s : %2d %%' % (classes[i], \
      100 * class_correct[i] / class_total[i]))
