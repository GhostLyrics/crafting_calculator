#!/usr/bin/env python3
"""GUI to calculate required base resources for crafting in games."""

import PySimpleGUI as sg
import subprocess

from pathlib import Path
from string import Template
from typing import Any, Dict, Tuple

# 3rd party
from yaml import safe_load

# internal
from crafting_calculator import load_recipes

def discover_games() -> Tuple[Dict[str, Any]]:
    games = []
    path = Path("recipes")
    for entry in path.rglob("**/meta.yml"):
        raw_content = entry.read_text()
        content = safe_load(raw_content)
        if content:
            if content.get("title"):
                games.append(entry.parent.name)

    return games

def _load_recipes(game):
    inventory, meta = load_recipes(game)
    return (inventory, meta)

def get_inventory_values(inventory, key):
    returnArray = []
    for item in inventory:
        returnArray.append(item.get(key))
    return returnArray

def window1():
    games = discover_games()
    if games[0]:
        inventory, meta = _load_recipes(games[0])
        items = sorted(get_inventory_values(inventory, 'name'))

    layout = [
        [sg.Text('Game:', size=(6,1)), sg.Combo(games, default_value=games[0], key='game', size=(40,1), enable_events=True)],
        [sg.Text('Item:', size=(6,1)), sg.Listbox(items, key='item', select_mode='extended', size=(40,10), enable_events=False)],
        [sg.Text('', size=(6,1)), sg.Button('Clear selected items', key='clear_items')],
        [sg.Text('Amount:', size=(6,1)), sg.InputText(key='amount', default_text='1', size=(40, 1))],
        [sg.Text('Tip: Use Ctrl+MouseClick to select or deselect multiple items.', size=(49,1))],
        [sg.Text('Output:', size=(6,1))],
        [sg.Multiline(size=(49, 20), key='output', enable_events=True)],
        [sg.Button('Calculate', key='calculate'), sg.Button('Cancel')]
    ]
    return sg.Window('Crafting Calculator', layout, resizable=True)

def main():
    #dir_path = os.path.dirname(os.path.realpath(__file__))

    window = window1()

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        outputElement = window['output']
        
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if event == "game":
            output(outputElement, '')
            inventory, meta = _load_recipes(values['game'])
            items = sorted(get_inventory_values(inventory, 'name'))
            window['item'].Update(items)

        if event == "calculate":
            game = values['game']
            item = values['item']
            if not item:
                output(outputElement, 'Please select an item')
            else:
                amount = int(values['amount'] or 1)
                output(outputElement, '')
                for i in item:
                    cmd = Template('python crafting_calculator.py --game "$game" "$item" --amount $amount --debug')
                    cmdSubstituted = cmd.substitute(game=game, item=i, amount=amount)
                    result = subprocess.check_output(cmdSubstituted, text=True)
                    output(outputElement, result+'\n', True)

        if event == 'clear_items':
            window['item'].set_value([])

    window.close()

def output(element, string, append=False):
    element.Update(disabled=False)
    element.Update(string, append=append)
    element.Update(disabled=True)

if __name__ == '__main__':
    main()
