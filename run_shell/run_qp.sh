Database=$1
Video=$2

python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video /home/bowen/videos/$Video.mov --crf 1
mv MPEG GroundTruth
rm -r GroundTruth/tempReserve

for qp in 1 10 20 30 40 46 51
do
python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video /home/bowen/videos/$Video.mov --qp $qp
./run_eval_MPEG.sh >> Ten_videos_results/new_Ten_videos_qp_$qp.log
rm -r MPEG/tempReserve
mv MPEG Results/MPEG_${Database}_qp_$qp
done

mv GroundTruth Results/MPEG_${Database}_qp_truth

