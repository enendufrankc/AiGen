# AiGen: AI Implementation Use Cases for Developers
### Overview
AiGen is an open-source project designed to streamline the process of developing AI applications. It offers a collection of pre-configured templates for various AI use cases, allowing developers to quickly set up and deploy AI-powered apps

### Goals and Objectives
- Ease of Use: Simplify the process of creating AI applications by providing ready-to-use templates that reduce setup time and complexity.
- Flexibility: Allow developers to choose from a variety of use cases and LLMs, catering to different project needs and preferences.
- Extensibility: Enable developers to extend and customize the provided templates to suit their specific requirements.
- Community-Driven Development: Foster a community of developers who can contribute new use cases, improvements, and features to the project.

### Key Features
1. Pre-Configured Templates:
- Templates for various AI applications such as SQL chat apps, PDF chat apps, web browser apps, and more.
- Each template includes necessary dependencies, a basic Streamlit app, and boilerplate code to get started.

2. Command Line Interface (CLI):
- Easy-to-use CLI to create new projects based on selected use cases.
- Commands to list available use cases, create new projects, and manage configurations.

3. Flexible LLM Integration:
- Support for multiple language models (LLMs).
- Simple configuration to input API keys and select the desired LLM.

4. Automated Setup:
- Automatic generation of project structure and dependencies.
- Streamlined process to set up and run the application with minimal manual intervention.

### How It Works
1. Installation:
- Install AiGen via PyPI using `pip install aigen`.

2. Creating a New Project:
- Use the CLI to create a new project: aigen create <use_case> <project_name>.
Example: `aigen create sql_chat_app my_sql_chat_project`.

3. Configuring the Project:
- Navigate to the project directory and install dependencies: `pip install -r requirements.txt`.
- Input your API key and select your LLM in the configuration file.

4. Running the Application:
- Run the application using Streamlit: `streamlit run main.py`.

5. Customization:
- Modify the generated code and configurations to tailor the application to your specific needs.

### Use Cases
1. SQL Chat App:
A conversational AI app that can interact with SQL databases and execute queries based on natural language input.

2. PDF Chat App:
An AI-powered application that allows users to interact with PDF documents, extracting information and answering questions based on the content.

3. Web Browser App:
An AI assistant that can browse the web, fetch information, and perform actions based on user queries.

4. Additional Use Cases:
Continuously expanding list of templates based on community contributions and emerging AI technologies.

### Contribution Guidelines
1. Submitting Issues:
- Report bugs and request features via the GitHub issues page.
2. Creating Pull Requests:
- Fork the repository, make your changes, and submit a pull request for review.
3. Writing Documentation:
- Contribute to the documentation to help others understand and use AiGen effectively.
4. Community Engagement:
- Participate in discussions, share your use cases, and collaborate with other developers.

### Roadmap
1. Expand Use Case Library:
- Continuously add new templates for diverse AI applications.
2. Enhance CLI Functionality:
- Introduce more CLI commands for better project management and configuration.
3. Improve LLM Integration:
- Support additional LLMs and improve the configuration process.
4. Community Building:
- Foster a vibrant community through forums, discussions, and collaborative events.
5. Documentation and Tutorials:
- Develop comprehensive tutorials and examples to help new users get started quickly.

### Conclusion
AiGen aims to democratize AI development by providing easy-to-use, pre-configured templates for various AI applications. Whether you're a seasoned developer or just starting with AI, AiGen helps you kickstart your projects with minimal setup and maximum flexibility. Join our community, contribute, and let's build the future of AI development together.
