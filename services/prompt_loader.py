from pathlib import Path

PROMPTS_DIR = Path("prompts")


def load_prompt(template_name, user_prompt):
    file_path = PROMPTS_DIR / f"{template_name}.txt"

    with open(file_path, "r") as file:
        template = file.read()

    return template.replace("{user_prompt}", user_prompt)
