# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 KuraLabs S.R.L
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
La Vida Es Una Tombola : Web Application Prototype
"""

from os import environ
from pathlib import Path
from random import shuffle
from string import Template
from itertools import cycle

from starlette.routing import Route
from starlette.responses import HTMLResponse
from starlette.applications import Starlette


RESPONSE_TPL = Template("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="La Vida Es Una Tombola" />
    <link
        href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap"
        rel="stylesheet"
    >
    <title>Tombola</title>

    <style>

#message {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  font-family: 'Roboto', sans-serif;
  font-size: 5em;
}

    </style>
  </head>

  <body>
    <span id="message">$message</span>
  </body>
</html>
""")

WORDS = None
ITERATOR = None
SUCCESS = cycle([
    '&#x1F60B',
    '&#x1F61B',
    '&#x1F61C',
    '&#x1F92A',
    '&#x1F61D',
])


def do_shuffle():
    shuffle(WORDS)
    global ITERATOR
    ITERATOR = iter(WORDS)


async def endpoint_shuffle(request):

    # Check secret
    secret = request.query_params.get('secret', '')
    if secret != environ.get('SHUFFLE_SECRET', ''):
        return HTMLResponse(
            RESPONSE_TPL.substitute(message='&#x1F928'),
            status_code=401,
        )

    do_shuffle()
    return HTMLResponse(
        RESPONSE_TPL.substitute(message=next(SUCCESS))
    )


async def endpoint_tombola(request):
    try:
        word = next(ITERATOR)
    except StopIteration:
        do_shuffle()
        word = next(ITERATOR)

    return HTMLResponse(
        RESPONSE_TPL.substitute(message=word)
    )


def on_load():
    global WORDS

    WORDS = [
        line.title() for line in (
            rawline.strip() for rawline in
            Path('words.txt').read_text(encoding='utf-8').strip().splitlines()
        ) if line
    ]
    do_shuffle()


routes = [
    Route('/', endpoint_tombola),
    Route('/shuffle', endpoint_shuffle),
]

app = Starlette(
    routes=routes,
    on_startup=[on_load],
)
