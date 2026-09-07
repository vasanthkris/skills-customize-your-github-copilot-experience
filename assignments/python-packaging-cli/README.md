# 📘 Assignment: Python Project Packaging and CLI Tools

## 🎯 Objective

Turn a small Python application into an installable command-line tool. Over several days, practice project organization, virtual environments, package metadata, command-line arguments, logging, and reproducible execution.

## 📝 Tasks

### 🛠️ Organize the Python Project

#### Description

Move the starter application into a package layout and create an isolated development environment so the project can be installed and run consistently on another computer.

#### Requirements

Completed program should:

- Use a `src/` package layout with a descriptive package name.
- Create and use a Python virtual environment for the project.
- Include a `pyproject.toml` file with the project name, version, Python requirement, and console-script entry point.
- Install the project in editable mode with `pip install -e .`.

### 🛠️ Build the Command-Line Interface

#### Description

Complete the provided task-tracking application and expose its main behavior through a command-line interface.

#### Requirements

Completed program should:

- Accept a command and its arguments from the terminal, such as `add`, `list`, and `complete`.
- Display helpful usage information when the user runs the tool with `--help` or invalid arguments.
- Keep application logic in importable functions or classes instead of placing all logic in the CLI entry point.
- Run the installed command from any working directory.

### 🛠️ Add Logging and Reproducible Documentation

#### Description

Make the tool easier to maintain and use by adding useful logs and documenting the complete setup and execution process.

#### Requirements

Completed program should:

- Use Python's `logging` module instead of debug `print()` calls.
- Log important events such as adding, listing, and completing tasks.
- Configure a default log level and allow a more detailed level such as `--verbose`.
- Include a README section showing how to create the environment, install the package, run each command, and uninstall it.
- Explain one design decision and one improvement that would be needed before using the tool with persistent data.
