import json
from task_manager import Task

class Storage:	
	def __init__(self):
		try:
			taskList = self.read_from_json_file('store.json')
			self.tasks = [Task(task['title'], task['description'], task['completed'], task['created_at'], task['completed_in']) for task in taskList]		
		except:
			self.tasks = []

	def save_task(self, task):
		self.tasks.append(task)
		self.write_to_json_file("store.json", self.tasks)

	def update_task(self, updated_task):
		for i, task in enumerate(self.tasks):
			if task.title == updated_task.title:
				self.tasks[i] = updated_task
				break

		self.write_to_json_file("store.json", self.tasks)

	def get_task(self, title):
		for task in self.tasks:
			if task.title == title:
				return task
		return None

	def get_all_tasks(self):
		return list(self.tasks)

	def clear_all_tasks(self):
		self.tasks = []



	
	def read_from_json_file(self, jsonFileName):
		with open(jsonFileName, 'r') as openFile:
				return json.load(openFile)
		
	def write_to_json_file(self, jsonFileName, array):
		json_object = json.dumps([obj.__dict__ for obj in array], indent=4)
		with open(jsonFileName, "w") as outfile:
			outfile.write(json_object)