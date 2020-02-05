## Purpose
The filepaths module is designed to ease file path navigation in python scripts.

## Installation

```python
python -m pip install filepaths
```

## Use
```python
from filepaths import paths


paths = paths(1)

for file in paths.data.filepaths():
    pd.read_csv(file)
    pass
```
### or
```python
from filepaths import Root


root = Root(1).paths()

for file in root.data.filepaths:
    pd.read_csv(file)
    pass
```
The root object builds a dictionary of files and directories starting in either the current directory, or `depth` levels up. By default, hidden files and folder are ignored, but `ignore_hidden` can be set to `False`.

The `.path()` method returns an [addict dictionary](https://github.com/mewwts/addict). This dictionary inherits the standard dictionary class; it can be accessed with either `root[data][files]` or `root.data.files`.

Alternitavely, one can call the function `paths()` with the same paramaters as the class `Root` which will return a addict dictionary directly.

The keys `'files', 'dirs', 'path',` and `'filepaths'` are reserved for the dictionary: if there are directories with these names in any of the children directories, an error will be thrown.

Either `Root` or `paths` dictionary has a key for every directory in root. Every directory, including `root`, has keys for `'files', 'dirs', 'path',` and `'filepaths'`. The values are either another nested dictionary for the `dirs`, or:

* `root.example.path` returns the absolute path to the `example/` as a string.
* `root.example.dirs` returns a list of the child directories in `example/`.
* `root.example.files` returns a list of the filenames, as strings, for every file in `example/`.
* `root.example.filepaths` returns a list of the absolute paths, as strings, to every file in `example/`.
