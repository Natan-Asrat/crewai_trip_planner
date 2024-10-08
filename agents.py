from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from tools.search_tools import SearchTool
from tools.calculator_tools import CalculateTools

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.groq = ChatGroq()
    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. I have decades of experience making travely iternaries."""),
            goal=dedent(f"""Create a 7-day travel itinerary with detailed per-day plans
                        include budget, packing, suggestions, and safety tips
                        """),
            tools=[SearchTool.search_internet, CalculateTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.groq,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analysing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices and traveler interest"""),
            tools=[SearchTool.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.groq,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city, its attractions and customs"""),
            goal=dedent(f"""Provde the best insights about the selected city"""),
            tools=[SearchTool.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.groq,
        )
