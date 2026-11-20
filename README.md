# Yocto Fetcher

[![CI](https://github.com/jhnc-oss/yocto-fetcher/workflows/ci/badge.svg)](https://github.com/jhnc-oss/yocto-fetcher/actions)
[![GitHub release](https://img.shields.io/github/release/jhnc-oss/yocto-fetcher.svg)](https://github.com/jhnc-oss/yocto-fetcher/releases)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
![Python 3.10](https://img.shields.io/badge/python-3.10-green.svg)

Standalone tool which fetches upstream source repositories into Yocto BitBake-compatible source archives.

## Requirements

- Python 3.10+
- `git`
- GNU `tar` (the tool relies on `--owner`, `--group`, and `--mtime`)

## Usage

`yoctofetcher --help` shows all arguments.

```bash
# Creates a source tarball of the given repository in the current directory
$ yoctofetcher https://github.com/jhnc-oss/yocto-fetcher.git
```

## Supported URLs

Repository URLs such as `https://…` and `ssh://…` are supported. `git://`
and BitBake's `gitsm://` URLs are rewritten to `https://` before cloning.

## Setup

Installing or updating this package with a Python package manager is recommended (e.g. [pip](https://pip.pypa.io/en/stable/), [pipx](https://pipx.pypa.io/stable/)).
Please refer to the package manager documentation for detailed instructions.

**Remote installation:**

```bash
# pip
pip install git+https://github.com/jhnc-oss/yocto-fetcher.git

# pipx
pipx install git+https://github.com/jhnc-oss/yocto-fetcher.git
```

Append `@<Tag>` to the URL to install a specific [release](https://github.com/jhnc-oss/yocto-fetcher/releases) (e.g. `…/yocto-fetcher.git@vX.Y.Z`).

**Local installation:**

Clone this repository and install from it:

```bash
# pip
pip install .

# pipx
pipx install .
```

