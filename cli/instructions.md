### Copy the CLI folder
Copy the cli folder on your local machine and open a terminal (or cmd) and "cd" into it.

### Create a virtual environment (optional)
This step is optional but it's highly recommended to avoid enviornment conflicts. Besides, you will be able to delete everything after your are done with it 

    python -m venv ./venv_click

***linux:***

    source ./venv_click/bin/activate

***windows:***

    .\venv_click\scripts\activate

### Install the click package
    pip install click

### Install the goodmorning package
    pip install --editable .

### Playing around 😀😀
Check the utility's help

    goodmorning --help
*result*

    Usage: goodmorning [OPTIONS]

    Options:
    --name TEXT  Introduce yourself
    --help       Show this message and exit.

Without options

    goodmorning
*result*

    Hello There!

With the name option

    goodmorning --name Mike
*result*

    Good Morning, Mike!

### Clean up (optional)
    deactivate
Delete the venv_click directory.