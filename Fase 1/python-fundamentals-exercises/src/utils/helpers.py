def validate_integer(value):
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        raise ValueError("Invalid input: Please enter a valid integer.")

def generate_random_number(min_value=1, max_value=100):
    import random
    return random.randint(min_value, max_value)

def format_output(message):
    return f"Output: {message}"