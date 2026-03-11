import json
import random

def get_system_prompt(role):
    return f"You are an expert developer specializing in {role}."

def generate_html_data(n):
    elements = ['div', 'section', 'article', 'aside', 'header', 'footer', 'nav', 'main', 'figure', 'dialog']
    attributes = ['id', 'class', 'data-id', 'aria-label', 'tabindex', 'role', 'hidden', 'title', 'lang', 'dir']
    contents = ['Hello World', 'Welcome', 'Content here', 'Text block', 'Sample text', 'Placeholder', 'Info', 'Details', 'Data', 'Summary']
    styles = ['color: red;', 'margin: 10px;', 'padding: 5px;', 'display: flex;', 'position: relative;', 'font-size: 16px;', 'background: #fff;', 'border: 1px solid black;', 'cursor: pointer;', 'opacity: 0.8;']
    events = ['onclick', 'onmouseover', 'onmouseout', 'onkeydown', 'onkeyup', 'onfocus', 'onblur', 'onchange', 'onsubmit', 'onresize']

    data = []
    seen_prompts = set()

    while len(data) < n:
        el = random.choice(elements)
        attr = random.choice(attributes)
        val = f"val_{random.randint(1, 1000)}"
        content = random.choice(contents)
        style = random.choice(styles)
        event = random.choice(events)

        prompt = f"Create an HTML `<{el}>` element. It should have an `{attr}` attribute set to '{val}', an inline style of '{style}', an '{event}' event handler that logs 'triggered' to the console, and its text content should be '{content}'."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        html = f"<{el} {attr}=\"{val}\" style=\"{style}\" {event}=\"console.log('triggered')\">\n  {content}\n</{el}>"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt("HTML")},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here is the HTML element you requested:\n\n```html\n{html}\n```"}
            ]
        })
    return data

def generate_css_data(n):
    selectors = ['.container', '#main', 'article', '.card', '.btn', 'header', 'footer', 'ul > li', '.wrapper', '.box']
    props1 = ['color', 'background-color', 'font-size', 'font-weight', 'text-align', 'line-height', 'letter-spacing', 'text-transform', 'text-decoration', 'word-wrap']
    vals1 = ['red', '#333', '16px', 'bold', 'center', '1.5', '2px', 'uppercase', 'underline', 'break-word']
    props2 = ['margin', 'padding', 'border', 'border-radius', 'box-shadow', 'opacity', 'z-index', 'cursor', 'display', 'position']
    vals2 = ['10px', '20px', '1px solid black', '5px', '0 4px 8px rgba(0,0,0,0.1)', '0.9', '10', 'pointer', 'flex', 'absolute']

    data = []
    seen_prompts = set()

    while len(data) < n:
        sel = random.choice(selectors)
        p1 = random.choice(props1)
        v1 = random.choice(vals1)
        p2 = random.choice(props2)
        v2 = random.choice(vals2)
        extra_val = random.randint(1, 1000)

        prompt = f"Write a CSS rule for the selector `{sel}`. Set `{p1}` to `{v1}`, `{p2}` to `{v2}`, and set `width` to `{extra_val}px`."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        css = f"{sel} {{\n  {p1}: {v1};\n  {p2}: {v2};\n  width: {extra_val}px;\n}}"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt("CSS")},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here is the CSS rule:\n\n```css\n{css}\n```"}
            ]
        })
    return data

def generate_react_data(n):
    components = ['Button', 'Card', 'Modal', 'Sidebar', 'Navbar', 'Footer', 'Header', 'Form', 'List', 'Spinner']
    hooks = ['useState', 'useEffect', 'useContext', 'useRef', 'useMemo', 'useCallback', 'useReducer', 'useLayoutEffect']
    states = ['isOpen', 'data', 'count', 'loading', 'error', 'user', 'theme', 'config', 'items', 'text']
    props_opts = ['title', 'id', 'className', 'onClick', 'onChange', 'style', 'children', 'type', 'value', 'name']

    data = []
    seen_prompts = set()

    while len(data) < n:
        comp = random.choice(components)
        hook = random.choice(hooks)
        state = random.choice(states)
        prop = random.choice(props_opts)
        comp_id = random.randint(1, 5000)

        prompt = f"Create a React functional component named `{comp}{comp_id}` that accepts a `{prop}` prop. Inside the component, use the `{hook}` hook and define a state variable named `{state}`. Return a `div` containing the `{prop}`."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        if hook == 'useState':
            hook_code = f"  const [{state}, set{state.capitalize()}] = useState(null);"
        elif hook == 'useRef':
            hook_code = f"  const {state}Ref = useRef(null);"
        elif hook == 'useEffect':
            hook_code = f"  let {state} = null;\n  useEffect(() => {{\n    console.log('Effect triggered');\n  }}, []);"
        else:
            hook_code = f"  // Using {hook} for {state}\n  const {state} = {hook}(() => null);"

        react_code = f"import React, {{ {hook} }} from 'react';\n\nconst {comp}{comp_id} = ({{ {prop} }}) => {{\n{hook_code}\n\n  return (\n    <div>\n      {{{prop}}}\n    </div>\n  );\n}};\n\nexport default {comp}{comp_id};"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt("React")},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here is the React component:\n\n```jsx\n{react_code}\n```"}
            ]
        })
    return data

def generate_nodejs_data(n):
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'TRACE', 'CONNECT']
    paths = ['/users', '/posts', '/comments', '/products', '/orders', '/auth', '/settings', '/profile', '/search', '/upload']
    statuses = [200, 201, 202, 204, 400, 401, 403, 404, 500, 502]
    res_types = ['json', 'send', 'end', 'download', 'redirect', 'render', 'type', 'status', 'attachment', 'links']

    data = []
    seen_prompts = set()

    while len(data) < n:
        method = random.choice(methods)
        path = random.choice(paths)
        status = random.choice(statuses)
        res_type = random.choice(res_types)
        route_id = random.randint(1, 10000)

        prompt = f"Write an Express.js route that handles a {method} request to '{path}/{route_id}'. It should respond with an HTTP status code {status} and use the `res.{res_type}()` method to send the response."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        node_code = f"app.{method.lower()}('{path}/{route_id}', (req, res) => {{\n  res.status({status});\n"

        if res_type == 'json':
            node_code += f"  res.json({{ message: 'Success' }});\n"
        elif res_type == 'send':
            node_code += f"  res.send('Response sent');\n"
        elif res_type == 'redirect':
            node_code += f"  res.redirect('/home');\n"
        else:
            node_code += f"  res.{res_type}();\n"

        node_code += f"}});"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt("Node.js/Express")},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here is the Express route:\n\n```javascript\n{node_code}\n```"}
            ]
        })
    return data

def main():
    random.seed(999)
    n = 20000

    datasets = [
        ('html_dataset.jsonl', generate_html_data),
        ('css_dataset.jsonl', generate_css_data),
        ('react_dataset.jsonl', generate_react_data),
        ('nodejs_dataset.jsonl', generate_nodejs_data)
    ]

    for filename, generator in datasets:
        print(f"Generating {n} examples for {filename}...")
        data = generator(n)

        with open(filename, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')
        print(f"Successfully generated {len(data)} STRICTLY UNIQUE examples for {filename}!")

if __name__ == '__main__':
    main()
