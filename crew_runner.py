import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_crew(branch, topic):
    prompt = f"""
You are a GATE Exam Expert Tutor.

Branch: {branch}
Topic: {topic}

Give output in EXACT format:

### Explanation
(detailed explanation)

### Code
(code only if required)

### Summary
(bullet points)

### Key Points
(exam-focused points)

### GATE Notes
(crisp revision notes)

### MCQs
(5 MCQs with answers)
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
