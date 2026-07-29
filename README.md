#  AI-Powered DevOps CLI Assistant

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/main/images/Project%20banner.png?raw=true" alt="AI-Powered DevOps CLI Assistant Banner" width="100%">
</p>

<p align="center">
  <strong>An AI-powered command-line assistant that helps DevOps engineers generate infrastructure, automation, and troubleshooting solutions using a local Ollama LLM.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-Cloud-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/DevOps-Automation-0A66C2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

---

##  About the Project

**AI-Powered DevOps CLI Assistant** is a local AI-based command-line application built for DevOps engineers, cloud engineers, and learners. Instead of searching through documentation or writing configuration files manually, you can describe what you need in plain English, and the assistant generates ready-to-use DevOps configurations using a locally running Ollama model.

Everything runs locally, making the project fast, private, and suitable for offline development.

###  What it can do

*  Generate production-ready Dockerfiles
*  Generate Terraform configurations
*  Generate Kubernetes YAML manifests
*  Create Declarative Jenkins Pipelines
*  Answer Linux administration questions
*  Design AWS architectures and best practices
*  Troubleshoot common DevOps issues
*  Save generated files automatically for immediate use

---

> **Built with ❤️ using Python, Ollama, Rich, and modern DevOps practices.**
---

#  Development Environment

This project was developed and tested on an **AWS EC2 Ubuntu instance**, where Ollama runs locally to generate DevOps configurations without relying on external AI APIs.

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/main/images/Screenshot%202026-07-29%20150614.png?raw=true" alt="AWS EC2 Instance" width="95%">
</p>

### EC2 Configuration

| Configuration | Details |
|---------------|---------|
| **Cloud Provider** | AWS EC2 |
| **Operating System** | Ubuntu Server 24.04 LTS |
| **Instance Type** | **m7i.large** |
| **vCPU** | 2 |
| **Memory** | 8 GB RAM |
| **Storage** | 30 GB EBS |
| **Python Version** | Python 3.14 |
| **AI Runtime** | Ollama |
| **LLM** | qwen2.5:3b |
| **Development Mode** | Local AI Inference |

>  **Why m7i.large?**
>
> I selected an **AWS EC2 m7i.large** instance because it provides **2 vCPUs and 8 GB RAM**, which is sufficient to run a lightweight local language model (`qwen2.5:3b`) with Ollama while developing and testing the AI-powered DevOps CLI. Running the model locally keeps the project private, avoids API costs, and demonstrates how AI-assisted DevOps workflows can be built on cloud infrastructure.

---
# Phase 1 – Prepare Ubuntu Server

This project was developed on an **AWS EC2 Ubuntu 24.04 LTS** instance. Before building the application, update the operating system and install the required development tools.

---

## Update Ubuntu Packages

Update the package repository:

```bash
sudo apt update
```

Upgrade installed packages:

```bash
sudo apt upgrade -y
```

Remove unused packages:

```bash
sudo apt autoremove -y
```

Verify the operating system:

```bash
lsb_release -a
```

Expected Output

```text
Distributor ID: Ubuntu
Description:    Ubuntu 24.04 LTS
Release:        24.04
Codename:       noble
```

---

## Install Development Tools

Install the required packages:

```bash
sudo apt install -y \
git \
python3 \
python3-pip \
python3-venv \
curl \
build-essential
```

Verify the installation:

```bash
python3 --version
git --version
pip3 --version
```

Example Output

```text
Python 3.14.x
git version 2.x.x
pip 25.x.x
```

---

# Install Ollama

Ollama is used as the local Large Language Model (LLM) runtime for this project. It processes user prompts locally and generates DevOps configurations without relying on external AI APIs.

---

## Install Ollama

Run the official installation script:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation:

```bash
ollama --version
```

Example Output

```text
ollama version 0.11.x
```

---

## Installation Output

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/main/images/olamma%20installation.png?raw=true" alt="Ollama Installation" width="100%">
</p>

---

## Download the Language Model

Download the lightweight model used by the application:

```bash
ollama pull qwen2.5:3b
```

Verify the downloaded model:

```bash
ollama list
```

Example Output

```text
NAME          SIZE
qwen2.5:3b    2.0 GB
```

---

## Test the Model

Start an interactive session:

```bash
ollama run qwen2.5:3b
```

Example Prompt

```text
Create a Dockerfile for a FastAPI application.
```

Exit the interactive session:

```text
/bye
```

---

## Verify the Ollama API

Confirm that the local API server is running:

```bash
curl http://localhost:11434/api/tags
```

Example Output

```json
{
  "models": [
    {
      "name": "qwen2.5:3b"
    }
  ]
}
```

---

## Phase Summary

At this stage, Ollama has been successfully installed and configured on the Ubuntu server. The local AI model is ready to generate DevOps configurations, making the application completely offline and independent of external AI services.
# Main Entry Point (`main.py`)

The `main.py` file serves as the entry point of the application. It provides an interactive command-line interface (CLI) where users can choose different DevOps automation tasks.

### Responsibilities

- Displays the main CLI menu.
- Accepts user input.
- Routes requests to the appropriate module.
- Integrates with the Ollama-powered AI engine.
- Provides a simple and interactive user experience.

### Available Features

- Dockerfile Generator
- Kubernetes YAML Generator
- Terraform Generator
- Jenkins Pipeline Generator
- Linux Assistant
- AWS Architecture Generator
- DevOps Troubleshooter

---

## Source Code (`main.py`)

The application starts from the `main.py` file, which provides the interactive command-line interface and routes user requests to the appropriate DevOps modules.

**View the source code:**

➡️ **[`main.py`](https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/main/main.py)**

---

### Responsibilities

- Displays the interactive CLI menu.
- Accepts user input.
- Routes requests to the appropriate generator module.
- Integrates with the Ollama-powered AI engine.
- Provides a simple and interactive user experience.
- # Dockerfile Generator

The Dockerfile Generator enables users to create production-ready Dockerfiles using natural language. It accepts application requirements from the command line, sends the prompt to the local Ollama language model, and automatically generates a Dockerfile following Docker best practices.

---

## Features

- Generate Dockerfiles from plain English prompts.
- Uses a locally running Ollama language model.
- Produces production-ready Dockerfiles.
- Automatically saves the generated Dockerfile to the `output/` directory.
- Supports various application frameworks and runtimes.

---

## Source Code

The implementation of the Docker Generator is available here:

**Python Source:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/cc242e2d70c94bd871d59fc9614eed01c31c7ac5/commands/docker.py

---

## Workflow

```text
User Prompt
      │
      ▼
Docker Generator
      │
      ▼
Load Docker Prompt Template
      │
      ▼
Ollama (qwen2.5:3b)
      │
      ▼
Generate Dockerfile
      │
      ▼
Save as output/Dockerfile
      │
      ▼
Display Generated Output
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/main/images/docker%20generator.png?raw=true" alt="Docker Generator Demo" width="95%">
</p>

---

## Generated Output

The generated Dockerfile can be viewed here:

**Dockerfile Output:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/cc242e2d70c94bd871d59fc9614eed01c31c7ac5/output/Dockerfile

---

## Sample Prompt

```text
Generate a production-ready multi-stage Dockerfile for a FastAPI application using Python 3.12 slim. Install dependencies from requirements.txt, use Docker layer caching, create a non-root user, expose port 8000, include a HEALTHCHECK, optimize the image size, and start the application with Gunicorn and Uvicorn workers.
```

---

## Generated File

```text
output/
└── Dockerfile
```

---

## Outcome

The Docker Generator transforms natural language requirements into a production-ready Dockerfile using a local AI model. This significantly reduces manual effort, improves consistency, and accelerates containerization for modern applications.
