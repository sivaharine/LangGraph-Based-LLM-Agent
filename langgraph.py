import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import load_tools, initialize_agent
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  # fast & quota friendly

# ✅ Load tools
tools = load_tools(["llm-math"], llm=llm)

# ✅ Initialize agent (zero-shot reasoning)
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

# ✅ Ask a sample question
response = agent.run("What's the square root of 625 plus 10?")
print("🔹 Agent Response:", response)
