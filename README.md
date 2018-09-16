# DDS-Python
A Python version of DDS

# Server Configuration
8vCpu 52G memory
1GPU


# Compile Environment
1. back to server instance-4 (original code)
2. cd /home/bowen
3. sudo tar -cf Allfiles.tar TF_Crop_DDS model models compile use_ffmpeg_gen_data.sh
4. scp Allfiles.tar newserver:~
5. go to the new server
6. mkdir data videos
7. tar -xf Allfiles.tar
8. ./compile/compile_opencv.sh
9. ./compile/compile_tensorflow.sh
10. ./compile/compile_ffmpeg.sh

# Run DDS Steps
1. Download the videos from BDD or KITTY

bowenw@instance-storage:~/videos

bowenw@instance-storaget:~/unused_videos

--1.5 #if the videos are from BDD#
      run shell use_ffmpeg_gen_data.sh to convert videos to png or jpeg
      
      emample : ./use_ffmpeg_gen_data.sh 0004a4c0-d4df3a18 BDD 0002
         
2. cd TF_Crop_DDS/

3. run shell run_DDS.sh <frame src directory>
   #the f1_score and bandwidth will be write into a log file
   
   example : ./run_DDS.sh 0002
   
 4. #if running many videos
 ./all_run.sh 
 #change the contents depend on your <frame src directory>
   
# Run MPEG Steps
1. Download the videos from BDD or KITTY
   --1.5 #if the videos are from BDD#
         run shell use_ffmpeg_gen_data.sh to convert videos to png or jpeg
         
         emample : ./use_ffmpeg_gen_data.sh 0004a4c0-d4df3a18 BDD 0002
         
         noted: change the shell content if you're going to run MPEG
         
2. cd TF_Crop_DDS/

3. run shell run_crf_res.sh <frame src directory>
   #the f1_score and bandwidth will be write into a log file
   
   emample : ./run_crf_res.sh 0002
   
4. run shell run_qp.sh <frame src directory>
   #the f1_score and bandwidth will be write into a log file
   
   ./run_qp.sh 0002
  
5.#if running many videos
   ./all_run_mpeg.sh #change the contents depend on your <frame src directory>
   #the f1_score and bandwidth will be write into a log file

# Generate Ellipse pictures

1. use DDS or MPEG to generate f1_score and bandwidth (see the steps above)

2. copy the results file to go/src/github.com/achowdhery/measurementanalytics2018/result/DDS_GO_MPEG

3. cd go/src/github.com/achowdhery/measurementanalytics2018

4. run command line : go run cmd/eval1/main_go_dds_res.go

5. The ellipse picture will be generated in go/src/github.com/achowdhery/measurementanalytics2018
#if want to generate different ellipse pictures, see the .go files in cmd/eval1

