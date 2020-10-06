export LANGUAGE="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
export LANG="en_US.UTF-8"
mkdir data
touch data/history.txt

### Deployment
## Step One — Install and Enable mod_wsgi
sudo apt update
sudo apt install apache2 libapache2-mod-wsgi python-dev

sudo a2enmod wsgi
systemctl restart apache2

