import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    # Convert image to grayscale if it's not already
    if len(img.shape) == 3:
        imArray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        imArray = img

    # Convert to float and normalize
    imArray = np.float32(imArray)
    imArray /= 255.0

    # Compute wavelet coefficients
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    # Process coefficients - thresholding high frequency components
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0

    # Reconstruct the image
    imArray_H = pywt.waverec2(coeffs_H, mode)

    # Clip values to be in the range [0, 255] and convert back to uint8
    imArray_H = np.clip(imArray_H * 255.0, 0, 255).astype(np.uint8)

    return imArray_H
