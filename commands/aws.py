from rich.console import Console

from services.ollama_service import generate_response
from services.file_service import save_output

console = Console()


def aws_generator():

    console.print("\n☁ AWS Architecture Generator\n")

    user_prompt = input(
        "Describe your AWS architecture requirement:\n> "
    )

    console.print(
        "\nGenerating AWS Architecture...\n"
    )

    result = generate_response(
        "aws",
        user_prompt
    )

    saved_file = save_output(
        "aws",
        "aws_architecture.md",
        result
    )

    console.print(result)

    console.print(
        f"\n✅ Saved to: {saved_file}"
    )
