FROM debian:latest
WORKDIR /api
EXPOSE 5000
# install chromium
RUN apt update
RUN apt -y -q install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y -q install ./google-chrome-stable_current_amd64.deb
RUN rm ./google-chrome-stable_current_amd64.deb
RUN apt -y -q install chromium-driver
RUN export PATH=$PATH:/usr/lib/chromium-browser/
# copy files
COPY ./getXIdToken.py ./getXIdToken.py
COPY ./main.py ./main.py
COPY ./requirements.txt ./requirements.txt
# install python and python lib
RUN apt -y -q install python3 pip
RUN pip install --break-system-packages -r ./requirements.txt

CMD "python3" "main.py"