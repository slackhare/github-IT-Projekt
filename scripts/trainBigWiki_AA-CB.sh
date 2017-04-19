for letterOne in {A..B} ; do
  for letterTwo in {A..Z} ; do
    echo $letterOne$letterTwo
    python3 trainBigWiki.py --data_dir=../data/bigWikiAllChars/$letterOne$letterTwo/ --num_epochs 1 --learning_rate 0.00025
  done
done
echo CA
python3 trainBigWiki.py --data_dir=../data/bigWikiAllChars/CA/ --num_epochs 1 --learning_rate 0.00025
echo CB
python3 trainBigWiki.py --data_dir=../data/bigWikiAllChars/CB/ --num_epochs 1 --learning_rate 0.00025
