from django import template
register = template.Library()
class ReverseNode(template.Node):
    def __init__(self, value):
        self.value = str(value)
    def render(self, context):
        return self.value[::-1]
# 声明定义标签
@register.tag(name='reversal')
# 定义标签的解析器
# parser 为解析器，token 为标签内容
def do_reverse(parser, token):
    try:
        tag_name, value = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return ReverseNode(value)