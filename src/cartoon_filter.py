import cv2
import numpy as np
from utils import *

class CartoonFilter(object):
	"""Cartoon filter for image"""
	def __init__(self):

	def catoon_color(img, bitmap, edgemap):
		
		# Actual full step for cartoon effect:
		
		# 1: Apply a bilateral filter to reduce the color palette of the image.
		# 2: Convert the original color image to grayscale.
		# 3: Apply a median blur to reduce image noise in the grayscale image.
		# 4: Create an edge mask from the grayscale image using adaptive thresholding.
		# 5: Combine the color image from step 1 with the edge mask from step 4.
		
		# 2,3,4 should already be done to do edge detection. 1,5 is in here. just pass the edgemap + blurred colored image here
		
		height = img.shape[0]
		width = img.shape[1]
		
		for i in range(1, height):
			for j in range(1, width):
				if edgemap[i,j]:		# cond which edge to accept to be done later 
					img[i,j] = [0,0,0]
				elif bitmap[i][j] == 1:
					img[i,j] = [img[i,j,0]//10*10,img[i,j,1]//10*10,img[i,j,2]//10*10]
		return img

	def catoon_color(img, edgemap):
		
		height = img.shape[0]
		width = img.shape[1]
		
		for i in range(1, height):
			for j in range(1, width):
				if edgemap[i,j]:		# cond which edge to accept to be done later 
					img[i,j] = [0,0,0]
				else:
					img[i,j] = [img[i,j,0]//10*10,img[i,j,1]//10*10,img[i,j,2]//10*10]
		return img