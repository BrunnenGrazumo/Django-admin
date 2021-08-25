from django import template

from simpleapp.models import Post
import os
register = template.Library()

# @register.filter(name='censor')
# def censor(text):
#     module_dir = os.path.dirname(__file__)
#     t = os.path.join(module_dir, 'badwords.txt')
#     for a in Post.text:
#         if a in t:
#             a = "****"
#             return a



