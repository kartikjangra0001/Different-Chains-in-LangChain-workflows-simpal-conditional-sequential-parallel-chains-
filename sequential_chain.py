from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# Load environment variables
load_dotenv()

# Load OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI-compatible client for OpenRouter
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# Define the first prompt
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

# Define the second prompt
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

# Define the model function for OpenRouter
def call_openrouter(inputs) -> str:
    # Handle both StringPromptValue (from prompt1) and string (from parser)
    user_prompt = inputs.text if hasattr(inputs, 'text') else str(inputs)
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=1.0,
        max_tokens=1000  # Increased for detailed report
    )
    return response.choices[0].message.content

# Wrap the model in LangChain-compatible Runnable
model = RunnableLambda(call_openrouter)

# Output parser
parser = StrOutputParser()

# Build the chain
chain = prompt1 | model | parser | prompt2 | model | parser

# Invoke the chain
result = chain.invoke({'topic': 'Unemployment in India'})

# Print the result
print(result)

# Optional: Show ASCII graph
chain.get_graph().print_ascii()









# output:
# Here’s a concise **5-pointer summary** of the report on unemployment in India:  

# 1. **Current Unemployment Trends**
#    - India’s overall unemployment rate is **3.2%** (2022-23), with urban areas (**6.6%**) and women (**9.2% urban**) disproportionately affected.
#    - Youth unemployment is high (**10%**), especially among educated individuals.

# 2. **Key Types & Causes**
#    - **Structural** (skill mismatch), **cyclical** (economic downturns), **seasonal** (agriculture), and **disguised** (underutilized labor).
#    - Causes include slow industrial growth, automation, population pressure, and outdated education systems.

# 3. **Regional Disparities**
#    - Southern states (e.g., Kerala: **5.1%**) face higher unemployment than states like Gujarat (**1.2%**).
#    - Urban areas struggle due to formal sector saturation.

# 4. **Government Interventions**
#    - Schemes like **Make in India**, **Skill India**, **MGNREGA**, and **PLI incentives** aim to boost jobs in manufacturing, skills, and rural employment.

# 5. **Future Challenges & Solutions**
#    - Risks: **Jobless growth**, AI-driven job losses, and the need for **10 million jobs/year**.       
#    - Recommendations: Vocational training, MSME support, labor reforms, and green/digital economy expansion.

# Let me know if you'd like a deeper dive into any specific area!
#      +-------------+       
#      | PromptInput |
#      +-------------+
#             *
#             *
#             *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#             *
#             *
#             *
#    +-----------------+
#    | call_openrouter |
#    +-----------------+
#             *
#             *
#             *
#    +-----------------+
#    | StrOutputParser |
#    +-----------------+
#             *
#             *
#             *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+
#             *
#             *
#             *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#             *
#             *
#             *
#    +-----------------+
#    | call_openrouter |
#    +-----------------+
#             *
#             *
#             *
#    +-----------------+
#    | StrOutputParser |
#    +-----------------+
#             *
#             *
#             *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+





# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# prompt1 = PromptTemplate(
#     template='Generate a detailed report on {topic}',
#     input_variables=['topic']
# )

# prompt2 = PromptTemplate(
#     template='Generate a 5 pointer summary from the following text \n {text}',
#     input_variables=['text']
# )

# model = ChatOpenAI()

# parser = StrOutputParser()

# chain = prompt1 | model | parser | prompt2 | model | parser

# result = chain.invoke({'topic': 'Unemployment in India'})

# print(result)

# chain.get_graph().print_ascii()