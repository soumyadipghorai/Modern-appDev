#! /bin/sh
echo "===================================="
echo "welcome to the setup. it will setup the local ven"
echo "and it will install required packages"
echo "you can rerun this without any issues"
echo "===================================="

if [ -d "env"]; 
then 
    echo "env folder exists. installing using pip"
else 
    echo "creating env and install using pip"
    python3.7 -m venv env 

fi 

# activate virtual env 
env/Scripts/activate 

# upgrade pip 
pip install --upgrade pip 
pip install -r requirements.txt 

deactivate 