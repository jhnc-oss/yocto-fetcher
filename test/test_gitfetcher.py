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
import unittest
from unittest.mock import MagicMock, patch

from yocto_fetcher.gitfetcher import GitFetcher


class TestGitFetcher(unittest.TestCase):
    def test_project_name_is_split_from_url(self):
        self.assertEqual(
            "projA",
            GitFetcher("https://gitrepo.com/ab/projA", MagicMock()).project_name,
        )
        self.assertEqual(
            "projB",
            GitFetcher("https://gitrepo.com/ab/projB", MagicMock()).project_name,
        )

    def test_project_name_throws_if_no_match_found(self):
        with self.assertRaises(ValueError):
            GitFetcher("https://gitrepo.url_ab", MagicMock())

    def test_dest_file_name(self):
        self.assertEqual(
            "git2_gitrepo.org.xyz.proj0.git.tar.gz",
            GitFetcher("https://gitrepo.org/xyz/proj0.git", MagicMock()).dest_filename,
        )
        self.assertEqual(
            "git2_gitrepo.org.x.y_z.p_r.o.j.0.git.tar.gz",
            GitFetcher(
                "https://gitrepo.org/x:y z/p r/o/j*0.git", MagicMock()
            ).dest_filename,
        )

    @patch("subprocess.check_call", autospec=True)
    def test_fetch_clones_to_path(self, mock_call):
        workdir = MagicMock()
        fetcher = GitFetcher("https://x.y/a/bc", workdir)
        fetcher.fetch()
        mock_call.assert_called_once_with(
            ["git", "clone", "--bare", "--mirror", "https://x.y/a/bc", "bc"],
            cwd=workdir,
        )

    @patch("subprocess.check_call", autospec=True)
    @patch(
        "subprocess.check_output",
        autospec=True,
        return_value="Tue, 20 Jun 2023 11:22:33 +0000",
    )
    def test_pack_creates_targz(self, mock_mtime, mock_call):
        workdir = MagicMock()
        fetcher = GitFetcher("https://x.y/a/proj-x", workdir)

        fetcher.pack("dest/dir")

        mock_mtime.assert_called_once_with(
            ["git", "log", "--all", "-1", "--format=%cD"],
            cwd=os.path.join(workdir, "proj-x"),
        )
        # pylint: disable=duplicate-code
        mock_call.assert_called_once_with(
            [
                "tar",
                "-czf",
                os.path.join("dest/dir", "git2_x.y.a.proj-x.tar.gz"),
                "--owner",
                "oe:0",
                "--group",
                "oe:0",
                "--mtime",
                "Tue, 20 Jun 2023 11:22:33 +0000",
                ".",
            ],
            cwd=os.path.join(workdir, "proj-x"),
        )
