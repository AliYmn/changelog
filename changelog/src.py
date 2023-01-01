import subprocess
import os
import sys
import pathlib

"""Generates git changelog for Conventional Commits"""


class ChangeLogs():
    def __init__(self, url):
        self.url = url

    def run_commands(self, command: str) -> complex:
        result = subprocess.Popen(
            f"{command}", stdout=subprocess.PIPE, shell=True)
        data = str(result.communicate()[0].decode('utf-8')).split()
        return data

    def run_commits(self, command: str) -> complex:
        result = subprocess.Popen(
            f"{command}", stdout=subprocess.PIPE, shell=True)
        data = str(result.communicate()[0].decode('utf-8'))
        return data

    def commits_to_emoji(self, commits_message: str):
        commits = {"feat": "✅", "fix": "🚀", "build": "💚", "chore": "🚀", "docs": "📝",
                   "style": "🎨", "refactor": "👷", "perf": "⚡️", "test": "🧪", "merge": "🎉", "revert": "⏪️"}

        return commits[commits_message]

    def replace_commits(self, commit):
        return commit.replace("fix:", f"{self.commits_to_emoji('fix')} fix:")\
                     .replace("feat:", f"{self.commits_to_emoji('feat')} feat:")\
                     .replace("build:", f"{self.commits_to_emoji('build')} build:")\
                     .replace("chore:", f"{self.commits_to_emoji('chore')} chore:")\
                     .replace("docs:", f"{self.commits_to_emoji('docs')} docs:")\
                     .replace("style:", f"{self.commits_to_emoji('style')} style:")\
                     .replace("refactor:", f"{self.commits_to_emoji('refactor')} refactor:")\
                     .replace("perf:", f"{self.commits_to_emoji('perf')} perf:")\
                     .replace("test:", f"{self.commits_to_emoji('test')} test:")\
                     .replace("merge:", f"{self.commits_to_emoji('merge')} merge:")\
                     .replace("revert:", f"{self.commits_to_emoji('revert')} revert:")\


    def getLogs(self):
        if os.path.exists("changelog.md"):
            os.remove("changelog.md")
        path = pathlib.Path().resolve()
        try:
            all_tags = self.run_commands("git tag --sort=-creatordate")
            previous_tag = all_tags[1]
        except:
            text = "tags system is not active in your repository."
            print('\033[91m' + 'result: ' + '\033[92m', text)
            exit()
        for tag in all_tags:
            tags_date = self.run_commands(
                f"git log -1 --pretty=format:'%ad' --date=short {previous_tag} {path}")
            title = f"## {previous_tag} -- {tags_date[0]}"
            commit = self.run_commits(
                f"git log {tag}...{previous_tag} --pretty=format:'* %s [View]({self.url}%H)' --reverse {path} | grep -v Merge")
            with open('changelog.md', 'a') as f:
                f.write(title)
                f.write("\n")
                f.write(self.replace_commits(commit))
            previous_tag = tag
        f.close()
        text = "changelogs.md created successfully."
        print('\033[91m'+'result: ' + '\033[92m', text)


def main():
    if (len(sys.argv)) > 1:
        url = str(sys.argv[1])
        logs = ChangeLogs(url)
        logs.getLogs()
    else:
        print("Please write commit link : changelogs link")
