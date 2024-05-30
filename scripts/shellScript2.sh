# It often comes the situations that you want to catch a special signal/interruption/user input in your script to prevent the unpredictables.
# Trap is your command to try:
# trap <arg/function> <signal>

# trap "echo Booh!" SIGINT SIGTERM
# echo "it's going to run until you hit Ctrl+Z"
# echo "hit Ctrl+C to be blown away!"

# while true
# do  
#     sleep 60
# done

# function booh {
#     echo "booh!"
# }
# trap booh SIGINT SIGTERM

# Some of the common signal types you can trap:
# SIGINT: user sends an interrupt signal (Ctrl + C)
# SIGQUIT: user sends a quit signal (Ctrl + D)
# SIGFPE: attempted an illegal mathematical operation
# kill -l

# Notice the numbers before each signal name, you can use that number to avoid typing long strings in trap:
#2 corresponds to SIGINT and 15 corresponds to SIGTERM
# trap booh 2 15

# one of the common usage of trap is to do cleanup temporary files:
# trap "rm -f folder; exit" 2

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                  # -------- SHELL SCRIPT TUTORIAL ---------- # 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Often you will want to do some file tests on the file system you are running. In this case, shell will provide you with several useful commands to achieve it.
# The command looks like the following

# -<command> [filename]
# [filename1] -<command> [filename2]

# use "-e" to test if file exist
# filename="sample.md"
# if [ -e "$filename" ]; then
#     echo "$filename exists as a file"
# fi


# use "-d" to test if directory exists
# directory_name="test_directory"
# if [ -d "$directory_name" ]; then
#     echo "$directory_name exists as a directory"
# fi


# use "-r" to test if file has read permission for the user running the script/test
# filename="sample.md"
# if [ ! -f "$filename" ]; then
#     touch "$filename"
# fi
# if [ -r "$filename" ]; then
#     echo "you are allowed to read $filename"
# else
#     echo "you are not allowed to read $filename"
# fi

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                  # -------- SHELL SCRIPT PIPELINES ---------- # 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# command1 | command2 
# if you want to include the standard error you need to use the form " |& " which is shorthand for " 2>&1 | " 


# Imagine you quickly want to know the number of entries in a directory, you can use a pipe to redirect the output of the ls command to the wc command with option -l.
# ls / | wc -l 
# ls / | head -1 # grabs the first 10 dead
# ls / | -head -n ??? Not sure how this works tbh 

# ls / | grep # this will grab any line/file that has a matching pattern in itd1


# In the previous section we've seen how to chain output of one command to the next one. But what if you want to chain the output of two or more commands to the another one? 
# What if you have a command that takes a file as argument but you would like to process whatever is send to that file? Process substitution allows a process’s input or 
# output to be referred to using a filename.   It has two forms: output <(cmd), and input >(cmd).


# Imagine you've two files for which you want to compare the content. Using diff file1 file2 could generate false positives in the case lines are not ordered. So if you want 
# to compare those files you could create two new files, ordered, and compare those. It would look like: # sort file1 > sorted_file1
# sort file2 > sorted_file2
# diff sorted_file1 sorted_file2
# With process substitution you can do it in one line:
# diff <sort file1) <(sort file2)


# Imagine you want to store logs of an application into a file and at the same time print it on the console. A very handy command for that is tee.
# echo "Hello, world!" | tee /tmp/hello.txt