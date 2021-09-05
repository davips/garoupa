echo
echo "----------------- updating poetry... -----------------------"
poetry update
poetry install
echo "----------------- updated -----------------------"
echo; echo

echo
echo "----------------- testing... -----------------------"
read -p "press enter"
poetry run pytest src tests --cov=src --doctest-modules
echo "----------------- tested -----------------------"
echo; echo

echo
echo "----------------- docs... -----------------------"
read -p "press enter"
rm docs -rf
poetry run pdoc --html --force garoupa -o docs
mv docs/garoupa/* docs/
rm docs/garoupa -rf
git add docs
echo "----------------- docs done -----------------------"
echo; echo

echo "---------------- readme ----------------"
read -p "press enter"
source venv/bin/activate
autoreadme -i README-edit.md -s examples/ -o README.md
deactivate
echo "---------------- readme done ----------------"
echo; echo

echo "--------------- version bump --------------"
read -p "press enter"
poetry version patch
echo "--------------- version bumped --------------"
echo; echo

echo "------------------ current status -----------------------"
git status
echo "------------------ current status shown-----------------"
echo; echo

echo "------------------ commit --------------------"
read -p "press enter"
git commit -am "Release"
echo "------------------ commited --------------------"
echo; echo

echo "------------------ new status... -----------------------"
read -p "press enter"
git status
echo "------------------ new status shown --------------------"
echo; echo

echo "------------------- tag ----------------------"
read -p "press enter"
git tag "v$(poetry version | cut -d' ' -f2)" -m "Release v$(poetry version | cut -d' ' -f2)"
echo "------------------- tagged ----------------------"
echo; echo

echo "------------------- push ----------------------"
read -p "press enter"
git push
echo "------------------- pushed ----------------------"
echo; echo

echo "------------------- publish ----------------------"
read -p "press enter"
poetry publish --build
