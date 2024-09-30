# Run pre-commit hooks on all files
pc:
    pre-commit run --all-files

# Serve the MkDocs hooks on all files
serve:
    poetry run mkdocs serve
