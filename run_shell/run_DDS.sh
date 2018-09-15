Database=$1

python3 main.py --src /home/bowen/data/$Database/src_1 --logic GroundTruth
python3 main.py --src /home/bowen/data/$Database/src --logic DDS --test 1
./run_eval_DDS.sh $Database >> Ten_new_videos_DDS.log
rm DDS -r
rm GroundTruth -r
#mv DDS DDS_results/DDS_${Database}
#mv GroundTruth DDS_results/GT_${Database}
