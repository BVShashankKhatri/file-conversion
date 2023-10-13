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
def convert_gitrepo_html_to_md(html_file_path, md_file_path):
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

@error_handler
def convert_gitrepo_html_files(folder_path):
  """Converts all of the HTML files in the specified folder and all of its subfolders to MD files.

  Args:
    folder_path: The path to the folder containing the HTML files.
  """

  for root, dirs, files in os.walk(folder_path):
    for filename in files:
      if filename.endswith(".html"):
        html_file_path = os.path.join(root, filename)
        md_file_path = os.path.join(root, filename[:-5]) + ".md"

        convert_gitrepo_html_to_md(html_file_path, md_file_path)

    for subdir in dirs:
      convert_gitrepo_html_files(os.path.join(root, subdir))


if __name__ == "__main__":
  folder_path = "path of the folder of html files."

  convert_gitrepo_html_files(folder_path)