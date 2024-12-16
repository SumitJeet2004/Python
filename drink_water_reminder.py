import os
import time

REPEAT_INTERVAL = 3600  # Repeat frequency in seconds

while True:
    # Command to display a notification using PowerShell
    command = 'powershell.exe -Command "Add-Type -AssemblyName System.Windows.Forms; ' \
              '(New-Object System.Windows.Forms.NotifyIcon).ShowBalloonTip(0, \'Drink Water\', \'Hey Harry, Drink water\', [System.Windows.Forms.ToolTipIcon]::Info)"'

    # Execute the command
    os.system(command)

    # Wait for the specified interval
    time.sleep(REPEAT_INTERVAL)
