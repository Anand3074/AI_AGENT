import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_function import call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set in environment")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read the contents of a file
    - Write to a file (create or update)
    - Run a python file with optional arguments

    When the user asks about the code project - they are referring to working directory.
    So you should typically start by looking at the project files and figuring out how to run the project and how to run its test, you'll always want to test the tests and the actual project to run to verify that behavior is working.

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)

    # Extract flags & prompt
    verbose_flag = "--verbose" in sys.argv
    prompt = next((arg for arg in sys.argv[1:] if not arg.startswith("--")), None)

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    max_iters = 20
    for i in range(max_iters):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=config,
        )

        if response is None or response.usage_metadata is None:
            print("Response is malformed")
            return

        if verbose_flag:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        function_calls = []
        handled_any = False

        if response.candidates:
            for candidate in response.candidates:
                if not candidate or not candidate.content:
                    continue

                # Add model response (if not just tool call)
                if candidate.content.parts:
                    # Extract function calls from parts
                    for part in candidate.content.parts:
                        if part.function_call:
                            function_calls.append(part.function_call)

                messages.append(candidate.content)

        if function_calls:
            response_parts = []
            for fc in function_calls:
                result = call_function(fc, verbose_flag)
                # call_function should already return a types.Content(role="tool", parts=[...])
                # so we just extract its part
                response_parts.extend(result.parts)

            # now append a single tool response with all parts
            messages.append(
                types.Content(
                    role="tool",
                    parts=response_parts
                )
            )
            continue  # go to next iteration, let Gemini use the responses


        if not handled_any:
            # No tool calls → final output
            print(response.text)
            return


if __name__ == "__main__":
    main()
