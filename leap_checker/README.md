# Leap Year Checker

![](https://github.com/approximator/python/workflows/Leap%20Year%20Checker%20tests/badge.svg)

---
An example of Python package and command line tool for checking if some specified year is leap or not.

## Installation

Just use `pip` to install from cloned repository:

```bash
pip install /leap_checker
```

Or directly from github:

```bash
pip install 'git+https://github.com/approximator/python.git#egg=leap_checker&subdirectory=leap_checker'
```

## Usage

1. The package can be use from other python programs:

```python
if is_leap(year):
    print(f'The {year} is leap')
else:
    print(f'The {year} is not leap')
```

2. Or it can be used as a command line tool

After installation the `is_leap` command will be available and it can be used in shell scripts.

The command returns zero if the year is leap, 1 otherwise:

```bash
> is_leap 2004
> echo $?
0
> is_leap 2019
> echo $?
1
```

Usage example in bash script:

```bash
CURRENT_YEAR=$(date "+%Y")
if is_leap $CURRENT_YEAR ; then
  echo "The $CURRENT_YEAR is leap"
else
  echo "The $CURRENT_YEAR is NOT leap"
fi
```
