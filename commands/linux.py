from rich.console import Console

from services.ollama_service import generate_response
from services.file_service import save_output

console = Console()


def linux_generator():

    console.print("\n🐧 Linux Assistant\n")

    user_prompt = input(
        "Ask your Linux question:\n> "
    )

    console.print(
        "\nGenerating Linux Solution...\n"
    )

    result = generate_response(
        "linux",
        user_prompt
    )

    saved_file = save_output(
        "linux",
        "linux_commands.txt",
        result
    )

    console.print(result)

    console.print(
        f"\n✅ Saved to: {saved_file}"
    )
