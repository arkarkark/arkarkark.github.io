```
DIR=${PWD/*assets/assets}; (for fil in *.jp?(?)g; do echo "[![](/$DIR/${fil/.jp?(?)g/.sml.jpg})](/$DIR/$fil)"; done) | pbcopy | pbpaste
for fil in *.jp?(?)g; do  magick $fil -resize 400 ${fil/.jp?(?)g/.sml.jpg}; done
```

you might also want

```
magick mogrify -monitor -format jpg *.HEIC
```
