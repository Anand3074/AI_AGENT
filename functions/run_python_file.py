import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(file_path)
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read content "{file_path}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_working_dir):
        return f'Error: "{working_directory}" is not a working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        final_args = ["python3",abs_file_path]
        final_args.extend(args)
        output = subprocess.run(final_args,
                        timeout=30, 
                        cwd = abs_working_dir,
                        capture_output=True, )
        final_string = f"""
        STDOUT : {output.stdout}
        STDERR : {output.stderr}
        """
        if output.stdout == "" and output.stderr == "":
            final_string = 'No output procedured.\n'

        if output.returncode !=0:
            final_string += f"Process exited with code : {output.returncode}"
        return final_string
    except Exception as e:
        return f"Error: executing Python file: {e}"    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file using python3 interpreter,Accepts additional CLI args as an optional array. constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as the CLI args for the python file.",
                items = types.Schema(
                type=types.Type.STRING,
                )
            ),
        },
    ),
)