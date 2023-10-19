from dataclasses import dataclass

from temporalio import activity


@dataclass
class YourParams:
    greeting: str
    name: str


@activity.defn
async def say_hello(input: YourParams) -> str:
    return f"{input.greeting}, {input.name}!"
