# LAB 02

## Load & Visualize MNIST DATA

MNIST is a simple computer vision dataset. It consists of a handwritten image, and it contains a label for each image that tells you what the number is. 

The downloaded data is divided into three parts: 60,000 training data (trainset) and 10,000 test data (testset). This division of data is very important. Because with test data, we can be sure that what we've learned is really generalized.

Each image in the data is 28x28 pixels. We can interpret this as a large array of numbers. We can expand this array and make it 28x28 = 784 vectors. It doesn't matter how you expand the array, as long as you process them consistently between the images. As a result of unfolding the data, image from train_image becomes a array of the form [28,28] to [784](flattened by Prob.4 code). 

At train_image [60000,28,28], the first dimension refers to the number of image and the second & third dimension refers to the size of each image. Every component in a tensor is a pixel intensity between 0 and 255 that identifies a particular pixel in a particular image.

TODO: Plot images from 0 to 9 with labels.

## Fully connected network without tensorflow

Building fully connected model without tensorflow is little bit difficult, so we will do simple backpropagation.

### Forward propagation
Calculate the output from the input training data and calculate the error in each ouput neuron. (It is called ‘forward’ propagation because information flows to input-> hidden-> output.) This is much easier than back propagation.

TODO: Fill the function affine_forward and relu_forward

### Back propagation

Backpropagation is a method of calculating gradients by applying a repetitive chain rule for the entire network. Let's look more specifically at the neural network perspective on why we are interested in this issue.

For example, the loss function can be the SVM Loss function, and the input values are training data $(x_i, y_i), i = 1... N$ and Weight, Bias $W, b$. Here, the learning data can be seen as a fixed value, and Weight is the value that is actually controlled for the neural network learning. Therefore, although the gradient calculation for the input value $x_i$ is easy, in practice, the gradient for the parameter value is generally calculated, and the parameter value can be used to update the gradient.

At the image, you can compute $σ_l$(the backpropagated loss function($L$)) with value $z_l$, $σ_{l+1}$ and weight $w$. Then you can use these $σ$ with gradient descent to update weight $w$.

TODO: Fill the function affine_forward and relu_forward

## Fully connected network with tensorflow

Pytorch supports many other layer types, loss functions, and optimizers - you will experiment with these next. Here's the official API documentation for these (if any of the parameters used above were unclear, this resource will also be helpful). 

* Layers, loss functions, activations : https://pytorch.org/docs/stable/nn.html
* Optimizers: https://pytorch.org/docs/stable/optim.html

TODO: Make test accuracy greater than 0.97 with your own model. You can change architectures, hyperparameters, loss functions, and optimizers. Also, you can use dropout or batchnorm.
