#Get source code

git clone https://github.com/tommy1008/ssh-command.git

cd ssh-command/

#setup the python and install plugin

sudo chmod +x *.sh

sudo chmod +x *.bat 

python -m venv venv 

source venv/bin/activate 

pip install -r requirements.txt 

#run

./run.bat
