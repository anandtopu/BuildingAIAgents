

'''Now that you have a custom tool to help you calculate the length of a roof, you can set your agent's outputs to respond to your entered
query. By slightly modifying your print statements, you can directly compare your query and your agent's response to ensure accuracy.
Your tools and query have already been set up and your model is ready to use.'''


import math

from langchain_core.tools import tool  # pylint: disable=import-error
from langchain_openai import ChatOpenAI  # pylint: disable=import-error
from langgraph.prebuilt import create_react_agent

@tool
def hypotenuse_length(lengths: str) -> float:
    """Calculate hypotenuse length from comma-separated side values."""
    sides = lengths.split(",")
    a = float(sides[0].strip())
    b = float(sides[1].strip())
    return math.sqrt(a**2 + b**2)


def main() -> None:
    tools = [hypotenuse_length]
    query = "What is the value of the hypotenuse for a triangle with sides 3 and 5?"
    model = ChatOpenAI(model="gpt-4o-mini")

    # Create the ReAct agent
    app = create_react_agent(model, tools)

    # Invoke the agent with a query and store the messages
    response = app.invoke({"messages": [("human", query)]})

    # Define and print the input and output messages
    print({
        "user_input": query,
        "agent_output": response["messages"][-1].content
    })


if __name__ == "__main__":
    main()