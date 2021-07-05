## Steps to release a new version

- Change version in  awacs/\_\_init\_\_.py
- Update CHANGELOG.md with changes made since last release
- Create a signed tag: ```git tag --sign -m "Release 1.1.1" 1.1.1```
- Build the distribution: ```python -m build --sdist --wheel .```
- Use twine to check the release: ```twine check dist/awacs-1.1.1*[.whl,.gz]```
- Upload using twine: ```twine upload -s dist/awacs-1.1.1*[.whl,.gz]```
- Push commits: ```git push```
- Push tag: ```git push --tags```
- Update github release page: https://github.com/cloudtools/awacs/releases


Helper to create CHANGELOG entries
----------------------------------

``git log --reverse --pretty=format:"%s" | tail -100 | sed 's/^/* /'``
