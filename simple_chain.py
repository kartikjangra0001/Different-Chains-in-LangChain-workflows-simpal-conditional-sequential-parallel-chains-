
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

# Define the prompt
prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

# Define the model and make it LangChain compatible using RunnableLambda
def call_deepseek(inputs) -> str:
    # Extract the text from StringPromptValue
    user_prompt = inputs.text if hasattr(inputs, 'text') else str(inputs)
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {"role": "user", "content": f"Generate 5 interesting facts about {user_prompt}"}
        ],
        temperature=1.0,
        max_tokens=300
    )
    return response.choices[0].message.content



# Wrap the model in LangChain-compatible Runnable
model = RunnableLambda(call_deepseek)

# Output parser
parser = StrOutputParser()

# Build the chain
chain = prompt | model | parser

# Invoke the chain
result = chain.invoke({'topic': 'cricket'})

# Print the result
print(result)

# Optional: Show ASCII graph 
chain.get_graph().print_ascii()



# O/P
# 1. **Oldest International Sport**: Cricket is one of the oldest team sports in the world, with records dating back to the 16th century in England. The first recorded international cricket match took place in 1844 between the USA and Canada.

# 2. **Longest Match in History**: The longest cricket match ever played was a Test match between England and South Africa in 1939. It lasted for **14 days** (including rest days) and ended in a draw because the English team had to catch their ship home!

# 3. **The "Ashes" Origin**: The famous Ashes rivalry between England and Australia began in 1882 after a satirical obituary in a British newspaper declared that English cricket had died after Australia's first-ever victory on English soil. A tiny urn, said to contain the "ashes of English cricket," became the trophy.

# 4. **First-Ever World Cup**: The first Cricket World Cup was held in **1975** in England, featuring only eight teams (six Test-playing nations and two associate members). The West Indies won the tournament, led by Clive Lloyd.

# 5. **Six Sixes in an Over**: In 2007, South Africa’s Herschelle Gibbs became the first batter to hit **six sixes in a single over** in a One Day International (ODI) against the Netherlands. Before him, only Sir Garfield Sobers (1968) and Ravi Shastri (1985)
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
#     +---------------+
#     | call_deepseek |
#     +---------------+
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

# prompt = PromptTemplate(
#     template='Generate 5 interesting facts about {topic}',
#     input_variables=['topic']
# )

# model = ChatOpenAI()

# parser = StrOutputParser()

# chain = prompt | model | parser

# result = chain.invoke({'topic':'cricket'})

# print(result)

# chain.get_graph().print_ascii()