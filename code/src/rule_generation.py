import openai

def generate_profiling_rules(regulatory_text):
    prompt = f"Based on the following regulatory guidelines, generate data profiling rules:\n\n{regulatory_text}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    rules = response.choices[0].text.strip()
    return rules
