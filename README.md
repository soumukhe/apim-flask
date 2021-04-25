# docker-compose-apim-flask

-  Install flask server (container based) on ubuntu.
- main.py is in /app directory

- Steps:
- sudo  -i 
- apt-get update && apt-get upgrade  -y 
- echo net.ipv4.ip_forward=1 >> /etc/sysctl.conf 
- sysctl --system
- exit  
- sudo apt install docker.io -y
- sudo systemctl start docker 
- sudo systemctl enable docker 
- sudo groupadd docker 
- sudo usermod -aG docker $USER 
-  exit #  and ssh back in for this to work
- docker  --version
- sudo apt install docker-compose  -y
- git clone https://github.com/soumukhe/apim-flask.git
- cd docker-compose-flask/
- docker-compose up --build -d
- #########################################
- How to get and post to api server:
- GET: curl http://newapimeastus.azure-api.net/myapiserver/accounts
- POST: curl -X POST -H "Content-Type: application/json" -d '{"name" : "kiwi", "balance" : 0.02 }' http://newapimeastus.azure-api.net/myapiserver/addaccounts
