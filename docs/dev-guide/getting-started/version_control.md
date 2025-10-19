# Version Control with Git and GitHub

Version control is essential for reproducible research, allowing you to track changes, collaborate with others, and maintain a history of your project. This guide covers Git fundamentals and GitHub integration for research projects.

## Installation

=== "Windows"

    ### Git for Windows
    - Download from [git-scm.com](https://git-scm.com/downloads)
    - Run the installer and follow the setup wizard
    - Choose your preferred options (recommended: use Git from command line and 3rd-party software)

    ### Package Manager
    ```bash
    # Using winget
    winget install Git.Git

    # Using Chocolatey
    choco install git

    # Using Scoop
    scoop install git
    ```

=== "macOS"

    ### Homebrew (Recommended)
    ```bash
    brew install git
    ```

    ### Direct Download
    - Download from [git-scm.com](https://git-scm.com/downloads)
    - Run the installer package

    ### Xcode Command Line Tools
    ```bash
    xcode-select --install
    ```
    This installs Git along with other development tools.

=== "Linux"

    ### Ubuntu/Debian
    ```bash
    sudo apt update
    sudo apt install git
    ```

    ### CentOS/RHEL/Fedora
    ```bash
    # CentOS/RHEL 7
    sudo yum install git

    # CentOS/RHEL 8+ / Fedora
    sudo dnf install git
    ```

    ### Arch Linux
    ```bash
    sudo pacman -S git
    ```

    ### openSUSE
    ```bash
    sudo zypper install git
    ```

## Git Fundamentals

Git is a distributed version control system that tracks changes in your files and coordinates work between multiple people.

### Initial Configuration

Set up your identity (required for commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Optional but recommended configurations:
```bash
# Set default branch name
git config --global init.defaultBranch main

# Enable colored output
git config --global color.ui auto

# Set default editor
git config --global core.editor "code --wait"  # VS Code
# git config --global core.editor "nano"       # Nano
```

### Repository Initialization

#### Starting a New Repository

1. **Initialize in existing project**:
    ```bash
    cd your-project-directory
    git init
    ```

2. **Clone existing repository**:
    ```bash
    git clone https://github.com/username/repository-name.git
    cd repository-name
    ```

### Basic Git Workflow

#### 1. Check Status
```bash
git status
```

#### 2. Stage Changes
```bash
# Stage specific files
git add filename.py

# Stage all changes
git add .

# Stage all Python files
git add *.py
```

#### 3. Commit Changes
```bash
# Commit with message
git commit -m "Add data analysis functions"

# Commit with detailed message
git commit -m "Add data analysis functions

- Implement statistical summary functions
- Add data visualization utilities
- Include unit tests for new functions"
```

#### 4. View History
```bash
# View commit history
git log

# Compact view
git log --oneline

# Graphical view
git log --graph --oneline --all
```

### Working with Branches

Branches allow you to work on different features or experiments without affecting the main codebase.

```bash
# Create and switch to new branch
git checkout -b feature-analysis

# Or using newer syntax
git switch -c feature-analysis

# List branches
git branch

# Switch branches
git checkout main
git switch main

# Merge branch
git checkout main
git merge feature-analysis

# Delete branch
git branch -d feature-analysis
```

### .gitignore File

Create a `.gitignore` file to exclude files that shouldn't be tracked:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Jupyter Notebook
.ipynb_checkpoints

# Data files (be selective)
*.csv
*.xlsx
*.json
data/raw/
data/processed/

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Research specific
*.log
results/
figures/
*.pdf
```

Use [gitignore.io](https://www.toptal.com/developers/gitignore) to generate comprehensive `.gitignore` files.

### Advanced Git Topics

#### Resolving Merge Conflicts
```bash
# When conflicts occur during merge
git status                    # See conflicted files
# Edit files to resolve conflicts
git add resolved-file.py
git commit
```

#### Undoing Changes
```bash
# Unstage file
git reset HEAD filename.py

# Discard local changes
git checkout -- filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

#### Stashing Changes
```bash
# Stash current changes
git stash

# Apply stashed changes
git stash pop

# List stashes
git stash list
```

## GitHub Integration

GitHub is a web-based hosting service for Git repositories, providing collaboration tools, issue tracking, and project management features.

### Setting Up GitHub

1. **Create Account**: Visit [github.com](https://github.com) and sign up
2. **Set up SSH Keys** (recommended for security):

    ```bash
    # Generate SSH key
    ssh-keygen -t ed25519 -C "your.email@example.com"

    # Start SSH agent
    eval "$(ssh-agent -s)"

    # Add key to agent
    ssh-add ~/.ssh/id_ed25519

    # Copy public key to clipboard
    cat ~/.ssh/id_ed25519.pub
    ```

3. **Add SSH Key to GitHub**:
    - Go to GitHub Settings > SSH and GPG keys
    - Click "New SSH key"
    - Paste your public key

### Creating a Repository on GitHub

#### Method 1: Create on GitHub First
1. Go to GitHub and click "New repository"
2. Fill in repository details
3. Clone to your local machine:
    ```bash
    git clone git@github.com:username/repository-name.git
    ```

#### Method 2: Push Existing Local Repository
1. Create empty repository on GitHub (don't initialize with README)
2. Add remote origin:
    ```bash
    git remote add origin git@github.com:username/repository-name.git
    git branch -M main
    git push -u origin main
    ```

### Working with Remotes

```bash
# View remotes
git remote -v

# Add remote
git remote add upstream git@github.com:original-owner/repository.git

# Fetch changes
git fetch origin

# Pull changes (fetch + merge)
git pull origin main

# Push changes
git push origin main

# Push new branch
git push -u origin feature-branch
```

### Collaboration Workflow

#### Fork and Pull Request Model

1. **Fork the repository** on GitHub
2. **Clone your fork**:
    ```bash
    git clone git@github.com:yourusername/repository.git
    ```
3. **Add upstream remote**:
    ```bash
    git remote add upstream git@github.com:originalowner/repository.git
    ```
4. **Create feature branch**:
    ```bash
    git checkout -b feature-improvement
    ```
5. **Make changes and commit**
6. **Push to your fork**:
    ```bash
    git push origin feature-improvement
    ```
7. **Create Pull Request** on GitHub

#### Keeping Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Switch to main branch
git checkout main

# Merge upstream changes
git merge upstream/main

# Push updates to your fork
git push origin main
```

### GitHub Features for Research

#### Issues and Project Management
- **Issues**: Track bugs, feature requests, and tasks
- **Labels**: Categorize issues (bug, enhancement, documentation)
- **Milestones**: Group issues for releases or project phases
- **Projects**: Kanban-style project management

#### Documentation
- **README.md**: Project overview and setup instructions
- **Wiki**: Detailed documentation
- **GitHub Pages**: Host project websites

#### Releases and Tags
```bash
# Create tag
git tag -a v1.0.0 -m "First release"

# Push tags
git push origin --tags
```

Create releases on GitHub to distribute your research code.

#### GitHub Actions (CI/CD)
Create `.github/workflows/tests.yml` for automated testing:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest
    - name: Run tests
      run: pytest
```

## Best Practices

### Repository Structure
```
research-project/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt          # or pyproject.toml
├── data/
│   ├── raw/                 # Original, immutable data
│   ├── processed/           # Cleaned, processed data
│   └── external/            # External datasets
├── notebooks/               # Jupyter notebooks
│   ├── exploratory/
│   └── reports/
├── src/                     # Source code
│   ├── __init__.py
│   ├── data/               # Data processing
│   ├── features/           # Feature engineering
│   ├── models/             # Model definitions
│   └── visualization/      # Plotting functions
├── tests/                  # Unit tests
├── docs/                   # Documentation
├── results/                # Model outputs, figures
└── scripts/                # Utility scripts
```

### Commit Message Guidelines

Use conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

Examples:
```bash
git commit -m "feat(analysis): add statistical summary functions"
git commit -m "fix(data): handle missing values in preprocessing"
git commit -m "docs: update installation instructions"
```

### Data Management

#### Large Files
- Use **Git LFS** (Large File Storage) for large datasets:
  ```bash
  git lfs install
  git lfs track "*.csv"
  git lfs track "*.xlsx"
  git add .gitattributes
  ```

- Consider external storage (cloud services, institutional repositories)
- Document data sources and access methods

#### Sensitive Data
- Never commit sensitive data (passwords, API keys, personal data)
- Use environment variables or config files (excluded from Git)
- Consider data anonymization techniques

### Reproducibility

#### Environment Documentation
- Include `requirements.txt`, `environment.yml`, or `pyproject.toml`
- Document Python version and OS requirements
- Consider using Docker for complete environment specification

#### Code Organization
- Write modular, reusable functions
- Include docstrings and comments
- Separate data processing, analysis, and visualization

#### Documentation
- Maintain comprehensive README with:
  - Project description and objectives
  - Installation and setup instructions
  - Usage examples
  - Data sources and methodology
  - Results and conclusions

### Collaboration Guidelines

1. **Establish workflow**: Agree on branching strategy and review process
2. **Code review**: Use pull requests for all changes
3. **Issue tracking**: Document bugs, features, and discussions
4. **Communication**: Use clear commit messages and PR descriptions
5. **Testing**: Implement automated tests where possible

## Resources

- [Pro Git Book](https://git-scm.com/book) - Comprehensive Git documentation
- [GitHub Guides](https://guides.github.com/) - GitHub-specific tutorials
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [gitignore.io](https://www.toptal.com/developers/gitignore) - Generate .gitignore files
