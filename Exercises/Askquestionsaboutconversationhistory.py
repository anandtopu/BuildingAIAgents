# pylint: disable=invalid-name
"""Ask a follow-up question by reusing an agent's conversation history."""

import math

from langchain_core.messages import AIMessage, HumanMessage  # pylint: disable=import-error
from langchain_core.tools import tool  # pylint: disable=import-error
from langchain_openai import ChatOpenAI  # pylint: disable=import-error
from langgraph.prebuilt import create_react_agent  # pylint: disable=import-error


@tool
def hypotenuse_length(lengths: str) -> float:
    """Calculate hypotenuse length from comma-separated side values."""
    sides = lengths.split(",")
    a = float(sides[0].strip())
    b = float(sides[1].strip())
    return math.sqrt(a**2 + b**2)


def main() -> None:
    """Run an initial query, then ask a follow-up question using message history."""
    tools = [hypotenuse_length]
    initial_query = (
        "What is the value of the hypotenuse for a triangle with sides 10 and 12?"
    )
    model = ChatOpenAI(model="gpt-4o-mini")
    app = create_react_agent(model, tools)

    initial_response = app.invoke({"messages": [("human", initial_query)]})
    message_history = initial_response["messages"]
    new_query = "What about one with sides 12 and 14?"

    response = app.invoke({"messages": message_history + [("human", new_query)]})
    filtered_messages = [
        msg
        for msg in response["messages"]
        if isinstance(msg, (HumanMessage, AIMessage)) and msg.content.strip()
    ]

    print(
        {
            "user_input": new_query,
            "agent_output": [
                f"{msg.__class__.__name__}: {msg.content}" for msg in filtered_messages
            ],
        }
    )


if __name__ == "__main__":
    main()