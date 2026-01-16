# MIT License
#
# Copyright (c) 2023-2026 jhnc-oss
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import os
import tempfile

from yocto_fetcher.gitfetcher import GitFetcher
from yocto_fetcher.version import __version__


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="yocto-fetcher",
        description="Create Yocto Bitbake compatible source tarballs",
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Shows the program version",
    )
    parser.add_argument("source", help="Upstream source repository URL")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    with tempfile.TemporaryDirectory(prefix="yoctofetcher") as temp_dir:
        fetcher = GitFetcher(args.source, temp_dir)
        fetcher.fetch()
        fetcher.pack(os.getcwd())


if __name__ == "__main__":
    main()
