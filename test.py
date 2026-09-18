from tools.tavily_tool import tavily_search
from tools.flight_ttol import search_flights



# res= tavily_search("Give me best 5 hotels in India")
# print(res)




res= search_flights("Plan 7 days trip IND  to Paris")
print(res)