import os
import subprocess
import sys

import typer

# Initialize Typer app
app = typer.Typer()

# Get the absolute path of the project directory
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
# Path to the Conda environment
CONDA_ENV = os.path.join(PROJECT_DIR, "env")


def run_command(command: str, capture_output: bool = False, use_conda: bool = False):
    """Run a shell command."""
    if use_conda:
        command = f'eval "$(conda shell.bash hook)" && conda activate "{CONDA_ENV}" && {command}'
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=capture_output
        )
        if capture_output:
            return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode() if e.stderr else str(e)
        print(f"Error: {stderr}")
        sys.exit(e.returncode)


def install_pre_commit():
    """Install pre-commit."""
    print("Installing pre-commit...")
    run_command("pre-commit install", use_conda=True)


@app.command()
def init():
    """Initialize Git and install dependencies with Conda."""
    show_logo()
    print("Initializing Git...")
    run_command("git init")
    run_command("git branch -m main")
    print("Installing dependencies...")
    run_command(f"conda env create --prefix {CONDA_ENV} --file environment.yml")
    install_pre_commit()


@app.command()
def env():
    """Show the command to activate the Conda environment."""
    show_logo()
    print_activate_command()


@app.command()
def tests():
    """Run tests with pytest."""
    show_logo()
    print("Running tests...")
    run_command("pytest", use_conda=True)


@app.command()
def docs():
    """Build and serve documentation with MkDocs."""
    show_logo()
    print("Building documentation cache...")
    run_command("mkdocs build", use_conda=True)
    print("Serving documentation...")
    run_command("mkdocs serve", use_conda=True)


@app.command()
def db_up():
    """Start the PostgreSQL database with Docker Compose."""
    show_logo()
    print("Starting PostgreSQL database with Docker Compose...")
    run_command("docker compose up -d")


@app.command()
def db_down():
    """Stop the PostgreSQL database."""
    show_logo()
    print("Stopping PostgreSQL database...")
    run_command("docker compose down")


def show_logo():
    """Show project logo."""
    logo = """
    \033[1m\033[33m█▀ █▀▀ █▄░█ ▀█▀ █░█\033[0m  ┎┤ Data Science          ├┒
    \033[1m\033[33m▄█ ██▄ █░▀█ ░█░ █▄█\033[0m  ┖┤ with \033[1mPython\033[0m on \033[1m\033[0m Archlinux ├┚
                .studio
    """
    print(logo)


def print_activate_command():
    """Print the command to activate the Conda environment."""
    print(
        "To activate the Conda environment, run the following command in your terminal:"
    )
    print("\033[1meval conda activate ./env\033[0m")


if __name__ == "__main__":
    app()
