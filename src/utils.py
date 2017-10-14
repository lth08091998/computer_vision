import numpy as np

def conv2d(image, kernel, padding='same'):
	image_height = image.shape[0]
	image_width = image.shape[1]
	kernel_height = kernel.shape[0]
	kernel_width = kernel.shape[1]
	offset_height = kernel_height // 2
	offset_width = kernel_width // 2
	padded_image = np.zeros(((image_height + offset_height * 2), (image_width + offset_width * 2)))
	output = np.zeros(((image_height + offset_height * 2), (image_width + offset_width * 2)))
	
	for i in range(image_height):
		for j in range(image_width):
			padded_image[i + offset_height][j + offset_width] = image[i][j]

	for x in range(image_height):
		for y in range(image_width):
			i = x + offset_height
			j = y + offset_width
			output[i][j] = sum(sum(padded_image[x : x + kernel_height][y : y + kernel_width] * kernel))

	return output[offset_height : offset_height + image_height][offset_width : offset_width + image_width]