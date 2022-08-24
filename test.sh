#!/bin/bash

# TODO:
#   - make it only compile the gui code when it's necessary.

# Executes the code for development.

# Compiles the gui code to python.
pyuic5 src/gui/app.ui > src/app/app_ui.py

# Executes the app.
python main.py
