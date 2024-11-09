
# Virtual Desktop Switcher with Python

This Python script uses the `pyvda` library to switch to a specified virtual desktop in Windows. If the specified desktop does not exist, the script creates additional virtual desktops until it reaches the desired desktop number.

## Requirements

- **Windows 10 or later**
- **Python 3.x**
- **pyvda**: A Python library for interacting with Windows virtual desktops.

## Installation

1. **Install Python**: Ensure that Python 3.x is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).

2. **Install `pyvda`**: Install the `pyvda` library using pip:

   ```bash
   pip install pyvda
   ```

## Usage

This script accepts a single command-line argument, which is the number of the virtual desktop to switch to.

### Running the Script

To run the script, use the following command format:

```bash
python script_name.py <desktop_number>
```

- Replace `script_name.py` with the actual name of your Python script.
- Replace `<desktop_number>` with the target virtual desktop number.

**Example**: To switch to Desktop 3:

```bash
python script_name.py 3
```

### Using `pythonw` (Optional)

If you prefer to run the script without opening a console window, you can use `pythonw`:

```bash
pythonw script_name.py <desktop_number>
```

### Creating a Shortcut (Optional)

You can create a shortcut to run the script with a specific desktop number:

1. **Create a Shortcut**:
   - Right-click on your desktop or in a folder and select **New > Shortcut**.
   - In the **Location** field, enter the path to `pythonw.exe`, the path to your script, and the desktop number. For example:
     ```
     "C:\Path\To\pythonw.exe" "C:\Path\To\script_name.py" 3
     ```

2. **Name the Shortcut**:
   - Give the shortcut a descriptive name, like **Switch to Desktop 3**.

3. **Customize Icon (Optional)**:
   - Right-click the shortcut, select **Properties**, and click **Change Icon** to customize.

## How It Works

- **Check for Existing Desktops**: The script retrieves the list of all current virtual desktops using `pyvda.get_virtual_desktops()`.

- **Create New Desktops (if needed)**: If the specified desktop number is greater than the number of existing desktops, it creates new desktops using `pyvda.VirtualDesktop.create()` until the desired desktop is available.

- **Switch to the Specified Desktop**: Once the specified desktop exists, the script switches to it using `pyvda.VirtualDesktop(desktop_number).go()`.

- **Print Desktop Count**: After switching, the script prints the current number of virtual desktops.

## Notes

- **Argument Validation**: Ensure that you pass a valid integer as the desktop number when running the script.
- **Error Handling**: The script includes basic error handling for invalid inputs.
- **Compatibility**: This script is designed for Windows systems where `pyvda` is supported for virtual desktop management.
