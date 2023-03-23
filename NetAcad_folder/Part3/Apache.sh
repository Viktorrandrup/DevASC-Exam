#!/bin/bash 
  
  
touch Dockerfile 
  
echo "FROM ubuntu:latest" >> Dockerfile 
echo "RUN apt-get update && apt-get install -y apache2" >> Dockerfile 
echo "EXPOSE 80" >> Dockerfile 
echo "CMD [\"apache2ctl\", \"-D\", \"FOREGROUND\"]" >> Dockerfile 
  
docker build -t min-apacheserver . 
  
docker run -t -d -p 8080:85 --name 12ApacheWebserver min-apacheserver:latest 
