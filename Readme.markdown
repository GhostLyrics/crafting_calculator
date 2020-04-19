# crafting_calculator.py

This is a generic Python CLI tool for resolving (breaking down) crafting
recipes in video games into their base components, to help assemble a shopping
list.

*I wrote this program because I love building things but dislike the
manual resolving into components enough to stop crafting as soon as it gets
a bit involved.*

- **Feedback welcome!** (e.g. ping me on Twitter: [@ghostlyrics][])
- **Pull requests with additional games, features or improvements welcome.**

[@ghostlyrics]: https://twitter.com/ghostlyrics

## installation

Currently this project is in alpha state and not packaged. To install:

- ensure you have [poetry][] installed
- check out this repository
- change into this repository
- `poetry shell`
- `poetry install`

[poetry]: https://python-poetry.org/

## usage

To calculate a shopping list for crafting, specify an item to craft:

```shell
./crafting_calculator.py --game YOUR_GAME YOUR_ITEM
# example: ./crafting_calculator.py --game yonder cobblestone
```

Use quotes when you have an item that contains a space, an apostrophe, etc:

```shell
./crafting_calculator.py --game YOUR_GAME "YOUR ITEM"
# example: ./crafting_calculator.py --game yonder "stone tiles"
```

You can optionally craft more than one copy:

```shell
./crafting_calculator.py --game YOUR_GAME YOUR_ITEM --amount YOUR_AMOUNT
# example: ./crafting_calculator.py --game yonder cobblestone 7
```

## development
- Code in this project is formatted with [black][], and linted with [pylint][].
- Dependency tracking is done with [poetry][].
- When releases will be available, they will follow [semantic versioning][] 
  and have a [changelog][].

[black]: https://github.com/psf/black
[pylint]: https://github.com/PyCQA/pylint
[semantic versioning]: https://semver.org/
[changelog]: https://keepachangelog.com/

## thanks
- Stephen Voss
