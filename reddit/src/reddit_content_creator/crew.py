from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from reddit_content_creator.tools.reddit import RedditGetTopPostsTool, RedditGetSubredditTool

@CrewBase
class RedditContentCreator():
	"""RedditContentCreator crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def digital_trends_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['digital_trends_analyst'],
			tools=[RedditGetTopPostsTool(), RedditGetSubredditTool()],
		)
	
	@agent
	def content_creator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['content_creator_agent'],
		)

	@task
	def monitor_trending_news(self) -> Task:
		return Task(
			config=self.tasks_config['monitor_trending_posts'],
			agent=self.digital_trends_analyst(),
		)
	
	@task
	def create_content(self) -> Task:
		return Task(
			config=self.tasks_config['create_content'],
			agent=self.content_creator_agent(),
			context=[self.monitor_trending_news()],
		)

	@task
	def rewrite_content(self) -> Task:
		return Task(
			config=self.tasks_config['rewrite_content'],
			agent=self.content_creator_agent(),
			context=[self.create_content()],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the RedditContentCreator crew"""
  
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			verbose=False,
		)
