git add .
echo -n "type commit message : "
read msg
git commit -m $msg
git push
