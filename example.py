from whiterock.main import WhiteRock
from whiterock.agents import due_diligence_agent, principal_investor

# Instantiate the WhiteRock class
whiterock = WhiteRock(
    agents=[due_diligence_agent, principal_investor],
    max_loops=5,
    phone_number="+16505188709",  ##+19729719060",
    phone_call_duration=160,
)

# Run the WhiteRock class
task = "Enter in your task"
whiterock.run(task)
