ga-proxy-server installation
----

__JUST_ONE_TIME__
0. follow "configure a developer project and account settings" and "register a device model" from here - https://developers.google.com/assistant/sdk/guides/service/python/embed/config-dev-project-and-account, then copy the credentials json file (from step "Download credentials") over the .client_credentials.json file


1. install docker and docker compose

2. run "docker-compose build" in the docker folder

3. run "docker-compose up -d"

4. you can see what is happening in container running "docker logs -f ga_proxy_server"


AUTHORIZATION STEPS (__JUST_ONE_TIME__)

1. run "docker exec -it ga_proxy_server bash" to get in the container

2. run "./generate_credentials.sh"

3. access the link in browser and follow the wizard

4. copy paste the authorization code in the container prompt

5. your auth data is now saved in /root/.config/google-oauthlib-tool/credentials.json (in the container); this path from container filesystem is persisted on the local machine disk as a volume (see docker-compose.yml), so next time you don't have to do these steps again, the json authorization file will be there.

//END AUTHORIZATION STEPS

