import os
import subprocess
import sys

# Obtener la ruta absoluta del directorio del proyecto
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
# Ruta al entorno Conda
CONDA_ENV = os.path.join(PROJECT_DIR, "env")


def run_command(command, capture_output=False, use_conda=False):
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
    print("Instalando pre-commit")
    run_command("pre-commit install", use_conda=True)


def init_git():
    """Initialize git repository."""
    print("Inicializando Git...")
    run_command("git init")
    run_command("git branch -m main")


def create_conda_env():
    """Create conda environment."""
    print("Instalación de dependencias...")
    run_command(f"conda env create --prefix {CONDA_ENV} --file environment.yml")
    install_pre_commit()


def show_logo():
    """Show project logo."""
    logo = """
    \033[1m\033[33m█▀ █▀▀ █▄░█ ▀█▀ █░█\033[0m  ┎┤ Ciencia de Datos          ├┒
    \033[1m\033[33m▄█ ██▄ █░▀█ ░█░ █▄█\033[0m  ┖┤ con \033[1mPython\033[0m en \033[1m\033[0m Archlinux ├┚
                .studio
    """
    print(logo)


def help():
    """Show help message."""
    show_logo()
    print("\n\033[1mComandos disponibles:\033[0m")
    commands = [
        ("help", "Muestra la ayuda en pantalla"),
        ("init", "Inicializa Git e instala dependencias con Anaconda"),
        ("env", "Comando para activar el entorno virtual con Anaconda"),
        ("tests", "Ejecuta pruebas con pytest"),
        ("docs", "Construye y sirve la documentación con MkDocs"),
        ("db-up", "Levanta la base de datos postgres con docker compose"),
        ("db-down", "Detiene la base de datos postgres"),
    ]
    for cmd, desc in commands:
        print(f"\033[36m{cmd:<20}\033[0m {desc}")


def run_tests():
    """Run tests with pytest."""
    print("Ejecutando pruebas...")
    run_command("pytest", use_conda=True)


def build_docs():
    """Build and serve documentation with MkDocs."""
    print("Construyendo cache de la documentación...")
    run_command("mkdocs build", use_conda=True)
    print("Sirviendo la documentación...")
    run_command("mkdocs serve", use_conda=True)


def db_up():
    """Start the PostgreSQL database with Docker Compose."""
    print("Levanta la base de datos postgres con docker compose")
    run_command("docker compose up -d")


def db_down():
    """Stop the PostgreSQL database."""
    print("Detiene la base de datos")
    run_command("docker compose down")


def print_activate_command():
    """Print the command to activate the conda environment."""
    print("Para activar el entorno Conda, ejecuta el siguiente comando en tu terminal:")
    print(
        f'\033[1meval "$(conda shell.bash hook)" && conda activate "{CONDA_ENV}"\033[0m'
    )


def main():
    if len(sys.argv) < 2:
        help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "help":
        help()
    elif command == "init":
        show_logo()
        init_git()
        create_conda_env()
    elif command == "env":
        show_logo()
        print_activate_command()
    elif command == "tests":
        show_logo()
        run_tests()
    elif command == "docs":
        show_logo()
        build_docs()
    elif command == "db-up":
        show_logo()
        db_up()
    elif command == "db-down":
        show_logo()
        db_down()
    else:
        print(f"Comando no reconocido: {command}")
        help()
        sys.exit(1)


if __name__ == "__main__":
    main()
