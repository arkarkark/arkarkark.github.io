all: tags images

tags:
	./bin/fix_posts.py --tags

SHELL:=$${SHELL} -O globstar
images:
	exiftool -all= assets/images/**/*.{png,jpg,jpeg}
