#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# install nginx
apt install -y nginx

# create folders
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create dummy web content
echo '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Web Page</title>
</head>
<body>
    <h1>This is a dummy webpage</h1>
    <h2>915b89ca-84ae-5e53-9f8f-2723ebb5163b</h2>
    <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius aut et iure modi, tenetur nostrum labore ad doloremque dolor sint voluptatum, recusandae obcaecati hic, quisquam eos. Earum vel totam alias!
        Vel accusantium ducimus atque enim, nam quibusdam, sequi aliquid distinctio porro ipsam est suscipit tempora! Eum eaque odit, sapiente laborum est voluptatibus hic in magni dignissimos nihil fugiat illum ea?
        Molestiae, commodi. Deserunt ipsum iure temporibus vel quasi facilis natus animi corrupti assumenda corporis, at mollitia unde sint hic quibusdam culpa quisquam reprehenderit, rem, exercitationem consectetur harum. Recusandae, saepe perspiciatis.
        Voluptas magnam repellendus veniam libero rerum iusto vero sed animi consequuntur maiores labore, nihil nostrum perspiciatis enim hic quibusdam ullam, similique dolorem. Repellendus, ab quam expedita quasi porro libero laborum!
        Eligendi, nesciunt facilis optio nobis veniam doloribus explicabo error vel cum est beatae eaque at soluta quam non magni recusandae repellat. Minus aliquid blanditiis dicta asperiores, odio ex iure quis.
    </p>
</body>
</html>' > /data/web_static/releases/test/index.html

# create symbolic link
ln -fs /data/web_static/releases/test/ /data/web_static/current

# change owner
chown -R ubuntu:ubuntu /data/

# serve dummy content
sed -i 's|error_log /var/log/nginx/error.log warn;|error_log /var/log/nginx/error.log warn;\
\
        location /hbnb_static {\
                alias /data/web_static/current/;\
        }\
|' /etc/nginx/sites-enabled/default

service nginx restart
