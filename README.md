# TweeterStreamConsumer

FastApi service with Oauth0

## Proposed Solutuion ##

With Docker

Requirements:

    Installed
            Docker
            docker compose

    Twitter consumer keys
            consumer key
            consumer Secret

    Clone repo

        git clone https://github.com/Sytac-DevCase/Python-bigintelligence.git

    In docker-compose file add the twitter keys:
            TWITTER_CONSUMER_KEY
            TWITTER_CONSUMER_SECRET

    Execute command

        docker-compose up --build

## Pytest ##

Run test with pytest

Requirements:

    Installed
            python 3.9

    Twitter consumer keys
            consumer key
            consumer Secret

    Clone repo

        git clone https://github.com/Sytac-DevCase/Python-bigintelligence.git

    Add the following vars on local env vars:
            TWITTER_CONSUMER_KEY
            TWITTER_CONSUMER_SECRET

    Execute command on project root directory

        pytest

## Process Flow ##

On  "bot flow.pdf" file you will find the Proposed process flow with Twitter pin authentication
and generating the report as a JSON
