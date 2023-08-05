# YouTube metadata downloader and video converter

FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.
The project aims to do the following:
- Receive a url of a YouTube video.
- Fetch and present video metadata.

## Start this project

The web service runs inside a Docker container. 
Before building the container, it is necessary to configure the `.env` file with the required environment variable values.

When the environment file is ready, run the commands below.

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

## Fetch video data

The service communicates with the YouTube API in order to fetch data related to a video specified by the user.
In order to access

See the docs in: [http://localhost:8000/docs](http://localhost:8000/docs)

Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)