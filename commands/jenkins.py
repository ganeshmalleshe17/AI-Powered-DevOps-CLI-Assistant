from rich.console import Console

from services.ollama_service import generate_response
from services.file_service import save_output

console = Console()


def jenkins_generator():

    console.print("\n⚙ Jenkins Pipeline Generator\n")

    user_prompt = input(
        "Describe your CI/CD pipeline:\n> "
    )

    console.print(
        "\nGenerating Jenkins Pipeline...\n"
    )

    result = generate_response(
        "jenkins",
        user_prompt
    )

    saved_file = save_output(
        "jenkins",
        "Jenkinsfile",
        result
    )

    console.print(
        "\n✅ Jenkinsfile generated successfully!"
    )

    console.print(
        f"📁 Saved to: {saved_file}"
    )
