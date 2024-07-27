# 1to50 Puzzle Automation Project

## Project Overview
The 1to50 Puzzle Automation Project is designed to automate the process of solving the 1to50 puzzle game using Selenium with Python. This project demonstrates how to use web automation techniques to interact with and solve a web-based puzzle game by replicating human actions in an efficient and accurate manner.

## Installation Guide

### Prerequisites
- Python 3.x: Ensure that Python 3.x is installed on your system.
- Chrome Browser: The Chrome browser is required for running the automation script.
- ChromeDriver: The WebDriver that interacts with Chrome.

### Setup Instructions
1. Install Python: Download and install Python from [python.org](https://www.python.org).
2. Set Up a Virtual Environment (Optional but recommended):
    
    ``` bash title="Bash"
    python -m venv venv
    ```

    Activate the virtual environment:
    
    - On Windows:
    ``` powershell title="PowerShell"
    venv\Scripts\activate
    ```

    - On macOS/Linux:
    ``` unixconfig title="Unix"
    source venv/bin/activate
    ```

3. Install Dependencies:

    Create a requirements.txt file with the following content:
    ``` text title="text"
    selenium
    ```
    Install dependencies:
    ``` bash title="bash"
    pip install -r requirements.txt
    ```

4. Download and Configure ChromeDriver:
    - Download ChromeDriver from [chromedriver.chromium.org](https://sites.google.com/chromium.org/driver/home?authuser=0).
    - Ensure that the version of ChromeDriver matches your Chrome browser version.
    - Place chromedriver in a directory included in your system's PATH or specify the path in the `main.py` file.

## Usage Instructions
### Running the Automation Script

1. Open a Terminal or Command Prompt.
2. Navigate to the Project Directory:
    ``` bash title="bash"
    cd path/to/project
    ```
3. Run the Script:
    ``` bash title="bash"
    python main.py
    ```
    The script will open Chrome, interact with the 1to50 puzzle game, and attempt to solve it.

### Example Output
- The browser will automatically open, and you will see the puzzle being solved in real-time.
- The final result will be displayed in the terminal or saved to a log file, depending on the script configuration.
