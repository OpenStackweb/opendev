A simple Django-based CMS built for the [OpenDev](http://www.opendevconf.com/) Conference.


# General environment setup
```bash
sudo apt install python3-dev python3-pip libjpeg-dev libssl-dev
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
```

# Project setup

```bash
git clone https://github.com/OpenStackweb/opendev.git opendev

cd opendev
virtualenv -p python3 .env
source .env/bin/activate

# Install reqs
pip install -r requirements.txt 

# Copy the settings template.
cp opendev/settings_local.py.template opendev/settings_local.py

# Make sure to review and edit the new settings file.
# You may want to edit ALLOWED_HOSTS to include local IP,
# setup a proper database backend, contact info, etc.
cat opendev/settings_local.py

# Setup initial DB
python manage.py migrate
```


# Development

```bash
# Running the dev server
# Defaults to 127.0.0.1
# Use 0.0.0.0:8000 to bind to the external IP
python manage.py runserver 0.0.0.0:8000
```


# PRODUCTION SERVER  

## Environment setup

First, follow all steps under "Env setup" and "Project setup". 

Clone the project under /var/www/opendev

Then run the below commands as root: `sudo -i`

## Install nginx and uwsgi
```bash
add-apt-repository ppa:nginx/stable
apt-get update && apt-get install nginx
pip3 install uwsgi
```

## Config nginx and uwsgi services

```bash 
# Carefully review the settings in conf/nginx.conf,
# including paths for media assets and SSL certs.
# Reference docs: https://gist.github.com/evildmp/3094281
ln -s /var/www/opendev/opendev/nginx.conf /etc/nginx/sites-enabled/
service nginx restart

mkdir -p /etc/uwsgi/vassals
mkdir -p /var/log/uwsgi
chown www-data:www-data /var/log/uwsgi
ln -s /var/www/opendev/opendev/opendev.ini /etc/uwsgi/vassals/

# Optional: Run this line in your bash to verify it's all working
/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --master

```
