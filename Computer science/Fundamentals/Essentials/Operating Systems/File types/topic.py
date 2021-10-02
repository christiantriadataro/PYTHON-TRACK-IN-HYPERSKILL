# Theory: File types

# As you may already know, it is convenient to store data in files.
# In this topic, we'll figure what else we can do with the files, how
# to distinguish them, and what their main types are.

#       Below we provide a list of file types in the Unix system. In
#       other operating systems, the types may slightly differ, but
#       the basic ones, which we will talk about in more detail,
#       can be found almost everywhere.

# 1. Unix file types
# In general, a file is a container for some information. We can put
# almost anything in this container: a photo, a text, a link to
# another file, or just another container with other nested files,
# etc. All this data is different and therefore the files in which it's
# stored are of various types.

# The Unix file types are:
#   1. regular files where you usually keep your personal data
#      such as texts, pictures, and so on,
#   2. directories, or folders that make it easier to organize other
#      files in the system,
#   3. named pipes, that allow different processes to exchange
#      data,
#   4. symbolic links, which contain links to other files,
#   5. device files, that contain data required by the operating
#      system to interact with physical devices,
#   6. sockets, which provide data exchange between processes.

# We will study the most commonly used file types in more detail.
# There are the ones that can be found in every operating system:
# regular files, directories, and symbolic links.

# 2. Regular Files

# Regular files are common because users usually store their data
# in them: documents, video,s photos, music, etc. In general, any
# data in such files can be presented in two forms:
# - textual data with some encoding, then the file will be
#   called a text file
# - any other sequences of bytes without constraints to
#   encoding, then such a file is called a binary file

# To make it easier to figure out which file is text and which is
# binary, let's study a couple of examples. Text fields usually
# contain texts in plain format, tabular data, configuration files,
# and data formats like CSV or JSON. Binary files often contain
# data such as video, audio, databases, archives.

# Binary and text files have different characteristics and thus
# require different tools to work with them. It is worth knowing
# these differences because it will definitely save you time when
# reading or writing your data to these files.

# The main difference between text and binary files is that the
# latter haven o inherent constraints. It means they can contain
# any bytes sequence, and they are to be opened in an appropriate
# program that knows the specific file format such as Media
# Player, Photoshop, Office, etc. On the other hand, text files can
# be edited in any text editor program. Also, they must correspond
# to several constraints such as human-readable content, line-
# oriented data format, universal reading of newline sequences,
# and so on.

# 3. Directory
# Directories, which sometimes are also called folders, are
# containers for the files. For example, you can put your music
# files into one directory title "Music". Most file systems also
# allow a directory to contain other directories. It's called a parent
# directory containing child directories or subdirectories. This way
# the organizing data is stored on a medium into tree-like
# hierarchical structures, where directories that have no parents
# are called root directories and serve as the base of this
# structure. This hierarchy provides clear links between files and
# makes it a lot more convenient to search for data on a disk. we
# just need to know the full path to a file, that's all. To get this full
# path, we need a full filename, i.e. we add the parent folder to the
# file, and for the parent folder, we also add its parent and so on
# till we get to the root.

# Directory names in a full filename are usually separated by
# slash / or backslash \. So if there is a root directory named
# "root_directory" that contains a subdirectory named
# "sub_directory", and in this subdirectory there is a file named
# "my_file", the file system will assign it a full filename like
# "root_directory/sub_directory/my_file".

# Moreover, tree-like hierarchical structures allow us to select file
# groups and manage them. Also, using a hierarchically organized
# structure, we can transfer it to another computer.

# 4. Symbolic links
# Lastly, there is one more special sort of file worth considering.
# These files are called symbolic links in the Unix system. If you
# use Windows, you may know them as shortcuts. A symbolic link
# contains a reference to another file or directory in the form of
# an absolute or relative path. Let's say you want somme files to be
# accessed from several directories. If you copy this file and put
# its copies into each directory, each time you modify one of the
# copies you'll have to go and modify all the others, and this feels
# like a waste of time. If you put symbolic links referencing this
# file into each directory, they would actually open the original file
# they are referencing.

# 5. Conclusion
# To sum up, in this topic we've learned that:
# - the personal data is stored in regular files,
# - the data in regular files can be either in binary or text
#   form,
# - in addition to regular files, there are also directories,
#   symbolic links, sockets, named pipes, and device files,
# - directories are containers for other files,
# - you can store links to files in the special files called
#   symbolic links.

# Now, let's turn to exercises to see how well you understand the
# different file types.
