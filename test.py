from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent


# res= tavily_search("Give me best 5 hotels in India")
# print(res)




# res= search_flights("Plan 7 days trip IND  to Paris")
# print(res)




user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])