# Dolphin

> For my dear friend, from Alan

## LEFTOVERS
For your main logic within the `translate_text` function, given the complexity and the requirement for extensive debugging, it's understandable to consider it as a work in progress. Therefore, you can treat the core processing logic as a placeholder, stored within a hypothetical `translator` object or module, for future implementation.

## Description
Dolphin is a project crafted with love by Alan, designed to transform tangible code blocks into pseudo-code using Google Cloud Vision API.

## Features
- Transform images of code into readable pseudo-code.
- Leverage Google Cloud Vision API for accurate text detection in code blocks.
- Intuitive interface for easy uploading and processing of code images.

## Prerequisites
- Google Cloud account
- Google Cloud Project with Vision API enabled
- Python 3.x environment

## Setup Instructions

### Google Cloud Vision API Setup
1. **Create a Google Cloud Project**: Initiate a new project within the Google Cloud Console to get started.
2. **Enable the Vision API**: From the "APIs & Services" dashboard in your project, activate the Vision API.
3. **Create a Service Account**: Set up a new service account, assigning it the roles required for accessing the Vision API (e.g., Vision User).
4. **Download Your Service Account Key**: Securely generate and download a JSON key for your service account.

### Virtual Environment Setup

Before running the application, it's crucial to set up a virtual environment to manage dependencies separately from your system Python installation. You can use either `venv` (built-in Python module) or `conda` (Anaconda distribution).

### Using venv

To create and activate a virtual environment with `venv`, follow these steps:

1. Navigate to your project directory:

    ```
    cd path/to/your/project
    ```

2. Create a virtual environment:

    ```
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

4. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

### Using Conda

If you're using Conda, you can create a new environment and install packages as follows:

1. Create a new Conda environment:

    ```
    conda create --name myenv python=3.8
    ```

2. Activate the Conda environment:

    ```
    conda activate myenv
    ```

3. Install the required packages (make sure you have a `requirements.txt` file):

    ```
    pip install -r requirements.txt
    ```

### Environment Setup
1. **Clone the Repository**: Execute `git clone https://github.com/alansynn/dolphin.git` to obtain the project.
2. **Project Directory**: Enter the project using `cd dolphin`.
3. **Install Dependencies**: Run `pip install -r requirements.txt` for installing the necessary Python packages.
4. **Configure `GOOGLE_APPLICATION_CREDENTIALS`**:
    - Linux/Mac: Use `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"` to set up.
    - Windows: Apply `set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\service-account-file.json` for configuration.

## Usage

Ensure you've activated your virtual environment as described above. To run the application, execute the following command in your terminal or command prompt:

1. **Launch the Application**: Start the app by running `python dolphin/server.py`.
2. **Web Interface**: Navigate to `http://localhost:1200/upload` in your browser.
3. **Image Upload**: Use the web interface to upload images of code blocks for processing.