Database=$1-$2
Video=$2

python3 main.py --src /home/bowen/data/$Database/src --logic GroundTruth
#python3 main.py --src /home/bowen/data/$Database/src --logic DDS
#./run_eval_DDS.sh >> Ten_videos_results/Ten_videos_DDS.log
#rm -r DDS
:<<!
for crf in 23 30 40 46 51
do
python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video /home/bowen/videos/$Video.mov --crf $crf
./run_eval_MPEG.sh >> Ten_videos_results/new_Ten_videos_crf_$crf.log
rm MPEG -r
done

for qp in 20 30 40 46 51
do
python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video /home/bowen/videos/$Video.mov --qp $qp
./run_eval_MPEG.sh >> Ten_videos_results/new_Ten_videos_qp_$qp.log
rm MPEG -r
done
!
for res in 1 0.8 0.6 0.4 0.25 0.2
do
python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video /home/bowen/videos/$Video.mov --res $res --qp 5
./run_eval_MPEG.sh >> res_$res.log
rm MPEG -r
done

#rm -r GroundTruth

