from datetime import datetime
import os.path
import re

import click


def make_slug(s):
    s = s.lower()
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')
    s = re.sub('\W', '', s)
    s = s.replace('_', ' ')
    s = re.sub('\s+', ' ', s)
    s = s.strip()
    s = s.replace(' ', '-')

    return s


@click.command()
@click.option('--directory', envvar='NIGEL_DIRECTORY')
@click.option('--title')
@click.option('--date', default=None)
@click.option('--tag', '-t', multiple=True)
def cli(directory, title, date, tag):

    if date is None:
        date = datetime.now().strftime('%Y-%m-%d %H:%M')
    else:
        try:
            n = datetime.strptime(date, '%Y-%m-%d %H:%M')
        except ValueError:
            raise click.BadParameter("Date format should be 'YYYY-MM-DD HH:MM'")

    short_date = date.split(' ')[0]
    slug = make_slug(title)
    tags = ', '.join(tag)

    base_content = f'Title: {title}\nDate: {date}\nSlug: {slug}\nTags: {tags}\n\n'

    if directory:
        filepath = os.path.join(directory, f'{short_date}-{slug}.markdown')

        with open(filepath, 'w') as initial:
            initial.write(base_content)

        click.edit(filename=filepath)
    else:
        click.echo(base_content)

