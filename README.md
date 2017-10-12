# stringer

## Purpose:
The purpose of tools is to master strings with Python.

It has two current uses:

1. It has a cli to take a string and return its permutations.

2. It can take a at tar.gz containing files and search those files and redact/mask credit card and ssn patterned numbers.
The patterns are defined in the mask_model.

Please feel free to use. While this has been tested on Ubuntu 14. It is currently being tested on different platforms.


## Required Tools:
 - Python
 - Docker
 - docker-compose


## Source Structure:
stringer/ is root level of the source.

test/ is root level of the tests for the wordsum python code.

## TODO

1. Complete all the TODO in code.

2. Test on a few more environments to check!

3. Test again in clean env Ubuntu and MacOS

4. use os.sep for separator where needed instead of literals.

5. Integration tests.

## Local Setup:

### Local Setup on Ubuntu with Python and virtualenv:

1. git clone &lt;source>

2. cd &lt;source>

3. (if pip and virtualenv not installed) sudo apt-get install python-pip python-dev python-virtualenv python

4. virtualenv .

5. source ./bin/activate

6. pip install -r requirements.txt


## Testing:
1.  cd &lt;source>

2.  pytest test

## permutations - an app to get permutations of a string.

#### permutations_cli.py

A tool to return permustations of a string.

1. setup virtualenv.

2. 'python permutations_cli.py --string test'

#### permutations_app.py

1. setup virtualenv.

2. execute this command to launch Flask restful app: 'python ./permutations_app.py'

3. open browser and input this URL: 'http://127.0.0.1:5000/api/v1.0/permutations?string=test'


## log redaction - an app to redact patterns in logs.

#### log_redaction_cli.py

A tool to redact patterns in a log file or files in a tar.gz arhive and create a log file.

1. setup virtualenv.

2. python log_redaction_cli.py --tarfile "test/files/test_output.tar.gz"  --working-dir "/home/kalab/github/stringer/test/files" --output-dir  log_redataction_example

- tarfile must be relative to python log_redaction_cli.py

- work-dir is an absolute path.

- output dir is string to name the dir for working dir

- All log files and tar files output in working dir.

- the log file is a formated json file with the same name as the tar file in the working directory.


## Docker
(currently only permutations, but working to get endpoint for log redaction)

1. cd &lt;source>

2. docker-compose up

## Copyright

  Open Story License

  Story: stringer
  Writer: Kalab J. Oster&trade;
  Copyright Holders: Kalab J. Oster&trade;
  copyright &copy; 2017 Kalab J. Oster&trade;

  Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
  if the humans or intelligent agents keep this Open Story License with the Story,
  and if the Story you tell remains free,
  and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.

