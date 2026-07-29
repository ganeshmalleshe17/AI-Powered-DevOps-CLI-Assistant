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
# Kubernetes Generator

The Kubernetes Generator converts natural language prompts into Kubernetes manifests using a locally running Ollama language model. It helps automate the creation of deployment configurations by generating Kubernetes YAML files that can be used as a starting point for deploying containerized applications.

---

## Features

- Generate Kubernetes manifests from plain English requirements.
- Uses a locally running Ollama language model.
- Creates Kubernetes deployment configurations automatically.
- Saves generated manifests in the `output/kubernetes` directory.
- Simplifies Kubernetes deployment configuration for developers and DevOps engineers.

---

## Source Code

The implementation of the Kubernetes Generator is available here:

**Python Source:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/commands/kubernetes.py

---

## Workflow

```text
User Prompt
      │
      ▼
Kubernetes Generator
      │
      ▼
Load Kubernetes Prompt Template
      │
      ▼
Ollama (qwen2.5:3b)
      │
      ▼
Generate Kubernetes Manifests
      │
      ▼
Save Output Files
      │
      ▼
Display Generated Result
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/images/kubernetes%20generator.png?raw=true" alt="Kubernetes Generator Demo" width="95%">
</p>

---

## Generated Output

The generated Kubernetes manifests can be viewed here:

**Output Directory:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/tree/3f0f95c28e81283aaed3ecf63897dcfa565233bd/output/kubernetes

Generated files include:

- `deployment.yaml`
- `service.yaml`
- `ingress.yaml`

---

## Sample Prompt

```text
Generate Kubernetes manifests for a FastAPI application with two replicas, ClusterIP service, resource requests and limits, readiness and liveness probes, and an NGINX Ingress exposing the application.
```

---

## Generated Files

```text
output/
└── kubernetes/
    ├── deployment.yaml
    ├── service.yaml
    └── ingress.yaml
```

---

## Outcome

The Kubernetes Generator transforms natural language requirements into Kubernetes YAML manifests using a local AI model. It accelerates the process of creating deployment configurations, reduces manual YAML writing, and provides a solid foundation for deploying containerized applications on Kubernetes clusters.
# Terraform Generator

The Terraform Generator enables users to generate Infrastructure as Code (IaC) using natural language. It accepts infrastructure requirements from the command line, sends the request to the local Ollama language model, and generates Terraform configuration files that can be used as the foundation for provisioning cloud infrastructure.

---

## Features

- Generate Terraform configurations using natural language.
- Uses a locally running Ollama language model.
- Automatically creates Terraform project files.
- Saves generated files in the `output/terraform` directory.
- Simplifies Infrastructure as Code (IaC) creation for AWS environments.

---

## Source Code

The implementation of the Terraform Generator is available here:

**Python Source:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/commands/terraform.py

---

## Workflow

```text
User Prompt
      │
      ▼
Terraform Generator
      │
      ▼
Load Terraform Prompt Template
      │
      ▼
Ollama (qwen2.5:3b)
      │
      ▼
Generate Terraform Configuration
      │
      ▼
Create Terraform Files
      │
      ▼
Save Output
      │
      ▼
Display Generated Result
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/main/images/terraform%20generator.png?raw=true" alt="Terraform Generator Demo" width="95%">
</p>

---

## Generated Output

The generated Terraform project can be viewed here:

**Output Directory:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/tree/3f0f95c28e81283aaed3ecf63897dcfa565233bd/output/terraform

Generated files include:

- `providers.tf`
- `variables.tf`
- `main.tf`
- `outputs.tf`

---

## Sample Prompt

```text
Create Terraform code to provision an AWS VPC with one public subnet, one EC2 instance, an Internet Gateway, route table, security group allowing SSH and HTTP traffic, and output the public IP address of the EC2 instance.
```

---

## Generated Files

```text
output/
└── terraform/
    ├── providers.tf
    ├── variables.tf
    ├── main.tf
    └── outputs.tf
```

---

## Outcome

The Terraform Generator converts infrastructure requirements into Terraform configuration files using a local AI model. It reduces the time required to write Infrastructure as Code, provides a consistent starting point for cloud deployments, and helps automate the provisioning workflow for DevOps and cloud engineers.

# Jenkins Pipeline Generator

The Jenkins Pipeline Generator allows users to generate Declarative Jenkins Pipelines using natural language. It takes CI/CD requirements as input, processes them through a locally running Ollama language model, and generates a production-ready `Jenkinsfile` that can be used to automate software build, test, and deployment workflows.

---

## Features

- Generate Declarative Jenkins Pipelines using natural language.
- Uses a locally running Ollama language model.
- Creates production-ready `Jenkinsfile` configurations.
- Automatically saves the generated pipeline to the `output/jenkins` directory.
- Simplifies CI/CD pipeline creation for modern DevOps workflows.

---

## Source Code

The implementation of the Jenkins Pipeline Generator is available here:

**Python Source:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/commands/jenkins.py

---

## Workflow

```text
User Prompt
      │
      ▼
Jenkins Pipeline Generator
      │
      ▼
Load Jenkins Prompt Template
      │
      ▼
Ollama (qwen2.5:3b)
      │
      ▼
Generate Jenkinsfile
      │
      ▼
Save Output
      │
      ▼
Display Generated Result
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/images/jenkins%20generator.png?raw=true" alt="Jenkins Pipeline Generator Demo" width="95%">
</p>

---

## Generated Output

The generated Jenkins pipeline can be viewed here:

**Output Directory:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/tree/3f0f95c28e81283aaed3ecf63897dcfa565233bd/output/jenkins

Generated file:

- `Jenkinsfile`

---

## Sample Prompt

```text
Generate a Declarative Jenkins Pipeline for a Java Maven application that performs source code checkout, Maven build, unit testing, SonarQube analysis, Docker image build, Docker Hub push, and Kubernetes deployment.
```

---

## Generated Files

```text
output/
└── jenkins/
    └── Jenkinsfile
```

---

## Outcome

The Jenkins Pipeline Generator transforms CI/CD requirements into a production-ready Declarative Jenkins Pipeline using a local AI model. It reduces manual pipeline development, promotes DevOps best practices, and provides a reusable foundation for automating application build, test, containerization, and deployment workflows.
# Linux Assistant

The Linux Assistant enables users to interact with a locally running AI model to solve Linux administration tasks using natural language. Users can ask questions related to file management, system monitoring, networking, user management, package management, shell scripting, and troubleshooting, and receive accurate Linux commands with concise explanations.

---

## Features

- Generate Linux commands using natural language.
- Uses a locally running Ollama language model.
- Assists with Linux administration and troubleshooting.
- Automatically saves the generated response to the `output/linux` directory.
- Helps users learn Linux commands and best practices.

---

## Source Code

The implementation of the Linux Assistant is available here:

**Python Source:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/commands/linux.py

---

## Workflow

```text
User Prompt
      │
      ▼
Linux Assistant
      │
      ▼
Load Linux Prompt Template
      │
      ▼
Ollama (qwen2.5:3b)
      │
      ▼
Generate Linux Commands
      │
      ▼
Save Output
      │
      ▼
Display Generated Result
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/images/linux%20assistant.png?raw=true" alt="Linux Assistant Demo" width="95%">
</p>

---

## Generated Output

The generated Linux response can be viewed here:

**Output Directory:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/tree/3f0f95c28e81283aaed3ecf63897dcfa565233bd/output/linux

Generated file:

- `linux_commands.txt`

---

## Sample Prompt

```text
Find files larger than 500MB and explain what the command does.
```

---

## Generated File

```text
output/
└── linux/
    └── linux_commands.txt
```

---

## Outcome

The Linux Assistant converts natural language requests into practical Linux commands using a local AI model. It helps users perform common system administration tasks more efficiently, reduces the need to search documentation, and provides clear command explanations for learning and troubleshooting.
# AWS Architecture Generator

The AWS Architecture Generator enables users to design cloud architectures using natural language. It accepts application requirements, processes them using a locally running Ollama language model, and generates AWS architecture recommendations, including suitable AWS services, deployment strategies, security considerations, scalability options, and best practices.

---

## Features

- Generate AWS architecture recommendations using natural language.
- Uses a locally running Ollama language model.
- Recommends appropriate AWS services for different workloads.
- Provides architecture design, scalability, and security best practices.
- Automatically saves the generated architecture in the `output/aws` directory.
- Assists in designing cloud-native and highly available applications.

---

## Source Code

The implementation of the AWS Architecture Generator is available here:

**Python Source:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/commands/aws.py

---

## Workflow

```text
User Prompt
      │
      ▼
AWS Architecture Generator
      │
      ▼
Load AWS Prompt Template
      │
      ▼
Ollama (qwen2.5:3b)
      │
      ▼
Generate AWS Architecture
      │
      ▼
Recommend AWS Services
      │
      ▼
Save Output
      │
      ▼
Display Generated Result
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/images/aws%20architecture.png?raw=true" alt="AWS Architecture Generator Demo" width="95%">
</p>

---

## Generated Output

The generated AWS architecture document can be viewed here:

**Output Directory:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/tree/3f0f95c28e81283aaed3ecf63897dcfa565233bd/output/aws

Generated file:

- `aws_architecture.md`

---

## Sample Prompt

```text
Design a highly available AWS architecture for a Spring Boot microservices application with a React frontend. Include networking, load balancing, compute, database, storage, monitoring, security, and deployment best practices.
```

---

## Generated File

```text
output/
└── aws/
    └── aws_architecture.md
```

---

## Outcome

The AWS Architecture Generator transforms natural language requirements into structured AWS architecture recommendations using a local AI model. It helps developers, cloud engineers, and DevOps professionals quickly design scalable, secure, and highly available cloud solutions while following AWS best practices.
# DevOps Troubleshooter

The DevOps Troubleshooter helps users diagnose and resolve common DevOps, cloud, and infrastructure issues using natural language. Users can describe an error message or problem, and the local Ollama language model analyzes the issue, identifies possible causes, suggests troubleshooting commands, and recommends best practices for resolution.

---

## Features

- Analyze DevOps and infrastructure-related issues.
- Uses a locally running Ollama language model.
- Suggests possible root causes of failures.
- Recommends Linux, Docker, Kubernetes, Terraform, Jenkins, and AWS troubleshooting commands.
- Automatically saves the generated troubleshooting report in the `output/troubleshooter` directory.
- Provides best practices to help prevent similar issues.

---

## Source Code

The implementation of the DevOps Troubleshooter is available here:

**Python Source:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/commands/troubleshoot.py

---

## Workflow

```text
User Error / Issue
         │
         ▼
DevOps Troubleshooter
         │
         ▼
Load Troubleshooting Prompt
         │
         ▼
Ollama (qwen2.5:3b)
         │
         ▼
Analyze the Issue
         │
         ▼
Generate Diagnosis & Fixes
         │
         ▼
Save Report
         │
         ▼
Display Results
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/3f0f95c28e81283aaed3ecf63897dcfa565233bd/images/troubleshooter.png?raw=true" alt="DevOps Troubleshooter Demo" width="95%">
</p>

---

## Generated Output

The generated troubleshooting report can be viewed here:

**Output Directory:**  
https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/tree/3f0f95c28e81283aaed3ecf63897dcfa565233bd/output/troubleshooter

Generated file:

- `troubleshooting.md`

---

## Sample Prompt

```text
My Kubernetes pod is stuck in CrashLoopBackOff. Identify the possible causes, provide the commands required to diagnose the issue, and recommend the appropriate solution.
```

---

## Generated File

```text
output/
└── troubleshooter/
    └── troubleshooting.md
```

---

## Outcome

The DevOps Troubleshooter converts natural language descriptions of infrastructure and deployment issues into structured troubleshooting guidance using a local AI model. It helps developers and DevOps engineers quickly identify root causes, execute the appropriate diagnostic commands, and apply recommended solutions, reducing the time required to resolve operational issues.
# Exit Function

The Exit function provides a clean and user-friendly way to terminate the AI-Powered DevOps CLI Assistant. Selecting this option safely closes the application and ends the interactive session.

---

## Features

- Gracefully exits the application.
- Prevents accidental execution of additional commands.
- Provides a clean termination of the CLI session.
- Improves the overall user experience.

---

## Workflow

```text
User Selects Option 8
          │
          ▼
    Exit Function
          │
          ▼
 Display Exit Message
          │
          ▼
Terminate Application
```

---

## Demonstration

<p align="center">
  <img src="https://github.com/ganeshmalleshe17/AI-Powered-DevOps-CLI-Assistant/blob/main/images/exit%20button.png?raw=true" alt="Exit Function" width="95%">
</p>

---

## Exit Message

```text
Goodbye!
```

---

## Outcome

The Exit function allows users to safely terminate the AI-Powered DevOps CLI Assistant after completing their tasks. It ensures a smooth shutdown of the application and provides a simple, intuitive way to end the interactive session.
---


# Final Thoughts

Building this project provided hands-on experience in integrating AI with modern DevOps workflows. Instead of relying on external AI services, the application runs completely on a local Ollama model, making it efficient, private, and cost-effective.

From generating Dockerfiles and Kubernetes manifests to creating Terraform configurations and troubleshooting infrastructure issues, this project demonstrates how AI can accelerate routine DevOps operations while serving as a learning platform for cloud and automation technologies.

I look forward to continuing to enhance this project with additional features and capabilities.

Thank you for visiting this repository.
---

## Author

**Ganesh Malleshe**

Cloud | DevOps | AWS | Linux | Kubernetes | Terraform | Jenkins | Python

- GitHub: https://github.com/ganeshmalleshe17
- LinkedIn: https://www.linkedin.com/in/ganeshmalleshe/
- Email: ganeshmalleshe17@outlook.com

---

If you found this project useful, consider giving it a ⭐ on GitHub. Your support is greatly appreciated.
