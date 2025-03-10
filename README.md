<div align="center">
<image src="https://psv4.userapi.com/s/v1/d/hQodqEWm7_huFTQUhbgZvgba9Grtt-Kq5lox7cdbWkl66 Pu6siUSO57Uz-cl5iMrNaDQucl6gHslmykwv4eOJNu0Uo0amnHxZD44hLsQRUFVTTxMy3thBQ/icon.png" alt="LOGO">
</div>

# Water Calculator Application

The code is a simple application for determining the amount of water drunk, written using the tkinter library to create a graphical interface and an action logging module to log actions.

## Main components of the code:
1. Logging:

- Configured using the logging module. Results logs in the Water_tracker.log file with time and messages.

- the log_status function records the number of current bottles and the volume of water drunk.

- the log_print function writes the final message to the log.

2. WaterTrackerApp class:

- This is the main class of the application, which controls the interface and the logic of operation.

- Initialization (__init__):

- The main application window with the title "Water Tracker" is created.

- Attempts to load an icon for the window from the icon.png file. If the icon is not found, enter a warning in the log.

- Variables for storing the volume of bottles, the number of bottles, and the total volume of water drunk are initialized.

3. Creating the interface (create_widgets):

- Interface elements are created: a field for entering the volume of bottles, buttons for increasing and adjusting the number of bottles, labels for displaying the current number of bottles and the volume of water drunk.

- Increment_count and Decrement_count methods:

- Increase or decrease the number of bottles and update the interface.

- Update_display method:

- Updates the labels with the proportion of bottles and the amount of water drunk.

- Logs the current state.

4. Launching the application:

- In the if __name__ == "__main__": block, the main application window is created, the log_print function appears to write empty lines to the log (to separate the records), and the main event processing loop mainloop is launched.

## How the application works:
- The user can specify the volume of one bottle (by default, 0.5 liters).

- Using the "+" and "-" buttons, you can specify or decrease the number of bottles drunk.

- The application automatically calculates the total volume of water drunk and displays it on the screen.

- All changes are logged in the Water_tracker.log file.

## Example of use:
- The user enters the volume of the bottle (for example, 0.5 liters).

- Press the "+" button several times to increase the number of bottles drunk.

- The application displays the current number of bottles and the total volume of water drunk.

- All changes in the registration.

This simple application can be useful for those who want to monitor the supply of water drunk during the day.

## TODO-LIST
1. Create an .exe file for the project.
2. Connect the integration with the Telegram bot.