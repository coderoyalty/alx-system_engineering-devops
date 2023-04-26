# setup nginx using puppet
exec { 'server config':
  provider => shell,
  command  => 'sudo apt-get update -y; sudo apt-get install -y nginx; echo "Hello World!" > 
/etc/nginx/html/index.html;
sudo sed -i "/server_name _;/a location /redirect_me {\n\treturn 301 https://alxafrica.com;\n\t}" /etc/nginx/sites-available/default
'
}
