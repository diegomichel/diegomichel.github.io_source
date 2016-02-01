ssh root@diego rm -frv /home/www-data/diegomichel.org/*
hugo
scp -r public/* root@diego:/home/www-data/diegomichel.org/
