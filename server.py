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

from pathlib import Path
from random import shuffle
from string import Template

from starlette.routing import Route
from starlette.responses import HTMLResponse
from starlette.applications import Starlette
from starlette.exceptions import HTTPException


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

#word {
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
    <span id="word">$word</span>
  </body>
</html>
""")

WORDS = None
ITERATOR = None


async def tombola(request):
    global ITERATOR

    if WORDS is None:
        raise HTTPException(400)

    try:
        word = next(ITERATOR)
    except StopIteration:
        shuffle(WORDS)
        ITERATOR = iter(WORDS)
        word = next(ITERATOR)

    return HTMLResponse(RESPONSE_TPL.substitute(word=word))


def on_load():
    global WORDS
    global ITERATOR

    WORDS = [
        line.title() for line in (
            rawline.strip() for rawline in
            Path('words.txt').read_text(encoding='utf-8').strip().splitlines()
        ) if line
    ]
    ITERATOR = iter(WORDS)


routes = [
    Route('/', tombola),
]

app = Starlette(
    routes=routes,
    on_startup=[on_load],
)
