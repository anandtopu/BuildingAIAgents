'''
Integrating custom tools and queries
You now have a custom math tool for calculating roof length. You can integrate it with an agentic workflow by creating a variable called query that accepts the user's natural language question as a string.
Your tool is already loaded as hypotenuse_length, as well as your model.

Create a list variable called tools and include your tool, hypotenuse_length, inside the list.
Create a variable called query that accepts questions as natural language strings.
Use the create_react_agent() function to create the agent, passing in the model and tools.
Invoke the agent app, passing in your query labeled "human", before storing and printing the agent's response.

'''



# Create a list variable and pass in your tool
tool = [____]

# Create a query using natural language
query = "What is the hypotenuse length of a triangle with side lengths of 10 and 12?"

# Pass in the hypotenuse length tool and create the agent
app = create_react_agent(____, ____)

# Invoke the agent and print the response
response = ____.____({"messages": [("____", ____)]})
print(____['messages'][-1].content)