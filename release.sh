echo
echo "----------------- test -----------------------"
pytest src tests --cov=src --doctest-modules
echo "----------------- tested -----------------------"
echo

echo "---------------- readme ----------------"
read -p "press any key"
pip install pathos progress
autoreadme -i README-edit.md -s examples/ -o README.md
pip uninstall pathos progress
echo "---------------- readme done ----------------"
echo

echo "--------------- version bump --------------"
read -p "press any key"
poetry version patch
echo "--------------- version bumped --------------"

echo
git status
echo "------------------ status -----------------------"
echo

echo "------------------ commit --------------------"
read -p "press any key"
git commit -am "Release"
echo "------------------ commited --------------------"
echo

echo "------------------ new status... -----------------------"
read -p "press any key"
git status
echo "------------------ new status -----------------------"
echo

echo "------------------- tag ----------------------"
read -p "press any key"
git tag "v$(poetry version | cut -d' ' -f2)" -m "Release v$(poetry version | cut -d' ' -f2)"
echo "------------------- tagged ----------------------"
echo

echo "------------------- push ----------------------"
read -p "press any key"
git push
echo "------------------- pushed ----------------------"
echo

echo "------------------- publish ----------------------"
read -p "press any key"
poetry publish --build
