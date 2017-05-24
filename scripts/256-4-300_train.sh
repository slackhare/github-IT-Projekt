rnns=256
numl=4
lr=0.002
bs=300
sl=300

save="../allSaves/$rnns-$numl-$sl-wiki"
data="../data/bigWikiAllChars"
init=$save

mkdir $save
for letterOne in {A..B} ; do
  for letterTwo in {A..Z} ; do
    echo $letterOne$letterTwo
    python3 trainWiki.py --data_dir=$data/$letterOne$letterTwo/ --save_dir=$save --init_from $init --num_layers $numl --rnn_size $rnns --num_epochs 1 --batch_size $bs --seq_length $sl --learning_rate $lr
  done
done
echo CA
python3 trainWiki.py --data_dir=$data/CA/ --save_dir=$save --init_from $init --num_layers $numl --rnn_size $rnns --num_epochs 1 --batch_size $bs --seq_length $sl --learning_rate $lr
echo CB
python3 trainWiki.py --data_dir=$data/CB/ --save_dir=$save --init_from $init --num_layers $numl --rnn_size $rnns --num_epochs 1 --batch_size $bs --seq_length $sl --learning_rate $lr
