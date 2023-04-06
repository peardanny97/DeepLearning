import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file "example_data.csv"
# Finally we need to load variables data_x(first column), data_y(second column)

###################################################################################
#                                   YOUR CODE HERE                                #
###################################################################################

xy = np.loadtxt('example_data.csv',delimiter = ',', dtype = np.float32)

data_x = xy[:,0]
data_y = xy[:,1]




###################################################################################
#                                  END OF YOUR CODE                               #
###################################################################################

# Make a scatter plot of training data to visualize the data

###################################################################################
#                                   YOUR CODE HERE                                #
###################################################################################
plt.scatter(data_x,data_y)

plt.show()

###################################################################################
#                                  END OF YOUR CODE                               #
###################################################################################

# Define Cost function J
def cost(x, y, theta):
    # Compute cost for linear regression
    # J is the cost using theta as the parameter for linear regression to fit the data points in X and y

    ###################################################################################
    #                                   YOUR CODE HERE                                #
    ###################################################################################
    m = len(x)
    h = np.dot(x, theta[0]) + theta[1]
    error = y - h
    J = np.sum(error ** 2) / 2

    ###################################################################################
    #                                  END OF YOUR CODE                               #
    ###################################################################################

    return J


# Implement Gradient descent algorithm
def gradient_descent(x, y, theta, alpha, num_iters):
    # gradient_descent performs gradient descent to learn theta
    # gradient_descent updates theta by taking num_iters gradient steps with learning rate alpha

    for iter in range(num_iters):
        ###################################################################################
        #                                   YOUR CODE HERE                                #
        ###################################################################################

        x_trans = x.transpose()
        m = len(x)
        x_0 = np.ones((1,m))

        h = np.dot(x, theta[0]) + theta[1]
        error = y - h
        g = np.dot(x_trans, error)
        g2 = np.dot(x_0,error)

        theta[0] = theta[0] + alpha * g
        theta[1] = theta[1] + alpha * g2

    ################################################w###################################
    #                                  END OF YOUR CODE                               #
    ###################################################################################

    # Save the cost J in every iteration
    J = cost(x, y, theta)

    if (iter + 1) % 100 == 0:
        print('cost at %d iterations : %f' % (iter + 1, J))


    return theta

# initialize values
theta = np.zeros(2)
num_iters = 2000
alpha = 0.0001

# compute initial cost
init_J = cost(data_x, data_y, theta)
print('initial cost : %f' %init_J)

# excute gradient descent
theta = gradient_descent(data_x, data_y, theta, alpha, num_iters)

# compute new cost
new_J = cost(data_x, data_y, theta)
print('updated theta : ', theta)
print('updated cost : %f' %new_J)

# Plot the scatter plot and linear regression fit

###################################################################################
#                                   YOUR CODE HERE                                #
###################################################################################

x_plot = np.arange(5,22.5)
y_plot = theta[0]*x_plot + theta[1]
plt.plot(x_plot,y_plot)
plt.scatter(data_x,data_y)
plt.show()

###################################################################################
#                                  END OF YOUR CODE                               #
###################################################################################