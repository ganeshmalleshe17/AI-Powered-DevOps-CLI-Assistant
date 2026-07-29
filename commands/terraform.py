from rich.console import Console

from services.ollama_service import generate_response
from services.file_service import save_output

console = Console()


def terraform_generator():

    console.print("\n🌍 Terraform Generator\n")

    user_prompt = input("Describe your infrastructure:\n> ")

    console.print("\nGenerating Terraform configuration...\n")

    terraform_code = generate_response(
        "terraform",
        user_prompt
    )

    # Save generated Terraform files

    save_output(
        "terraform",
        "providers.tf",
        ""
    )

    save_output(
        "terraform",
        "variables.tf",
        ""
    )

    main_file = save_output(
        "terraform",
        "main.tf",
        terraform_code
    )

    save_output(
        "terraform",
        "outputs.tf",
        ""
    )

    console.print("\n✅ Terraform files generated successfully!")
    console.print(f"📁 Main file saved to: {main_file}")
