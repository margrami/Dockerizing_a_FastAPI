[MRE 11-1-23]
to run this app from terminal :
C:\Users\ars\Documents\docker_cfg\more_fastAPI\repo\service> uvicorn main:app

docker build --pull --rm -f "Dockerfile" -t repotwo:latest "." 

to access the console 
docker run -it 9cbebf4084c8 bash

the long string is the image id

to run manually from docker console :
root@2dbbfa564d49:/app# /usr/local/bin/gunicorn main:app -b 0.0.0.0 80

[MRE 18-1-23]

This configuration works properly with this commands:
# Image
docker build -t <image name> .
docker run -p 80:80 <image name>