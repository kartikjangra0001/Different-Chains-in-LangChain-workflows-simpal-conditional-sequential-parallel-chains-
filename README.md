# LangChain Playground: Different Types of Workflows

A Python-based project that demonstrates the flexibility and power of **LangChain** by implementing four distinct workflows — **Simple**, **Sequential**, **Parallel**, and **Conditional** Chains — all integrated with **OpenRouter's DeepSeek** model.

![Workflow Types](https://github.com/user-attachments/assets/23670e84-cd42-4761-aff5-b04390e39cca)

---

## 🔍 Short Project Description

**LangChainPlayground** showcases how to utilize LangChain to solve various NLP tasks:

- **Simple Chains**: Generate interesting facts.
- **Sequential Chains**: Build reports and summarize them.
- **Parallel Chains**: Produce notes and quizzes simultaneously.
- **Conditional Chains**: Perform sentiment-based responses.

Perfect for developers learning LangChain, building AI workflows, or experimenting with OpenRouter APIs.

---

## 🚀 Features

- 🔹 **Simple Chain**: Generates 5 interesting facts about any topic (e.g., Cricket).
- 🔹 **Sequential Chain**: Builds a full report and summarizes it in 5 points.
- 🔹 **Parallel Chain**: Simultaneously generates notes and a quiz from a topic (e.g., LangGraph generative AI).
- 🔹 **Conditional Chain**: Detects sentiment and provides a tailored response.
- 🔹 **OpenRouter Integration**: Uses DeepSeek model via OpenRouter API.
- 🔹 **ASCII Graphs**: Visualizes each chain using `grandalf`.

---

## 🛠️ Technologies Used

- **Python** – Programming language.
- **LangChain / langchain-core** – For building and composing chains.
- **OpenAI & OpenRouter** – For leveraging LLMs.
- **Pydantic** – Structured output handling.
- **dotenv** – Environment variable management.
- **Grandalf** – For ASCII graph rendering of LangChain workflows.

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vishal815/Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-.git
   cd Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-

2. **Create virtual environment** *(optional but recommended)*:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows:
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**:

   * Create a `.env` file in the root directory:

     ```env
     OPENROUTER_API_KEY=your-api-key-here
     ```

---

## ▶️ How to Use

Ensure your `.env` contains a valid `OPENROUTER_API_KEY`, then run:

```bash
python simple_chain.py         # To get 5 facts about a topic
python sequential_chain.py     # To create a report and summary
python parallel_chain.py       # To generate notes and a quiz together
python conditional_chain.py    # To respond to sentiment-based feedback
```

Each script displays a visual **ASCII graph** of the workflow using `grandalf`.

---

## 📂 Folder Structure

```
Different-Chains-in-LangChain-workflows/
├── simple_chain.py         # Simple chain for generating facts
├── sequential_chain.py     # Sequential chain for report and summary
├── parallel_chain.py       # Parallel chain for notes and quiz
├── conditional_chain.py    # Conditional chain for sentiment-based responses
├── requirements.txt        # Project dependencies
├── .env                   # Environment variables (not included in repo)
└── README.md              # Project documentation
```

---

##  Output
   Output of code and ASCII graphs of LangChain workflows written after the code as a comment in the respective file.



---

## 🔐 API Key Setup

1. Sign up at openrouter
2. Generate your API key.
3. Save it in a `.env` file:

   ```env
   OPENROUTER_API_KEY=your-api-key-here
   ```

✅ Add `.env` to `.gitignore` to avoid exposing secrets.

---

## 👨‍💻 Author

**Name**: Vishal Lazrus
**GitHub**: [@vishal815](https://github.com/vishal815/Different-Chains-in-LangChain-workflows-simpal-conditional-sequential-parallel-chains-.git)

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for more details.

---
