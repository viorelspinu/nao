"google-assistant-cegeka" - connects to Google Assistant API; uses a Coreographe application running on the robot and a python proxy server running in docker; human speech is saved as mp3 on the robot, next is sent over HTTP POST to the proxy server in docker; the audio file received from google is send as POST response to the robot; the robot plays that file


"google-cloud-vision" - the robot uses the Google VIsion API to tell what it sees; also Google Translate API is used for Romanian

"ibm-resnet-on-docker" - same as above, but instead of Google Vision API the robot is using an IBM neural network running in docker

"install_new_pkg" - python file running on the robot in order to install a pkg file