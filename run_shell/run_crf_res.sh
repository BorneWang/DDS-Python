Database=$1

:<<!
python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video /home/bowen/videos/$Video.mov --crf 1
mv MPEG GroundTruth
rm -r GroundTruth/tempReserve

for crf in 1 10 23 30 40 46 51
do
python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video /home/bowen/videos/$Video.mov --crf $crf
./run_eval_MPEG.sh >> Ten_videos_results/new_Ten_videos_crf_$crf.log
rm -r MPEG/tempReserve
mv MPEG Results/MPEG_${Database}_crf_$crf
done

mv GroundTruth Results/MPEG_${Database}_crf_truth
!

python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video $Database --test 1
mv MPEG GroundTruth
rm -r GroundTruth/tempReserve

for res in 1 0.9 0.8 0.6 0.4 0.2 0.1
do
python3 main.py --src /home/bowen/data/$Database/src --logic MPEG --video $Database --res $res --test 1
./run_eval_MPEG.sh >> New_traial_result/new_five_videos_res_$res.log
rm -r MPEG/tempReserve
mv MPEG Results/MPEG_${Database}_res_$res
done


mv GroundTruth Results/MPEG_${Database}_res_truth
