from datetime import datetime


class Task:

	# I have updated the __init__ function to be able to convert the json file data to Task class object
	def __init__(self, title, description, completed=False, created_at=datetime.now().isoformat(), completed_in=None):
		self.title = title
		self.description = description
		self.completed = completed
		self.created_at = created_at
		self.completed_in = completed_in


class TaskManager:

	def __init__(self, storage):
		self.storage = storage

	def add_task(self, title, description):
		task = Task(title, description)
		self.storage.save_task(task)
		return task

	def complete_task(self, title):
		task = self.storage.get_task(title)
		if task:
			# Completed task doesn't require completion, it may change completion time and the time required to complete it
			if task.completed == True:
				print("Task is already completed")
				return True
			else:
				task.completed = True
				# Added a new parameter completed_in to calculate how much time it takes to complete a task
				task.completed_in = (datetime.now() - datetime.fromisoformat(task.created_at)).total_seconds() 
				self.storage.update_task(task)
				return True
		return False

	def list_tasks(self, include_completed=False):
		# Updated list function to filter completed task if --all is not applied
		tasks = [task for task in self.storage.get_all_tasks() if task.completed==include_completed or include_completed == True]
		return tasks

	def generate_report(self):
		tasks = self.storage.get_all_tasks()
		total_tasks = len(tasks)
		completed_tasks = len([task for task in tasks if task.completed])
		
		# Calculates average time of all the completed tasks
		avg_time = 0
		for task in tasks:
			if task.completed == True:
				avg_time = avg_time + (task.completed_in or 0)

		report = {
		    "total": total_tasks,
		    "completed": completed_tasks,
		    "pending": total_tasks - completed_tasks,
		    "avg completion time": f"{round(avg_time / 60, 2)} minutes"
		}

		return report

