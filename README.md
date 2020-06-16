#create module
python3 setup.py sdist
sudo python3 setup.py install 
twine upload dist/*
