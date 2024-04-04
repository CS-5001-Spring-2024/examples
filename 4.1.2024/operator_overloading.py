class Widget:

	def __init__(self, string, number):
		self.string = string
		self.number = number

	def __str__(self):
		return f'{self.string} - {self.number}'

	def __repr__(self):
		return f'{self.string} - {self.number}'

	def __lt__(self, other):
		if self.string == other.string:
			return self.number < other.number
		return self.string < other.string
		# return self.number < other.number

widgeta = Widget('hello', 12345)
widgetb = Widget('goodbye', 9876)

# widgeta < widgetb
# widgeta.__lt__(widgetb)

# print(widget)

widget_list = []
widget_list.append(Widget('A', 10))
widget_list.append(Widget('C', 8))
widget_list.append(Widget('B', 9))

widget_list_by_string = sorted(widget_list, key=lambda widget: widget.string)
widget_list_by_number = sorted(widget_list, key=lambda widget: widget.number)
widget_list = sorted(widget_list)

print(widget_list)