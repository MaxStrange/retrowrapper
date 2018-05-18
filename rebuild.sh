rm -rf build/
rm -rf dist/
rm -rf retrowrapper.egg-info/
pipreqs --force .
python setup.py bdist_wheel
twine upload dist/*
echo "Done. Please remember to make a release on github via:"
echo "git tag -a v<VERSION_NUMBER> -m \"<Message>\""
echo "git push origin v<VERSION_NUMBER>"