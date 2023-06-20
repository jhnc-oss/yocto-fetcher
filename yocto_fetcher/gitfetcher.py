# MIT License
#
# Copyright (c) 2023 jhnc-oss
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

import os
import subprocess
from urllib.parse import urlparse


class GitFetcher:

    def __init__(self, repo_url, workdir):
        self.repo_url = repo_url
        self.workdir = workdir
        url = urlparse(repo_url)
        self.project_name = os.path.basename(url.path)

        if not self.project_name:
            raise ValueError(f"Invalid url: {repo_url}")

        path_escaped = url.path.replace("/", ".").replace("*", ".").replace(
            ":", ".").replace(" ", "_")
        self.dest_filename = f"git2_{url.netloc}{path_escaped}.tar.gz"

    def fetch(self):
        subprocess.check_call([
            "git", "clone", "--bare", "--mirror", self.repo_url,
            self.project_name
        ],
                              cwd=self.workdir)

    def pack(self, dest_dir):
        subprocess.check_call([
            "tar", "-czf",
            os.path.join(dest_dir, self.dest_filename), "--owner", "oe:0",
            "--group", "oe:0", "--mtime",
            self.__query_mtime(), "."
        ],
                              cwd=os.path.join(self.workdir,
                                               self.project_name))

    def __query_mtime(self):
        return subprocess.check_output(
            ["git", "log", "--all", "-1", "--format=%cD"],
            cwd=os.path.join(self.workdir, self.project_name))
