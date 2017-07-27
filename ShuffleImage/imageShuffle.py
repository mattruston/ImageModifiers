
from PIL import Image
from random import *

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
NONE = 4


im = Image.open("squirrel.png")

print(im.format, im.size, im.mode)

width, height = im.size
pixels = list(im.getdata())
length = len(pixels)

index = randrange(0, len(pixels))
previous = NONE

for n in range(50):
	for _ in range(length * n):
		options = []
		if (index + 1) < length and previous != LEFT:
			options.append(RIGHT)
		if (index - 1) >= 0 and previous != RIGHT:
			options.append(LEFT)
		if (index + width) < length and previous != UP:
			options.append(DOWN)
		if (index - width) >= 0 and previous != DOWN:
			options.append(UP)

		direction = options[randrange(0, len(options))]
		previous = direction

		choice = index
		if direction == LEFT:
			choice = index - 1
		if direction == RIGHT:
			choice = index + 1
		if direction == UP:
			choice = index - width
		if direction == DOWN:
			choice = index + width

		temp = pixels[index]
		pixels[index] = pixels[choice]
		pixels[choice] = temp 
		index = choice

	newImage = Image.new(im.mode, im.size)
	newImage.putdata(pixels)
	newImage.save("sqrl" + str(n) + ".png")
		