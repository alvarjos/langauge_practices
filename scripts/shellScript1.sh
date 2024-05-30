#!/bin/bash

# echo "File name is "$0 # holds the current script
# echo $3 # $3 holds banana
# Data=$5
# echo "A $Data costs just $6."
# echo $#
# echo !$# 

# ---------------------------------------------------------------------------------------------
#ARRAYS
# my_array=(apple banana "Fruit Basket" orange)
# my_array[4]="apricot"
# echo ${my_array[4]}

# ---------------------------------------------------------------------------------------------
#STRINGS
# NAMES=( John Eric Jessica )
# # write your code here
# NUMBERS=(1 2 3)
# STRINGS=("Hello" "world")
# NumberOfNames=${NAMES[@]}
# second_name=${NAMES[1]}
# echo $NumberOfNames
# echo $second_name

# ---------------------------------------------------------------------------------------------
# MATH
# A=3
# B=$((100 * $A + 5)) 
# echo $B

# ---------------------------------------------------------------------------------------------
#BASIC STRINGS
# #String Length
# STRING="this is a string"
# echo ${#STRING} #outputs 16

# INDEX
# STRING="this is a string"
# SUBSTRING="ha"
# expr index "$STRING" "$SUBSTRING"

# STRING="this is a string"
# POS=10
# LEN=6
# echo ${STRING:$POS:$LEN}

# string="to be or not to be"
# echo ${string[@]/be/eat}
# echo ${string[@]//be/eat}
# echo ${string[@]// not/}
# echo ${string[@]/#to be/eat now}
# echo ${string[@]/%be/eat}
# echo ${string[@]/%be/be on $(date +%Y-%m-%d)}
# echo ${string[@]/%be/be on $(date +$1-$2-$3)}
# ^ use bash my_shopping.sh 2020 12 25 for th $1-3 variables

# ---------------------------------------------------------------------------------------------
# BUFFETT="Life is like a snowball. The important thing is finding wet snow and a really long hill."

#     # write your code here
#     ISAY=$BUFFETT
#     change1=${ISAY[@]/snow/foot}
#     change2=${change1[@]//snow/}
#     change3=${change2[@]/finding/getting}
#     loc=`expr index "$change3" 'w'`
#     ISAY=${change3::$loc+2}

# # Test code - do not modify
# echo "Warren Buffett said:"
# echo $BUFFETT
# echo "and I say:"
# echo "$ISAY"

# NAME="John"
# if [ "$NAME" = "John" ]; then
#     echo "True - my name is John"
# fi 

# NAME="George"
# if [ "$NAME" = "John" ]; then
#     echo "True - my name is John"
# elif [ "$NAME" = "George" ]; then
#     echo "George Harrison"
# else
#     # echo "False"
#     # echo "You must mistaken me for $NAME"
#     echo "This leaves us with Paul and Ringo"
# fi 

# ---------------------------------------------------------------------------------------------
# comparison    Evaluated to true when
# $a -lt $b    $a < $b
# $a -gt $b    $a > $b
# $a -le $b    $a <= $b
# $a -ge $b    $a >= $b
# $a -eq $b    $a is equal to $b
# $a -ne $b    $a is not equal to $b

# comparison    Evaluated to true when
# "$a" = "$b"     $a is the same as $b
# "$a" == "$b"    $a is the same as $b
# "$a" != "$b"    $a is different from $b
# -z "$a"         $a is empty

# ---------------------------------------------------------------------------------------------
# LOGICAL COMBINATIONS
# VAR_A=2
# VAR_B=golf
# VAR_T=tee

# if [[ $VAR_A -ge 1 && ($VAR_B = "bee" || $VAR_T = "tee") ]] ; then
#     echo "This is true"
# fi

# honestly confused on how this one worked in the example provided 
# case "$variable" in 
#     "$condition1" )
#     echo "true"
#     ;;
#     "$condition2" )
#     echo "False"
#     ;;
# esac


# ---------------------------------------------------------------------------------------------
#SIMPLE CASE BASH STRUCTURE
# mycase=4
# case $mycase in
#     1) echo "You selected bash";;
#     2) echo "You selected perl";;
#     3) echo "You selected phyton";;
#     4) echo "You selected c++";;
#     5) exit
# esac

# # change these variables
# NUMBER=16
# APPLES=16
# KING=LUIS
# # modify above variables
# # to make all decisions below TRUE
# if [ $NUMBER -gt 15 ] ; then
#   echo 1
# fi
# if [ $NUMBER -eq $APPLES ] ; then
#   echo 2
# fi
# if [[ ($APPLES -eq 12) || ("$KING" = "LUIS") ]] ; then
#   echo 3
# fi
# if [[ $(($NUMBER + $APPLES)) -le 32 ]] ; then
#   echo 4
# fi

# ---------------------------------------------------------------------------------------------
# LOOPS
# Basic Construct
# NAMES=(Nick Wilson Sarah Matt)
# for N in ${NAMES[@]} ; do 
#   echo "My name is ${N}"
# done

# for f in $( ls shell_scripting_practice.sh /etc/localtime ); do
#   echo "File is: $f"
# done

# while loop = do until condition is false
# count=4
# while [ $count -gt 0 ]; do
#   echo "Value of count is: $count"
#   count=$(($count - 1))
# done

# # until loop = do until condition is true
# count=1
# until [ $count -gt 5 ]; do
#   echo "Value of count is: $count"
#   count=$(($count + 1))
# done

# ---------------------------------------------------------------------------------------------

# COUNT=0
# while [ $COUNT -ge 0 ]; do
#   echo "Value of COUNT is: $COUNT"
#   COUNT=$((COUNT+1))
#   if [ $COUNT -ge 5 ] ; then
#     break
#   fi
# done

# COUNT=0
# while [ $COUNT -lt 10 ]; do
#   COUNT=$((COUNT+1))
#   # Check if COUNT is even
#   if [ $(($COUNT % 2)) = 0 ] ; then
#     continue
#   fi
#   echo $COUNT
# done

# ---------------------------------------------------------------------------------------------
#ARRAY COMPARISON

# To refer to all the array values
# echo ${array[@]}

# To evaluate the number of elements in an array
# echo ${#array[@]}

# ARRAY COMPARISON EXERCISE
# In this exercise, you will need to compare three list of arrays and write the common elements of all the three arrays:

# a=(3 5 8 10 6),b=(6 5 4 12),c=(14 7 5 7) result is the common element 5.

# enter your array comparison code here
	# # initialize arrays a b c
	# a=(3 5 7 10 6) 
	# b=(6 5 7 3) 
	# c=(14 3 5 7)
	# #comparison of first two arrays a and b
	# for x in "${a[@]}"; do 
	#   in=false 
	#   for y in "${b[@]}"; do 
	#     if [ $x = $y ];then 
	#       # assigning the matching results to new array z
	#       z[${#z[@]}]=$x
	#     fi
	#   done 
	# done
	# #comparison of third array c with new array z
	# for i in "${c[@]}"; do 
	#   in=false
	#   for k in "${z[@]}"; do
	#     if [ $i = $k ];then
	#       # assigning the matching results to new array j
	#       j[${#j[@]}]=$i
	#     fi
	#   done 
	# done 
	# # print content of array j
	# echo ${j[@]}



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                              # -------- SHELL FUNCTION ---------- # 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# function function_A {
#   echo "Print this out"
# }
# function function_B {
#   echo $1
# }
# function adder {
#   echo "$(($1 + $2))"
# }

# function_A "Function A"
# function_B 
# adder 12 56

# EXERCISE 
# function ENGLISH_CALC {
#   OPERATION=$2
#   if [ $OPERATION == "plus" ]; then
#     total=$(($1 + $3))
#     echo "$1 + $3 = $total"
#   elif [ $OPERATION == "minus" ]; then
#     total=$(($1 - $3))
#     echo "$1 - $3 = $total"
#   elif [ $OPERATION == "times" ]; then
#     total=$(($1 * $3))
#     echo "$1 * $3 = $total"
#   fi
# }

# # testing code
# ENGLISH_CALC 3 plus 5
# ENGLISH_CALC 5 minus 1
# ENGLISH_CALC 4 times 6


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                  # -------- SHELL FUNCTION SPECIAL VARIABLES ---------- # 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tutorial
# In last tutorial about shell function, you use "$1" represent the first argument passed to function_A. Moreover, here are some special variables in shell:

# $0 - The filename of the current script.|
# $n - The Nth argument passed to script was invoked or function was called.|
# $# - The number of argument passed to script or function.|
# $@ - All arguments passed to script or function.|
# $* - All arguments passed to script or function.|
# $? - The exit status of the last command executed.|
# $$ - The process ID of the current shell. For shell scripts, this is the process ID under which they are executing.|
# $! - The process number of the last background command.|
# Note: $@ and $* have different behavior when they were enclosed in double quotes.