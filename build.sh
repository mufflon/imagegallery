mkdir code/source
mkdir code/dest
docker build -t mufflonicus/imagelibrary:1.0.0 .
docker push mufflonicus/imagelibrary:1.0.0