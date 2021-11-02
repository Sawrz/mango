from django import template
from django.urls import reverse
from blog.models import Post
from portfolio.models import Project
import re
from flashtext import KeywordProcessor

register = template.Library()


@register.filter
def internal_links(value):
    pattern = r'\[(.+?)\]\({{(\S+):(\S+)}}\)'
    link_patterns = list(set(re.findall(pattern, value)))

    if len(link_patterns) == 0:
        return value

    model_types = {'blog': Post,
                   'portfolio': Project}
    view_names = {'blog': 'post',
                  'portfolio': 'project'}
    keyword_processor = KeywordProcessor()

    for lp in link_patterns:
        link_text, app_name, slug = lp

        internal_link = f'[{link_text}]' + r'({{' + f'{app_name}:{slug}' + r'}})'

        try:
            model = model_types[app_name]
            view_name = view_names[app_name]

            if not validate_slug_exists(slug, model):
                markdown_link = r'**!!!INVALID SLUG!!!**'
            elif not validate_slug_published(slug, model):
                markdown_link = link_text
            else:
                url = locate_url(app_name, slug, view_name)
                markdown_link = f'[{link_text}]({url})'

        except KeyError:
            markdown_link = r'**!!!INVALID APP NAME!!!**'

        keyword_processor.add_keyword(internal_link, markdown_link)

    return keyword_processor.replace_keywords(value)


def locate_url(app_name, slug, view_name):
    return reverse(f'{app_name}:{view_name}', args=(slug,))


def validate_slug_exists(slug, model):
    return len(model.objects.filter(slug=slug)) > 0


def validate_slug_published(slug, model):
    return len(model.released_objects.filter(slug=slug)) > 0
