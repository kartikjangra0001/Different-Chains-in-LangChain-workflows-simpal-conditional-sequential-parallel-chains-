from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

# Load environment variables
load_dotenv()

# Load OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI-compatible client for OpenRouter
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# Define the model function for DeepSeek
def call_deepseek(inputs) -> str:
    # Handle both StringPromptValue and string inputs
    user_prompt = inputs.text if hasattr(inputs, 'text') else str(inputs)
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=1.0,
        max_tokens=500  # Adjusted for short notes
    )
    return response.choices[0].message.content

# Define the model function for Google Gemma
def call_gemma(inputs) -> str:
    # Handle both StringPromptValue and string inputs
    user_prompt = inputs.text if hasattr(inputs, 'text') else str(inputs)
    response = client.chat.completions.create(
        # model="google/gemma-2-9b-it:free",
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=1.0,
        max_tokens=500  # Adjusted for short Q&A
    )
    return response.choices[0].message.content

# Define the model function for merging (using DeepSeek again)
def call_merge(inputs) -> str:
    # Handle dictionary input from parallel chain
    user_prompt = inputs.text if hasattr(inputs, 'text') else str(inputs)
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=1.0,
        max_tokens=1000  # Increased for merged document
    )
    return response.choices[0].message.content

# Wrap models in LangChain-compatible Runnable
deepseek_model = RunnableLambda(call_deepseek)
gemma_model = RunnableLambda(call_gemma)
merge_model = RunnableLambda(call_merge)

# Define the prompts
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

# Output parser
parser = StrOutputParser()

# Define the parallel chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | deepseek_model | parser,
    'quiz': prompt2 | gemma_model | parser
})

# Define the merge chain
merge_chain = prompt3 | merge_model | parser

# Combine the chains
chain = parallel_chain | merge_chain

# Input text
text = """
LangGraph, created by LangChain, is an open source AI agent framework designed to build, deploy and manage complex generative AI agent workflows. It provides a set of tools and libraries that enable users to create, run and optimize large language models (LLMs) in a scalable and efficient manner. At its core, LangGraph uses the power of graph-based architectures to model and manage the intricate relationships between various components of an AI agent workflow.
"""

# Invoke the chain
result = chain.invoke({'text': text})

# Print the result
print(result)

# Optional: Show ASCII graph (if supported)
chain.get_graph().print_ascii()






# # Output 

# Here’s the merged document combining the notes and quiz in a structured format:

# ---

# # **LangGraph: Overview & Quiz**

# ## **Short Notes on LangGraph**

# - **Creator**: LangChain
# - **Type**: Open-source AI agent framework
# - **Purpose**: Build, deploy, and manage complex generative AI workflows
# - **Features**:
#   - Tools & libraries for creating, running, and optimizing LLMs

#   - Scalable and efficient execution
#   - Uses **graph-based architecture** to model relationships between AI workflow components

# ---

# ## **Quick Quiz: Test Your Knowledge**

# 1. **What is LangGraph?**
#    - LangGraph is an open-source AI agent framework created by LangChain for building, deploying, and managing complex generative AI workflows.

# 2. **What does LangGraph provide?**
#    - It provides tools and libraries to create, run, and optimize large language models (LLMs) efficiently and at scale.        

# 3. **How does LangGraph manage AI workflows?**
#    - It uses graph-based architectures to model and manage relationships between different components in AI agent workflows.    

# 4. **Who developed LangGraph?**
#    - LangGraph was developed by LangChain.

# 5. **What is the main advantage of LangGraph’s architecture?**  
#    - Its graph-based approach helps efficiently handle complex dependencies and interactions in AI workflows.

# ---

# Let me know if you'd like further adjustments!
#             +---------------------------+
#             | Parallel<notes,quiz>Input |
#             +---------------------------+
#                  **               **
#               ***                   ***
#             **                         **
# +----------------+                +----------------+
# | PromptTemplate |                | PromptTemplate |
# +----------------+                +----------------+
#           *                               *
#           *                               *
#           *                               *
#  +---------------+                  +------------+
#  | call_deepseek |                  | call_gemma |
#  +---------------+                  +------------+
#           *                               *
#           *                               *
#           *                               *
# +-----------------+              +-----------------+
# | StrOutputParser |              | StrOutputParser |
# +-----------------+              +-----------------+
#                  **               **
#                    ***         ***
#                       **     **
#            +----------------------------+
#            | Parallel<notes,quiz>Output |
#            +----------------------------+
#                           *
#                           *
#                           *
#                  +----------------+
#                  | PromptTemplate |
#                  +----------------+
#                           *
#                           *
#                           *
#                    +------------+
#                    | call_merge |
#                    +------------+
#                           *
#                           *
#                           *
#                 +-----------------+
#                 | StrOutputParser |
#                 +-----------------+
#                           *
#                           *
#                           *
#               +-----------------------+
#               | StrOutputParserOutput |
#               +-----------------------+


## using paid api

# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableParallel

# load_dotenv()

# model1 = ChatOpenAI()

# model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

# prompt1 = PromptTemplate(
#     template='Generate short and simple notes from the following text \n {text}',
#     input_variables=['text']
# )

# prompt2 = PromptTemplate(
#     template='Generate 5 short question answers from the following text \n {text}',
#     input_variables=['text']
# )

# prompt3 = PromptTemplate(
#     template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
#     input_variables=['notes', 'quiz']
# )

# parser = StrOutputParser()

# parallel_chain = RunnableParallel({
#     'notes': prompt1 | model1 | parser,
#     'quiz': prompt2 | model2 | parser
# })

# merge_chain = prompt3 | model1 | parser

# chain = parallel_chain | merge_chain

# text = """

# """

# result = chain.invoke({'text':text})

# print(result)

# chain.get_graph().print_ascii()
