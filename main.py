from commands.troubleshoot import troubleshoot_generator
from commands.aws import aws_generator
from commands.linux import linux_generator
from commands.jenkins import jenkins_generator
from commands.kubernetes import kubernetes_generator
from commands.terraform import terraform_generator
from commands.docker import docker_generator
from rich.console import Console
from rich.panel import Panel

console = Console()


def show_menu():
    console.print(
        Panel.fit(
            "[bold cyan]AI DevOps CLI Assistant[/bold cyan]",
            border_style="green"
        )
    )

    console.print("[bold yellow]1.[/bold yellow] Dockerfile Generator")
    console.print("[bold yellow]2.[/bold yellow] Kubernetes Generator")
    console.print("[bold yellow]3.[/bold yellow] Terraform Generator")
    console.print("[bold yellow]4.[/bold yellow] Jenkins Generator")
    console.print("[bold yellow]5.[/bold yellow] Linux Assistant")
    console.print("[bold yellow]6.[/bold yellow] AWS Architecture")
    console.print("[bold yellow]7.[/bold yellow] Troubleshooter")
    console.print("[bold yellow]8.[/bold yellow] Exit")

def docker():
    docker_generator()

def kubernetes():
    kubernetes_generator()


def terraform():
    terraform_generator()

def jenkins():
    jenkins_generator()


def linux():
    linux_generator()


def aws():
    aws_generator()


def troubleshoot():
    troubleshoot_generator()


def main():
    while True:
        show_menu()

        choice = input("\nSelect an option: ")

        if choice == "1":
            docker()

        elif choice == "2":
            kubernetes()

        elif choice == "3":
            terraform()

        elif choice == "4":
            jenkins()

        elif choice == "5":
            linux()

        elif choice == "6":
            aws()

        elif choice == "7":
            troubleshoot()

        elif choice == "8":
            console.print("\n Exiting AI DevOps CLI Assistant...")
            break

        else:
            console.print("\n Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
