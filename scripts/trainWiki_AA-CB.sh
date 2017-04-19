for letterOne in {A..B} ; do
  for letterTwo in {A..Z} ; do
    echo $letterOne$letterTwo
    python3 trainWiki.py --data_dir=../data/bigWiki/$letterOne$letterTwo/ --num_epochs 1 --learning_rate 0.0005
  done
done
echo CA
python3 trainWiki.py --data_dir=../data/bigWiki/CA/ --num_epochs 1 --learning_rate 0.0005
echo CB
python3 trainWiki.py --data_dir=../data/bigWiki/CB/ --num_epochs 1 --learning_rate 0.0005
