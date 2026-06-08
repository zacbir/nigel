from datetime import datetime
from pathlib import Path
from typing_extensions import Annotated
import os.path
import re

import typer


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


def nigel(
    directory: Annotated[Path, typer.Argument(help="", envvar="NIGEL_DIRECTORY")] = Path(".").absolute(),
    title: Annotated[str, typer.Argument(help="")] = "",
    date: Annotated[datetime, typer.Argument(help="")] = datetime.now().strftime('%Y-%m-%d %H:%M'),
    tag: Annotated[list[str], typer.Argument(help="")] = []
    body: Annotated[str, typer.Argument(help="")] = ""
):

    short_date = date.split(' ')[0]
    slug = make_slug(title)
    tags = ', '.join(tag)

    content = f'Title: {title}\nDate: {date}\nSlug: {slug}\nTags: {tags}\n\n{body}'

    if directory:
        filepath = os.path.join(directory, f'{short_date}-{slug}.markdown')

        with open(filepath, 'w') as initial:
            initial.write(content)

    else:
        print(content)

