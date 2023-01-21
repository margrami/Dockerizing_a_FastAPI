[MRE 10-1-23]
to run this app from terminal :
C:\Users\ars\Documents\docker_cfg\more_fastAPI\repo\service> uvicorn main:app

I need to solve the problem about the uvicorn. cheking if the name must be app instead of service.
because when I run uvicorn as unicorn service.main:app. it can import movie_data.py.

for the time being it is running with this configuration:
.
├── Dockerfile
├── main.py
|── movie_data.py
   |── models
└── requirements.txt

but this implies made a copy of every file to the workdir /code.




with this config to run To run in docker: from terminal ../repo/service

# docker build -t <nme> .
docker build -t fastapi-tut .
# docker run -p <host_port>:<containe_port> <image name>
docker run -p 80:80 fastapi-tut  

# docker start/stop <container_name> <container_id>

2. Check the port mapping!