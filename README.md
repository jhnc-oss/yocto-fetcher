# Yocto Fetcher

[![CI](https://github.com/jhnc-oss/yocto-fetcher/workflows/ci/badge.svg)](https://github.com/jhnc-oss/yocto-fetcher/actions)
[![GitHub release](https://img.shields.io/github/release/jhnc-oss/yocto-fetcher.svg)](https://github.com/jhnc-oss/yocto-fetcher/releases)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
![Python 3.8](https://img.shields.io/badge/python-3.9-green.svg)

Standalone tool which fetches upstream source repositories to Yocto Bitbake compatible source archives.


# Usage

`yoctofetcher --help` shows all arguments.

```bash
# Creates a source tarball of the given repository in the current directory
$ yoctofetcher https://github.com/jhnc-oss/yocto-fetcher.git
```
