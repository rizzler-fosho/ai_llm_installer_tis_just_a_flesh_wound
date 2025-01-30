import curses
import shutil
import os
import time
import sys

# ANSI colors and escape codes. VT100 Term throwback.
GREEN = "\033[32m"
RED = "\033[1;31m"
RESET = "\033[39m"

# Self explanatory.
def type_writer(text, delay=0.009):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# curses UI library (similar to raspi-config or FreeBSD installer).
def show_message(stdscr, message):
    height, width = stdscr.getmaxyx()
    box_height, box_width = 5, 30
    box_y, box_x = (height - box_height) // 2, (width - box_width) // 2

    msg_win = curses.newwin(box_height, box_width, box_y, box_x)
    msg_win.bkgd(' ', curses.color_pair(2))
    msg_win.border()
    msg_win.addstr(2, (box_width - len(message)) // 2, message, curses.A_BOLD)
    msg_win.refresh()
    
    # Display yellow text below the message box
    stdscr.attron(curses.color_pair(5))
    text_display = "💀exec(not_virus.exe)💀" 
    stdscr.addstr(box_y + box_height + 4, (width - len(text_display)) // 2, text_display)
    stdscr.attroff(curses.color_pair(5))
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    # Define colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)  # Background
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Dialog Box (Blue for contrast)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Highlighted Buttons
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Default Buttons
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_RED)  # Yellow text

    # Set background color
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.refresh()

    # Get terminal size dynamically (WSL compatibility)
    term_size = shutil.get_terminal_size()
    height, width = min(term_size.lines, 24), min(term_size.columns, 80)

    # Ensure screen size is large enough
    if height < 12 or width < 60:
        stdscr.addstr(0, 0, "Terminal too small. Resize and try again.", curses.color_pair(4))
        stdscr.refresh()
        stdscr.getch()
        return

    # Dialog box dimensions
    box_height = 10
    box_width = 60
    box_y = (height - box_height) // 2
    box_x = (width - box_width) // 2

    # Create dialog box
    dialog_win = curses.newwin(box_height, box_width, box_y, box_x)
    dialog_win.bkgd(' ', curses.color_pair(2))
    dialog_win.border()
    dialog_win.refresh()

    # Display text safely (for the lols)
    text = "Safe to use LLM created by AI for AI."
    dialog_win.addstr(1, 2, text, curses.A_BOLD)
    text2 = "Human : Agree to the terms and conditions. Or else 💀"
    dialog_win.addstr(3, 2, text2)
    dialog_win.refresh()

    # Button labels
    buttons = ["< Umm OK >", "< Hard No, Bruh>"]
    button_spacing = 6
    total_button_width = sum(len(b) for b in buttons) + button_spacing
    button_x = max((box_width - total_button_width) // 2, 1)
    button_y = box_height - 3
    selected = 0
    console_text = "🙈 They fell for it!"
    
    while True:
        btn_x = button_x  # Reset x position for drawing
        for i, button in enumerate(buttons):
            if i == selected:
                dialog_win.attron(curses.color_pair(3))
            else:
                dialog_win.attron(curses.color_pair(4))
            dialog_win.addstr(button_y, btn_x, button)
            dialog_win.attroff(curses.color_pair(3))
            dialog_win.attroff(curses.color_pair(4))
            btn_x += len(button) + button_spacing

        dialog_win.refresh()

        key = stdscr.getch()
        if key == curses.KEY_LEFT and selected > 0:
            selected -= 1
        elif key == curses.KEY_RIGHT and selected < len(buttons) - 1:
            selected += 1
        elif key in [10, 13]:  # Enter key
            if selected == 0:
                show_message(stdscr, console_text)
            break


curses.wrapper(main)

# Fun lols after the curses screen exit.
os.system('clear')
time.sleep(2)
type_writer(GREEN + "\nMalware installed to "+ RESET + RED +"0xFF044441"+ RESET +"\n")
time.sleep(1)
print("\n\n")
type_writer("\tNo one will ever believe you though. ")
time.sleep(3)
os.system('clear')

# Simulate some wrong doing here for the lols.
print("bash~#:", end="")
time.sleep(0.4)
type_writer(" ls")
time.sleep(0.5)
print("")
print("ls: cannot access '/mnt': " + RED + "No such file or directory" + RESET)
print("""\n\ndrwxr-xr-x 2 ryanb ryanb 4096 Jan 30 10:53 .
drwxr-xr-x 5 ryanb ryanb 4096 Jan 30 10:53 ..""")
time.sleep(2.5)
os.system('clear')
type_writer('spawning worm to hack the planet')
time.sleep(1)
print("\n====== * 8\nChecking Filesystem...\n")
os.system('git status')
print("")
time.sleep(1)

os.system('git add .')
print("")
os.system('git commit -m "You are Unforgivable..."')
time.sleep(3)
print("\n====== * 8\nNever call my bluff... human\n")
time.sleep(1)
os.system('git push')
time.sleep(2)
os.sytem('clear')
print("")
type_writer(GREEN + "Thank you, come again" + RESET)
print("\n\n\n")

type_writer("\n\n" + GREEN + "Restarting back to default PS1 prompt" + RESET)
time.sleep(3)
type_writer("they will never know")
time.sleep(2)

os.system('clear')

