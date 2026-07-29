from rich.console import Console

from services.ollama_service import generate_response
from services.file_service import save_output

console = Console()


def kubernetes_generator():

    console.print("\n☸ Kubernetes Generator\n")

    user_prompt = input(
        "Describe your application:\n> "
    )

    console.print(
        "\nGenerating Kubernetes YAML...\n"
    )

    result = generate_response(
        "kubernetes",
        user_prompt
    )

    deployment = save_output(
        "kubernetes",
        "deployment.yaml",
        result
    )

    save_output(
        "kubernetes",
        "service.yaml",
        ""
    )

    save_output(
        "kubernetes",
        "ingress.yaml",
        ""
    )

    console.print(
        "\n✅ Kubernetes files generated successfully!"
    )

    console.print(
        f"📁 Deployment saved to: {deployment}"
    )
