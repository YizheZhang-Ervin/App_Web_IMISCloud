FROM python:3.7

# create dir
RUN mkdir /imis 

# work dir
WORKDIR /imis

# add current dir to work dir
ADD . /imis
RUN pip3 install -r requirements.txt
# out port 
EXPOSE 80 8080 8000 5000
# env variable
ENV SPIDER=/imis