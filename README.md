# stringer

## Purpose:
The purpose of tools is to master strings with Python.


## Tools:
Python3 3.6.1


## Source Structure:
stringer/ is root level of the source. It is intended that the source structure will
        loosely mirror wordsum-java, it will for now be shallow and allow to
        see where the code writes.

tests/ is root level of the tests for the wordsum python code.

data/ is a directory to contain any test data or output data before it is put
        into a container image for archive.

data/test/ is a directory of wordsum modeled test data. The file hierarchy may get
        deeper as more test are had.

containers/ is a directory containing the Dockerfiles.

## Local Setup:

### Local Setup on MacOS with Python3 and virtualenv:
TODO: TEST MAC STEPS AGAIN!
1. git clone <source>

2. cd <source>

3. (if not installed) sudo easy_install pip

4. (if virtualenv not installed) sudo pip install --upgrade virtualenv

5. (if brew and python3 not installed) ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

6. (if python3 not installed) brew install python3 --with-tcl-tk

7. virtualenv --system-site-packages -p python3 .

8. source ./bin/activate

9. export PYTHONHASHSEED=0

10. pip3 install -r requirements.txt

11. python3 test/test_tensor_install.py

12. wait for Tensorflow to say 'Hi'. If it doesn't then something is wrong.


### Local Setup on Ubuntu with Python3 and virtualenv:

1. git clone <source>

2. cd <source>

3. (if pip and virtualenv not installed) sudo apt-get install python3-pip python3-dev python-virtualenv python3.6-tk

4. virtualenv --system-site-packages -p python3 .

5. source ./bin/activate

6. export PYTHONHASHSEED=0

7. pip3 install -r requirements.txt

8. python3 -m spacy.en.download all

9. python3 test/test_tensor_install.py

10. wait for TensorFlow to say 'Hi'. If it doesn't then something is wrong.


## Testing:
1  cd <source>
2. pytest 

## ToDo:

##Copyright

  Open Story License

  Story: stringer
  Writer: Kalab J. Oster&trade;
  Copyright Holders: Kalab J. Oster&trade;
  copyright &copy; 2017 Kalab J. Oster&trade;

  Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
  if the humans or intelligent agents keep this Open Story License with the Story,
  and if the Story you tell remains free,
  and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.
