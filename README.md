# tweeter

Parameters supported (hashtag, author/username, text)


Runs with `docker-compose up -d --build`

First must make an env file called twitter.env and set the appropriate env variables in it:

- ACCESS_TOKEN=your_token
- ACCESS_SECRET=your_token
- CONSUMER_TOKEN=your_token
- CONSUMER_SECRET=your_token

then you can start the stream after running `docker-compose up -d --build` by finding the name of your container and running 

`docker exec -it your_container_name bash`.  After getting into the container simply run `python manag.py startstream`
