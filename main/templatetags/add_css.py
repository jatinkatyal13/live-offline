from django import template

register = template.Library()

@register.filter
def addCss(value, arg):
	return value.as_widget(attrs={'class':arg})
