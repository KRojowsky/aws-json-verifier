import sys
import json


def verify_input(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

            for statement in data['PolicyDocument']['Statement']:
                if 'Resource' in statement:
                    if statement['Resource'] == '*':
                        return False

            return True

    except FileNotFoundError:
        print("Error: JSON file not found.")
        return True

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return True

    except KeyError as e:
        print(f"Error: Missing key in JSON: {str(e)}")
        return True

    except TypeError as e:
        print(f"Error: Type error in JSON: {str(e)}")
        return True

    except ValueError as e:
        print(f"Error: Value error in JSON: {str(e)}")
        return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    result = verify_input(json_file)
    print(result)
