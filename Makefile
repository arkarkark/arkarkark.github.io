all: tags images

tags:
	./bin/fix_posts.py --tags

SHELL:=/usr/local/bin/bash -O globstar
images:
	exiftool -all= assets/images/**/*.{png,jpg,jpeg}
