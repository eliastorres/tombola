# Tombola

*La Vida Es Una Tombola*

Tombola is a small web application prototype written in Python that simulates
a raffle.

To simulate a raffle, a dictionary is randomly shuffled and then words are
served until exhausted. Then the dictionary is randomly shuffled again and
the process repeats.

A new shuffle can be forced with the `/shuffle` endpoint.


## Deployment

```
docker run --detach --publish=8000:8000 kuralabs/tombola:latest
```

To create your own words dictionary create a file `words.txt` with one word(s)
to show per line. For example:

```
hello world
good bye
my friend
```

Then, mount it to the container as follows:

```
docker run --volume /path/to/mywords.txt:/src/words.txt --detach --publish=8000:8000 kuralabs/tombola:latest
```

By default the `/shuffle` endpoint is unprotected. To setup a secret set the
`SHUFFLE_SECRET` environment variable. For example:

```
docker run --env SHUFFLE_SECRET=mysupersecret --volume /path/to/mywords.txt:/src/words.txt --detach --publish=8000:8000 kuralabs/tombola:latest
```

If set, the endpoint needs to be called with:

```
/shuffle?secret=mysupersecret
```

The application will answer with a happy emoji if the shuffle succeeded
(and HTTP code 200 OK), or a skeptical face with raised eyebrow
(and HTTP code 401 Unauthorized) if the secret mismatched.


## Development

A Python environment with [Tox](https://tox.readthedocs.io/) is required.

To run the application in development mode:

```
tox
```

The application will be available in `http://localhost:8000/`

Optionally, the Docker image can be built with:

```
tox -e build
```


## License

```
Copyright (C) 2020 KuraLabs S.R.L

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
```