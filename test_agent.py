from agent import agent

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Mark task ID 1 as completed."
        }
    ]
})

print(response["messages"][-1].content)