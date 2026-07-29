```Dockerfile
FROM alpine:latest

WORKDIR /usr/share/nginx/html

COPY index.html /usr/share/nginx/html/
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
```

Note: This Dockerfile assumes the presence of an `index.html` file and a configuration file named `default.conf` in the root directory. Adjust paths as necessary for your application's specific requirements.