# imagegallery
used to generate docker container for generating an image library

# Usage
```
docker run --mount type=bind,source=<local source>,target=/usr/src/app/source --mount type=bind,source=<local dest>,target=/usr/src/app/dest sigalsolution
```
Will generate image library in <local dest> based on the images found in <local source>

# Shell command for using Automator to pipe relevant input

echo "prefix$@" | python3 ~/Applications/Skapa\ Webbgalleri/imagegallery/pythoncode.py | xargs -I {} ~/Applications/Skapa\ Webbgalleri/imagegallery/localcode_mac.sh {}
