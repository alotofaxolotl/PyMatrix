# PyMatrix

A clone of cmatrix written in Python3 with the curses module.

## Features

* Two charactersets
  * Classic (ASCII printable characters)
  * Japanese (UTF-8 Hiragana characters)
* Variable density and frequency
* RC file compatibility

## Using PyMatrix

To use PyMatrix, simply run `pymatrix.py` using Python `^3.6`.

```shell
$ python3 pymatrix.py
```

To quit, press `CTRL+C`.

By default, PyMatrix will use the japanese characterset with a frequency of 1 and a density of 2. Frequency controls the time between creating new "heads", and density controls how many "heads" will be created. You can specify the characterset, density, and frequency using the flags `-set`, `-d`, and `-f` respectively.

```shell
$ python3 pymatrix.py -set cl -d 5 -f 3
```

Additionally, PyMatrix looks for an rc file to read from at `~/.pymatrix.rc`. You can set custom defaults there.

```
SET=jp
DENSITY=5
FREQUENCY=3
```

Lastly, because PyMatrix is one file and self-contained, you can put it in you `bin` and run from anywhere.

```shell
cp ./pymatrix.py /usr/local/bin/pymatrix
chmod a+x /usr/local/bin/pymatrix
```
The included `install.sh` script performs these two commands automatically. Afterwards, PyMatrix can be run simply by typing `pymatrix` from anywhere in you file system.
