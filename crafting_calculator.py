#!/usr/bin/env python3

"""Calculate required base resources for crafting in games."""

import logging
import argparse

from json import dumps
from typing import Any, Dict, List, Tuple
from pathlib import Path

from yaml import safe_load, safe_dump


EXITCODE_NO_RECIPES = 1


class ShoppingList:
    """A shopping list holds all items required to craft the given item."""

    def __init__(self, inventory: List[Dict[str, Any]]):
        self.items: Dict[str, int] = {}
        self.inventory = inventory

    def add_items(self, items: Dict[str, int], amount: int) -> None:
        """Add items to the shopping list."""
        for item in items:
            logging.debug("Adding %s to shopping list.", item)
            self.items.update({item: items[item] * amount})
        # self.items.update(items)

    def simplify(self) -> None:
        """Recursively replace intermediate crafted items with their components."""
        logging.info("Simplifying shopping list.")

        replacements = {}
        for item in self.items:
            recipe = find_recipe(item, self.inventory)
            if recipe:
                replacements.update({item: recipe})

        for item in replacements:
            self.replace_items(item, replacements[item])

        if replacements:
            self.simplify()
        else:
            logging.info("Nothing to simplify.")

    def replace_items(self, item: str, replacement_items: Dict[str, int]) -> None:
        """Replace items in the shopping list with smaller components."""
        amount_replaced_item = self.items[item]
        logging.info("Replacing %s of %s.", amount_replaced_item, item)
        self.items.pop(item)
        for replacement in replacement_items:
            amount_replacement = (
                self.items.get(replacement, 0)
                + replacement_items[replacement] * amount_replaced_item
            )
            self.items.update({replacement: amount_replacement})

    def to_yaml(self) -> str:
        """Return ShoppingList contents as YAML formatted string."""
        prepared_string: str = safe_dump(
            self.items, default_flow_style=False, sort_keys=True
        )
        prepared_string = prepared_string.rstrip("\n")
        return prepared_string

    def to_json(self) -> str:
        """Return ShoppingList contents as JSON formatted string."""
        return dumps(self.items, sort_keys=True, indent=2)


def parse_arguments() -> argparse.Namespace:
    """Parse given command line arguments."""
    parser = argparse.ArgumentParser(
        allow_abbrev=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    calculation = parser.add_argument_group("crafting options")
    verbosity = parser.add_argument_group("verbosity options")
    export = parser.add_argument_group("export options")

    verbosity.add_argument(
        "--debug",
        "-d",
        default=False,
        action="store_true",
        help="enable debug logging with timestamps",
    )
    verbosity.add_argument(
        "--verbose",
        "-v",
        default=False,
        action="store_true",
        help="enable verbose output",
    )

    export.add_argument(
        "--as-json",
        action="store_true",
        default=False,
        help="return a JSON string instead of a user-friendly message",
    )

    calculation.add_argument("item", type=str, help="the item you want to craft")

    calculation.add_argument(
        "--amount",
        type=int,
        default=1,
        help="craft this amount of the item",
        required=False,
    )
    calculation.add_argument(
        "--game",
        help="load recipes for this game from the recipes folder (e.g. yonder)",
        required=True,
    )

    options = parser.parse_args()
    return options


def setup_logging(debug: bool, verbose: bool) -> None:
    """Create a logging configuration according to given flags."""
    if debug:
        logging.basicConfig(
            format="%(asctime)s %(levelname)s: %(message)s", level=logging.DEBUG
        )
        logging.debug("Debug logging enabled.")
    elif verbose:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s")


def load_recipes(game: str) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Load all recipes for a given game."""
    inventory = []
    meta = {"title": "unknown game (meta data incomplete)"}

    path = Path("recipes").joinpath(game)
    logging.info("Loading recipes from %s.", path)

    for entry in path.rglob("*.yml"):
        raw_content = entry.read_text()
        content = safe_load(raw_content)

        if content:
            if entry.name == "meta.yml":
                meta = content
                if meta.get("title"):
                    logging.debug("Game detected as %s.", meta.get("title"))
            else:
                inventory.extend(content)
                logging.debug("Read %s recipes from %s.", len(content), entry)

    sum_recipes = len(inventory)
    if sum_recipes:
        logging.info(
            "Loaded a total of %s recipes for %s.", sum_recipes, meta.get("title")
        )
    else:
        logging.info("No recipes detected for %s.", meta.get("title"))

    if not inventory:
        logging.error("No recipes were detected for %s.", meta.get("title"))
        raise RuntimeWarning("No recipes detected.")

    return (inventory, meta)


def find_recipe(item: str, inventory: List[Dict[str, Any]]) -> Dict[str, int]:
    """Find the first matching recipe from the inventory."""

    recipe_items: Dict[str, int] = {}

    logging.debug("Searching recipe for %s.", item)
    for recipe in inventory:
        if recipe.get("name") == item:

            recipe_items = recipe["items"]
            logging.debug("Found recipe for %s.", item)
            logging.debug(recipe_items)
            break

    if not recipe_items:
        logging.debug("No recipes for %s.", item)

    return recipe_items


def craft_item(item: str, inventory: List[Dict[str, Any]], amount: int) -> ShoppingList:
    """Calculate the items required to craft a recipe."""
    shopping_list = ShoppingList(inventory)
    required_items = find_recipe(item, inventory)
    shopping_list.add_items(required_items, amount)
    shopping_list.simplify()

    return shopping_list


def main() -> None:
    """Break a recipe down into its base components and create  shopping list."""
    options = parse_arguments()
    setup_logging(options.debug, options.verbose)

    try:
        inventory, meta = load_recipes(options.game)
    except RuntimeWarning as error:
        if str(error.args) == "No recipes detected.":
            raise SystemExit(EXITCODE_NO_RECIPES)

    shopping_list = craft_item(options.item, inventory, options.amount)

    if options.as_json:
        print(shopping_list.to_json())
    else:
        message = (
            "\n"
            + "You need these items to craft {} of {}:".format(
                options.amount, options.item
            )
            + "\n"
        )
        print(message)
        print(shopping_list.to_yaml())


if __name__ == "__main__":
    main()
