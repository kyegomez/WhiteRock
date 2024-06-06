from whiterock.main import WhiteRock
from whiterock.agents import due_diligence_agent, principal_investor

# Instantiate the WhiteRock class
whiterock = WhiteRock(
    agents=[due_diligence_agent, principal_investor],
    max_loops=5,
    phone_number="+17866955339",  # "+17866955339",  ##+19729719060",
    phone_call_duration=160,
)

# Run the WhiteRock class
task = "Smartglasses with AI capabilities for the visually impaired."
whiterock.run(task)
