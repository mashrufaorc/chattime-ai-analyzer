from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_prompts(prompts):

    categories = []

    for prompt in prompts:

        message = f"""
            Classify the following prompt into ONE category.
            Categories:
                Repetitive
                Information
                Problem Solving
                Critical Thinking
                Creativity
            Prompt: {prompt}

            Return only the category name.
        """

        response = client.chat.completions.create(
        # extra_headers={
        #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        #     "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        # },
        # extra_body={},
        model="openai/gpt-oss-120b",
        messages=[
            {
            "role": "user",
            "content": message
            }
        ]
        )
        print(response.choices[0].message.content)

        category = response.choices[0].message.content.strip()
        categories.append(category)

    return categories
