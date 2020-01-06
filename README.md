# flask-docker-swarm-load-balancer-demo
docker swarm init --advertise-addr=YOUR_IP  
docker stack deploy --compose-file docker-compose.yml stackdemo  
docker stack services stackdemo  
docker stack ps stackdemo  
docker service ls -f name=stackdemo  
#scale up for flask service  
docker service scale stackdemo_flask=2  
Test API and load balancing in swarm mode  
curl -XGET http://0.0.0.0:8081/ha  
You will get  
curl -XGET http://0.0.0.0:8081/ha  
>Container Hostname: b5ddd8844e84 , UUID: af45a26a-31e0-40a9-99d1-4b381527a70f  
curl -XGET http://0.0.0.0:8081/ha  
>Container Hostname: 1a846eb36e81 , UUID: 64809a59-c085-4a59-a639-90e15bd0bb06  

Down the stack  
docker stack rm stackdemo  
Leave swarm mode  
docker swarm leave --force  
