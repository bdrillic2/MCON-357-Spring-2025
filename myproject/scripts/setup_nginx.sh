#!/bin/bash

# Get the EC2 public IP using ec2metadata
EC2_PUBLIC_IP=$(ec2metadata --public-ipv4)

# Replace placeholder in the nginx config template
CONFIG_TEMPLATE="/home/ubuntu/MCON-357-Spring-2025/myproject/config/myproject-nginx.conf"
CONFIG_TEMP="/tmp/myproject-nginx.conf"
sed "s/your-ec2-ip/${EC2_PUBLIC_IP}/g" "$CONFIG_TEMPLATE" > "$CONFIG_TEMP"

# Link the updated config into nginx sites
sudo cp "$CONFIG_TEMP" /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled || true

# Test and reload Nginx
sudo nginx -t && sudo systemctl restart nginx
