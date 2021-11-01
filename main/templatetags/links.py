from django import template
from django.urls import reverse
from django.core.validators import URLValidator
from blog.models import Post

import re

register = template.Library()


@register.filter
def internal_links(value):
    pattern = r'\[(.+?)\]\({{(\S+):(\S+)}}\)'
    link_patterns = list(set(re.findall(pattern, value)))

    if len(link_patterns) == 0:
        return value

    for lp in link_patterns:
        link_text, app_name, slug = lp

        internal_link = f'[{link_text}]' + r'({{' + f'{app_name}:{slug}' + r'}})'

        if not validate_slug_exists(slug):
            markdown_link = r'**!!!INVALID SLUG!!!**'
        elif not validate_slug_published(slug):
            markdown_link = link_text
        else:
            try:
                url = locate_url(app_name, slug)
                markdown_link = f'[{link_text}]({url})'
            except KeyError:
                markdown_link = r'**!!!INVALID APP NAME!!!**'

        value = value.replace(internal_link, markdown_link)

    return value


def locate_url(app_name, slug):
    link_types = {'blog': 'post',
                  'portfolio': 'project'}

    return reverse(f'{app_name}:{link_types[app_name]}', args=(slug,))


def validate_slug_exists(slug):
    return len(Post.objects.filter(slug=slug)) > 0


def validate_slug_published(slug):
    return len(Post.released_objects.filter(slug=slug)) > 0
