from rich.console import Console

from services.ollama_service import generate_response
from services.file_service import save_output

console = Console()


def troubleshoot_generator():

    console.print("\n🛠 DevOps Troubleshooter\n")

    user_prompt = input(
        "Enter the error or issue:\n> "
    )

    console.print(
        "\nAnalyzing issue...\n"
    )

    result = generate_response(
        "troubleshoot",
        user_prompt
    )

    saved_file = save_output(
        "troubleshooter",
        "troubleshooting.md",
        result
    )

    console.print(result)

    console.print(
        f"\n✅ Saved to: {saved_file}"
    )
