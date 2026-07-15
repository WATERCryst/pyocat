# BIOCAT Python Client Library

[![Test Python Package][releases-shield]][releases]
[![PyPI version][pypi-shield]][pypi]
[![PyPI License][license-shield]][license]


## About

A Python client library to connect to BIOCAT devices.


## Installation

```bash
pip install pyocat
```

## Usage

```python
import asyncio
import httpx

from pyocat import AsyncAuth, AsyncApiClient

async def main():
    async with httpx.AsyncClient() as client:
        auth = AsyncAuth(client, "<api-key>")
        api = AsyncApiClient(auth)
        state = await api.get_state()
        print(state)

if __name__ == "__main__":
    asyncio.run(main())
```

## Development

Execute to download dependencies:

```bash
poetry install
```

Execute to run the unit tests:

```bash
poetry run pytest
```

Execute to build the library:

```bash
poetry build
```

## License

MIT License

Copyright (c) 2026 WATERCryst GmbH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[releases-shield]: https://github.com/WATERCryst/pyocat/actions/workflows/push.pipeline.yml/badge.svg?branch=main
[releases]: https://github.com/WATERCryst/pyocat/actions/workflows/push.pipeline.yml
[pypi-shield]: https://img.shields.io/pypi/v/pyocat
[pypi]: https://pypi.org/project/pyocat
[license-shield]: https://img.shields.io/pypi/l/pyocat
[license]: https://raw.githubusercontent.com/WATERCryst/pyocat/refs/heads/main/LICENSE
