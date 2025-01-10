# Tekken Keyboard Overlay

## Overview
This is a program I made while I was bored that allows me to show my keyboard inputs in OBS while I play Tekken 8. Currently, it only supports default bindings, and no macros/extra bindings. 

## Running this application
To run this, you will need PyQt6 and Pynput. I will also be providing a prebuilt .exe file. 

The application uses a `keybinds.cfg` file that is in the same directory as the app to get keybinds. If the file does not exist, it will make one for you with the default binds. If there are any issues with the keybinds cfg file, it will use default binds.

## Known Issues
There is no way to tell if the application reset to default binds on load. This will be fixed later.