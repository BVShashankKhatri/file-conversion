"""Install markdownify by running pip3 install markdownify"""

import markdownify
import os
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def error_handler(func):
  """A decorator that handles errors in the decorated function."""

  @wraps(func)
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as e:
      logger.error("Error in function: %s", func.__name__, e)

  return wrapper

@error_handler
def convert_html_to_md(html_file_path, md_file_path):
  """Converts an HTML file to an MD file.

  Args:
    html_file_path: The path to the HTML file.
    md_file_path: The path to the MD file.
  """

  with open(html_file_path, "r") as html_file:
    html_text = html_file.read()

  markdown_text = markdownify.markdownify(html_text)

  with open(md_file_path, "w") as md_file:
    md_file.write(markdown_text)
    print(md_file_path+' is successfully created.')

if __name__ == "__main__":
  html_file_path = "path of the html file with extension(.html)."
  md_file_path = "path of the md file with extension(.md)."

  convert_html_to_md(html_file_path, md_file_path)