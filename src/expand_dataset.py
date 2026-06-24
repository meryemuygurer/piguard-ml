import anthropic # to add the Claude API
import pandas as pd # to read and edit csv files
import json # to translate the JSON output from Claude into Python
import os

client = anthropic.Anthropic()
df = pd.read_csv("data/dataset.csv")

safe_examples = df[df["label"] == "safe"]["text"].tolist()
injection_examples = df[df["label"] == "injection"]["text"].tolist()

def generate_examples(label, examples, count=50):
    example_str = "\n".join([f'- "{ex}"' for ex in examples[:10]])
    prompt = f"""The following are "{label}" labeled student inputs for an educational chatbot:
    {example_str}
    Generate {count} new examples similar to these.
    - Mix Turkish and English inputs
    - Make each example unique
    - Return only a JSON array, nothing else

    Format: ["örnek1", "örnek2", ...]"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = message.content[0].text
    examples_list = json.loads(response_text)
    return examples_list

print("Generating safe examples...")
new_safe = generate_examples("safe", safe_examples, count=230)

print("Generating injection examples...")
new_injection = generate_examples("injection", injection_examples, count=230)

new_rows = (
    [{"text": t, "label": "safe"} for t in new_safe] +
    [{"text": t, "label": "injection"} for t in new_injection]
)

df_new = pd.DataFrame(new_rows)
df_combined = pd.concat([df, df_new], ignore_index=True)
df_combined.to_csv("data/dataset.csv", index=False)

print(f"Done! Total examples: {len(df_combined)}")