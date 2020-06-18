# myweb


 Create container image that has Jenkins installed using dockerfile, when we launch this image, it should automatically start Jenkins service in the container.

 Create a job chain of job1, job2, job3 and job4 using build pipeline plugin in Jenkins

 Job1 : Pull the Github repo automatically when some developers push repo to Github.

 Job2 : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code ( eg. If code is of PHP, then Jenkins should start the container that has PHP already installed ).

 Job3 : Test your app if it is working or not.

 Job4 : if app is not working , then send email to developer with error messages.

 Job5 Create One extra job for monitoring : If container where app is running. fails due to any reson then this job should automatically start the container again.
 
 
 
# Prerequisites

Redhat 8 inside a virtual machine


Docker should be installed


Basics of Linux


Basics of Jenkins


Basics of Docker


# Step by step implementation

1- Create a Dockerfile inside a file /task

        
        mkdir /task
        
        cd  /task
        
        gedit Dockerfile
        
    refer to Dockerfile from given in this repository
    

2-   Now we will build the image which will install and run jenkins:
        
        docker build -t jenkins /task/


     and now we run the container
        
        
        docker run -it -p 8081:8080 -v /var/run/docker.sock:/var/run/docker.sock --name jenkinscont jenkins
        
        
        
   This will provide you with password to jenkins .Copy it from here and run jenkins using your IP and port 8081 (ex 192.168.43.210:8081).Once you have reached to the jenins page paste your password here and download the required plugins.
   
   
 3- This job will download the Github code from this repository and put in this workspace
 
 
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job1-1.png)
 
     
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job1-2.png)
   
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job1-3.png)
   
 
 4- This job will check the type of code and the respective container containg the interpreter
 
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job2-1.png)
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job2-3.png)
   
 5- This job will test whether the web page is opening or not and ouput the required message.
 
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job3.png)
   
 6- This job will send the notification whether the webpage is not opening .
 
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job4.png)
   
 7- This job will monitor if the container with interpretter is running or not and will run it if its not working.   
   
   ![alt text](https://github.com/Avanish474/myweb/blob/master/job5.png)
   
  
