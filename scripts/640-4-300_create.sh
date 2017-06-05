rnns=640
numl=4
lr=0.002
bs=300
sl=300

save="../allSaves/$rnns-$numl-$sl-wiki"
data="../data/bigWikiAllChars"
init=$save

mkdir $save
python3 trainWiki.py --data_dir=$data/AA/ --save_dir=$save --num_layers $numl --rnn_size $rnns --num_epochs 1 --batch_size $bs --seq_length $sl --learning_rate $lr