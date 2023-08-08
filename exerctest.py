import subprocess

def check_python_file(file_path):
    try:
        output = subprocess.check_output(['python', file_path], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        print(e.output)
        return False

# Example usage
if check_python_file('exerc.py'):
    print("The file runs without errors.")
else:
    print("The file generated errors.")


import importlib
import openai

# load the student's script
student_script = importlib.import_module('exerc')

def test_generate_response():
    # Prepare dummy inputs
    prompt = 'Translate the following English text to French: "{0}"'.format('Hello, how are you?')
    model = 'text-davinci-002'

    # Run the student's function
    try:
        response = student_script.generate_response(prompt, model)
        # The openai.Completion.create method returns a dictionary where the response is located in ['choices'][0]['text']
        # We can simulate a dummy return to compare with the student's function
        dummy_response = openai.Completion.create(engine=model, prompt=prompt)
    
        if  response == dummy_response['choices'][0]['text']:
            print( "The function output does not match expected output")

        print("Test passed!")
    except Exception as e:
        print(f"Test failed: {e}")

# Run the test function
test_generate_response()
