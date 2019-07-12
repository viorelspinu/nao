FROM ubuntu:18.10
RUN apt-get update
RUN apt-get -yq install nano
RUN apt-get -yq install python3-dev python3-venv 
RUN python3 -m venv env
RUN env/bin/python -m pip install --upgrade pip setuptools wheel
RUN /bin/bash -c "source env/bin/activate"
RUN apt-get -yq install portaudio19-dev libffi-dev libssl-dev
RUN apt-get  -yq install curl
RUN apt-get  -yq install ffmpeg
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install --upgrade google-assistant-sdk[samples]
RUN python3 -m pip install flask

#generate credentials
RUN python3 -m pip install --upgrade google-auth-oauthlib[tool]
COPY ./generate_credentials.sh /generate_credentials.sh
RUN chmod +x /generate_credentials.sh

COPY ./client_credentials.json /client_credentials.json
#//credentials

COPY ./push-to-talk.sh /push-to-talk.sh
RUN chmod +x /push-to-talk.sh
COPY ./server.py /server.py


COPY ./start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT [ "/start.sh" ]