# README
### Setup
To clone this repository, run:

`$ git clone https://github.com/jmarsto/kapost-challenge.git`

cd into the repository:

`$ cd kapost-challenge`

### In action
Manipulate the ENTRYPOINT in Dockerfile to reflect the bucket names and threshold desired

Run the following to generate the Docker image:

```no-highlight
$ docker build .
```

Run the container:

```no-highlight
docker run -e AWS_ACCESS_KEY_ID=<your_aws_access_key> \
-e AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key> \
<docker_image_id>
```
