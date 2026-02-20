from pathlib import Path
import sys


def _ensure_src_on_path() -> None:
    repo_root = Path(__file__).resolve().parent
    src_dir = repo_root / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))


def main() -> None:
    _ensure_src_on_path()
    from tax_prep_assistant.ui.streamlit_app import run

    run()


if __name__ == "__main__":
    main()
