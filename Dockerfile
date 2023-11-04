# Set Ubuntu latest image
FROM ubuntu:latest

# Update apt
RUN apt-get update

# Install libraries needed
RUN apt-get install -y python3 python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create app directory
RUN mkdir -p /home/doc-bd-a1

# Set working directory
WORKDIR /home/doc-bd-a1

# Copy dataset to docker
COPY data.csv .
COPY load.py .
COPY dpre.py .
COPY eda.py .
COPY vis.py .
COPY model.py .

