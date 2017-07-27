from PIL import Image
from random import *
# from colormath.color_objects import sRGBColor, LabColor
# from colormath.color_conversions import convert_color
#  3 from colormath.color_diff import delta_e_cie2000

#  color1_rgb = sRGBColor(oldPixel[0]/255.0, oldPixel[1]/255.0, oldPixel[2]/255.0)
# 			color2_rgb = sRGBColor(pixel[0]/255.0, pixel[1]/255.0, pixel[2]/255.0)
# 			color1_lab = convert_color(color1_rgb, LabColor);
# 			color2_lab = convert_color(color2_rgb, LabColor);
# 			delta_e = delta_e_cie1976(color1_lab, color2_lab);



# def findHSL(color):
# 		r = color[0]/255.0
# 		g = color[1]/255.0
# 		b = color[2]/255.0
# 		h = 0

# 		maxValue = max(r, g, b)
# 		minValue = min(r, g, b)

# 		bottom = ((maxValue - minValue))
# 		if(bottom <= 0):
# 			return 0
# 		if (r > g and r > b):
# 			h = (g - b)/bottom
# 		elif (g > r and g > b):
# 			h = (2.0 + (b - r))/bottom
# 		else:
# 			h = (4.0 + (r - g))/bottom

		
# 		h *= 60
# 		if (h < 0):
# 			h += 360
# 		return h

# find how similar
		# hue1 = findHSL(oldPixel)
		# hue2 = findHSL(pixel)
		# larger = max(hue1, hue2)
		# smaller = min(hue1, hue2)

		# diff1 = abs(larger - smaller)
		# diff2 = abs((360 - larger) + smaller)




imageA = Image.open("matt.png")
imageB = Image.open("squirrel.png")

pixelPool = list(imageA.getdata())
newPixels = list(imageB.getdata())
remainingSpots = list(range(len(newPixels)))

width, height = imageB.size

while len(remainingSpots) > 0:
	length = len(remainingSpots)
	# if length % width == 0:
	# 	print(length)

	r = randrange(0, length)
	index = remainingSpots[r]
	del remainingSpots[r]

	oldPixel = newPixels[index]

	bestDiff = 999999
	bestPixel = 0

	pixelCount = len(pixelPool)
	numberToCheck = min(1000, pixelCount)

	for _ in range(numberToCheck):
		p = randrange(0, pixelCount)
		pixel = pixelPool[p]

		diff = 0
		diff += (2 * (oldPixel[0] - pixel[0])) ** 2
		diff += (4 * (oldPixel[1] - pixel[1])) ** 2
		diff += (3 * (oldPixel[2] - pixel[2])) ** 2
		diff = diff ** 0.5

		if diff < bestDiff:
			bestDiff = diff
			bestPixel = p

		if bestDiff == 0:
			break

	if len(pixelPool) == 0:
		# for now we will cheat and use the old pixel
		newPixels[index] = newPixel
	else:
		newPixel = pixelPool[bestPixel]
		newPixels[index] = newPixel
		del pixelPool[bestPixel]

newImage = Image.new(imageB.mode, imageB.size)
newImage.putdata(newPixels)
newImage.save("output/matt to squirrel.png")
newImage.show()
