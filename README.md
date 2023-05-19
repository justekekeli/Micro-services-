# OpenAI_bot_for_Name_Meaning_And_Translation

 ## Goals
 I wanted to create 2 micro-services that use the OpenAI model 'text-davinci-003' to :

- Give the meaning of a name
- Give a synonym name in another language

## Used Tools :
- OpenAI library
- FastAPI

## Installation

1. Clone the repository
1. Create a virtualenv : `virtualenv ~/.env && source ~/.env/bin/activate`
1. set an environment variable name `OPENAI` which will have your OpenAI API Keys
1. install : make all
1. Run the main file : python main.py
1. Test the microservices on 127.0.0.1:8080/docs 

## References :
I made it possible thanks to Noahgift [project](https://github.com/noahgift/fastapi)

