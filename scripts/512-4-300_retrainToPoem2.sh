rnns=512
numl=4
lr=0.001
bs=300
sl=300


data="../data/deutscheLyrik"
init="../allSaves/$rnns-$numl-$sl-wiki"

for myNumber in {1..9} ; do
  save="../allSaves/$myNumber-wiki"
  mkdir $save
  python3 trainWiki.py --data_dir=$data/ --save_dir=$save --init_from $init --num_layers $numl --rnn_size $rnns --num_epochs 1 --batch_size $bs --seq_length $sl --learning_rate $lr
  init=$save
done
