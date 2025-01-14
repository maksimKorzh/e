# Minimalist VI-like Text Editor for Linux
    Navigation mode:

    h - move cursor left
    j - move cursor down, Ctrl-d moves cursor 5 lines down
    k - move cursor up, Ctrl-u moves cursor 5 lines up
    l - move cursor right
    g - move cursor to first line
    G - move cursor to last line
    d - delete current line
    x - delete current char
    i - go to insert mode

    Insert mode:

    Englsih ASCII chars only, no unicode
    No tabs, only spaces
    Backspace assumes linux terminal generates ASCII DEL

    I/O:

    Ctrl-w - write changes to current file
    Ctrl-q - quit editor without saving changes

# Limitations
    Copy/Paste and Find are not implemented but assuming, say,
    gnome terminal you can select text with mouse, copy via
    Ctrl-Shift-C and paste with Ctrl-Shift-V, searching via
    Ctrl-Shift-F is limited to the scope of current page because
    ncurses have its own buffer and only visible part of it is
    accessible by the terminal emulator.

# Installation
    git clone https://github.com/maksimKorzh/e
    cd e
    chmod +x e.py
    sudo cp e.py /usr/local/bin/e

# Usage
    e - opens empty file "o.txt"
    e e.py - opens existing file "e.py"
    e test.txt - if no such file opens empty file and sets filename to "test.txt"
