## here we say to docker with the version we want to start
FROM python:3.10

## we create a directory with this name
WORKDIR /app

## we copy the file with dependencies as a good practice
## left is local and right is the container
COPY requirements.txt /app/requirements.txt

##In this environment install all dependencies from our file after -r 
## We say that do not apply cache
## if there is an upgrade do it with --upgrade
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#We make a last copy to copy everything and put it in app
COPY . /app


# we create a comand to keep the container on 
CMD bash -c "while true; do sleep 1; done"