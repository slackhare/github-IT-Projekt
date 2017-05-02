rnns=256
numl=3
lr=0.0002
bs=500
sl=500

save="../allSaves/$rnns-$numl-$sl-test-wiki"
data="../data/bigWikiAllChars"
init=$save

mkdir $save
python3 trainWiki.py --data_dir=$data/AA/ --save_dir=$save --init_from $init --num_layers $numl --rnn_size $rnns --num_epochs 1 --batch_size $bs --seq_length $sl --learning_rate $lr
