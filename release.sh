pytest src --cov=src --doctest-modules
echo "----------------- tested -----------------------"
read -p "press any key"

autoreadme -i README-edit.md -s examples/ -o README.md
echo "---------------- readme done ----------------"
read -p "press any key"

poetry version patch
echo "--------------- version bumped --------------"

git status
echo "------------------ status -----------------------"
read -p "press any key"

git commit -am "Release"
echo "------------------ commited --------------------"
read -p "press any key"

git status
echo "------------------ new status -----------------------"
read -p "press any key"

git tag "v$(poetry version | cut -d' ' -f2)" -m "Release v$(poetry version | cut -d' ' -f2)"
echo "------------------- tagged ----------------------"
read -p "press any key"

git push
echo "------------------- pushed ----------------------"
read -p "press any key"

poetry publish --build
