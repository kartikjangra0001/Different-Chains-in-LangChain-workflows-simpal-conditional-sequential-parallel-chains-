from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

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
    # Handle both StringPromptValue and Pydantic object inputs
    user_prompt = inputs.text if hasattr(inputs, 'text') else str(inputs)
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=1.0,
        max_tokens=500 
    )
    return response.choices[0].message.content

# Wrap the model in LangChain-compatible Runnable
model = RunnableLambda(call_deepseek)

# Define parsers
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Define prompts
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Define the classifier chain
classifier_chain = prompt1 | model | parser2

# Define the branch chain
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

# Combine the chains
chain = classifier_chain | branch_chain

# Invoke the chain
print(chain.invoke({'feedback': 'This is a beautiful phone'}))

# Optional: Show ASCII graph (if supported)
chain.get_graph().print_ascii()






##output
# Certainly! Here’s a warm and professional response to positive feedback:

# **"Thank you so much for your kind words! We’re thrilled to hear that you had a great experience. Your feedback means a lot to us and motivates us to keep delivering the best service. We look forward to serving you again soon!"**

# If you'd like a more personalized response, feel free to share the specific feedback or context, and I can tailor it further!   
#     +-------------+      
#     | PromptInput |
#     +-------------+
#             *
#             *
#             *
#    +----------------+
#    | PromptTemplate |
#    +----------------+
#             *
#             *
#             *
#     +---------------+
#     | call_deepseek |
#     +---------------+
#             *
#             *
#             *
# +----------------------+
# | PydanticOutputParser |
# +----------------------+
#             *
#             *
#             *
#        +--------+
#        | Branch |
#        +--------+
#             *
#             *
#             *
#     +--------------+
#     | BranchOutput |
#     +--------------+