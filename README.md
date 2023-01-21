# Dockerizing_a_FastAPI

This repository contains three examples of containerizing using the same fastAPI code.

Repo
----

The Dockerfile of this repo is typical of a single file FastAPI application. It doesn't support modules. 

Repo_two
--------

This version support modules and subdirectories. The Dockerfile starts from a Ubuntu image. This containerization is a one-to-one translation of the commands needed to deploy an app "bare metal" in an Ubuntu server.

Repo_five
---------

Pretty similar to Repo_two, but it starts from a "Python image". It is quick to build. As repo_two it supports modules and subdirectories.

To run each app, please consult the readme.md file in every directory.
