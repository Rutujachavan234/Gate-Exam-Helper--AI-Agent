from crewai import Task

def build_tasks(topic, branch, mode):
    prompt = f"""
    Branch: {branch}
    Topic: {topic}
    Mode: {mode}

    TASK:
    - If mode='explain', explain the topic clearly with examples.
    - If mode='mcq', generate 10 MCQs with answers.
    - If mode='chat', answer the follow-up question.
    - If mode='notes', generate short handwritten-style notes.
    """

    return [
        Task(
            description=prompt,
            agent="study_agent",
            expected_output="High-quality educational content"
        )
    ]
