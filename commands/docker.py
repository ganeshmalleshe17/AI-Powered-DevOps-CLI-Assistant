from rich.console import Console

from services.ollama_service import generate_response
from services.file_service import save_output

console = Console()


def docker_generator():

    console.print("\n🐳 Dockerfile Generator\n")

    user_prompt = input("Describe your application:\n> ")

    console.print("\nGenerating Dockerfile...\n")

    dockerfile = generate_response(
        "docker",
        user_prompt
    )

    saved_file = save_output(
        "",
        "Dockerfile",
        dockerfile
    )

    console.print("\n✅ Dockerfile generated successfully!")
    console.print(f"📁 Saved to: {saved_file}")
