FROM ubuntu:18.04
RUN apt-get update && apt-get install -y iputils-ping curl dnsutils telnet python3 net-tools && apt-get clean
WORKDIR /opt
COPY python-server-multi.py .
EXPOSE 8088 8087
CMD python3 /opt/python-server-multi.py