# pylint: disable=invalid-name
"""Integrate a custom math tool and run a ReAct query."""

import math

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
    """Create an agent, invoke it with a natural-language math query, and print output."""
    tools = [hypotenuse_length]
    query = "What is the hypotenuse length of a triangle with side lengths of 10 and 12?"
    model = ChatOpenAI(model="gpt-4o-mini")
    app = create_react_agent(model, tools)

    response = app.invoke({"messages": [("human", query)]})
    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
