# wordcloud-streamlit

## Requirements

1. [Streamlit](https://docs.streamlit.io/)
2. [Wordcloud](https://amueller.github.io/word_cloud/)


## Usage

Note:
Requires prior installation of Docker engine.

Clone this repository

```
DOCKER_BUILDKIT=1 docker build --no-cache -t wordcloud-streamlit .
```

Start the docker container

```
docker run --rm --name wordcloud -p 8501:8501 wordcloud-streamlit
```

Open browser and visit URL

```
URL: http://localhost:8501
```