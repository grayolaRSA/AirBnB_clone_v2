#!/usr/bin/env bash
#script to set up web servers

#install nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

#create required folders if not present
if [ ! -d "/data/" ]; then
  echo "/data/ folder doesn't exist. Creating..."
  sudo mkdir /data/
fi

if [ ! -d "/data/web_static/" ]; then
  echo "/data/web_static/ folder doesn't exist. Creating..."
  sudo mkdir /data/web_static/
fi

if [ ! -d "/data/web_static/releases/" ]; then
  echo "/data/web_static/releases/ folder doesn't exist. Creating..."
  sudo mkdir /data/web_static/releases/
fi

if [ ! -d "/data/web_static/shared/" ]; then
  echo "/data/web_static/shared/ folder doesn't exist. Creating..."
  sudo mkdir /data/web_static/shared/
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
  echo "/data/web_static/releases/test/ folder doesn't exist. Creating..."
  sudo mkdir /data/web_static/releases/test/
fi

#create a test file
sudo touch /data/web_static/releases/test/index.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Define the source and target paths
source_path="/data/web_static/releases/test/"
target_path="/data/web_static/current"

# Check if the symbolic link already exists and delete it if it does
if [ -L "$target_path" ]; then
  echo "Symbolic link already exists. Deleting..."
  sudo rm "$target_path"
fi

# Create the new symbolic link
sudo ln -s "$source_path" "$target_path"

echo "Symbolic link created successfully!"

#change grp and user ownership of folder
sudo chown -hR ubuntu:ubuntu /data/

#update Nginx configuration to serve content of new l
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start

echo "process complete!"
