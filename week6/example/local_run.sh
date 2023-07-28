#! /bin/sh
echo "===================================="
echo "welcome to the setup. it will setup the local ven"
echo "and it will install required packages"
echo "you can rerun this without any issues"
echo "===================================="

if [ -d "env"]; 
then 
    echo "enabling virtual env"
else 
    echo "no virtual env. Please run setup.sh first"
    exit N 
fi 

# activate virtual env 
env/Scripts/activate 

export ENV = development 
python main.py 
deactivate 