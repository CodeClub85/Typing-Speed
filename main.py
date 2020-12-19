
import kivy, time, random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class TypingTest(BoxLayout):
	def __init__(self, **kwargs):
		super(TypingTest, self).__init__(**kwargs)
		self.initial_time = 0
		
		with open('data.txt', 'r') as fp:
			self.phases = fp.readlines()
		self.phase.text = random.choice(self.phases).replace('\n', '')
	
	def focused(self):
		if self.initial_time == 0:
			self.initial_time = time.time()
			self.score.text = ''
			
	def get_score(self):
		total_time_taken =  (time.time() - self.initial_time) / 60
		total_words_typed = len(self.input.text.split())
		wpm = total_words_typed / total_time_taken
		return int(wpm)
		
	def show_score(self):
		text = ''
		if self.input.text != self.phase.text:
			text = 'You Typed Wrong, Type Again.'
		else:
			text = 'Your Typing Speed is ' + str(self.get_score()) + ' wpm'
		
		self.initial_time = 0
		self.score.text = text
		self.input.text = ''
		self.phase.text = random.choice(self.phases).replace('\n', '')

class MainApp(App):
	def build(self):
		return TypingTest()
		
if __name__ == '__main__':
	app = MainApp()
	app.run()
