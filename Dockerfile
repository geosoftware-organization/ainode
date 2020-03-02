FROM python:3.6

# Set python output straight to the terminal
ENV PYTHONUNBUFFERED 1
# Set python NOT to write *.pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Creating the root directory of the project
RUN mkdir /ainode

# Set the working directory
WORKDIR /ainode

# install psycopg2 dependencies
# RUN apk update \
#     && apk add bash && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /ainode/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /ainode/

# run healty check of the database
ENTRYPOINT ["/ainode/entrypoint.sh"]

# # Copy the current content to working directory
# ADD . /ainode/

# COPY init.sql /docker-entrypoint-initdb.d/


