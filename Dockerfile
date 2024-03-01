FROM python:3-slim

# Set the working directory
WORKDIR /usr/src/python

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/search
COPY . .

CMD [ "python", "./welcome.py" ]