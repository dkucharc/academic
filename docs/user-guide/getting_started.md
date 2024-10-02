# Getting Started

Setting up a consistent and reproducible development environment is crucial for conducting reproducible research. This section will guide you through the process of setting up Python environment, along with an Integrated Development Environment (IDE).

## 1. Python distribution

[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is popular distribution system for Python and R, designed for scientific computing. It simplifies package management and deployment.

1. Visit the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html) and download the appropriate installer.
2. Run the installer and follow the prompts.
3. Miniconda provides a base Python installation with conda package manager.

## 2. Creating a Conda Environment

After Miniconda, create a new environment for your research project:

1. Open a terminal (or Anaconda Prompt on Windows).
2. Create a new environment named `myresearch` with ``python 3.9``:
   ```
   conda create --name myresearch python=3.9
   ```
3. Activate the environment:
   ```
   conda activate myresearch
   ```
4. Install necessary packages:
   ```
   conda install numpy pandas matplotlib scipy
   ```

## 3. Setting Up an IDE

An Integrated Development Environment (IDE) can significantly enhance your productivity. Here's how to set up two popular IDEs:

### PyCharm

1. Download and install [PyCharm](https://www.jetbrains.com/pycharm/) (Community Edition is free).
2. Open PyCharm and create a new project.
3. In the project settings, set the Python interpreter to your conda environment:
   - Go to File > Settings (on Windows/Linux) or PyCharm > Preferences (on macOS).
   - Navigate to Project > Python Interpreter.
   - Click the gear icon and select "Add".
   - Choose "Conda Environment" and select the environment you created.

### Visual Studio Code

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
2. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the VS Code Marketplace.
3. Open your project folder in VS Code.
4. Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the command palette.
5. Type "Python: Select Interpreter" and choose your conda environment.

### Project Jupyter*
   To provides interactive notebook environments ideal for reproducible research.
   Official website: [Project Jupyter](https://jupyter.org/),

## 4. Version Control

To ensure reproducibility, use version control for your code:

1. Install [Git](https://git-scm.com/downloads) if not already installed.
2. Initialize a Git repository in your project folder:
   ```
   git init
   ```
3. Create a `.gitignore` file to exclude unnecessary files. You can use [gitignore.io](https://www.toptal.com/developers/gitignore) to generate a suitable `.gitignore` file for your project.
4. Make your initial commit:
   ```
   git add .
   git commit -m "Initial commit"
   ```

## Additional resources

For further reading on reproducible research practices, consider exploring resources from:

- [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html)
- [Software Carpentry](https://software-carpentry.org/lessons/)

