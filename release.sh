echo
pytest src --cov=src --doctest-modules
echo "----------------- tested -----------------------"
read -p "press any key"

echo
autoreadme -i README-edit.md -s examples/ -o README.md
echo "---------------- readme done ----------------"
read -p "press any key"

echo
poetry version patch
echo "--------------- version bumped --------------"

echo
git status
echo "------------------ status -----------------------"
read -p "press any key"

echo
git commit -am "Release"
echo "------------------ commited --------------------"
read -p "press any key"

echo
git status
echo "------------------ new status -----------------------"
read -p "press any key"

echo
git tag "v$(poetry version | cut -d' ' -f2)" -m "Release v$(poetry version | cut -d' ' -f2)"
echo "------------------- tagged ----------------------"
read -p "press any key"

echo
git push
echo "------------------- pushed ----------------------"
read -p "press any key"

echo
poetry publish --build
