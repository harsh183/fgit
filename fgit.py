#!python3

from plumbum import cli 
from pyfiglet import Figlet
from plumbum.cmd import ls, git
from questionary import checkbox
from rich.progress import Progress
from rich import print as rprint

import time

def print_banner(text: str):
    print(Figlet(font='slant').renderText(text))

def get_files():
    ls_output = ls().strip()
    files = ls_output.split("\n")
    return files

def display_push_progress():
    # Note: Actually getting progress from git is surprisingly non-trivial
    # So I've hard coded an example for now, but in real code, emit things as they happen
    with Progress() as progress:
        push_progress = progress.add_task("Pushing files :partying_face:")

        for i in range(100):
            progress.update(push_progress, advance=1)
            time.sleep(0.05)

class FancyGitAdd(cli.Application):
    VERSION = "1.3"
    commit = cli.Flag(['c', 'commit'], help="Commits the added files")
    push = cli.Flag(['p', 'push'], help="Pushes the added files")
    def main(self):
        print_banner("Git Fancy add")

        files = get_files()

        selected_files = checkbox("Select a file", choices=files).ask()
        git('add', selected_files)
        rprint("The files were [bold]added[/bold].")

        if self.commit:
            git('commit', '-m', 'updates')
            rprint("Files successfully added to [green]commit![/]")

        if self.push:
            git('push')
            display_push_progress()

if __name__ == "__main__":
    FancyGitAdd()