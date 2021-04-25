FROM soumukhe/python3flask:latest
    
# STATIC paths for file.
# Don't use flask static. Nginx is your friend
ENV STATIC_URL /static
ENV STATIC_PATH /app/static
    
# Place your flask application on the server
COPY ./app /app
WORKDIR /app
RUN apt-get update
    
# Install requirements.txt
#RUN pip3 install -r requirements.txt
RUN apt install python3-pip -y

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip3 install -r requirements.txt
    
# NGINX setup
COPY ./nginx.sh /nginx.sh
COPY ./certs /etc/nginx/certs
RUN chmod +x /nginx.sh

    
ENV PYTHONPATH=/app
    
ENTRYPOINT ["/nginx.sh"]
CMD ["/start.sh"]
    
EXPOSE 80 443
