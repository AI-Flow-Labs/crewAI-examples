# AI Crew for Posting content on reddit
## Introduction
This project use the CrewAI framework to automate the analysis and creation of a post on a specific subreddit. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [License](#license)

## CrewAI Framework
[CrewAI](https://github.com/crewAIInc/crewAI) is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to analyse a subreddit then create a specific content for a post.

## Running the Script
It uses gemini-flash by default so you should have access to that to run it.

***Disclaimer:** This will use gemini-flash unless you change it to use a different model, and by doing so it can be ran at no cost on the free tier.*

- **Install Dependencies**: Install [CrewAI](https://github.com/crewAIInc/crewAI?tab=readme-ov-file#1-installation) and run `crewai install`.
- **Configure Environment**: Copy `.env.example` and set up the environment variables for [Gemini](https://aistudio.google.com/app/apikey) and other tools as needed, like [Reddit](https://www.reddit.com/prefs/apps).
- **Customize**: Modify `src/reddit_content_creator/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/reddit_content_creator/config/agents.yaml` to update your agents and `src/reddit_content_creator/config/tasks.yaml` to update your tasks.
- **Execute the Script**: Run `crewai run` and check the output 🪄.

## Details & Explanation
- **Running the Script**: Execute `crewai run`. The script will leverage the CrewAI framework to generate a specific post in a subreddit.
- **Key Components**:
  - `src/reddit_content_creator/main.py`: Main script file.
  - `src/reddit_content_creator/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/reddit_content_creator/config/agents.yaml`: Configuration file for defining agents.
  - `src/reddit_content_creator/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/reddit_content_creator/tools/reddit.py`: Contains Reddit tool classes used by the agents to call Reddit API.

## License
This project is released under the MIT License.