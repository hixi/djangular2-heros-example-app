#!/bin/bash
cd compass-frontend

# Change these wto lines to use whatever you need to build your angular2 app
rm -rf dist
ng build -prod


docker-compose build
