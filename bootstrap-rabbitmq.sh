sudo apt-get update
sudo apt-get install erlang-nox -y
wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.2.3/rabbitmq-server_3.2.3-1_all.deb
sudo dpkg -i rabbitmq-server_3.2.3-1_all.deb
sudo rabbitmqctl delete_user guest
sudo rabbitmqctl add_user bunny ilovecarrots
sudo rabbitmqctl set_permissions bunny '.*' '.*' '.*'