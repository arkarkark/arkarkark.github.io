all: tags images

tags:
	./bin/fix_posts.py --tags

images:
	exiftool -all= assets/images/*.{png,jpg} assets/images/*/*.{png,jpg}
