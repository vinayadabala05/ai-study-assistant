import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_study_content(topic):
    prompt = f"""
    Explain {topic} in simple terms.
    Also provide 3 quiz questions with answers.
    Keep it clear and beginner-friendly.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    topic = input("Enter topic: ")
    result = generate_study_content(topic)
    print("\nGenerated Content:\n")
    print(result)
