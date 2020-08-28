```
DIR=${PWD/*assets/assets}; for fil in *.jpg; do echo "[![](/$DIR/${fil/.jpg/.sml.jpg})](/$DIR/$fil)"; done
for fil in *.jpg*; do  magick $fil -resize 400 ${fil/./.sml.}; done
```

you might also want

```
magick mogrify -monitor -format jpg *.HEIC
```
