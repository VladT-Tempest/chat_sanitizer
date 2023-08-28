import argparse
import os
import tomllib
from pathlib import Path
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class Settings(dict):
    """Handle loading and accessing application settings from file."""

    @classmethod
    def load(cls, path) -> "Settings":
        """Load tomllib settings file and pass it to class constuctor."""
        with path.open("rb") as file:
            return cls(tomllib.load(file))

    def __init__(self, *args, **kwargs) -> None:
        """Add general settings and prompts as instance attributes."""
        super().__init__(*args, **kwargs)
        # Settings
        self.chat_models = self["general"]["chat_models"]
        self.model = self["general"]["model"]
        self.max_tokens = self["general"]["max_tokens"]
        self.temperature = self["general"]["temperature"]
        self.model_supports_chat_completions = self.model in self.chat_models
        # Prompts
        self.instruction_prompt = self["prompts"]["instruction_prompt"]
        self.role_prompt = self["prompts"]["role_prompt"]
        self.positive_example = self["prompts"]["positive_example"]
        self.positive_reasoning = self["prompts"]["positive_reasoning"]
        self.positive_output = self["prompts"]["positive_output"]
        self.negative_example = self["prompts"]["negative_example"]
        self.negative_reasoning = self["prompts"]["negative_reasoning"]
        self.negative_output = self["prompts"]["negative_output"]

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

def get_completion(content: str, settings: Settings) -> str:
    """  OpenAI’s GPT-3.5 model (text-davinci-003) """
    message = "get_completion in process!"
    return message

def get_chat_completion(content: str, settings: Settings) -> str:
    """ OpenAI’s GPT-4 model (gpt-4) """
    message = "get_chat_completion in process!"
    return message

if __name__ == "__main__":
    main(parse_args())