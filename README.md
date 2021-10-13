# fgit: Fancy Git Client 

Command lne git client with fancy interface features! Note this is an example project just to demonstrate the wide variety of command line interface building libraries that python has available.

Based off a [tutorial workshop](https://125summer.tech/cli) I did in Summer 2021 as part of UIUC Summer of Side Projects.

## Install

After cloning the repository

1. Have a recent version of `python3` and `pip` installed. 

2. Install from the requirements file
   ```bash 
   $ pip install -r requirements.txt
   ```

## Run

Use `python3` to just run it once the dependencies are setup. 

```bash
$ python fgit.py [OPTIONS]
```

If you like, you can make it an executable, add it to your path and indicate the language with a #! hash-bang to make the initial start command smaller.*

### Options 

* `-h`/`--help` - Get help text
* `-v`/`--version` - Get version 
* `-c`/`--commit` - Commit files after adding
* `-p`/`--push` - Push files at the end 
