apt-get update
apt-get upgrade --yes
apt-get install --yes wget
wget http://download.opensuse.org/repositories/home:p_conrad:coins/xUbuntu_14.04/Release.key
apt-key add - < Release.key
sh -c "echo 'deb http://download.opensuse.org/repositories/home:/p_conrad:/coins/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/namecoin.list"
apt-get update
apt-get install --yes namecoin
mkdir ~/.namecoin
touch ~/.namecoin/namecoin.conf
chmod 600 ~/.namecoin/namecoin.conf
echo "rpcuser=namecoinrpc\nrpcpassword=namecoin\nrpcallowip=*" > ~/.namecoin/namecoin.conf
/usr/bin/namecoind
