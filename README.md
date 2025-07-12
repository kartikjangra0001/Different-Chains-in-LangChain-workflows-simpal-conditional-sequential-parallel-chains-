# Different Chains in LangChain Workflows: Simple, Conditional, Sequential, and Parallel Chains

![LangChain Workflows](https://img.shields.io/badge/LangChain-Workflows-blue?style=for-the-badge&logo=python)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Workflows](#workflows)
  - [Simple Chain](#simple-chain)
  - [Sequential Chain](#sequential-chain)
  - [Parallel Chain](#parallel-chain)
  - [Conditional Chain](#conditional-chain)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Releases](#releases)

## Overview

This project demonstrates the power of LangChain by implementing four distinct workflows—simple, sequential, parallel, and conditional chains—using OpenRouter’s DeepSeek model. It processes text inputs to generate facts, summaries, notes, quizzes, sentiment-based responses, and more.

For more details on the releases, visit the [Releases section](https://github.com/kartikjangra0001/Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-/releases).

## Features

- **Simple Chain**: Quickly processes single inputs to generate direct outputs.
- **Sequential Chain**: Executes a series of tasks in order, ensuring that each step feeds into the next.
- **Parallel Chain**: Handles multiple tasks at once, optimizing for speed and efficiency.
- **Conditional Chain**: Makes decisions based on input, allowing for dynamic workflows.

## Workflows

### Simple Chain

The Simple Chain allows users to input a single piece of text and receive a direct output. This is ideal for tasks such as generating summaries or extracting facts.

**Example**:
```python
from langchain import SimpleChain

chain = SimpleChain()
result = chain.run("What is the capital of France?")
print(result)  # Output: Paris
```

### Sequential Chain

The Sequential Chain processes inputs in a step-by-step manner. Each output becomes the input for the next step, allowing for complex workflows.

**Example**:
```python
from langchain import SequentialChain

chain = SequentialChain()
result = chain.run("Tell me about the Eiffel Tower.")
print(result)  # Output: [Summary, Facts, Notes]
```

### Parallel Chain

The Parallel Chain executes multiple tasks simultaneously. This approach is efficient for tasks that can be performed independently.

**Example**:
```python
from langchain import ParallelChain

chain = ParallelChain()
results = chain.run(["What is AI?", "Explain machine learning."])
print(results)  # Output: [Definition of AI, Explanation of ML]
```

### Conditional Chain

The Conditional Chain allows the workflow to change based on specific conditions. This flexibility is useful for handling diverse inputs.

**Example**:
```python
from langchain import ConditionalChain

chain = ConditionalChain()
result = chain.run("Is it raining today?")
print(result)  # Output: [Weather Response]
```

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kartikjangra0001/Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-.git
   ```

2. **Install Dependencies**:
   Navigate to the project directory and install the required packages.
   ```bash
   cd Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Execute the main script to start using the workflows.
   ```bash
   python main.py
   ```

## Usage

Once the application is running, you can interact with the various chains. Each chain can be called independently based on your needs.

### Example Usage
```python
# Import the necessary chains
from langchain import SimpleChain, SequentialChain

# Create instances of the chains
simple_chain = SimpleChain()
sequential_chain = SequentialChain()

# Use the simple chain
simple_result = simple_chain.run("What is the capital of Italy?")
print(simple_result)  # Output: Rome

# Use the sequential chain
sequential_result = sequential_chain.run("Tell me about the Colosseum.")
print(sequential_result)  # Output: [Summary, Facts, Notes]
```

## Technologies Used

- **Python**: The primary programming language for this project.
- **LangChain**: A framework that allows for the creation of complex workflows.
- **OpenRouter’s DeepSeek Model**: A powerful AI model used for processing text.
- **dotenv**: For managing environment variables.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Submit a pull request.

Please ensure your code follows the project's style guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases

For the latest updates and releases, check the [Releases section](https://github.com/kartikjangra0001/Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-/releases). You can download the latest version and execute it to explore the features.

![Release Badge](https://img.shields.io/badge/Latest_Release-v1.0.0-brightgreen?style=for-the-badge)

## Topics

This project covers a range of topics related to AI and machine learning, including:

- ai
- chain
- deepseek
- dotenv
- generative-ai
- generativeai
- langchain
- langchain-python
- learning
- machine-learning
- nlp
- openai
- openrouter
- python
- vishal-lazrus
- vishallazrus

Feel free to explore and learn from the workflows implemented in this repository.