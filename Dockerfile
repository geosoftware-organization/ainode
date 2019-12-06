FROM python:3.6

# Set python output straight to the terminal
ENV PYTHONUNBUFFERED 1

# Creating the root directory of the project
RUN mkdir /ainode

# Set the working directory
WORKDIR /ainode

# Copy the current content to working directory
ADD . /ainode/

# Install all the needed packages specified in requirements.txt
RUN pip install -r requirements.txt
