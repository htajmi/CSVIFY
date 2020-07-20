# CSVIFY

## Overview
CSVIFY is a web-based tool to convert excel file to csv.

![img](/assets/csvify.png)
## Deployment
TO run the tool, cd to CSVIFY directory and install the dependencies with 

`poetry install`

run 

`poetry run python csvify.py`

If you do not have poetry installed you can follow: 

`https://python-poetry.org/docs/#installation`

Alternatively, you can build and run a docker image:

`docker build -t csvify-image .`

`docker run -p 7070:7070 csvify-image`


Open a browser and navigate to 

`localhost:7070`