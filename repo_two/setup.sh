# setup to perform a "bare metal" configuration in a linux server.

apt update && apt upgrade -y

apt install -y -q build-essential python3-pip python3-dev
pip3 install -U pip setuptools wheel
# Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.
# uvloop is a fast, drop-in replacement of the built-in asyncio event loop. 
# uvloop is released under the MIT license. uvloop and asyncio
pip3 install gunicorn uvloop httptools

cp .requirements.tx /app/requirements.txt

pip3 install -r /app/requirements.txt

cp ./service/ /app

/usr/local/bin/gunicorn  \
-b 0.0.0.0 80 \
-w 4 \
-k uvicorn.works.UvicornWorker main:app \

--chdir /app 