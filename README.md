## Instructions to set AWS EMI instance

1. If you are a new user for AWS, create an AWS account (either free tier or paid tier) based on the infrastructure required.

2. Once you create the account, sign-in to the aws console with your credentials.

3. You will land up in a page which shows you the services list. 

4. In order to typically run a loan prediction model involving more data, we need a system with high RAM and more computation power. To make this happen, we go for AWS cloud and initiate an Linux EC2 instance (in my case, it can be different as per your need). Make a selection on the location attribute as well at the top right corner of the window.

5. Navigate to Services -> EC2. Select Launch instance and proceed for configuring the EC2 instance.

6. Considering the machine and packages which we need for running the model, we go for Community AMI -> Other Linux -> Deep Learning AMI (Amazon Linux) Version 2.0 - ami-3a533040 EC2 (It contains pre built Tensorflow and Keras bindings) and click Select.

7. You will land up in a page where you need to choose the instance type. Based on your requirement, say considering data size, processing speed and more, you can go for high ended machines. For now, select the check box of free tier (t2.micro) type and select configure instance details.

8. Based on your needs, you can edit the configuration of the instance in the page right now you are in. Once you are done with the configuration, select Add Storage.

9. In the next page, you can configure the storage volume if you need. After configuring the select Add Tags

10. In the next page, if you need tags for naming your instance, you can add tag. Once you are done, select Configure Security Group

11. In the next page, you need to configure the security group access, say the inbound and outbound links using which you can access the EC2 machine using putty. Once you are done with configuring the security group select Review and Launch.

12. In the next page, check for the configurations once again. When all the configuration is set, select Launch.

13. This will open a dialog box which is the main part of setting up the EC2 instance. Select the Create a new key pair from the first drop-down list box. Give a specific name for the key say "ssht2micro" and select Download Key Pair. It will prompt you to save the "ssht2micro" as ".pem" file. Save it in your local drive.

14. Now select Launch instance, which will launch your EC2 instance. Now you can see that your instance got launched and will take some time to access the machine.

## Generating the private key

15. In meantime, we need to create a private key using the "ssht2micro.pem" using PuTTygen. 

16. Install PuTTygen. Open PuTTygen. Select Load and locate the "ssht2micro.pem" and select Open. It will pop-up showing "Successfully imported Foreign Key". Select OK. 

17. Now save this key as private by selecting Save private key -> Yes. Save the private key with some name as "ssht2micro_private". By default it will get saved as ".ppk" file extension.

18. We are done with configuring the EC2 instance and the key for accessing the instance too.

**********************************************************************************************************************************************

## Initiating the EC2 instance

19. Open PuTTy. In the Host Name box enter "ec2-user@<your instance public ip available in the EC2 console>".
NOTE: The prefix "ec2-user" is the user name for any linux instance which you are running. There is a documentation available which will guide you to configure the instance.

20. In the left pane of the PuTTy expand SSH and select Auth. Browse for the ".ppk" file, here "ssht2micro_private.ppk" and select Open.

21. After few seconds a pop-up will ask for clearing the SSH certificate for accessing the instance. Select Yes and will open the EC2 instance.

**********************************************************************************************************************************************

## Get access for the build in EC2 instance

22. To run the model in EC2, transfer the build using any SFTP, FTP client(say WinSCP). To login to in WinSCP, follow the same step as above mentioned for initiating the EC2 instance.

**********************************************************************************************************************************************

## Running the model

23. There are two repository namely, loan_data_cleansing and loan_data_prediction_using_tensorflow for building the model and using the pre built model for new set of data respectively.

24. Separate README.md file are given in each folder. Once you are ready with the EC2 instance, navigate to README.md file available in loan_data_prediction_using_tensorflow folder and follow the steps.