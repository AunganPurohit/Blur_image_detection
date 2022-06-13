# Blur_image_detection
This code is used to detect the blur images using Laplacian Detector. This code is not for just an image but to run over the whole dataset.

#Laplacian Operator:
It uses the Laplacian matrix or kernel and performs convolution with the given image (only with a single channel of the image). Then it 
evaluates the variance(sqaure of the Standard deviation).

#Evaluation:
For the evaluation, the value can be set manually or the threshold method can be used to determine the results.


#Main_Drawback:
The threshold needs to be manually set by the user for the particular use. This might lead to less accuracy than the desired level. To
overcome this, FFT (Fast Fourier Transform) can be used. 
