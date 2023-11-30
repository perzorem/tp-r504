docker fill $(docker ps -q)
docker rm $(docker ps -aq) 
