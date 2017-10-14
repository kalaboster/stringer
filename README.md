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

2. Test in again in Ubuntu and MacOS

3. Use os.path.join for separator where needed instead of string or os.sep.

4. Test on widows where possible.

5. Integration tests.

## Local Setup:

### Local MacOS:

1.	git clone https://github.com/kalaboster/stringer.git

2.  cd stringer

3.	(if not pip installed) sudo easy_install pip

4.	(if virtualenv not installed) sudo pip install --upgrade virtualenv

5.	virtualenv .

6.	source ./bin/activate

7.  pip install -r requirements.txt

 

### Local Setup on Ubuntu with Python and virtualenv:

1. git clone https://github.com/kalaboster/stringer.git

2. cd stringer

3. (if pip and virtualenv not installed) sudo apt-get install python-pip python-dev python-virtualenv python

4. virtualenv .

5. source ./bin/activate

6. pip install -r requirements.txt


## Testing:
1.  cd stringer

2.  pytest test

## permutations - an app to get permutations of a string.

#### permutations_cli.py

A tool to return permustations of a string.

1. Do Local Setup

2. 'python permutations_cli.py --string test'

#### permutations_app.py

1. Do Local Setup. 

2. execute this command to launch Flask restful app: 'python ./permutations_app.py'

3. open browser and input this URL: 'http://0.0.0.0:5000/api/v1.0/permutations?string=test'


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


## AWS Deploy

(Under constructions to make AWS command line commands as those tools are now in requirements.txt)

TODO:
a. Create template IAM polices to attach to the role.
b. Create template S3 bucket.
c. Create subnet and security group template.

1. Launch CF stack for IAM role and instance-profile: stringer-iam.yaml

2. Launch CF stack for the EC2 instance: stringer-cf.yaml

3. Working...


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

