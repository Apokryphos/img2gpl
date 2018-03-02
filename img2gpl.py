# Requires Pillow
# https://github.com/python-pillow/Pillow
#
# Usage: img2gpl [IMAGE FILENAME] [PALETTE FILENAME]
import sys
from PIL import Image

argc = len(sys.argv)

if (argc < 3 or argc > 3):
	print "Usage: img2gpl [IMAGE FILENAME] [PALETTE FILENAME]"
	sys.exit(1)

image_filename = sys.argv[1]
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