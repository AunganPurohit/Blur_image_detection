# Blur_image_detection
This code is used to detect the blur images using Laplacian Detector. 

#Laplacian Operator
It uses the Laplacian matrix or kernel and performs convolution with the given image (only with a single channel of the image). Then it 
evaluates the variance(sqaure of the Standard deviation).

#Evaluation
If the variance comes out to be a value more than the threshold set by us, then the image will be considered "Not BLurry". If the value 
is lower than the desired threshold then the image will be considered "Blurry".

#Main_Drawback
The threshold needs to be manually set by the user for the particular use. This might lead to less accuracy than the desired level. To
overcome this, FFT (Fast Fourier Transform) can be used. 
