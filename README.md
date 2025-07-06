LangChain diffrent type of workflows simpal conditional sequential parallel chains
Short Project Description
LangChainPlayground is a Python-based project that showcases the versatility of LangChain through four distinct workflows: simple, sequential, parallel, and conditional chains. Integrated with OpenRouter’s DeepSeek model, it demonstrates AI-driven text processing tasks, such as generating facts about a topic, summarizing reports, creating notes and quizzes, and responding to feedback based on sentiment analysis. Perfect for developers exploring LangChain and NLP workflows.

Type of langchin
![image](https://github.com/user-attachments/assets/23670e84-cd42-4761-aff5-b04390e39cca)


The command python parallel_chain.py being executed.
The output showing generated notes and a 5-question quiz about Support Vector Machines (SVMs).
The ASCII graph of the chain displayed at the end.This visual will highlight the project’s ability to process text in parallel and display structured outputs, making it engaging for viewers.

Features

Simple Chain: Generates five interesting facts about a user-specified topic (e.g., cricket).
Sequential Chain: Creates a detailed report and then summarizes it into a 5-point summary.
Parallel Chain: Simultaneously generates notes and a quiz from a given text, merging them into a single document.
Conditional Chain: Classifies feedback sentiment (positive/negative) and generates tailored responses.
OpenRouter Integration: Leverages the DeepSeek model via OpenRouter’s API for efficient text processing.
ASCII Graph Visualization: Displays the structure of each LangChain workflow using grandalf.

Technologies Used

Python: Python
LangChain: For building and managing NLP workflows.
langchain-core: Core components for LangChain chains.
python-dotenv: For secure environment variable management.
openai: For interacting with OpenRouter’s API.
pydantic: For structured output parsing in the conditional chain.
grandalf: For rendering ASCII graphs of LangChain workflows.

Installation Instructions

Clone the repository:git clone https://github.com/vishal815/Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-.git
cd Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-


Create a virtual environment (optional but recommended):python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install the required dependencies:pip install -r requirements.txt


Create a .env file in the project root with your OpenRouter API key:OPENROUTER_API_KEY=your-api-key-here



How to Use

Ensure your .env file contains a valid OPENROUTER_API_KEY.
Run any of the chain scripts to see the results:python simple_chain.py


simple_chain.py: Generates 5 facts about a topic (e.g., cricket).
sequential_chain.py: Generates a report and a 5-point summary on a topic (e.g., unemployment).
parallel_chain.py: Creates notes and a quiz in parallel from a text (e.g., SVMs).
conditional_chain.py: Classifies feedback sentiment and responds accordingly.


View the ASCII graph output for each chain to understand its workflow.

Folder Structure
Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-/
├── simple_chain.py         # Simple chain for generating facts
├── sequential_chain.py     # Sequential chain for report and summary
├── parallel_chain.py       # Parallel chain for notes and quiz
├── conditional_chain.py    # Conditional chain for sentiment-based responses
├── requirements.txt        # Project dependencies
├── .env                   # Environment variables (not included in repo)
└── README.md              # Project documentation

Output of code and ASCII graphs of LangChain workflows witten in after code as comment.

API Keys/Secrets Setup

Sign up for an OpenRouter account at https://openrouter.ai to obtain an API key.
Create a .env file in the project root with the following content:OPENROUTER_API_KEY=your-api-key-here


Ensure the .env file is listed in .gitignore to prevent accidental exposure of your API key.



Name: Vishal Lazrus
GitHub: //github.com/vishal815/Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-.git
Credits: Built using the LangChain framework and OpenRouter’s DeepSeek model.

License
This project is licensed under the MIT License. See the LICENSE file for details.
