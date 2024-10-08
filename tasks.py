from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_date, interests):
        return Task(
            description=dedent(
                f"""
            Task: Develop a 7-day travel itinerary
            Description: Expand the city guide into a full 7-day travel itinerary with detailed per-day plans , including weather forecasts, places to eat, packing suggestions, and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay, and actual restaurants to go to. This itinerary should cover all aspects of the trip, from arrival to departure, investigating the city guid information with practical travel logistics.
            Parameters:
            -city: {city}
            - Trip date: {travel_date}
            - Traveler Interests: {interests}

            Note: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_date):
        return Task(
            description=dedent(
                f"""
                Task: Identify the best city for the trip
                Description: analyze and select the best city for the trip based on specific criteria such as weather patterns, seasonal events, and travel costs. this task involves comparing multiple cities, considering factors like current weather conditions, upcoming cultural or seasonal events, and overall travel expenses. Your final answer must be a detailed report on the chosen city, including actual flight costs, weather forecast, and attractions.
                Parameters:
                - origin: {origin}
                - cities: {cities}
                - interests: {interests}
                - travel date: {travel_date}
                                            
            Note: {self.__tip_section()}

        """
            ),
            agent=agent,
        )
    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description = dedent(
                f"""
                Task: Gather In-depth City GUide Information
                Description: Compile an in-depth guide for the selected city, gathering information about key attractions, local custom, special events, and daily activity recommendations. This guide should provide a thorough overview of what the city has to offer, including hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level cost
                Parameters:
                - City: {city}
                - Interests: {interests}
                - Travel Date: {travel_dates}
                Note: {self.__tip_section()}
                """
            ),
            agent=agent,
        )
