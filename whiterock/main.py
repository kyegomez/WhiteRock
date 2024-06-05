from swarms import BaseSwarm, Agent
from typing import List
from swarms import Conversation
from whiterock.agents import principal_investor, due_diligence_agent
from whiterock.prompts import analyst_caller_agent
from whiterock.tools import call_api, fetch_transcription

class WhiteRock(BaseSwarm):
    """
    WhiteRock class represents a swarm of agents involved in a due diligence process.

    Args:
        agents (List[Agent]): List of agents participating in the swarm. Defaults to vc_agents.
        max_loops (int): Maximum number of loops the swarm will run. Defaults to 5.
        phone_number (str): Phone number used for making phone calls. Defaults to "+17866955339".
        phone_call_duration (int): Maximum duration of a phone call in seconds. Defaults to 160.
        vc_rules (str): Rules for the conversation. Defaults to None.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        agents (List[Agent]): List of agents participating in the swarm.
        max_loops (int): Maximum number of loops the swarm will run.
        phone_number (str): Phone number used for making phone calls.
        phone_call_duration (int): Maximum duration of a phone call in seconds.
        history (Conversation): Conversation history object.

    Methods:
        run(task: str, *args, **kwargs) -> Any: Runs the swarm and returns the output.

    """

    def __init__(
        self,
        agents: List[Agent] = None,
        max_loops: int = 5,
        phone_number: str = "+17866955339",
        phone_call_duration: int = 160,
        vc_rules: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.agents = agents
        self.max_loops = max_loops
        self.phone_number = phone_number
        self.phone_call_duration = phone_call_duration

        # History
        self.history = Conversation(
            time_enabled=True,
            auto_save=True,
            rules=vc_rules,
        )

    def run(self, task: str, *args, **kwargs):
        """
        Runs the swarm and returns the output.

        Args:
            task (str): The task to be performed by the swarm.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Any: The output of the swarm.

        """
        loop = 0
        
        for _ in range(self.max_loops):
            # Combine strings into one
            out = f"{analyst_caller_agent()} {task}"

            transcription = call_api(
                self.phone_number,
                max_duration=self.phone_call_duration,
                prompt=out,
            )

            out = fetch_transcription(transcription, max_duration=self.phone_call_duration)

            self.history.add(
                role="Due Diligence Agent",
                content=out,
            )

            # Due Diligence Agent
            due_diligence_agent = self.agents[0]
            out = due_diligence_agent.run(
                self.history.return_history_as_string(), *args, **kwargs
            )
            print(out)
            self.history.add(
                role="Due Diligence Agent",
                content=out,
            )
            # Function call to mercury, add docs into a folder so rag can pick it up
            # Function call to rag, add perplexity agent to the rag agent so it can search the web for more information

            # Principal Investor Agent
            principal_investor_agent = self.agents[1]
            out = principal_investor_agent.run(
                self.history.return_history_as_string(), *args, **kwargs
            )
            print(out)
            self.history.add(
                role="Principal Investor Agent",
                content=out,
            )
            
            loop += 1

        return out

