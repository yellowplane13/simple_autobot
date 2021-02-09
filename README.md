How to run the Autobot application

Step1 : Clone the github repo :
            - Open Terminal and change the current working directory to the location where you want the cloned directory.
            - Run the comman <<git clone https://github.com/yellowplane13/simple_autobot>> to clone

Step2 : In order to run the server, the following steps need to be followed :
        - Prerequisites :Firstly docker needs to be installed on your system. 
            - Type <$ sudo pip3 install docker> command on the terminal.
        - Run docker command to create image and run the image to form a server container.
        - Commands to create image:
            1. In the cloned repo, cd to the server directory in where the Dockerfile present 
            2. docker build -t <image_name> .
            3. example: docker build -t server_image .

        - Commands to run the image:
            - docker run -p 9999:9999 <image_name> // 9999:9999 are the port numbers through which the TCP/IP comm is taking place.
            - example: docker run -p 9999:9999 server_image

Step3 : In order to run the client, the following steps need to be followed :
        - Prerequisites :  python3.9 must be installed.
        - cd to client directory in the terminal.
        - python3 client.py 
        - You will then be prompted to enter number of repositories and to enter the values in "org/repo" format.
        - Example: 
        Enter the number of repositories : 2
        Enter the values in org/repo format : twilio/twilio-php,twilio/twilio-python

        - A dictionary that contains the "org/repo" as the key and number of stars for that particular repo is obtained
        - Example : Enter the number of repositories : 1
                    Enter the values in org/repo format : twilio/twilio-php,gibberish_repo
                    *****stars received from server****
                    [RESULT] {'twilio/twilio-php': 1253}
                    ['[SUCCESS] twilio/twilio-php is a valid Repository', '[ERROR] gibberish_repo not a valid GitHub Repository']                      

Step4 : In order to run the unit tests :
        - cd to the server directory in the terminal
        - run "pytest -s"
        - This particular test is testing the business logic (which is the API call to github)

NOTE: Everytime a push is done, an image of the repository is automatically uploaded to Docker hub. 
It can be accessed from here:
https://hub.docker.com/repository/docker/yellowplane/simple_autobot