# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo(r'C:\Git\rat')
# Your mock repo
mock_repo = git.Repo(r'C:\Git\Contributions-Importer-For-Github')
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['michael.vogginger@gmail.com', 'michael.vogginger@mercedes-benz.com'])
importer.import_repository()
print("woeav")
