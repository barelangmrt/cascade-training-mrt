# cascade-training-mrt
This the program for documentation of traning data with haar cascade method

first you must create folder p and n
p for cropping image
n for background image
for the comparison of p and n data is 1: 2

after that

run this command for train folder n
python3 neg.py --dir n

and then run this for resize picture positive afte cropping
python3 resizer.py --dir p

python3 infogenerator.py --dir pos_res/

run this and change the number with your positive number data -num

opencv_createsamples -info info.dat -vec ball.vec -num 1000 -w 24 -h 24 

create new folder and rename with "data"

run this command

opencv_traincascade -data data -vec ball.vec -bg neg.txt -numPos 1000 -numNeg 2001 -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -w 24 -h 24 -mode ALL -precalcValBufSize 256 -precalcIdxBufSize 256 -acceptanceRatioBreakValue 10e-5 -nonsym -baseFormatSave -featureType LBP 

change numPos 1000 with your positive picture total
change numNeg 2002 with your negative picture total
