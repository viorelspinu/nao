ga-proxy-server installation
----

0. follow "configure a developer project and account settings" and "register a device model" from here - https://developers.google.com/assistant/sdk/guides/service/python/embed/config-dev-project-and-account

0.a. copy the credentials json file (step "Download credentials") over ./client_credentials.json

1. install docker and docker compose

2. run "docker-compose build"

3. run "docker-compose up -d"

AUTHORIZATION (only one time)

4. run "docker exec -it ga_proxy_server bash" to get in the container

5. run "./generate_credentials.sh"

6. access the link in browser and follow the wizard

7. copy paste the authorization code in the container prompt

8. your auth data is now saved in /root/.config/google-oauthlib-tool/credentials.json (in the container); this container path is persisted on the local machine volume (see docker-compose.yml), so next time you don't have to do these steps, the file will be there.

//END AUTHORIZATION

