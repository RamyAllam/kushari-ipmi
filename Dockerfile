FROM python:2
# ARGS
ARG SSH_PRIVATE_KEY
ARG PROJECT_DIR

RUN mkdir ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

# SSH Key
RUN mkdir /root/.ssh/ && echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa  && chmod 600 /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

# Clone
RUN git clone git@github.com:RamyAllam/kushari-ipmi.git

# Run
WORKDIR ${PROJECT_DIR}/kushari-ipmi

RUN apt-get update && \
    apt-get -y install python-dev && \
    virtualenv -p /usr/bin/python2 venv && \
    /bin/bash -c "source venv/bin/activate && venv/bin/pip install -r requirements.txt"

EXPOSE 8001

CMD ["venv/bin/python2", "manage.py", "runserver", "0.0.0.0:8001"]
