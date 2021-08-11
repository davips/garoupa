echo
echo "----------------- test -----------------------"
pip install numpy pathos progress
pytest src tests --cov=src --doctest-modules
echo "----------------- tested -----------------------"
echo; echo

echo "---------------- readme ----------------"
read -p "press any key"
autoreadme -i README-edit.md -s examples/ -o README.md
pip uninstall numpy pathos progress
echo "---------------- readme done ----------------"
echo; echo

echo "--------------- version bump --------------"
read -p "press any key"
poetry version patch
echo "--------------- version bumped --------------"
echo; echo

echo "------------------ current status -----------------------"
git status
echo "------------------ current status shown-----------------"
echo; echo

echo "------------------ commit --------------------"
read -p "press any key"
git commit -am "Release"
echo "------------------ commited --------------------"
echo; echo

echo "------------------ new status... -----------------------"
read -p "press any key"
git status
echo "------------------ new status shown --------------------"
echo; echo

echo "------------------- tag ----------------------"
read -p "press any key"
git tag "v$(poetry version | cut -d' ' -f2)" -m "Release v$(poetry version | cut -d' ' -f2)"
echo "------------------- tagged ----------------------"
echo; echo

echo "------------------- push ----------------------"
read -p "press any key"
git push
echo "------------------- pushed ----------------------"
echo; echo

echo "------------------- publish ----------------------"
read -p "press any key"
poetry publish --build
