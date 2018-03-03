# Requires Pillow
# https://github.com/python-pillow/Pillow
#
# Usage: img2gpl IMAGE [PALETTE]
import os
import sys
from PIL import Image

argc = len(sys.argv)

if (argc < 2 or argc > 3):
	print "Usage: img2gpl IMAGE [PALETTE]"
	sys.exit(1)

image_filename = sys.argv[1]

# If palette filename is omitted, use image filename with replaced extension
if argc == 2:
	palette_filename = os.path.splitext(image_filename)[0]+'.gpl'
else:
	palette_filename = sys.argv[2]

image = Image.open(image_filename).convert('RGB')

width, height = image.size
pixels = list(image.getdata())

# Use set to ignore duplicate colors
palette = set()

# Use list to preserve order colors appear in image
colors = []

# Collect colors
for y in range(0, height):
	for x in range(0, width):
		pixel = pixels[y * width + x]
		if (pixel not in palette):
			palette.add(pixel)
			colors.append(pixel)

# Write palette file
palette_file = open(palette_filename, "w")

palette_file.write("GIMP Palette\n")
palette_file.write("# %d colors\n" % len(colors))

for c in colors:
	palette_file.write("%3d %3d %3d Untitled\n" % c)

palette_file.close()