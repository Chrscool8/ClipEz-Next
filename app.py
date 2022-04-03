# https://github.com/timethrow/yt-dlp/blob/patch-1/README.md#embedding-yt-dlp
# https://github.com/aegirhall/console-menu
# https://www.youtube.com/watch?v=EpJPkmCupEo
# https://pypi.org/project/tabulate/

from consolemenu import *
from consolemenu.items import *
import yt_dlp
from yt_dlp.postprocessor.common import PostProcessor
import json
from tabulate import tabulate
import functools
import os
import glob


verified = False
global downloaded
downloaded = False


def set_verify(whether):
    global verified
    verified = whether


def list_entry(json_data, title, tag):
    entry = ["", ""]

    entry[0] = title

    answer = json_data.get(tag, "N/A")
    line_length = 50
    list_lines = [answer[i:i+line_length] for i in range(0, len(answer), line_length)]

    for line in list_lines:
        entry[1] += line + "\n"

    return entry


def verify_video(chosen_url="", deep_info=False):
    print()
    ydl = yt_dlp.YoutubeDL({})
    info_dict = ""
    try:
        info_dict = ydl.extract_info(url=chosen_url, download=False)
        #info_dump = json.dumps(ydl.sanitize_info(info_dict))
    except:
        pu = PromptUtils(Screen())
        pu.enter_to_continue("Press [Enter] to return to the main menu.")
        return False

    menu_title = "Here's some information. Does it look correct?"
    list_info = [
        list_entry(info_dict, "Title", "title"),
        list_entry(info_dict, "Uploader", "uploader"),
        list_entry(info_dict, "ID", "id"),
        list_entry(info_dict, "URL", "webpage_url"),
    ]
    table_format = "fancy_grid"

    if deep_info:
        list_info += [
            ["view_count", info_dict.get("view_count", None)],
            ["duration", info_dict.get("duration", None)],
            ["upload_date", info_dict.get("upload_date", None)],
            ["age_limit", info_dict.get("age_limit", None)],
            ["uploader_id", info_dict.get("uploader_id", None)],
            ["uploader_url", info_dict.get("uploader_url", None)],
            ["Subscribers", info_dict.get("channel_follower_count", None)],
        ]

        table_format = "presto"
        menu_title = "Here's even more information. Does it look correct?"

    table = (tabulate(list_info, tablefmt=table_format))

    menu = ConsoleMenu(menu_title, table, clear_screen=False)
    item_yes = FunctionItem("Yes!",  functools.partial(set_verify, True), should_exit=True)
    menu.append_item(item_yes)
    item_no = FunctionItem("No!", functools.partial(set_verify, False), should_exit=True)
    menu.append_item(item_no)

    if not deep_info:
        item_more_info = FunctionItem("Show me more info first", functools.partial(verify_video, chosen_url, True), should_exit=True)
        menu.append_item(item_more_info)

    menu.show(show_exit_option=False)

    return verified


def clear_temps():
    files = glob.glob(os.getcwd()+"/temp/downloaded.*")
    for file in files:
        os.remove(file)


def my_hook(d):
    global downloaded
    if d['status'] == 'finished':
        #print('\n\nDone downloading.\n')
        downloaded = True
    if d['status'] == 'error':
        #print('\n\nSomething went wrong with the download.\n')
        downloaded = False


def download_video(url):
    try:
        os.makedirs(os.getcwd()+"/temp/")
    except:  # all good
        a = 0

    if (not os.path.isdir(os.getcwd()+"/temp/")):
        print("Can't find temp directory. Returning.")
        return False

    clear_temps()

    options = {
        'outtmpl': os.getcwd()+"/temp/downloaded.%(ext)s",
        'fixup': "detect_or_warn",
        'noplaylist': True,
        'progress_hooks': [my_hook],
    }

    ydl = yt_dlp.YoutubeDL(options)
    info_dict = ydl.extract_info(url, download=True)
    info_dump = json.dumps(ydl.sanitize_info(info_dict))

    global downloaded
    return downloaded


def full_wizard():
    print()
    print("This will lead you through downloading and converting a video all in one process.")
    pu = PromptUtils(Screen())
    result = pu.input("Enter a URL")

    verified = verify_video(result.input_string)

    if not verified:
        return

    downloaded = download_video(result.input_string)

    print(str(downloaded))


def main():
    menu = ConsoleMenu("ClipEz-Next", clear_screen=False)
    function_item = FunctionItem("Full Wizard", full_wizard, should_exit=False)
    menu.append_item(function_item)
    menu.show()


if __name__ == "__main__":
    main()
