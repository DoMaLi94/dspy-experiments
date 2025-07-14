# DSPy Experiments

Experiments with the **DSPy** framework using **Ollama** as the default local language model backend.

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama** (recommended for local models):
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Install Poetry** (for dependency management):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

### Setup

1. **Clone and install dependencies**:
   ```bash
   git clone https://github.com/DoMaLi94/dspy-experiments.git
   cd dspy-experiments
   poetry install
   ```

2. **Set up Ollama**:
   ```bash
   # Start Ollama server
   ollama serve

   # Install recommended model
   ollama pull gemma3:1b
   ```

3. **Run experiments**:
   ```bash
   # Basic QA example
   poetry run python experiments/basic_qa.py

   # Image to text example (requires llava model)
   ollama pull llava:7b
   poetry run python experiments/image_to_text.py

   # Jupyter notebook (normaly you want to run this notebook cell by cell)
   poetry run jupyter notebook notebooks/getting_started.ipynb
   ```

## 📁 Project Structure

```
dspy-experiments/
├── experiments/          # Python experiment scripts
│   ├── basic_qa.py      # Basic question-answering example
│   ├── image_to_text.py # Image-to-text description using LLaVA
├── notebooks/           # Jupyter notebooks
│   └── getting_started.ipynb
├── scripts/             # Utility scripts
│   ├── check_code.sh    # Code quality checks
│   └── format_code.sh   # Code formatting
├── images/              # Sample images for experiments
├── pyproject.toml       # Poetry configuration
└── README.md
```

## 🤖 Language Model Backend

### Ollama (Local)
- **Default model**: `gemma3:1b`
- **Server**: `http://localhost:11434`
- **Advantages**: Privacy, no API costs, offline usage

**Additional models supported:**
- `llava:7b` – For image-to-text experiments

For more available models, see the [Ollama models library](https://ollama.com/library).

## 🧪 Available Experiments

### 1. Basic QA (`experiments/basic_qa.py`)
Simple question-answering system demonstrating DSPy basics with Ollama.

### 2. Image to Text (`experiments/image_to_text.py`)
Image description using DSPy with LLaVA multimodal model. Demonstrates how to process images and generate text descriptions.

### 3. Getting Started Notebook (`notebooks/getting_started.ipynb`)
Interactive notebook covering:
- Language model setup with Ollama
- DSPy signatures
- Basic QA system
- Sentiment classification
- Chain of thought reasoning
- Optimization techniques

## 🔧 Configuration

The experiments use Ollama as the local language model backend:

- **Primary model**: `gemma3:1b` for text generation and QA
- **Multimodal model**: `llava:7b` for image-to-text tasks
- **Server**: `http://localhost:11434`

Copy `.env.example` to `.env` and modify settings if needed for your setup.

## 🐛 Troubleshooting

### Ollama Issues
- **Server not running**: `ollama serve`
- **Model not found**: `ollama pull gemma3:1b`
- **Connection refused**: Check if Ollama is running on port 11434

### Poetry Issues
- **Lock file outdated**: `poetry lock`
- **Dependencies not installed**: `poetry install`

## 📚 Resources

- [Ollama Website](https://ollama.com)
- [Ollama Documentation](https://ollama.readthedocs.io/en/)
- [DSPy Website](https://dspy.ai)
- [DSPy GitHub Repository](https://github.com/stanfordnlp/dspy)
- [DSPy Documentation](https://dspy.readthedocs.io/en/latest/)

## 🛠️ Development

### Code Quality Tools

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting (PEP 8 compliance)
- **mypy**: Static type checking

### Quick Commands

```bash
# Format code and run all checks
./scripts/format_code.sh

# Check code quality (without making changes)
./scripts/check_code.sh

# Or run pre-commit directly
poetry run pre-commit run --all-files

# Individual tools (if needed for debugging)
poetry run black experiments/ notebooks/
poetry run isort experiments/ notebooks/
poetry run flake8 experiments/
poetry run mypy experiments/
```

### Pre-commit Setup (Recommended)

You can set up automatic code formatting and linting on commit:

```bash
# Install git hooks
poetry run pre-commit install

# Run hooks manually on all files (optional)
poetry run pre-commit run --all-files

# Update hooks to latest versions
poetry run pre-commit autoupdate
```

Once installed, pre-commit will automatically run code quality checks on your staged files before each commit, ensuring consistent code quality across the project.
