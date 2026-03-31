# 🙏 Thanks !

Oh if you open this page, it's for contributing for this project, great ! A big thanks 🙏

To contribute, it's simple, check the [existing issues](https://github.com/thib1984/pyterm2048/issues). If you see an issue you are interested to work, please let a message and i assign you the task. With this, all people know you are working on this issue.

If it's a new subject, don't hesitate to create an issue. I will check this one to affect some labels and let contribution open 😉

You can initialize a draft merge request directly when you start to work on an issue.

When you finish, past the merge request in "ready" mode and i will check this quickly.

Feel free to reach out if you have any questions. 😁

# Work

```
# Uninstall the globally installed version via pipx if needed (optional, just to reset the published app)
pipx uninstall pyterm2048 

# Clone the repository only the first time
git clone https://github.com/thib1984/pyterm2048.git
# Afterwards, update it using regular git commands (git pull, git fetch, etc.)
cd pyterm2048 

# Remove any previous virtual environment to start fresh
rm -rf pyterm2048_env 

# Create a virtual environment to isolate dependencies for this project
python3 -m venv pyterm2048_env
source pyterm2048_env/bin/activate

# Install the local package in the isolated environment
pip install .

# Test the app locally within the virtual environment
pyterm2048 [...] 

# Optional: reinstall if needed and retest
pip install .
pyterm2048 [...] 

# Exit the virtual environment
deactivate

# Reinstall the globally published version via pipx if needed
pipx install pyterm2048 
``` 

A venv (virtual environment) isolates this project's Python dependencies from the system, preventing version conflicts and keeping things clean.


# Publish to pypi (WIP)

```
#from work directory
python3 -m build && python3 -m twine upload dist/* #to publish to pypi
```