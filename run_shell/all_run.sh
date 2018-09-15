#./run_crf_res.sh 0001 02514ff2-5fafa3bc
#./run_qp.sh 0001 02514ff2-5fafa3bc

#./run_crf_res.sh 0002 0004a4c0-d4df3a18
#./run_qp.sh 0002 0004a4c0-d4df3a18


#./run_crf_res.sh 0003 06661450-f52ed9ce
#./run_qp.sh 0003 06661450-f52ed9ce

#./run_crf_res.sh 0004 07895b8a-3a843bb5
#./run_qp.sh 0004 07895b8a-3a843bb5

#./run_crf_res.sh 0005 08022699-d03af7f6
#./run_qp.sh 0005 08022699-d03af7f6


../pull_data_from_emulab.sh 00b04b30-501822fa BDD 0001
./run_DDS.sh 0001
rm ~/data/0001 -r


../pull_data_from_emulab.sh 00d79c0a-a2b85ca4 BDD 0002
./run_DDS.sh 0002
rm ~/data/0002 -r

../pull_data_from_emulab.sh 015fcc2d-2d44d478 BDD 0003
./run_DDS.sh 0003
rm ~/data/0003 -r


../pull_data_from_emulab.sh 015fe6c9-e880c0d7 BDD 0004
./run_DDS.sh 0004
rm ~/data/0004 -r


../pull_data_from_emulab.sh 0289eba3-d1fd00fc BDD 0005
./run_DDS.sh 0005
rm ~/data/0005 -r

../pull_data_from_emulab.sh 02c2a4d8-94d32b2f BDD 0006
./run_DDS.sh 0006
rm ~/data/0006 -r

../pull_data_from_emulab.sh 04095551-efe2622a BDD 0007
./run_DDS.sh 0007
rm ~/data/0007 -r

../pull_data_from_emulab.sh 04810e69-d5018754 BDD 0008
./run_DDS.sh 0008
rm ~/data/0008 -r

../pull_data_from_emulab.sh 04e55a30-fc0b249b BDD 0009
./run_DDS.sh 0009
rm ~/data/0009 -r

../pull_data_from_emulab.sh 0573f031-8ef23cf6 BDD 0010
./run_DDS.sh 0010
rm ~/data/0010 -r
