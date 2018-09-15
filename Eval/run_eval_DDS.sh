
database=$1
#echo DDS :
python3 Eval.py --truth GroundTruth/Results/serverSideResults --ServerSideResults DDS/Results/serverSideResults --ClientSideResults DDS/Results/trackingResults --logic DDS

totalB=`find DDS/Sendtoserver -name "*jpeg" | xargs du -cb | tail -1`
totalNum=`ls ~/data/${database}/src | wc -l`
totalBytes=` echo ${totalB%to*}`
#echo total : $totalBytes Bytes
#echo frames : $totalNum
python3 calcu_bd.py --Bytes $totalBytes --frames $totalNum --fps 10

