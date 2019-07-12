#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --save --headless --client-secrets /client_credentials.json