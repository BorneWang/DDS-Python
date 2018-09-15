#echo MPEG :

python3 Eval.py --logic MPEG --truth GroundTruth/Results/serverSideResults --ServerSideResults MPEG/Results/serverSideResults

python3 static.py
