import ast

def summarize_code(file_path):
    try:
        with open(file_path, "r") as f:
            code = f.read()
    except Exception as e:
        return f"Error reading file: {e}"

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"Syntax error in strategy file: {e}"

    func_count = 0
    loop_count = 0
    if_count = 0
    constants = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_count += 1
        elif isinstance(node, (ast.For, ast.While)):
            loop_count += 1
        elif isinstance(node, ast.If):
            if_count += 1
        elif isinstance(node, ast.Assign):
            for target in node.targets:
            # Only extract simple variable assignments, skip things like position[0]
                if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                    constants[target.id] = node.value.value


    const_str = ", ".join(f"{k}={v}" for k, v in constants.items()) if constants else "none"
    
    return (
        f"Functions: {func_count}, Loops: {loop_count}, Ifs: {if_count}, "
        f"Constants: {const_str}"
    )

