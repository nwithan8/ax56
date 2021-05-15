# A Python client for A(x56)'s URL lengthener
[![PyPi](https://static.pepy.tech/personalized-badge/ax56?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pypi.org/project/ax56)
[![License](https://img.shields.io/pypi/l/ax56?color=orange&style=flat-square)](https://github.com/nwithan8/ax56/blob/master/LICENSE)

[![Open Issues](https://img.shields.io/github/issues-raw/nwithan8/ax56?color=gold&style=flat-square)](https://github.com/nwithan8/ax56/issues?q=is%3Aopen+is%3Aissue)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/nwithan8/ax56?color=black&style=flat-square)](https://github.com/nwithan8/ax56/issues?q=is%3Aissue+is%3Aclosed)
[![Latest Release](https://img.shields.io/github/v/release/nwithan8/ax56?color=red&label=latest%20release&logo=github&style=flat-square)](https://github.com/nwithan8/ax56/releases)

[![Discord](https://img.shields.io/discord/472537215457689601?color=blue&logo=discord&style=flat-square)](https://discord.gg/7jGbCJQ)
[![Twitter](https://img.shields.io/twitter/follow/nwithan8?label=%40nwithan8&logo=twitter&style=flat-square)](https://twitter.com/nwithan8)

Interact with A(x56)'s URL lengthener in Python

# Installation
From PyPi: ``python -m pip install ax56``

From GitHub ``python -m pip install git+https://github.com/nwithan8/ax56.git``

# Usage
Can get a lengthened URL for any input URL

Import the ``ax56`` package
Example:

```python
import ax56

link = ax56.link("https://google.com")
```