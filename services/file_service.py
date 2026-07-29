from pathlib import Path


def save_output(folder_name, file_name, content):

    output_dir = Path("output") / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / file_name

    with open(output_file, "w") as file:
        file.write(content)

    return output_file.resolve()
