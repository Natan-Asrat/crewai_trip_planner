from langchain.tools import tool

class CalculateTools():
    @tool("Make a calculation")
    def calculate(operation):
        """
        This tool allows you to make a calculation using Python's built-in eval() function."""
        try:
            return eval(str(operation))
        except SyntaxError:
            return "Error: invaid syntax in mathematical expression"
        except Exception as e:
            return f"Error: {e}"