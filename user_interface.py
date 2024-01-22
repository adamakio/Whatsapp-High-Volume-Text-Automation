import time
from enum import Enum

import pandas as pd
from rich.console import Console
from rich.table import Table

import custom_auth
from pywhatbot import PyWhatBot
from open_file import select_file
from text import english_text, spanish_text


class Language(Enum):
    english = 1
    espanol = 2


def safeApp(lang):
    if lang == Language.english:
        text = english_text
    elif lang == Language.espanol:
        text = spanish_text
    console = Console()

    authenticated = custom_auth.authenticate_user()
    if not authenticated:
        console.print(text["license_prompt"], style="green")
        authenticated = custom_auth.activate_user()
    if authenticated:
        console.print(text["license_success"], style="green")
        while True:
            try:
                App(console, text)
            except Exception as e:
                console.print(f"{text['app_failed']}\n {e}", style="red")
                sleep_time = 5  # seconds
                console.print(text["app_restarting"].format(sleep_time))
                time.sleep(sleep_time)
    else:
        console.print(text["license_failed"], style="red")
        sleep_time = 5  # seconds
        console.print(text["app_restarting"].format(sleep_time))
        time.sleep(sleep_time)
        safeApp(lang)


def App(console: Console, text: dict):

    console.print(text["welcome"], style="green on white bold", justify="center")

    print()

    wait_time = input_wait_time(console, text["wait_time"])

    contacts = import_contacts(console, text["import_contacts"])
    print_contacts(console, contacts)
    numbers = contacts[text["number"]]
    names = contacts[text["name"]]

    print()

    messages = input_messages(console, text["input_messages"])
    if len(messages) > 1:
        delay = input_delay(console, text["delay"])
    else:
        delay = 3
    confirmed = confirm_task(console, numbers, messages, text["confirm_task"])
    if confirmed:
        pywhatbot = PyWhatBot(wait_time, delay)
        pywhatbot.send_message_to_numbers(names, numbers, messages)
    else:
        App(text)


def input_wait_time(console: Console, text: dict):
    console.print(text["prompt"], style="green bold")
    console.print(text["info"])
    options = text["options"]
    wait_times = [20, 15, 10, 7]  # in seconds
    for i, option in enumerate(options):
        console.print(f"[green]{i+1}[/green] -- {option}")
    ans = input()

    try:
        opt = int(ans)
        if 0 < opt <= 3:
            console.print(text["success"].format(options[opt - 1]))
            return wait_times[opt - 1]
        else:
            console.print(text["error"].format(ans), style="red")
            return input_wait_time(console, text)
    except:
        console.print(text["error"].format(ans), style="red")
        return input_wait_time(console, text)


def import_contacts(console: Console, text: dict):
    console.print(text["prompt"], style="bold", justify="center")
    input()
    filetypes = (("CSV files", "*.csv"), ("All files", "*.*"))
    filename = select_file(filetypes)
    try:
        contacts = pd.read_csv(filename, dtype=str)
        console.print(text["success"], style="green", justify="center")
        return contacts
    except:
        console.print(text["failure"].format(filename), style="red", justify="center")
        return import_contacts(console, text)


def print_contacts(console: Console, contacts: pd.DataFrame):
    contacts_table = Table(title="Contacts List")
    for column in contacts:
        contacts_table.add_column(column, justify="center")
    for _, row in contacts.iterrows():
        contacts_table.add_row(*(row.values))
    console.print(contacts_table, justify="center")


def input_messages(console: Console, text: dict):
    console.print(text["prompt"], style="green on white bold")
    console.print(text["info"])
    exit = False
    message_no = 1
    messages = []
    while not exit:
        console.print(f"{text['message']} #{message_no}", style="green")
        console.print(f"1 -- {text['text']}")
        console.print(f"2 -- {text['media']}")
        if message_no > 1:
            console.print(f"3 -- {text['exit']}")
        ans = input()
        try:
            opt = int(ans)
            if opt == 1:
                console.print(text["prompt_1"], style="green1")
                msg = input()
                messages.append([msg])
                message_no += 1
            elif opt == 2:
                console.print(text["prompt_2"])
                input()
                filetypes = filetypes = (
                    ("JPG Images", "*.jpg"),
                    ("JPEG Images", "*.jpeg"),
                    # ("PNG Images", "*.png"),
                    # ("MP3 Audio Files", "*.mp3"),
                    # ("MP4 Videos", "*.mp4"),
                    # ("PDF Documents", "*.pdf"),
                    ("All files", "*.*"),
                )
                filename = select_file(filetypes)
                console.print(text["prompt_3"], style="green1")
                caption = input()
                messages.append([filename, caption])
                message_no += 1
            elif opt == 3:
                exit = True
            else:
                console.print(text["error"], style="red")
        except:
            console.print(text["error"], style="red")
    return messages


def input_delay(console: Console, text: dict):
    console.print(text["prompt"], style="green bold", justify="center")
    console.print(text["info"], justify="center")
    ans = input()
    try:
        delay = float(ans)
        bounds = [2.5, 15.0]
        in_range = (delay > bounds[0]) and (delay <= bounds[1])
        if in_range:
            console.print(
                text["success"].format(delay), style="green", justify="center"
            )
            return delay
        else:
            console.print(
                text["bounds_error"].format(*bounds), style="red", justify="center"
            )
            console.print(text["error"].format(ans), style="red", justify="center")
            return input_delay(console, text)
    except:
        console.print(text["error"].format(ans), style="red", justify="center")
        return input_delay(console, text)


def confirm_task(console: Console, numbers: list, messages: list, text: dict):
    console.print(text["display_messages"], style="green bold")
    for message in messages:
        if len(message) == 1:
            [msg] = message
            console.print(text["text_message"].format(msg))
        else:
            [path, caption] = message
            console.print(text["media_message"].format(path, caption))

    print()

    console.print(text["display_numbers"], style="green")
    [console.print(num) for num in numbers]

    print()

    console.print(
        f"{text['confirm']} ([green]{text['yes']}[/green]|[red]{text['no']}[/red])"
    )
    ans = input()
    return ans == text["yes"]


if __name__ == "__main__":
    safeApp(Language.english)
