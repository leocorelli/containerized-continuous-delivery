# containerized-continuous-delivery
## IDS 721, Project 2

[![Python application test with Github Actions](https://github.com/leocorelli/containerized-continuous-delivery/actions/workflows/main.yml/badge.svg)](https://github.com/leocorelli/containerized-continuous-delivery/actions/workflows/main.yml)

[Click here to go to website](https://kdwbwy6hmu.us-east-1.awsapprunner.com/)

Hi there! This is my Duke IDS 721 individual project 2. In this project, I have built a containerized web microservice that automatically deploys to AWS App Runner. Every time a new container image is pushed to my AWS ECR repository, App Runner automatically deploys the newest version. 

## What the microservice does

**My microservice returns a list of the first n square numbers, where n is obtained from user input. In order to use this microservice, please add "/squares/{n}" to the url, where n is an integer. For example: if you want to see the first 7 square numbers, then you would add "/squares/7" to the URL of the website.**

## How I did it
1. Build web microservice logic with a function and FastAPI
2. Test both the logic (test_logic.py) and the functionality of my web app (test_app.py)
3. Set up GitHub actions to do continuous integration of my code on GitHub (lint, format, and test)
4. Locally containerize my microservice using docker
5. Authenticate to AWS from command line, and push container image to AWS ECR
6. Set up App Runner to automatically deploy from latest container image in my AWS ECR repository
