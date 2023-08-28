import argparse
import os
import tomllib
from pathlib import Path
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def main(args: argparse.Namespace) -> None:
    file_content = args.file_path.read_text("utf-8")
    settings = Settings.load(Path("settings.toml"))
    if settings.model_supports_chat_completions:
        print(get_chat_completion(file_content, settings))
    else:
        print(get_completion(file_content, settings))

def parse_args() -> argparse.Namespace:
    """Parse command-line input."""
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path, help="Path to the input file")
    return parser.parse_args()

if __name__ == "__main__":
    main(parse_args())