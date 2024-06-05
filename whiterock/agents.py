import os

from dotenv import load_dotenv
from swarms import Agent

from swarms import OpenAIChat
from whiterock.memory import ChromaDB
from whiterock.prompts import (
    PRINCIPAL_SYSTEM_PROMPT,
    due_diligence_agent_system_prompt,
)

# Load the environment variables
load_dotenv()

# Memory
memory = ChromaDB(
    output_dir="whiterock",
    n_results=1,
)

# GROQ API key
groq_api_key = os.getenv("GROQ_API_KEY")

# GROQ LLM
model = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    max_tokens=3000,
    temperature=0.2,
)


agent_names = [
    "Due Diligence Agent",
    "Principal Investor Agent",
]

system_prompts = [
    due_diligence_agent_system_prompt(),
    PRINCIPAL_SYSTEM_PROMPT(),
]


due_diligence_agent = Agent(
    agent_name=agent_names[0],
    system_prompt=system_prompts[0],
    agent_description=system_prompts[0],
    llm=model,
    max_loops=1,
    autosave=True,
    # dashboard=False,
    # verbose=True,
    # interactive=True,
    # interactive=True,
    state_save_file_type="json",
    saved_state_path=f"{agent_names[0].lower().replace(' ', '_')}.json",
    # docs_folder="data", # Folder of docs to parse and add to the agent's memory
    # long_term_memory=memory,
    # dynamic_temperature_enabled=True,
    # pdf_path="docs/medical_papers.pdf",
    # list_of_pdf=["docs/medical_papers.pdf", "docs/medical_papers_2.pdf"],
    # docs=["docs/medicalx_papers.pdf", "docs/medical_papers_2.txt"],
    # memory_chunk_size=2000,
)


principal_investor = Agent(
    agent_name=agent_names[1],
    system_prompt=system_prompts[1],
    agent_description=system_prompts[1],
    llm=model,
    max_loops=1,
    autosave=True,
    # dashboard=False,
    # verbose=True,
    # interactive=True,
    # interactive=True,
    state_save_file_type="json",
    saved_state_path=f"{agent_names[0].lower().replace(' ', '_')}.json",
    # docs_folder="data", # Folder of docs to parse and add to the agent's memory
    # long_term_memory=memory,
    # dynamic_temperature_enabled=True,
    # pdf_path="docs/medical_papers.pdf",
    # list_of_pdf=["docs/medical_papers.pdf", "docs/medical_papers_2.pdf"],
    # docs=["docs/medicalx_papers.pdf", "docs/medical_papers_2.txt"],
    # memory_chunk_size=2000,
)
