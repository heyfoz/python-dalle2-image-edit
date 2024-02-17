import os
import subprocess
import json

def get_user_input(prompt):
    """ Function to get user input """
    return input(prompt)

def main():
    # Fetch the API key from the system environment
    api_key = os.environ.get('OPENAI_API_KEY')

    if not api_key:
        print("API key not found in environment. Please set OPENAI_API_KEY.")
        return

    while True:
        # Prompt user for file locations and the prompt
        image_file = get_user_input("Enter the file location of the original image or c to cancel: ")
        if image_file.lower() == "c":
            print("Script cancelled.")
            break

        mask_file = get_user_input("Enter the file location of the mask image or c to cancel: ")
        if mask_file.lower() == "c":
            print("Script cancelled.")
            break

        user_prompt = get_user_input("Enter your DALLE editing prompt or c to cancel: ")
        if user_prompt.lower() == "c":
            print("Script cancelled.")
            break

        # Confirm the input
        confirm = get_user_input("Are you sure you want to submit this prompt with the specified images? Enter y for Yes or n to cancel: ")
        if confirm.lower() == "n":
            continue

        # JSON data for the API request
        data = {
            "model": "dall-e-2",           # Specifies the model to be used
            "prompt": user_prompt,         # The user-provided prompt
            "n": 1,                        # Number of images to generate
            "size": "1024x1024"            # Size of the generated images
        }

        # Constructing the cURL command for the API request
        curl_command = [
            "curl", "-X", "POST", "https://api.openai.com/v1/images/edits",
            "-H", "Authorization: Bearer {}".format(api_key),
            "-F", "image=@{}".format(image_file),
            "-F", "mask=@{}".format(mask_file),
            "-F", "model=dall-e-2",
            "-F", "prompt={}".format(user_prompt),
            "-F", "n=1",
            "-F", "size=1024x1024"
        ]

        # Print the created cURL request for debugging
        print("cURL Command:", " ".join(curl_command))
        
        # Executing the cURL command and capturing the response
        try:
            response = subprocess.run(curl_command, capture_output=True, text=True, check=True)
            print("Response:\n", response.stdout)
        except subprocess.CalledProcessError as e:
            # Handling errors during the API request
            print("Error occurred:")
            print(e.stderr)

        break

if __name__ == "__main__":
    main()
