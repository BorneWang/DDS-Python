
../pull_data_from_emulab.sh 02514ff2-5fafa3bc BDD 0001
./run_crf_res.sh 0001
rm ~/data/0001 -r

../pull_data_from_emulab.sh 0004a4c0-d4df3a18 BDD 0002
./run_crf_res.sh 0002
rm ~/data/0002 -r

../pull_data_from_emulab.sh 06661450-f52ed9ce BDD 0003
./run_crf_res.sh 0003
rm ~/data/0003 -r

../pull_data_from_emulab.sh 07895b8a-3a843bb5 BDD 0004
./run_crf_res.sh 0004
rm ~/data/0004 -r

../pull_data_from_emulab.sh 08022699-d03af7f6 BDD 0005
./run_crf_res.sh 0005
rm ~/data/0005 -r
