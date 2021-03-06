# Purpose
The filepaths module is designed to ease file path navigation in python scripts. It is particularly useful for iterating through many files in a directory.

# Use

## Installation
```python
pip install filepaths
```

## Example
```python
from filepaths import Root


paths = Root(__file__).paths()

for csv in paths.data.filepaths:
    pd.read_csv(csv)
```
## Options
    file=None: for default behavior pass in __file__
    depth=0: how many levels up up from __file__ to start the walk down
    ignore_hidden=True: whether or not to include hidden files/paths
    alt_path=False: if desired, specify an absolute path to another directory instead of file=__file__

# Description
The Root object stores information to build the strings for the desired directories and paths. The `paths()` method returns a nested [addict dictionary](https://github.com/mewwts/addict) of files, directories, absolute paths to the files and directories. This dictionary inherits the standard dictionary class; it can be accessed with either `root[data][files]` or `root.data.files`. The keys of the dictionary are the names of the directories below the root directory, as well as `['files', 'dirs', 'path', filepaths']`. 

The keys `'files', 'dirs', 'path',` and `'filepaths'` are reserved for the dictionary: if there are directories with these names in any of the children directories, an error will be thrown.

The values to the mentioned keys are as follows:
* `root.example.path` returns the absolute path to the `example/` as a string.
* `root.example.dirs` returns a list of the child directories in `example/`.
* `root.example.files` returns a list of the filenames, as strings, for every file in `example/`.
* `root.example.filepaths` returns a list of the absolute paths, as strings, to every file in `example/`.

If needed, `paths()` can be called again to return an updated dictionary from the same Root().
