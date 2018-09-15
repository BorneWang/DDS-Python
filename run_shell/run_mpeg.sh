rm MPEG -r
:<<!
#default crf:23 qp:23 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov
./run_eval_MPEG.sh > mpeg_default
rm MPEG -r

#crf:10 qp:23 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --crf 10
./run_eval_MPEG.sh > mpeg_crf_10
rm MPEG -r

#crf:30 qp:23 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --crf 30
./run_eval_MPEG.sh > mpeg_crf_30
rm MPEG -r

#crf:40 qp:23 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --crf 40
./run_eval_MPEG.sh > mpeg_crf_40
rm MPEG -r


#crf:51 qp:23 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --crf 51
./run_eval_MPEG.sh > mpeg_crf_51
rm MPEG -r



#crf:45 qp:23 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --crf 45
./run_eval_MPEG.sh > mpeg_crf_45
rm MPEG -r


#crf:48 qp:23 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --crf 48
./run_eval_MPEG.sh > mpeg_crf_48
rm MPEG -r



#crf:23 qp:10 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --qp 10
./run_eval_MPEG.sh > mpeg_qp_10
rm MPEG -r

#crf:23 qp:20 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --qp 20
./run_eval_MPEG.sh > mpeg_qp_20
rm MPEG -r

#crf:23 qp:30 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --qp 30
./run_eval_MPEG.sh > mpeg_qp_30
rm MPEG -r

#crf:23 qp:40 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --qp 40
./run_eval_MPEG.sh > mpeg_qp_40
rm MPEG -r

#crf:23 qp:51 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --qp 51
./run_eval_MPEG.sh > mpeg_qp_51
rm MPEG -r


#crf:23 qp:45 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --qp 45
./run_eval_MPEG.sh > mpeg_qp_45
rm MPEG -r

#crf:23 qp:48 res:1
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --qp 48
./run_eval_MPEG.sh > mpeg_qp_48
rm MPEG -r



#crf:23 qp:23 res:0.8
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --res 0.8
./run_eval_MPEG.sh > mpeg_res_0.8
rm MPEG -r

#crf:23 qp:23 res:0.6
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --res 0.6
./run_eval_MPEG.sh > mpeg_res_0.6
rm MPEG -r
!

#crf:23 qp:23 res:0.4
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --res 0.4
./run_eval_MPEG.sh > mpeg_res_0.4
#rm MPEG -r

:<<!
#crf:23 qp:23 res:0.2
python3 main.py --src /home/bowen/data/BDD-0004a4c0-d4df3a18/src --logic MPEG --video /home/bowen/videos/0004a4c0-d4df3a18.mov --res 0.2
./run_eval_MPEG.sh > mpeg_res_0.2
rm MPEG -r
!

