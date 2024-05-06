#!/usr/bin/env bash
# Function to exit with an error message


function error_exit() {
    echo "Error: $1"
    exit 1
}

# Function to check if a directory exists and create it if not
function create_dir() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1" || error_exit "Failed to create directory $1"
    fi
}

# Update package lists
apt-get update || error_exit "Failed to update package lists"

# Install Nginx
apt-get install -y nginx || error_exit "Failed to install Nginx"

# Create necessary folders
create_dir /data/web_static/releases/test
create_dir /data/web_static/shared

# Create a test index.html file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
rm -f /data/web_static/current && ln -s /data/web_static/releases/test/ /data/web_static/current || error_exit "Failed to create symbolic link"

# Change ownership of the "data" directory
chown -R ubuntu:ubuntu /data || error_exit "Failed to change ownership of /data directory"

# Modify the Nginx configuration
sed -i '26i\    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-available/default || error_exit "Failed to modify Nginx configuration"
