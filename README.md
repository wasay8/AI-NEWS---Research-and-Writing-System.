# AI-Powered News Research and Writing System

This project is an AI-driven solution designed to automate news research and article writing using advanced language models like Groq's Llama3-70B and Google Generative AI. The system consists of specialized agents responsible for analyzing trending technologies and generating industry-relevant content in markdown format.

## Features

- **Multi-Agent Architecture**: 
  - **Senior Researcher Agent**: Uncovers cutting-edge trends and analyzes their market potential and risks.
  - **Writer Agent**: Crafts engaging, easy-to-understand articles based on research findings.
  
- **Automated Workflow**: Agents collaborate seamlessly to research and generate reports/articles on the latest tech trends.
  
- **Real-Time Search Capabilities**: Integrated with SerperDevTool for dynamic content retrieval and real-time data analysis.

- **Customizable Outputs**: Articles are formatted in markdown, making them easy to export or integrate into other workflows.

- **Streamlit User Interface**: Simple and interactive UI where users can input topics and generate articles with a single click.

## Tech Stack

- **Language Models**: Groq Llama3-70B, Google Generative AI
- **Tools**: SerperDevTool for search capabilities
- **Frameworks**: Langchain for LLM integration, Streamlit for the UI
- **Environment Management**: Python, dotenv for managing environment variables

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-news-system.git
   cd ai-news-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory and add the following keys:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key
     OPENAI_API_KEY=your_openai_api_key
     SERPER_API_KEY=your_serper_api_key
     ```

4. Run the Streamlit app:
   ```bash
   streamlit run crew.py
   ```

## Usage

1. Launch the app in your browser.
2. Enter a topic (e.g., "Latest AI trends").
3. Click the **Get News** button to generate the research report and article.

## Project Structure

- **agents.py**: Defines the `news_researcher` and `news_writer` agents with their respective goals and tasks.
- **tasks.py**: Configures the research and writing tasks assigned to the agents.
- **tools.py**: Handles the integration of search capabilities using SerperDevTool.
- **crew.py**: Orchestrates the overall process and manages user interactions via the Streamlit interface.

## Contributing

Feel free to open issues or submit pull requests to improve this project.

Special Thanks to Krish Naik!!!
