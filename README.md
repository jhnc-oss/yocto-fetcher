# Yocto Fetcher

[![CI](https://github.com/jhnc-oss/yocto-fetcher/workflows/ci/badge.svg)](https://github.com/jhnc-oss/yocto-fetcher/actions)
[![GitHub release](https://img.shields.io/github/release/jhnc-oss/yocto-fetcher.svg)](https://github.com/jhnc-oss/yocto-fetcher/releases)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
![Python 3.8](https://img.shields.io/badge/python-3.10-green.svg)

Standalone tool which fetches upstream source repositories to Yocto Bitbake compatible source archives.


## Usage

`yoctofetcher --help` shows all arguments.

```bash
# Creates a source tarball of the given repository in the current directory
$ yoctofetcher https://github.com/jhnc-oss/yocto-fetcher.git
```

## Setup

Installation and update of this package using a Python package manager is recommended (ie. [pip](https://pip.pypa.io/en/stable/), [pipx](https://pipx.pypa.io/stable/)).
Please refer to the package manager documentation for detailed instructions.

**Remote installation:**

```bash
# pip
pip install git+https://github.com/jhnc-oss/yocto-fetcher.git

# pipx
pipx install git+https://github.com/jhnc-oss/yocto-fetcher.git
```
Append `@<Tag>` to install a specific [release](https://github.com/jhnc-oss/yocto-fetcher/releases) (ie. `…/yocto-fetcher.git@v0.0.8`).

**Local installation:**

Clone this repository and run install in it:

```bash
# pip
pip install .

# pipx
pipx install .
```

