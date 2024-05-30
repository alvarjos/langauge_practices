#!/bin/bash
# echo "hello world"

# # Standard system variables
# echo $BASH
# echo $BASH_VERSION
# echo $HOME
# echo $PWD

# name=Mark
# echo $Mark
# value=10
# echo The name is $name
# echo Value = $value


# read acts an input button in the terminal
# echo "Enter names : " 
# read name1 name2 name3
# echo "Names: $name1, $name2, $name3"

# to do this on the same line do this
# read -p 'username : ' user_var
# read -sp 'password : ' pass_var
# echo 
# -sp means silent input, which means the password wont be shown when typing in the terminal
# echo "username : $user_var"
# echo "password : $pass_var"

# -a creates an array
# echo "Enter names : "
# read -a names
# echo "Names : ${names[0]}, ${names[1]}"

# echo "Enter name : "
# read 
# echo "Name : $REPLY "
# $REPLY is a built in variable that holds unknown read variables without a name

# TUTORIAL VIDEO 4 
# PASS ARGUMENTS TO A BASH SCRIPT

# echo $0 $1 $2 $3 ' > echo $1 $2 $3' 

# args=("$@")

# echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}

# prints out all arguments
# echo $@

# prints out number of arguments given
# echo $#

# TUTORIAL VIDEO 5
# If Statements

# count=10
# if [ $count > 10 ]
# then 
#     echo "condition is true" 
# fi

# word=a
# if [[ $word == 'b' ]]
# then 
#     echo "condition is true"
# else 
#     echo "condition is false"
# fi


# TUTORIAL VIDEO 6
# File test operators 

# -e flag is used to enable the interpetation of the backslash \c which keeps the cursor on the same line
# echo -e "Enter the name of the file: \c"
# read file_name
# -e is for if the file exists 
# -f is for if the file is a regular file or not
# -d is for if the directory exists 
# -b is for block special files (videos, images etc...)
# -c is for character special file(basically normal files with text/basic code)
# -s checks whether file is empty or not 
# -r checks to see if it has read permission
# -w checks to see if it has write permission
# -x checks to see if it has execute permission  

# if [ -s $file_name ]
# then   
#     echo "$file_name not empty"
# else 
#     echo "$file_name empty"
# fi


# TUTORIAL VIDEO 7
# hOW TO APPEND OUTPUT TO THE END OF TEXT FILE

echo -e "Enter the name of the file : \c"
read file_name

if [ -f $file_name ]
then   
    if [ -w $file_name ]
    then 
        echo "Type some text data. To quit, press ctrl+D"
        cat >> $file_name
    # double >> allows us to append to the end. Single > rewrites the file 
    else
        echo "The file doesn't have write permissions"
    fi 
else 
    echo "$file_name doesn't exist"
fi

# chmod +w $file_name = allows u to have write permission on that file
# chmod -w $file_name = takes away write permission on that file
# chmod -r/+r $file_name = same thing but with read permissions 

