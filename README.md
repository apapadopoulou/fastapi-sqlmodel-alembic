# YouTube metadata downloader and video converter

FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.
The project aims to do the following:
- Receive a url of a YouTube video.
- Fetch and present video metadata.
- Download the video file in an `.mp4` format.
- Convert the `.mp4` to and `.mp3` audio file.
- Perform song recognition uding ShazamIO.
- Obtain urls of the recognized song in other media and export all metadata into a CSV file.

## Start this project

The web service runs inside a Docker container. 
Before building the container, it is necessary to configure the `.env` file with the required environment variable values.
Currently, the only required environment variable is the YouTube API key, which can be generated following [these](https://developers.google.com/youtube/v3/getting-started) instructions.

When the environment file is completed, run the commands below.

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)

## Fetch video data

The service communicates with the YouTube API in order to fetch data related to a video specified by the user.
Currently, the service fetches metadata related to the video title, the video views and the publication date.
To fetch the data, use the address 

` http://localhost:8004/video?url={YOUTUBE_URL} `

where `YOUTUBE_URL` is the url of the requested video.

## Download video file and convert to audio

The video file is automatically downoladed using the `pytube` library. 
Then, the video file is converted to audio using the `pydub` library.
Both files are saved in the `files` folder which is automatically created in the `project` directory.

## Recognize audio track

Using the `shazamio` library, we can use the audio file to recognize the recorded track. 
For the purpose of this project, we obtain metadata related to the identification of the track in other media platforms,
namely Apple Music and Spotify.
These details are also displayed when fetching the video details.

## Export metadata to CSV

The video and audio metadata are exported into a csv file. The file is also stored in the
automatically created `files` folder in the `project` directory.

## Example

By requesting [http://localhost:8004/video?url=https://www.youtube.com/watch?v=EWeIWVGPibc](http://localhost:8004/video?url=https://www.youtube.com/watch?v=EWeIWVGPibc)
we view data related to the YouTube video of the song *Starry Night* and the track presence on other media platforms.
Furthermore, the files `Starry Night.mp4`, `Starry Night.mp3` and `Starry Night.csv` are created in the `project/files` directory.