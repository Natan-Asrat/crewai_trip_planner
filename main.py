import os
from crewai import Crew, Process

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin =origin
        self.cities = cities
        self.date_range=date_range
        self.interests=interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        local_tour_guide = agents.local_tour_guide()
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )
        identify_city = tasks.identify_city(
            city_selection_expert, 
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range, 
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    origin = input(dedent("""Enter origin: """))
    cities = input(dedent("""Enter cities: """))
    date_range = input(dedent("""Enter date_range: """))

    interests = input(dedent("""Enter interests: """))

    trip_crew = TripCrew(origin, cities, date_range,interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
