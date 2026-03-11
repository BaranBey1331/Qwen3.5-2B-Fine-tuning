import json

files = ['html_dataset.jsonl', 'css_dataset.jsonl', 'react_dataset.jsonl', 'nodejs_dataset.jsonl']

for f_name in files:
    try:
        with open(f_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) != 20000:
            print(f"Error: {f_name} has {len(lines)} lines, expected 20000.")
            continue

        unique_prompts = set()
        for i, line in enumerate(lines):
            try:
                data = json.loads(line.strip())
                # Check chatml format
                if "messages" not in data or len(data["messages"]) != 3:
                    print(f"Format error in {f_name} at line {i+1}")
                    continue

                # Verify prompt uniqueness
                user_prompt = data["messages"][1]["content"]
                if user_prompt in unique_prompts:
                    print(f"Duplicate prompt found in {f_name}: {user_prompt}")
                unique_prompts.add(user_prompt)
            except json.JSONDecodeError:
                print(f"Invalid JSON in {f_name} at line {i+1}")

        if len(unique_prompts) == 20000:
            print(f"Success: {f_name} is valid with 20000 strictly unique examples.")
        else:
            print(f"Error: {f_name} has {len(unique_prompts)} unique examples out of 20000.")

    except FileNotFoundError:
        print(f"Error: {f_name} not found.")
