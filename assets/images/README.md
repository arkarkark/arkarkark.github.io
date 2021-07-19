make thumbnails
```
for fil in *.jpeg; do  magick $fil -resize 400 ${fil/.jp?(?)g/.sml.jpg}; done
```

create markdown
```
DIR=${PWD/*assets/assets}; (for fil in *.jpeg; do echo "[![](/$DIR/${fil/.jp?(?)g/.sml.jpg})](/$DIR/$fil)"; done) | pbcopy
```

you might also want

```
magick mogrify -monitor -format jpg *.HEIC
```
