@echo off
echo "This is for registering images via the cmd using elastix"
elastix -f ./Reference_Mask.png -m ./test_file_1_Mask.png -out ./Out -p Parameters.txt
echo "SUCCESS"
pause