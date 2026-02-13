import ast
import json

def extract_logic(code_content):
    """
    Parses Python code and extracts class and function definitions.
    Returns a string containing only the extracted logic.
    """
    try:
        tree = ast.parse(code_content)
    except SyntaxError as e:
        return f"Syntax Error during parsing: {e}"

    logic_nodes = []
    
    for node in tree.body:
        # Extract Functions, Async Functions, and Classes
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # ast.unparse is available in Python 3.9+
            # If n8n runs older python, we might need a workaround, but let's assume modern.
            try:
                logic_nodes.append(ast.unparse(node))
            except AttributeError:
                # Fallback or error for older python 
                return "Python version in n8n is too old for ast.unparse. Need Python 3.9+"
            
    return "\n\n".join(logic_nodes)

# This is the entry point for n8n
# n8n provides 'ndata' globally or we can use the following structure:
# items is a list of objects with a 'json' property

def main():
    # In n8n, the script is executed in a context where 'items' is available.
    # We will wrap this logic in a way that n8n can use it easily.
    pass

if __name__ == "__main__":
    # Test block
    with open(__file__, 'r') as f:
        content = f.read()
    print(extract_logic(content))
