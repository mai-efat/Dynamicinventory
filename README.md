# **Install  cloud watch agent on all ec2 in the project **

## **Project Overview**

This project automates the installation and configuration of the **AWS CloudWatch Agent** on all running EC2 instances in an AWS environment using **AWS Lambda**. The solution integrates **AWS EC2**, **AWS CloudWatch**, **AWS Systems Manager (SSM)**, and **Jenkins CI/CD pipeline** for centralized monitoring and automation of EC2 management.

### **Key Features**
- **Ansible Playbook**: Installs and configures CloudWatch Agent on EC2 instances.
- **AWS Lambda**: Triggers the installation process by using AWS Systems Manager (SSM) to install the CloudWatch agent.
- **Dynamic EC2 Inventory**: Uses the EC2 instance metadata to dynamically target EC2 instances for CloudWatch Agent installation.
- **CloudWatch Integration**: Sends logs and metrics to AWS CloudWatch for centralized monitoring and analysis.
- **Jenkins Pipeline**: The Lambda function triggers the Jenkins pipeline to automate the installation and management of the CloudWatch Agent.

## **File Descriptions**

- **ansible.cfg**: Ansible configuration file with default settings for playbooks.
- **aws_ec2.yml**: Dynamic inventory configuration that fetches EC2 instance details to target instances for CloudWatch Agent installation.
- **jenkinsfile**: Jenkins pipeline configuration for automating the deployment process.
- **lambda_function.py**: Python script for AWS Lambda that triggers CloudWatch Agent installation via AWS Systems Manager (SSM).
- **playbook.yaml**: Ansible playbook that installs and configures the CloudWatch Agent on the targeted EC2 instances.

## **Project Setup**

Follow these steps to set up the environment and use the scripts:

### **Prerequisites**
1. **AWS Account** with appropriate permissions for EC2, SSM, CloudWatch, Lambda, and Jenkins.
2. **Ansible** installed on your local machine or Jenkins server.
3. **AWS CLI** configured with the correct permissions for your AWS environment.
4. **Jenkins Server**  to automate the deployment pipeline.

### **Steps to Deploy**

1. **Set up AWS Lambda**:
   - Deploy the **lambda_function.py** to AWS Lambda.
   - Ensure that the Lambda function has an IAM role with the necessary permissions to execute SSM commands on EC2 instances.
   - Set up the Lambda trigger for CloudWatch to invoke the Lambda function.

2. **Configure Jenkins Pipeline**:
   - The **lambda_function.py** triggers the **Jenkins pipeline** upon CloudWatch events.
   - The **Jenkinsfile** defines the steps in the pipeline, automating tasks like CloudWatch agent installation on EC2 instances.
   - The pipeline can be configured to invoke **Ansible** playbooks or AWS SDK to trigger the SSM commands from Lambda.

3. **Configure Ansible Playbook**:
   - Update the **aws_ec2.yml** inventory file to include your EC2 instances.
   - Customize the **playbook.yaml** to ensure the CloudWatch agent is installed and configured on all EC2 instances.
   - Run the playbook via Jenkins or manually to install the CloudWatch Agent across your EC2 instances:
     ```bash
     ansible-playbook -i aws_ec2.yml playbook.yaml
     ```

4. **Lambda and CloudWatch Integration**:
   - When an event ( EC2 instance launch) is triggered in CloudWatch, it will invoke the **lambda_function.py**.
   - This function triggers the **Jenkins pipeline**  to install the CloudWatch Agent on the target EC2 instances.
