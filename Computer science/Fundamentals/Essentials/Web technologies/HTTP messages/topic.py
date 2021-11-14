# Theory: HTTP messages

# The HTTP protocol relies on the "client-server"
# architecture that is built on the basis of messaging. HTTP
# messages are a way to exchange data between clients
# and servers in the Web. There are two types of messages:
# requests and responses.

# A request is an operation that a client wants to perform
# on the server, and a response is an answer from the
# server to an incoming request. Usually, programmers do
# not need to worry about creating HTTP messages since
# they are produced by browsers, applications, and web
# servers.

# 1. The format of messages
# In the HTTP protocol, all messages consists of text strings.
# Both requests and responses have roughly the same
# standarized format:

#   1. Start line which may vary:
#       - for requests, it indicates the type of requests
#         (method) and the URL where to send it
#         (target);
#   2. Headers which describe the message and convey
#      various parameters.
#   3. Body in which the message data is located.

# The start line and the header are required attributes, so
# the other parts may be empty.

# The full format can be quite complicated for beginners, so
# we have considered only its part which is the most
# important for understanding the general principles.

# 2. The simplified HTTP interaction.
# Here is a simplified HTTP interaction between a browser
# client and a server. The client and the server interact
# through requests and response which follow the studied
# format:

# Method | Target               Status Code
#     Headers                     Headers
#  Optional body               Optional body

#               HTTP request
# Browser client ---------->   Internet <--------------- Server
# Browser client <----------   Internet ---------------> Server


#       Note that there are other possible types of client
#       programs, not just a browser. You can even write
#       your own HTTP client and interact with servers. The
#       only requirement is that such a program should
#       always follow the message format.

# 3. Methods
# HTTP defines a set of requests method that specify what
# the desired action will be a given resource. Despite
# the fact that their names can be nouns, these query
# methods are sometimes referred to as HTTP verbs.

# Let's look at the most commonly used query methods:
# - GET method is only used to retrieve data from the
#   server;
# - POST method is used to send data to the server ;
# - HEAD requests data from server in the same
#   way as the GET method, but without a response
#   body.

# Every time you click on a link, you basically communicate
# to your browser that you want to GET this page. When
# you want to log in to your favorite site, you POST your
# login and password to receive access to it.

# There are more available verbs to learn. You don't need to
# memorize them all right now.

#4. Status codes
# For normal operation of computer programs and web
# pages that work via HTTP, except for the content of the
# page, the server returns a three-digit code, which
# specifies the response client. With the help of this
# code, it is possible to redirect the client to another site or
# to indicate the change of the page, as well as to detect an
# error in data processing.

# Currently, the standards define five classes of status
# codes:                                                                                                           '''''''''''''''''''''''dcvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# 1xx: Informational        Code beginning with "1"
#                           are called information codes.
#                           They report on how client
#                           requests are processed.

# 2xx: Success              Message of this class inform that the
#