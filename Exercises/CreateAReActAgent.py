# pylint: disable=invalid-name
"""Create and run a simple ReAct agent with one custom tool."""

from langchain_core.tools import tool  # pylint: disable=import-error
from langchain_openai import ChatOpenAI  # pylint: disable=import-error
from langgraph.prebuilt import create_react_agent  # pylint: disable=import-error


@tool
def count_r_in_word(word: str) -> int:
    """Return how many times the letter 'r' appears in the provided word."""
    return word.lower().count("r")


def main() -> None:
    """Build an agent and ask it to count letters using the custom tool."""
    model = ChatOpenAI(model="gpt-4o-mini")
    app = create_react_agent(model=model, tools=[count_r_in_word])

    query = "How many r's are in the word 'Terrarium'?"
    response = app.invoke({"messages": [("human", query)]})
    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
