# simple_crm

Based off this article for [Hello World](https://www.slingacademy.com/article/write-your-first-backend-api-with-fastapi-hello-world/)

Also based off this article for [using postgresql database](https://mattermost.com/blog/building-a-crud-fastapi-app-with-sqlalchemy/) and [the repo on Github](https://github.com/EzzEddin/fastapi-todo)


python3 -m venv env

pip install fastapi uvicorn 

pip install sqlalchemy

uvicorn main:app --reload



# Setup data

This is part of the [simple_crm_test_data repo](https://github.com/rowlandm/simple_crm_test_data).

git clone git@github.com:rowlandm/simple_crm.git

cd simple_crm

mkdir data

git clone git@github.com:rowlandm/simple_crm_test_data.git data

This should put data_simple_crm.db under the simple_crm/data directory
