#!/bin/bash

sh install_docker.sh
docker pull phpmyadmin
docker run --name phpmyadmin -d -e PMA_HOST=51.159.25.115 -e PMA_PORT=29404 -p 8080:80 phpmyadmin