# DDS-Python
A Python version of DDS

# Run DDS Steps
1. Download the videos from BDD or KITTY

--1.5 #if the videos are from BDD#
      run shell use_ffmpeg_gen_data.sh to convert videos to png or jpeg
         
2. cd TF_Crop_DDS/

3. run shell run_DDS.sh <frame src directory>
   #the f1_score and bandwidth will be write into a log file
   
 4.#if running many videos
   run shell all_run.sh #change the contents depend on your <frame src directory>
   
# Run MPEG Steps
1. Download the videos from BDD or KITTY
   --1.5 #if the videos are from BDD#
         run shell use_ffmpeg_gen_data.sh to convert videos to png or jpeg
         
2. cd TF_Crop_DDS/

3. run shell run_crf_res.sh <frame src directory>
   #the f1_score and bandwidth will be write into a log file
   
4. run shell run_qp.sh <frame src directory>
   #the f1_score and bandwidth will be write into a log file
  
5.#if running many videos
   run shell all_run_mpeg.sh #change the contents depend on your <frame src directory>
   #the f1_score and bandwidth will be write into a log file

# Generate Ellipse pictures

1. use DDS or MPEG to generate f1_score and bandwidth (see the steps above)

2. copy the results file to go/src/github.com/achowdhery/measurementanalytics2018/result/DDS_GO_MPEG

3. cd go/src/github.com/achowdhery/measurementanalytics2018

4. run command line : go run cmd/eval1/main_go_dds_res.go

5. The ellipse picture will be generated in go/src/github.com/achowdhery/measurementanalytics2018
#if want to generate different ellipse pictures, see the .go files in cmd/eval1

