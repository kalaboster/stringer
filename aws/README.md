## aws

Purpose of these files is to automate deploy and configure-as-code stringer hosted by AWS.


### Tools

- python: https://www.python.org/
- pip: https://pip.pypa.io/en/stable/installing/
- awscli: http://docs.aws.amazon.com/cli/latest/userguide/installing.html
- aws services: https://aws.amazon.com/
- ec2 key pairs: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
- stringer-env-var.sh = A shell script you input your unique values into then execute, so you don't need to manually
alter the commands to create the stack.


### CloudFormation Templates

- stringer-sg.yaml - The security group for stringer.

- stringer-iam-roles.yaml - The IAM roles of stringer.

- stringer-iam-policy.yaml - The IAM policies for stringer roles. (Creating...)

- stringer-s3.yaml - The S3 template to deploy stringer to the EC2 instance.

- stringer-ec2.yaml - The template to launch and configure an ec2 instance for stringer.

- stringer-cb.yaml - The code build template to build stringer.

- stringer-cd.yaml - The code deploy template to deploy stringer to the EC2 instance. (under construction)

- install_ec2 - The files used by appspec.yml and codedeploy to install stringer on to the instance created by stringer-ec2.yaml.


#### TODO:
1. Replace stringer-iam-policy in wild card resource definitions with parameterized explicit resource definitions.
2. complete on shell to executed commands and wait fo the stack to create checking every ten seconds until I decide
on how to master all the templates.
3. Use Lex to automate the configuration and help a person configure it and alter templates through the API.

### Creation and Configuration of AWS Services for stringer.


1. Install Tools.

2. Configure AWS CLI with AWS account.

3. git clone https://github.com/kalaboster/stringer

4. cd stringer/aws

5. Get you VPC id and replace it with REPLACE_VPC_ID in the following command.

5. aws cloudformation create-stack --stack-name stringer-sg --template-body file://stringer-sg.yaml  --parameters ParameterKey=VpcId,ParameterValue=REPLACE_VPC_ID

5. Write and save values into stringer-env-var.sh

6. source stringer-env-var.sh

7. aws cloudformation create-stack --stack-name stringer-iam-role --template-body file://stringer-iam-role.yaml --capabilities CAPABILITY_NAMED_IAM

8. aws cloudformation create-stack --stack-name stringer-iam-policy --template-body file://stringer-iam-policy.yaml --capabilities CAPABILITY_NAMED_IAM

9. aws cloudformation create-stack --stack-name stringer-s3 --template-body file://stringer-s3.yaml  --parameters ParameterKey=BuildBucketName,ParameterValue=$REPLACE_BUILD_BUCKET_NAME

10. aws cloudformation create-stack --stack-name stringer-ec2 --template-body file://stringer-ec2.yaml  --parameters ParameterKey=Ami,ParameterValue=ami-718c6909 ParameterKey=Instance,ParameterValue=t2.micro ParameterKey=Zone,ParameterValue=us-west-2a ParameterKey=Subnet,ParameterValue=$REPLACE_WITH_EC2_SUBNET_STRING ParameterKey=SecurityGroups,ParameterValue=$REPLACE_WITH_SECURITYGROUPS_LIST ParameterKey=KeySSH,ParameterValue=$REPLACE_WITH_KEYSSH_NAME ParameterKey=IamProfile,ParameterValue=stringer-instance-profile ParameterKey=OwnerKey,ParameterValue=owner ParameterKey=OwnerValue,ParameterValue=$REPLACE_WITH_YOU

11. aws cloudformation create-stack --stack-name stringer-cb --template-body file://stringer-cb.yaml --parameters ParameterKey=ProjectName,ParameterValue=stringer-codebuild-service  ParameterKey=ServiceRole,ParameterValue=codebuild-service-role ParameterKey=BuildBucketName,ParameterValue=$REPLACE_BUILD_BUCKET_NAME

12. ...Wait from stacks to Complete.

13. aws cloudformation create-stack --stack-name stringer-cd --template-body file://stringer-cd.yaml --parameters ParameterKey=ServiceRoleArn,ParameterValue=$REPLACE_CODE_DEPLOY_ARN_ROLE ParameterKey=BuildBucketName,ParameterValue=$REPLACE_BUILD_BUCKET_NAME  ParameterKey=S3Key,ParameterValue=$REPLACE_S3_KEY ParameterKey=EC2TagValue,ParameterValue=$REPLACE_WITH_YOU

14. ...Wait for stack to Complete.

15. TEST: http://<eip>:8080/api/v1.0/permutations?string=test