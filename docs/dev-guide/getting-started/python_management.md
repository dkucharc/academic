# Python Environment Management

Setting up a consistent and reproducible Python environment is crucial for conducting reproducible research. This guide covers four popular Python environment management approaches, organized by tool for easy navigation.

=== "pip + venv"

    The native Python approach using `pip` (Python's package installer) and `venv` (Python's built-in virtual environment module). This is the most basic and widely supported method.

    ## Prerequisites

    - Python 3.3+ (venv is included in the standard library)
    - pip (usually comes with Python installations)

    ## Creating a Virtual Environment

    1. Navigate to your project directory:
        ```bash
        cd /path/to/your/project
        ```

    2. Create a virtual environment:
        ```bash
        python -m venv myresearch
        ```

        Or specify a Python version (if you have multiple versions):
        ```bash
        python3.9 -m venv myresearch
        ```

    3. Activate the environment:
        - **Unix/macOS:**
            ```bash
            source myresearch/bin/activate
            ```
        - **Windows:**
            ```bash
            myresearch\Scripts\activate
            ```

    4. Verify activation (you should see the environment name in your prompt):
        ```bash
        which python  # Unix/macOS
        where python  # Windows
        ```

    5. Upgrade pip (recommended):
        ```bash
        python -m pip install --upgrade pip
        ```

    ## Installing Packages

    With the virtual environment activated:

    ```bash
    # Install individual packages
    pip install numpy pandas matplotlib scipy

    # Install from requirements file
    pip install -r requirements.txt

    # Install in development mode (for your own package)
    pip install -e .
    ```

    ## Managing Dependencies

    ### Creating Requirements Files

    Generate a requirements file with exact versions:
    ```bash
    pip freeze > requirements.txt
    ```

    Create a more flexible requirements file manually:
    ```txt
    # requirements.txt
    numpy>=1.21.0
    pandas>=1.3.0
    matplotlib>=3.4.0
    scipy>=1.7.0
    requests>=2.25.0
    ```

    ### Development Dependencies

    Keep development tools separate:
    ```txt
    # requirements-dev.txt
    pytest>=6.2.0
    black>=21.0.0
    flake8>=3.9.0
    mypy>=0.910
    jupyter>=1.0.0
    ```

    Install development dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```

    ### Using pip-tools for Better Dependency Management

    Install pip-tools for more sophisticated dependency management:
    ```bash
    pip install pip-tools
    ```

    Create a `requirements.in` file with high-level dependencies:
    ```txt
    # requirements.in
    numpy
    pandas
    matplotlib
    scipy
    requests
    ```

    Generate a locked requirements file:
    ```bash
    pip-compile requirements.in
    ```

    This creates `requirements.txt` with pinned versions for reproducibility.

    ## Deactivating and Removing Environments

    ### Deactivate
    ```bash
    deactivate
    ```

    ### Remove Environment
    Simply delete the environment directory:
    ```bash
    rm -rf myresearch  # Unix/macOS
    rmdir /s myresearch  # Windows
    ```

    ## Project Structure Example

    ```
    myresearch/
    ├── myresearch/          # Virtual environment (don't commit to git)
    ├── src/                 # Source code
    ├── tests/               # Test files
    ├── data/                # Data files
    ├── notebooks/           # Jupyter notebooks
    ├── requirements.txt     # Production dependencies
    ├── requirements-dev.txt # Development dependencies
    ├── README.md
    └── .gitignore          # Include myresearch/ here
    ```

    ## When to Use pip + venv

    - Learning Python or starting with Python development
    - Working with pure Python packages
    - Need maximum compatibility across systems
    - Want to understand the basics of Python packaging
    - Working in environments where conda/poetry aren't available
    - Simple projects with straightforward dependencies

    ## Advantages

    - **Built-in**: No additional tools to install
    - **Universal**: Works everywhere Python works
    - **Simple**: Straightforward workflow
    - **Lightweight**: Minimal overhead
    - **Educational**: Helps understand Python packaging

    ## Limitations

    - **Manual dependency resolution**: No automatic conflict resolution
    - **No binary package management**: Relies on PyPI wheels
    - **Basic environment management**: Less sophisticated than alternatives
    - **No built-in project management**: Requires manual setup

=== "Conda"

    [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a popular distribution system for Python and R, designed for scientific computing. It simplifies package management and deployment.

    ## Installation

    ### Miniconda (Traditional)
    1. Visit the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html) and download the appropriate installer.
    2. Run the installer and follow the prompts.
    3. Miniconda provides a base Python installation with conda package manager.

    ### Mamba (Faster Alternative)
    [Mamba](https://mamba.readthedocs.io/) is a fast, robust, and cross-platform package manager that's a drop-in replacement for conda. It uses the same commands and configuration files as conda but is significantly faster.

    **Install Mamba:**
    ```bash
    # Option 1: Install mamba in base environment
    conda install -n base -c conda-forge mamba

    # Option 2: Install Mambaforge (recommended for new installations)
    # Download from: https://github.com/conda-forge/miniforge#mambaforge
    ```

    ## Creating a Conda Environment

    After installing Miniconda or Mambaforge, create a new environment for your research project:

    1. Open a terminal (or Anaconda Prompt on Windows).
    2. Create a new environment named `myresearch` with Python 3.9:

        **Using conda:**
        ```bash
        conda create --name myresearch python=3.9
        ```

        **Using mamba (faster):**
        ```bash
        mamba create --name myresearch python=3.9
        ```

    3. Activate the environment:
        ```bash
        conda activate myresearch
        # or
        mamba activate myresearch
        ```

    4. Install necessary packages:

        **Using conda:**
        ```bash
        conda install numpy pandas matplotlib scipy
        ```

        **Using mamba (faster):**
        ```bash
        mamba install numpy pandas matplotlib scipy
        ```

    ## Managing Dependencies

    Create an `environment.yml` file to track your dependencies:

    ```yaml
    name: myresearch
    channels:
      - conda-forge
      - defaults
    dependencies:
      - python=3.9
      - numpy
      - pandas
      - matplotlib
      - scipy
      - pip
      - pip:
        - some-pip-only-package
    ```

    Recreate the environment from the file:

    **Using conda:**
    ```bash
    conda env create -f environment.yml
    ```

    **Using mamba (faster):**
    ```bash
    mamba env create -f environment.yml
    ```

    ## Mamba vs Conda

    **Mamba advantages:**
    - **Speed**: 5-10x faster package resolution and installation
    - **Better error messages**: More informative when conflicts occur
    - **Parallel downloads**: Downloads packages in parallel
    - **Same interface**: Drop-in replacement for conda commands
    - **Better dependency solving**: More robust solver algorithm

    **When to use Mamba:**
    - Large environments with many packages
    - Frequent package installations/updates
    - Complex dependency resolution scenarios
    - When conda feels slow

    **Mamba command equivalents:**
    ```bash
    # Replace 'conda' with 'mamba' in any command
    mamba install package_name
    mamba create -n env_name python=3.9
    mamba env export > environment.yml
    mamba list
    mamba search package_name
    ```

    ## When to Use Conda/Mamba

    - Working with scientific computing packages
    - Need packages from multiple languages (Python, R, C++)
    - Working with complex binary dependencies
    - Need pre-compiled packages for performance
    - Large environments with many packages (prefer mamba)

=== "uv"

    [uv](https://github.com/astral-sh/uv) is an extremely fast Python package installer and resolver, written in Rust. It's designed as a drop-in replacement for pip and pip-tools.

    ## Installation

    Install uv using pip:
    ```bash
    pip install uv
    ```

    Or using curl (on Unix systems):
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    ## Creating a Virtual Environment

    1. Create a new virtual environment:
        ```bash
        uv venv myresearch
        ```

    2. Activate the environment:
        - On Unix/macOS: `source myresearch/bin/activate`
        - On Windows: `myresearch\Scripts\activate`

    3. Install packages:
        ```bash
        uv pip install numpy pandas matplotlib scipy
        ```

    ## Managing Dependencies

    Create a `requirements.txt` file:
    ```bash
    uv pip freeze > requirements.txt
    ```

    Install from requirements:
    ```bash
    uv pip install -r requirements.txt
    ```

    For development dependencies, use `requirements-dev.txt`:
    ```bash
    uv pip install -r requirements-dev.txt
    ```

    ## When to Use uv

    - Want the fastest package installation
    - Working primarily with pure Python packages
    - Need a drop-in replacement for pip
    - Want minimal overhead

=== "Poetry"

    [Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and manages them for you.

    ## Installation

    Install Poetry using the official installer:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Or using pip:
    ```bash
    pip install poetry
    ```

    ## Creating a New Project

    1. Create a new project:
        ```bash
        poetry new myresearch
        cd myresearch
        ```

    2. Or initialize Poetry in an existing project:
        ```bash
        cd myresearch
        poetry init
        ```

    ## Managing Dependencies

    1. Add dependencies:
        ```bash
        poetry add numpy pandas matplotlib scipy
        ```

    2. Add development dependencies:
        ```bash
        poetry add --group dev pytest black flake8
        ```

    3. Install all dependencies:
        ```bash
        poetry install
        ```

    4. Activate the virtual environment:
        ```bash
        poetry shell
        ```

    ## Configuration File

    Poetry uses `pyproject.toml` to manage project configuration:

    ```toml
    [tool.poetry]
    name = "myresearch"
    version = "0.1.0"
    description = "My research project"
    authors = ["Your Name <your.email@example.com>"]

    [tool.poetry.dependencies]
    python = "^3.9"
    numpy = "^1.21.0"
    pandas = "^1.3.0"
    matplotlib = "^3.4.0"
    scipy = "^1.7.0"

    [tool.poetry.group.dev.dependencies]
    pytest = "^6.2.0"
    black = "^21.0.0"
    flake8 = "^3.9.0"

    [build-system]
    requires = ["poetry-core>=1.0.0"]
    build-backend = "poetry.core.masonry.api"
    ```

    ## When to Use Poetry

    - Building distributable Python packages
    - Need sophisticated dependency resolution
    - Want integrated project management
    - Prefer declarative dependency management

## Best Practices

1. **Always use virtual environments** to isolate project dependencies
2. **Pin dependency versions** for reproducibility
3. **Document your environment setup** in your project README
4. **Use lock files** (`poetry.lock`, `conda-lock`) when available
5. **Keep development and production dependencies separate**
6. **Regularly update dependencies** while testing for compatibility

## Reproducibility Tips

- Include environment files (`environment.yml`, `pyproject.toml`, `requirements.txt`) in version control
- Document the Python version and environment manager used
- Consider using Docker for ultimate reproducibility
- Test your environment setup on different machines
