from groq import Groq
from swarms import BaseLLM


class GroqChat(BaseLLM):
    """
    A client for interacting with the Groq API.

    Args:
        system_prompt (str, optional): The system prompt to use for generating completions. Defaults to None.
        model_name (str, optional): The name of the model to use for generating completions. Defaults to "llama3-8b-8192".
        temperature (float, optional): The temperature parameter for generating completions. Defaults to 0.5.
        max_tokens (int, optional): The maximum number of tokens in the generated completions. Defaults to 1024.
        top_p (float, optional): The top-p parameter for generating completions. Defaults to 1.
        stop (str, optional): The stop sequence to use for generating completions. Defaults to None.
    """

    def __init__(
        self,
        groq_api_key: str = None,
        system_prompt: str = None,
        model_name: str = "llama3-8b-8192",
        temperature: float = 0.5,
        max_tokens: int = 1024,
        top_p: float = 1,
        stop: str = None,
        *args,
        **kwargs,
    ):
        self.groq_api_key = groq_api_key
        self.system_prompt = system_prompt
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.stop = stop

        self.client = Groq(api_key=self.groq_api_key, *args, **kwargs)

    def run(self, task: str = None, *args, **kwargs):

        output = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {
                    "role": "user",
                    "content": task,
                },
            ],
            model=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            stop=self.stop,
            *args,
            **kwargs,
        )

        output = output.choices[0].message.content
        return output


# # Model
# model = GroqChat(
#     groq_api_key="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",
#     system_prompt="Welcome to GroqChat! How can I assist you today?",
# )

# # Run
# out = model.run(task="What is the capital of France?")
# print(out)
