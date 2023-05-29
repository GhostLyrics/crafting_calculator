"""Shopping List class to hold all required items."""

import logging
from json import dumps
from typing import List, Dict, Any

# 3rd party
from yaml import safe_dump

# internal
from crafting.common import find_recipe
from crafting.common import get_recipe_cost

class ShoppingList:
    """A shopping list holds all items required to craft the given item."""

    def __init__(self, inventory: List[Dict[str, Any]], item: str, amount: int):
        self.items: Dict[str, int] = {}
        self.cost: Dict[str, float] = {}
        self.sell_to_vendor: float = None
        self.target_item: str = item
        self.target_amount: int = amount
        self.intermediate_steps: Dict[str, int] = {}
        self.inventory = inventory

    def add_items(self, items: Dict[str, int], amount: int) -> None:
        """Add items to the shopping list."""
        for item in items:
            logging.debug("Adding %s to shopping list.", item)
            self.items.update({item: items[item] * amount})

    def add_item_costs(self, items: Dict[str, float]) -> None:
        """Add items to the shopping list."""
        cost = None
        for item in items:
            recipe_cost = get_recipe_cost(item, self.inventory)
            if recipe_cost is not None:
                self.cost.update({item: items[item] * recipe_cost})
                                
            logging.debug("Summing item costs for %s item in shopping list.", item)
            
        return cost

    def add_step(self, item: str, amount: int) -> None:
        """Add intermediate items to the crafting tree."""
        logging.debug("Adding %s of %s to crafting tree.", amount, item)
        self.intermediate_steps.update(
            {item: self.intermediate_steps.get(item, 0) + amount}
        )

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
        amount_replaced_item = self.items.pop(item)
        logging.info("Replacing %s of %s.", amount_replaced_item, item)
        for replacement in replacement_items:
            amount_replacement = (
                self.items.get(replacement, 0)
                + replacement_items[replacement] * amount_replaced_item
            )
            self.items.update({replacement: amount_replacement})
        self.add_step(item, amount_replaced_item)

    def to_yaml(self) -> str:
        """Return ShoppingList contents as YAML formatted string."""
        prepared_string: str = safe_dump(
            self.items, default_flow_style=False, sort_keys=True
        )
        prepared_string = prepared_string.rstrip("\n")
        return prepared_string

    def to_json(self) -> str:
        """Return ShoppingList contents as JSON formatted string."""

        output = {
            "shopping_list": self.items,
            "intermediates": self.intermediate_steps,
            "target_item": self.target_item,
            "target_amount": self.target_amount,
        }
        return dumps(output, sort_keys=True, indent=2)

    def format_for_display(self) -> str:
        """Format the ShoppingList for printing to stdout."""
        total_cost = sum(self.cost.values())
        total_cost_formatted = f'{total_cost:,}'
        message = "\n".join(
            [
                "",
                f"You need these items to craft {self.target_amount} of {self.target_item}:",
                safe_dump(self.items, default_flow_style=False, sort_keys=True),
                "The following intermediate items need to be crafted:",
                safe_dump(
                    self.intermediate_steps, default_flow_style=False, sort_keys=True
                ).rstrip("\n"),
                "",
                f"It will cost a total of {total_cost_formatted} to craft the intermediate items:",
                safe_dump(self.cost, default_flow_style=False, sort_keys=True),
            ]
        )
        if self.sell_to_vendor is not None:
            sell_to_vendor_formatted = f'{self.sell_to_vendor:,}'
            message += "\n"+self.target_item+" sells to a vendor for: "+sell_to_vendor_formatted

        return message
