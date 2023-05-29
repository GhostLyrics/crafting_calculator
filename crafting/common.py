"""Common functionality not related to a class."""

import logging
from typing import List, Dict, Any, Union

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

def get_recipe_cost(item: str, inventory: List[Dict[str, Any]]) -> Union[float, None]:
    """Get the first matching recipe cost from the inventory."""

    recipe_cost = None

    logging.debug("Getting recipe cost for %s.", item)
    for recipe in inventory:
        if recipe.get("name") == item:
            if 'cost' in recipe.keys():
                recipe_cost = recipe.get("cost")
                logging.debug("Found recipe cost for %s.", item)
            else:
                recipe_cost = 0
                logging.warning("No recipe cost for %s.", item)
            break

    return recipe_cost

def get_sell_to_vendor(item: str, inventory: List[Dict[str, Any]]) -> Union[float, None]:
    """Get the first matching recipe cost from the inventory."""

    sell_to_vendor = None

    logging.debug("Getting recipe cost for %s.", item)
    for recipe in inventory:
        if recipe.get("name") == item:
            if 'cost' in recipe.keys():
                sell_to_vendor = recipe.get("cost")
                logging.debug("Found recipe cost for %s.", item)
            else:
                sell_to_vendor = 0
                logging.warning("No vendor sell amount for %s.", item)
            break

    return sell_to_vendor