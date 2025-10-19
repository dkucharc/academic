# Integrated Development Environment (IDE) Setup

An Integrated Development Environment (IDE) can significantly enhance your productivity when conducting research and writing code. This guide covers setting up popular IDEs for Python development, organized by platform for easy navigation.

=== "PyCharm"

    PyCharm is a powerful IDE specifically designed for Python development, offering advanced features like intelligent code completion, debugging, and integrated version control.

    ## Installation

    1. Visit the [PyCharm website](https://www.jetbrains.com/pycharm/)
    2. Download PyCharm:
        - **Community Edition**: Free, open-source version with essential features
        - **Professional Edition**: Paid version with additional features (web development, database tools, etc.)
    3. Run the installer and follow the installation prompts

    ## Initial Setup

    1. **Create a New Project**:
        - Open PyCharm and click "New Project"
        - Choose your project location
        - Select the Python interpreter (see Python Interpreter Configuration below)

    2. **Configure Python Interpreter**:
        - Go to **File > Settings** (Windows/Linux) or **PyCharm > Preferences** (macOS)
        - Navigate to **Project > Python Interpreter**
        - Click the gear icon and select "Add"
        - Choose your environment type:
          - **Conda Environment**: Select existing conda environment or create new
          - **Virtual Environment**: Select existing venv or create new
          - **Poetry Environment**: Automatically detected if `pyproject.toml` exists

    ## Key Features and Configuration

    ### Code Quality Tools
    1. **Enable Code Inspections**:
        - Go to **Settings > Editor > Inspections**
        - Enable Python-specific inspections for better code quality

    2. **Configure Code Style**:
        - Go to **Settings > Editor > Code Style > Python**
        - Set up PEP 8 compliance or import custom style configurations

    ### Version Control Integration
    1. **Git Integration**:
        - PyCharm automatically detects Git repositories
        - Access via **VCS** menu for commit, push, pull operations
        - Built-in diff viewer and merge conflict resolution

    ### Scientific Tools (Professional Edition)
    1. **Jupyter Notebook Support**:
        - Create and edit `.ipynb` files directly
        - Run cells interactively within PyCharm

    2. **Database Tools**:
        - Connect to databases for data analysis projects
        - SQL query execution and result visualization

    ## Useful Plugins

    Install plugins via **Settings > Plugins**:
    - **Markdown**: Enhanced markdown editing
    - **CSV Plugin**: Better CSV file handling
    - **Requirements**: Requirements.txt management
    - **.ignore**: Gitignore file support

    ## When to Use PyCharm

    - You want a full-featured Python IDE
    - Working on large, complex projects
    - Need advanced debugging and profiling tools
    - Prefer integrated database and web development tools
    - Want comprehensive code analysis and refactoring

=== "Visual Studio Code"

    Visual Studio Code is a lightweight, extensible code editor with excellent Python support through extensions.

    ## Installation

    1. Visit the [Visual Studio Code website](https://code.visualstudio.com/)
    2. Download the installer for your operating system
    3. Run the installer and follow the setup prompts

    ## Essential Extensions

    Install these extensions for Python development:

    1. **Python Extension Pack** (includes multiple Python-related extensions):
        - Python (by Microsoft)
        - Pylance (language server)
        - Python Debugger
        - Jupyter

    2. **Additional Recommended Extensions**:
        - **GitLens**: Enhanced Git capabilities
        - **Markdown All in One**: Markdown editing support
        - **autoDocstring**: Automatic docstring generation
        - **Black Formatter**: Code formatting
        - **isort**: Import sorting

    ## Python Environment Configuration

    1. **Select Python Interpreter**:
        - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
        - Type "Python: Select Interpreter"
        - Choose from detected environments or browse to specific interpreter

    2. **Configure for Different Environment Managers**:
        - **Conda**: VS Code automatically detects conda environments
        - **Poetry**: Ensure poetry is in PATH, VS Code will detect poetry environments
        - **venv/virtualenv**: Activate environment in terminal or select interpreter path

    ## Workspace Configuration

    Create a `.vscode/settings.json` file in your project root:

    ```json
    {
        "python.defaultInterpreterPath": "./venv/bin/python",
        "python.linting.enabled": true,
        "python.linting.pylintEnabled": true,
        "python.formatting.provider": "black",
        "python.formatting.blackArgs": ["--line-length", "88"],
        "python.sortImports.args": ["--profile", "black"],
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        },
        "files.exclude": {
            "**/__pycache__": true,
            "**/*.pyc": true
        }
    }
    ```

    ## Jupyter Notebook Integration

    1. **Install Jupyter Extension** (included in Python Extension Pack)
    2. **Create/Open Notebooks**:
        - Create new `.ipynb` files
        - Run cells interactively
        - Variable explorer and debugging support

    3. **Configure Jupyter Server**:
        - Use local Jupyter installation
        - Connect to remote Jupyter servers
        - Kernel selection and management

    ## Debugging Configuration

    Create a `.vscode/launch.json` file for debugging:

    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "justMyCode": true
            },
            {
                "name": "Python: Module",
                "type": "python",
                "request": "launch",
                "module": "your_module_name",
                "console": "integratedTerminal",
                "justMyCode": true
            }
        ]
    }
    ```

    ## Terminal Integration

    1. **Integrated Terminal**:
        - Access via `View > Terminal` or `Ctrl+`` (backtick)
        - Automatically activates Python environment
        - Multiple terminal support

    2. **Task Configuration**:
        Create `.vscode/tasks.json` for common tasks:
        ```json
        {
            "version": "2.0.0",
            "tasks": [
                {
                    "label": "Run Tests",
                    "type": "shell",
                    "command": "python",
                    "args": ["-m", "pytest"],
                    "group": "test"
                },
                {
                    "label": "Format Code",
                    "type": "shell",
                    "command": "black",
                    "args": ["."],
                    "group": "build"
                }
            ]
        }
        ```

    ## When to Use Visual Studio Code

    - You prefer a lightweight, fast editor
    - Working with multiple programming languages
    - Want extensive customization through extensions
    - Need strong Git integration
    - Prefer a more minimalist interface

=== "Jupyter"

    For interactive computing and data analysis, Jupyter provides notebook environments ideal for reproducible research.

    ## Installation

    ```bash
    # Via pip
    pip install jupyter

    # Via conda
    conda install jupyter

    # Via poetry
    poetry add jupyter
    ```

    ## JupyterLab vs Jupyter Notebook

    - **Jupyter Notebook**: Classic notebook interface
    - **JupyterLab**: Next-generation interface with enhanced features

    Install JupyterLab:
    ```bash
    pip install jupyterlab
    ```

    ## Running Jupyter

    ```bash
    # Start Jupyter Notebook
    jupyter notebook

    # Start JupyterLab
    jupyter lab
    ```

    ## Best Practices for Jupyter

    1. **Version Control**:
        - Use `nbstripout` to remove output from notebooks before committing
        - Consider using `jupytext` for better version control

    2. **Environment Management**:
        - Install `ipykernel` in your environment
        - Register kernel: `python -m ipykernel install --user --name myresearch`

    3. **Extensions**:
        - **Variable Inspector**: Monitor variables
        - **Table of Contents**: Navigate large notebooks
        - **Code Folding**: Organize code cells

    ## When to Use Jupyter

    - Conducting exploratory data analysis
    - Creating interactive reports and presentations
    - Prototyping and experimenting with code
    - Teaching or learning Python concepts
    - Need to combine code, visualizations, and documentation

## General Setup Tips

1. **Consistent Configuration**:
    - Use configuration files (`.editorconfig`, `pyproject.toml`)
    - Share settings across team members

2. **Code Quality Tools**:
    - Set up linting (pylint, flake8)
    - Configure formatting (black, autopep8)
    - Enable type checking (mypy)

3. **Keyboard Shortcuts**:
    - Learn essential shortcuts for your chosen IDE
    - Customize shortcuts for frequently used actions

4. **Backup and Sync**:
    - Use cloud sync for settings (VS Code Settings Sync, PyCharm Settings Repository)
    - Regular backup of custom configurations

## Official Resources

- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Project Jupyter](https://jupyter.org/)
