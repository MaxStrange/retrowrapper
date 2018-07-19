Remove-Item .\build -Recurse -Force
Remove-Item .\dist -Recurse -Force
Remove-Item .\retrowrapper.egg-info -Recurse -Force

pipreqs.exe --force .

python setup.py bdist_wheel

twine.exe upload dist\*

Write-Host "Done. Please remember to make a release on github via:"
Write-Host "git tag -a v<VERSION_NUMBER> -m <MSG>"
Write-Host "git push origin v<VERSION_NUMBER>"