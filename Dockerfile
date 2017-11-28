FROM centos:7

RUN yum install -y epel-release \
    && yum update -y \
    && yum install -y \
            gcc \
            git \
            openssh-clients \
            bind-utils \
            expect \
            python-pip \
    && yum clean all

RUN pip install selenium
RUN pip install selene
RUN pip install behave

RUN pip install git+https://github.com/yashaka/selene.git

# Исходники проекта
ADD . /root/

WORKDIR /root

CMD ["unbuffer", "behave"]
