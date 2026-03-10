import json
import random

def get_system_prompt():
    return "You are a helpful and highly capable coding assistant."

def generate_python_data(n):
    ops = ['sum', 'product', 'average', 'max', 'min']
    conds = ['greater than', 'less than', 'equal to', 'not equal to', 'divisible by', 'not divisible by']
    data = []
    seen_prompts = set()

    while len(data) < n:
        op = random.choice(ops)
        cond = random.choice(conds)
        val = random.randint(1, 10000)

        prompt = f"Write a Python function named `process_list` that takes a list of integers `arr`. It should calculate and return the {op} of all elements that are {cond} {val}. If no elements match the condition, return 0."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        # Generate code
        code = f"def process_list(arr):\n    filtered = []\n    for x in arr:\n"
        if cond == 'greater than': code += f"        if x > {val}:\n"
        elif cond == 'less than': code += f"        if x < {val}:\n"
        elif cond == 'equal to': code += f"        if x == {val}:\n"
        elif cond == 'not equal to': code += f"        if x != {val}:\n"
        elif cond == 'divisible by': code += f"        if x % {val} == 0:\n"
        elif cond == 'not divisible by': code += f"        if x % {val} != 0:\n"

        code += "            filtered.append(x)\n    \n    if not filtered:\n        return 0\n    \n"

        if op == 'sum': code += "    return sum(filtered)"
        elif op == 'product':
            code += "    res = 1\n    for num in filtered:\n        res *= num\n    return res"
        elif op == 'average': code += "    return sum(filtered) / len(filtered)"
        elif op == 'max': code += "    return max(filtered)"
        elif op == 'min': code += "    return min(filtered)"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here is the Python function to achieve this:\n\n```python\n{code}\n```"}
            ]
        })
    return data

def generate_sql_data(n):
    columns_opts = ['name', 'id, name', 'name, department', '*', 'id, salary', 'name, salary']
    op_map = {
        '>': 'greater than',
        '<': 'less than',
        '>=': 'greater than or equal to',
        '<=': 'less than or equal to',
        '=': 'equal to',
        '!=': 'not equal to'
    }
    order_cols = ['name', 'salary', 'id', 'hire_date']
    order_dirs = ['ASC', 'DESC']

    data = []
    seen_prompts = set()
    operators = list(op_map.keys())

    while len(data) < n:
        cols = random.choice(columns_opts)
        op = random.choice(operators)
        op_text = op_map[op]
        val = random.randint(300, 20000) * 10
        order_col = random.choice(order_cols)
        order_dir = random.choice(order_dirs)
        limit = random.choice([5, 10, 50, 100, 500, None])

        prompt = f"Write a SQL query to select {cols} from the `employees` table where the `salary` is {op_text} {val}. Order the results by `{order_col}` in {order_dir}ending order"
        if limit:
            prompt += f" and limit the output to {limit} rows."
        else:
            prompt += "."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        query = f"SELECT {cols}\nFROM employees\nWHERE salary {op} {val}\nORDER BY {order_col} {order_dir}"
        if limit:
            query += f"\nLIMIT {limit};"
        else:
            query += ";"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here is the SQL query based on your requirements:\n\n```sql\n{query}\n```"}
            ]
        })
    return data

def generate_js_data(n):
    entities = [
        ('users', 'age', 'name'),
        ('products', 'price', 'id'),
        ('cars', 'mileage', 'model'),
        ('books', 'pages', 'title'),
        ('transactions', 'amount', 'transactionId'),
        ('employees', 'tenure', 'email')
    ]
    op_map = {
        '>': 'greater than',
        '<': 'less than',
        '>=': 'greater than or equal to',
        '<=': 'less than or equal to',
        '===': 'strictly equal to',
        '!==': 'strictly not equal to'
    }

    data = []
    seen_prompts = set()
    operators = list(op_map.keys())

    while len(data) < n:
        entity, prop, map_prop = random.choice(entities)
        op = random.choice(operators)
        op_text = op_map[op]
        val = random.randint(5, 5000)

        prompt = f"Write a JavaScript function named `getFiltered{entity.capitalize()}` that takes an array of `{entity}` objects. It should filter the array to keep only objects where `{prop}` is {op_text} {val}, and then return a new array containing only the `{map_prop}` of the filtered objects."

        if prompt in seen_prompts:
            continue
        seen_prompts.add(prompt)

        code = f"function getFiltered{entity.capitalize()}({entity}) {{\n"
        code += f"  return {entity}\n"
        code += f"    .filter(item => item.{prop} {op} {val})\n"
        code += f"    .map(item => item.{map_prop});\n"
        code += f"}}"

        data.append({
            "messages": [
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here is the JavaScript function:\n\n```javascript\n{code}\n```"}
            ]
        })
    return data

def main():
    # Set seed for reproducibility
    random.seed(42)

    # 5000 examples per topic, total 15000 examples
    n_per_topic = 5000
    dataset = []

    print("Generating Python data...")
    dataset.extend(generate_python_data(n_per_topic))

    print("Generating SQL data...")
    dataset.extend(generate_sql_data(n_per_topic))

    print("Generating JS data...")
    dataset.extend(generate_js_data(n_per_topic))

    # Shuffle the dataset
    random.shuffle(dataset)

    output_file = 'qwen_coding_dataset.jsonl'
    print(f"Writing to {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in dataset:
            f.write(json.dumps(item) + '\n')

    print(f"Successfully generated {len(dataset)} STRICTLY UNIQUE examples!")

if __name__ == '__main__':
    main()
