import json
import random
import itertools

def get_system_prompt():
    return "You are an expert frontend developer specializing in HTML, CSS, and vanilla JavaScript."

def generate_frontend_data(n):
    # We will combine attributes to ensure uniqueness
    elements = ['button', 'card', 'navbar', 'modal', 'form', 'footer', 'sidebar', 'hero', 'accordion', 'tooltip']
    colors = ['#ff5733', '#33ff57', '#3357ff', '#f333ff', '#33fff3', '#ff3333', '#33ff33', '#3333ff', '#ffff33', '#33ffff']
    bg_colors = ['#f4f4f4', '#e0e0e0', '#dcdcdc', '#c0c0c0', '#a9a9a9', '#808080', '#696969', '#778899', '#708090', '#2f4f4f']
    font_sizes = ['12px', '14px', '16px', '18px', '20px', '24px', '32px', '48px', '64px', '72px']
    border_radius = ['0px', '2px', '4px', '8px', '12px', '16px', '24px', '50%', '100px', '999px']
    margins = ['0px', '4px', '8px', '12px', '16px', '20px', '24px', '32px', '40px', '48px']
    paddings = ['0px', '4px', '8px', '12px', '16px', '20px', '24px', '32px', '40px', '48px']
    js_actions = ['alert', 'console.log', 'toggle_class', 'change_text', 'change_color', 'hide', 'show', 'fetch_data', 'animate', 'scroll']

    data = []
    seen_prompts = set()

    # Let's use permutations or just random with a while loop, since 10^8 combinations exist
    while len(data) < n:
        el = random.choice(elements)
        color = random.choice(colors)
        bg_color = random.choice(bg_colors)
        fs = random.choice(font_sizes)
        br = random.choice(border_radius)
        margin = random.choice(margins)
        padding = random.choice(paddings)
        action = random.choice(js_actions)

        prompt = f"Write an HTML, CSS, and JS snippet for a {el}. The text color should be {color}, background color {bg_color}, font size {fs}, border-radius {br}, margin {margin}, and padding {padding}. When interacted with, it should perform a {action} action."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        # Build the HTML/CSS/JS response
        html = f'<div id="my-{el}" class="custom-{el}">\n  Click me!\n</div>'
        css = f"""
.custom-{el} {{
    color: {color};
    background-color: {bg_color};
    font-size: {fs};
    border-radius: {br};
    margin: {margin};
    padding: {padding};
    cursor: pointer;
    transition: all 0.3s ease;
}}
"""
        js = f"""
document.getElementById('my-{el}').addEventListener('click', function() {{
"""
        if action == 'alert':
            js += f"    alert('You clicked the {el}!');"
        elif action == 'console.log':
            js += f"    console.log('Action triggered on {el}');"
        elif action == 'toggle_class':
            js += f"    this.classList.toggle('active');"
        elif action == 'change_text':
            js += f"    this.innerText = 'Interacted!';"
        elif action == 'change_color':
            js += f"    this.style.color = '{random.choice(colors)}';"
        elif action == 'hide':
            js += f"    this.style.display = 'none';"
        elif action == 'show':
            js += f"    this.style.display = 'block';" # simple fallback
        elif action == 'fetch_data':
            js += f"    fetch('https://jsonplaceholder.typicode.com/todos/1').then(r => r.json()).then(d => console.log(d));"
        elif action == 'animate':
            js += f"    this.style.transform = 'scale(1.1)';"
        elif action == 'scroll':
            js += f"    window.scrollTo(0, 0);"

        js += "\n});"

        content = f"Here is the requested code for the {el}:\n\n**HTML:**\n```html\n{html}\n```\n\n**CSS:**\n```css\n{css}\n```\n\n**JavaScript:**\n```javascript\n{js}\n```"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": content}
            ]
        })

    return data

def main():
    random.seed(1337)

    n_examples = 40000
    print(f"Generating {n_examples} frontend examples...")
    dataset = generate_frontend_data(n_examples)

    output_file = 'frontend_dataset.jsonl'
    print(f"Writing to {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in dataset:
            f.write(json.dumps(item) + '\n')

    print(f"Successfully generated {len(dataset)} STRICTLY UNIQUE examples!")

if __name__ == '__main__':
    main()
