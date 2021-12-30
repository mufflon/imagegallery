#!/bin/bash
#This code is to be used on the host machine
#It gets a file as the first argument
#It will generate a directory with the same name with a prefix of web- in the same directory
echo "The passed arguments are: $@"
echo "$1 first instruction"

DIRECTORY=$(dirname "$1")
BASENAME=$(basename "$1")
echo "directory is $DIRECTORY"
echo "basename is $BASENAME"

NEWOUTPUT=$DIRECTORY"/web-$BASENAME"

mkdir "$NEWOUTPUT"

echo "output is $NEWOUTPUT"
echo "will now run docker"
docker run --mount type=bind,source="$1",target=/usr/src/app/source --mount type=bind,source="$NEWOUTPUT",target=/usr/src/app/dest mufflonicus/imagelibrary