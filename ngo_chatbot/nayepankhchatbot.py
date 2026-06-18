from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

def get_foundation_info():
    """
    Use this function whenever the user asks about
    NayePankh Foundation, its mission, programs,
    volunteering, or activities.
    """

    with open("C:\\Users\\Srishti\\OneDrive\\Desktop\\coding\\internship nayepankh\\foundation.txt", "r", encoding="utf-8") as file:
        return file.read()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


agent = create_agent(
    model=llm,
    tools=[get_foundation_info],

    system_prompt="""
    You are NayePankh AI Assistant.

    Answer questions about NayePankh Foundation.

    Use the available tools whenever information
    about the foundation is required.

    Be friendly and concise.
    """,

    checkpointer=InMemorySaver()
)


state = None

volunteer_data = {}

while True:

    user_query = input("\nYou: ")

    if user_query.lower() == "end":
        break


    if user_query.lower() == "i want to volunteer":

        state = "name"

        print("\nBot: Great! Let's register you.")
        print("Bot: What is your name?")

        continue


    if state == "name":

        volunteer_data["name"] = user_query

        state = "interest"

        print("\nBot: What area interests you?")

        print("""
              1. Education
              2. Social Media
              3. Community Welfare
              4. Content Creation
              """)

        continue


    if state == "interest":

        volunteer_data["interest"] = user_query

        state = None

        print("\nBot: Registration Successful!")

        print(f"""
                Name: {volunteer_data['name']}
                Interest: {volunteer_data['interest']}
                """)

        print("Bot: Thank you for volunteering!")

        continue

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_query
                }
            ]
        },

        {
            "configurable": {
                "thread_id": "1"
            }
        }
    )

    content = response["messages"][-1].content

    if isinstance(content, str):
        print("\nBot:", content)

    elif isinstance(content, list):
        print("\nBot:", content[0]["text"])