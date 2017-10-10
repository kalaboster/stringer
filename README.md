# stringer

## Purpose:
The purpose of tools is to master strings with Python.


## Required Tools:
Python
Docker
docker-compose


## Source Structure:
stringer/ is root level of the source. It is intended that the source structure will
        loosely mirror wordsum-java, it will for now be shallow and allow to
        see where the code writes.

test/ is root level of the tests for the wordsum python code.

containers/ is a directory containing the Dockerfile distribution.

## Local Setup:

### Local Setup on Ubuntu with Python and virtualenv:

1. git clone <source>

2. cd <source>

3. (if pip and virtualenv not installed) sudo apt-get install python3-pip python3-dev python-virtualenv python3.6-tk

4. virtualenv .

5. source ./bin/activate

7. pip install -r requirements.txt


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
