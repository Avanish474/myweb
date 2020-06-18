import os
for file in os.listdir("/var/lib/jenkins/workspace/Githubtask1"):
    if file.endswith(".html"):
        os.system('docker run -it -v /var/lib/jenkins/workspace/Githubtask1:/var/www/html -p 8082:8080 httpd')
    elif file.endswith(".php"):
        os.system('docker run -it -v /var/lib/jenkins/workspace/Githubtask1:/var/www/html -p 8083:8080 php')
    elif file.endswith(".py"):
        os.system('docker run -it -v /var/lib/jenkins/workspace/Githubtask1:/var/www/html -p 8082:8080 python')
