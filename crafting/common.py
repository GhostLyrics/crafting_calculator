"""Common functionality not related to a class."""

import logging
from typing import List, Dict, Any


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
