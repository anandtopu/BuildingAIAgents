'''Creating a ReAct agent
Now that you've learned the basic components of LangChain, you'll jump right in and create a ReAct agent that can count how many 'r's there are in any word with the tool count_r_in_word.

The following have been loaded for you: tool, ChatOpenAI, create_react_agent, math, and model.


Set up the agent app using create_react_agent() by passing in the model and the count_r_in_word to the list of tools.
Define a query variable that accepts the user's question as a string.
Invoke the app with .invoke() and pass a dictionary with a "messages" key, labeling the query as "human".
Access the last message in the response and print its .content attribute to get the agent's answer.'''



# Create the agent
app = create_react_agent(model=model, tools=[count_r_in_word])

# Create a query
query = "How many r's are in the word 'Terrarium'?"

# Invoke the agent and store the response
response = app.invoke({"messages": [("human", query)]})

# Print the agent's response
print(response['messages'][-1].content)


'''The key components of a LangChain agent are Prompts, LLMs, and tools.
This combination lets an agent reason using an LLM, interpret instructions via prompts, and take actions through tools.

✅ Why this is the correct answer
LangChain agents are built around three pillars:
- Prompts — define how the agent reasons, plans, and decides what to do next.
- LLMs — act as the agent’s “brain,” interpreting prompts and generating actions.
- Tools — external functions/APIs the agent can call (e.g., search, calculators, databases).
This trio enables the agent’s core loop: reason → act → observe → repeat.


'''