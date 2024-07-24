# DALL-E 2 Image Editor Script

This Python script enables users to interact with OpenAI's DALL-E 2 API for image editing. Users can specify an original image, a mask image, and a text prompt for the DALL-E 2 model to edit the image accordingly.

**NOTE**: OpenAI API documentation and capabilities may change over time. For the most current information, refer to the official [OpenAI site for developers](https://platform.openai.com/docs/guides/images/introduction).

## Important Note
The images generated or edited by the DALL-E 2 API are typically available immediately after the request. However, it's important to handle the data responsibly and in accordance with OpenAI's use case policies.

## Authentication
The script requires an API key from OpenAI for authentication. Before running the script, you must set up an environment variable `OPENAI_API_KEY` or similarly named variable with your OpenAI API key. Retrieve your API key from the [API Keys page on OpenAI](https://platform.openai.com/account/api-keys). 

Alternatively, the environment variable name can be customized if needed. The purpose of setting this environment variable is to securely store and access the API key within your application without hardcoding it into the script.

For assistance on setting up environment variables:
- On Windows, see Microsoft's guide on [Environment Variables](https://learn.microsoft.com/en-us/windows/win32/procthread/environment-variables).
- On Linux/Unix, refer to the guide on [setting environment variables in Linux](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/).

## Features

- Interactive prompts for user input of the original image, mask image, and editing prompt.
- Integration with OpenAI's DALL-E 2 API for image editing.
- Execution of a constructed cURL command to make the API request.

## Prerequisites

Ensure you have the following installed before running this script:

- Python (3.x or higher)
- Access to a terminal or command prompt
- An API key from OpenAI for DALL-E 2 access

## Installation

1. Install Python from [Python's official website](https://www.python.org/downloads/).
2. Ensure you have access to a terminal or command prompt for executing Python scripts.
3. Set up an environment variable `OPENAI_API_KEY` with your OpenAI API key.

## Usage

Run the script in a Python environment. Follow the interactive prompts to enter the locations of your original image, mask image, and your editing prompt. The script will then perform the image editing and provide feedback.

## OpenAI DALL-E 2 API Resources

For detailed information about the DALL-E 2 API and its image editing capabilities, refer to the following resources:

- [OpenAI Edit Image API Reference](https://platform.openai.com/docs/api-reference/images/createEdit)
- [OpenAI Edit Image Guide](https://platform.openai.com/docs/guides/images/edits-dall-e-2-only)
- [DALL·E](https://labs.openai.com/)
- [OpenAI API Pricing](https://openai.com/api/pricing)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
