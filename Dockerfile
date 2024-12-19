FROM python:3.12-slim
WORKDIR /api
EXPOSE 5000
# install chromium
# RUN apt update
# RUN apt -y -q install wget
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN apt -y -q install ./google-chrome-stable_current_amd64.deb
# RUN rm ./google-chrome-stable_current_amd64.deb
# RUN apt -y -q install chromium-driver
# RUN export PATH=$PATH:/usr/lib/chromium-browser/

RUN apt update && apt -y install wget unzip gnupg \
    && wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    # && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    # && apt update && apt -y install google-chrome-stable \
    && apt -y install chromium-driver \
    && apt clean

# copy files
COPY ./getXIdToken.py ./getXIdToken.py
COPY ./main.py ./main.py
COPY ./requirements.txt ./requirements.txt
# install python and python lib
RUN pip install --no-cache-dir --break-system-packages -r ./requirements.txt

CMD "python3" "main.py"