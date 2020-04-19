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

- ensure you have [Python3][] and [poetry][] installed
- check out this repository
- change into this repository
- `poetry shell`
- `poetry install`

[Python3]: https://www.python.org/
[poetry]: https://python-poetry.org/

## usage

To calculate a shopping list for crafting, specify an item to craft:

```shell
./crafting_calculator.py --game YOUR_GAME YOUR_ITEM
# example: ./crafting_calculator.py --game yonder cobblestone
```

Result:

```text
You need these items to craft 1 of cobblestone:
stick: 1
stone: 5

The following intermediate items need to be crafted:
constructor's kit: 1
```

Use quotes when you have an item that contains a space, an apostrophe, etc:

```shell
./crafting_calculator.py --game YOUR_GAME "YOUR ITEM"
# example: ./crafting_calculator.py --game yonder "stone tiles"
```

Result:

```text
You need these items to craft 1 of stone tiles:
clay: 2
fodder: 2
stick: 6
stone: 27

The following intermediate items need to be crafted:
cobblestone: 4
constructor's kit: 6
keystone: 1
mortar: 2
```

You can optionally craft more than one copy:

```shell
./crafting_calculator.py --game YOUR_GAME YOUR_ITEM --amount YOUR_AMOUNT
# example: ./crafting_calculator.py --game yonder cobblestone --amount 7
```

Result:

```text
You need these items to craft 7 of cobblestone:
stick: 7
stone: 35

The following intermediate items need to be crafted:
constructor's kit: 7
```

Check the help for all available options:

```shell
./crafting_calculator.py --help
```

### writing your own recipes
Recipes are automatically loaded from [YAML][] files in the folder in `recipes/`
that you ask for with `--game`. Try writing your own recipes for your own games!

- create a folder in `recipes/` (e.g. `nyancat`)
- add a `meta.yml` file with information about the game (e.g. `Cats and Dogs XI`)
    - mandatory keys: **title**
- add at least one more file with recipes (e.g. `example.yml`, recipe: `yarn`)
    - mandatory keys per recipe: **name**, **items**
- That's it! Try it: `./crafting_calculator.py --game nyancat yarn`

[YAML]: https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html

If you want to contribue your recipes to the database, please have a look at
the **General Style Guide** section.

## development
- Code in this project is formatted with [black][], linted with [pylint][] as well as [yamllint][] and
  type hints are checked with [mypy][]. Black, pylint and yamllint are run automatically via [pre-commit][].
- Dependency tracking is done with [poetry][].
- When releases will be available, they will follow [semantic versioning][]
  and have a [changelog][].

[black]: https://github.com/psf/black
[pylint]: https://github.com/PyCQA/pylint
[mypy]: https://github.com/python/mypy
[semantic versioning]: https://semver.org/
[changelog]: https://keepachangelog.com/
[yamllint]: https://github.com/adrienverge/yamllint
[pre-commit]: https://github.com/pre-commit/pre-commit

To get started:

```shell
git clone git@github.com:GhostLyrics/crafting_calculator.git
cd crafting_calculator
pre-commit install
poetry shell
poetry install
```

### general style guide
- Keeping the recipes in files that are easy to scan simplifies maintenance.
  For example, if a game has levels or sections, you could separate by those
  (`carpenter_1_10.yml`, `smith_apprentice.yml`, etc.)
- Keeping the recipe names in lowercase helps keep things simple.
- Keeping the recipes sorted alphabetically in the recipe files makes it easier
  to update things.

## thanks
- Stephen Voss
