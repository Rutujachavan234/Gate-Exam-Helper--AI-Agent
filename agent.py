from crewai import Agent

study_agent = Agent(
    role="GATE Study Tutor",
    goal="Provide explanations, summaries, notes, code, and MCQs for any topic.",
    backstory="You are an expert GATE exam teacher.",
    llm="gemini/gemini-2.5-flash"  # still used for CrewAI registry
)
