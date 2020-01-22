# This is a base Image which install new relic agent for java and splunk universal forwarder inside the container.

# -- Base -- #
FROM openjdk:11-jre-slim as base

LABEL maintainer="ViniciusRocha"
LABEL application="BaseImage"

# -- Requirements -- #
RUN apt-get update && apt-get install -y \
    curl \
    procps

# -- New Relic Agent Installation -- #
WORKDIR /opt/newrelic
RUN curl -O "http://download.newrelic.com/newrelic/java-agent/newrelic-agent/current/newrelic-java.zip"
RUN ["apt-get", "install", "unzip"]
RUN ["unzip", "newrelic-java.zip", "-d", "/opt"]
# -- New Relic Agent Installation -- #

# -- Splunk Universal Forwarder Agent 7.3.2 Installation -- #
WORKDIR /opt
RUN curl -O https://flintapp-bucket-resources.s3.amazonaws.com/splunkforwarder-7.3.2-c60db69f8e32-Linux-x86_64.tgz
RUN tar xvzf splunkforwarder-7.3.2-c60db69f8e32-Linux-x86_64.tgz
# download config files
WORKDIR /opt/splunkforwarder/etc/system/local
# NEED TO CHANGE THIS
RUN curl -O https://ienoh3theixas3ga0iephi9vopeiw3chitaip5heehoyoowiemae2achoo8chai.s3.amazonaws.com/binaries/outputs.conf
RUN curl -O https://ienoh3theixas3ga0iephi9vopeiw3chitaip5heehoyoowiemae2achoo8chai.s3.amazonaws.com/binaries/user-seed.conf
# -- Splunk Universal Forwarder Agent 7.3.2 Installation -- #

# FOR AWS EC2 INSTANCES
