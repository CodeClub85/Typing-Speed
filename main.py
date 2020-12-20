
import kivy, time, random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class TypingTest(BoxLayout):
	def __init__(self, **kwargs):
		super(TypingTest, self).__init__(**kwargs)
		self.initial_time = time.time()
		
		with open('data.txt', 'r') as fp:
			self.phases = fp.readlines()
		self.phase.text = random.choice(self.phases).replace('\n', '')
		self.per_letter_value = 100 / len(self.phase.text)
		
	def focused(self):
		if self.initial_time == 0:
			self.initial_time = time.time()
			self.score.text = ''
			
	def get_accuracy(self):
		count = 0
		for i in range(len(self.phase.text)):
			try:
				if self.input.text[i] != self.phase.text[i]:
					count += 1
			except IndexError:
				count += 1
		
		return 100 - self.per_letter_value * count
			
	def get_score(self, t):
		if t == 0:
			return 0
			
		words_typed = len(self.input.text.split())
		wpm = words_typed * 60 // t
		return int(wpm)
		
	def show_score(self):
		time_taken = int(time.time() - self.initial_time)
		self.time.text = 'Time: ' + str(time_taken) + 's'
		self.acc.text = f'Accuracy: {self.get_accuracy():.2f}%'
		self.score.text = 'Speed: ' + str(self.get_score(time_taken)) + 'wpm'
		
		self.initial_time = 0
		self.input.text = ''
		self.phase.text = random.choice(self.phases).replace('\n', '')
		self.per_letter_value = int(100 // len(self.phase.text))
		
		
		
class MainApp(App):
	def build(self):
		return TypingTest()
		
if __name__ == '__main__':
	app = MainApp()
	app.run()
