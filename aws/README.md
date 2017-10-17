## aws

Purpose of these files is to automate deploy and configure-as-code stringer hosted by AWS.


### Tools

- python: https://www.python.org/
- pip: https://pip.pypa.io/en/stable/installing/
- awscli: http://docs.aws.amazon.com/cli/latest/userguide/installing.html
- aws services: https://aws.amazon.com/
- ec2 key pairs: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

### CloudFormation Templates

- stringer-iam-roles - The IAM roles of stringer.

- stringer-iam-policy - The IAM policies for stringer roles. (Creating...)

- stringer-s3 - The S3 template to deploy stringer to the EC2 instance.

- stringer-ec2 - The template to launch and configure an ec2 instance for stringer.

- stringer-cb - The code build template to build stringer. (under construction)

- stringer-cd - The code deploy template to deploy stringer to the EC2 instance. (under construction)


### Creation and Configuration of AWS Services for stringer.


1. Install Tools.

2. Configure AWS CLI with AWS account.

3. git clone https://github.com/kalaboster/stringer

4. cd stringer/aws

5. aws cloudformation create-stack --stack-name stringer-iam-role --template-body file://stringer-iam-role.yaml --capabilities CAPABILITY_NAMED_IAM

6. aws cloudformation create-stack --stack-name stringer-iam-policy --template-body file://stringer-iam-policy.yaml --capabilities CAPABILITY_NAMED_IAM

7. NOTE: All values of parameters can be replaced. All the following REPLACE_UPPER_CASE values beginning with REPLACE need to be replaced.

8. aws cloudformation create-stack --stack-name stringer-s3 --template-body file://stringer-s3.yaml  --parameters ParameterKey=BuildBucketName,ParameterValue=REPLACE_BUILD_BUCKET_NAME

9. aws cloudformation create-stack --stack-name stringer-ec2 --template-body file://stringer-ec2.yaml  --parameters ParameterKey=Ami,ParameterValue=ami-718c6909 ParameterKey=Instance,ParameterValue=t2.micro ParameterKey=Zone,ParameterValue=us-west-2a ParameterKey=Subnet,ParameterValue=REPLACE_WITH_EC2_SUBNET_STRING ParameterKey=SecurityGroups,ParameterValue=REPLACE_WITH_SECURITYGROUPS_LIST ParameterKey=KeySSH,ParameterValue=REPLACE_WITH_KEYSSH_NAME ParameterKey=IamProfile,ParameterValue=stringer-instance-profile ParameterKey=OwnerKey,ParameterValue=owner ParameterKey=OwnerValue,ParameterValue=REPLACE_WITH_YOU

10. aws cloudformation create-stack --stack-name stringer-cb --template-body file://stringer-cb.yaml --parameters ParameterKey=ProjectName,ParameterValue=stringer-codebuild-service  ParameterKey=ServiceRole,ParameterValue=codebuild-service-role ParameterKey=BuildBucketName,ParameterValue=REPLACE_BUILD_BUCKET_NAME

11. (under construction)