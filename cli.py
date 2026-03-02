from agent_setup import agent   #  existing agent

def main():
    print("\n💰 Personal Finance Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        try:
            result = agent.invoke({
            "messages": [
                {"role": "user", "content": user_input}
                ]
            })

            print("Assistant:", result["messages"][-1].content)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()