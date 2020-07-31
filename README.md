# Artificial-Intelligence-for-Diabetic-Retionopathy
You-Tube link of my Project:- https://youtu.be/QdtmTSDxQZM

Methodology:- Here we take a 256 x 256 input image and multiply it with a different feature detector with a stride of 1 and also with rectilinear activation function to get the best feature from the input image .Here we take  3 x 3 feature detector and multiply with huge matrix of 256 x 256 input image to reduce the size of the matrix of the image. After that we apply Max pooling, so we take a box of two by two pixels and place it in the top left hand corner and we find the maximum value in that box and then we reduced only that value. Then we move the box to the right with a stride of two. Here  we do Max pooling to reduce the size of the 32 different feature maps and as a result we get 32 pooled feature map. To get best accuracy in our train and test set we have added 3 more convolution layer - First one with 3 x 3 matrix of 32 feature detector. Second one is with 3 x 3 matrix of 64 feature detector and third one is 3 x 3 matrix of 128 feature detector and I have added max pooling with each of these convolution layer. Now we take each and every pooled feature map and flatten it into a column so basically you just take the number row by row from pooled feature map and put them into one long column to get a one huge vector of inputs for an artificial neural network .

![2019-11-21 (49)](https://user-images.githubusercontent.com/44479743/89050632-a8cc9880-d370-11ea-8238-561469c23155.png)

Now we make two fully connected layer with output_dim(Dimension of dense embedding ) of 128 and also with rectilinear activation function. we use categorical cross entropy to calculate the loss so the error is calculated in the output layer with softmax activation function and with adam optimizer is back propagated through the network again and again to adjust the network and to optimize the performance. After that we train the dataset of Mild, Moderate, Severe, Prolifrative DR & Normal with a target size of 256 x 256 batch size of 10 and also the test set of Mild, Moderate, Severe, Prolifrative DR & Normal with a target size of 256 x 256 batch size of 2 and with 50 epoch 

![Screenshot (87)](https://user-images.githubusercontent.com/44479743/89050884-0365f480-d371-11ea-94f4-75cd9ead3b96.png)

and we get 98% accuracy on train set and 93% accuracy on  test set. Some Screenshot of my SOFTWARE.. 
 
![Screenshot (139)](https://user-images.githubusercontent.com/44479743/89053304-a2d8b680-d374-11ea-873b-e9b95869cb26.png)


