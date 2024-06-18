from pathlib import Path


def project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).parent.parent.parent.parent


def src_dir() -> Path:
    return project_root() / "src"


def cmds_dir() -> Path:
    return src_dir() / "healgen" / "cmds"


def subcommand_dir() -> Path:
    return Path(__file__).parent.parent / 'cmds'


def main():
    print(cmds_dir())


if __name__ == "__main__":
    main()
