import json
import google.genai

client = google.genai.Client(api_key="api_key")

def read_prompts(file):
    with open(file, "r") as f:
        for line in f:
            if line.strip() != "":
                return line.strip()

def gen_resp(prompt):
    responses = client.models.generate_content(model="gemini-2.5-flash", contents = prompt)
    return responses.text

def save_resp(responses, file):
    with open(file, "w") as f:
        json.dump(responses, f)

prompts = read_prompts("prompt.txt")

print(prompts)
resp = {}

for prompt in prompts:
    ans = gen_resp(prompt)
    resp[prompt] = ans

save_resp(resp, "responses.json")
