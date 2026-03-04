from agent_setup import agent 
from langchain_core.messages import HumanMessage  

def main():
    print("\nPersonal Finance Assistant")
    print("Type 'exit' to quit\n")

    messages= []

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            messages.append(HumanMessage(content=user_input))

            result = agent.invoke({
                "messages": messages
            })

            ai_msg = result["messages"][-1]

            print("Assistant:", ai_msg.content)

            messages.append(ai_msg)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()