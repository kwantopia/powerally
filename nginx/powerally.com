server {
    listen 80;
    server_name www.powerally.com;
    rewrite ^/(.*) http://powerally.com/$1 permanent;
}

server {
    listen 80;
    server_name powerally.com;

    access_log /home/www/powerally.com/nginx/logs/access.log;
    error_log /home/www/powerally.com/nginx/logs/error.log;

    location /static/ {
      alias /home/www/powerally.com/electrify/sitestatic/;
    }

    location /downloads {
        root /home/www/powerally.com/htdocs/downloads/;
        index index.html;
    }

    location / {
        #root /home/www/powerally.com/htdocs/;
        #index index.html;
        proxy_pass http://127.0.0.1:8089/;
        include /etc/nginx/proxy.conf;
    }

}
