## Theory: Google Colab

You already know the basics of Jupyter Notebook. Now
imagine that your laptop lacks computing power, but you 
need to train a huge model. This is where **Google Colab**
comes in handy. This is an online service provided by 
Google. With Colab, you can write and execute programs,
save and share your results, and have access to powerful
computing resources in your browser. In this topic, we will
show the main advantages and disadvantages of the 
service and describe how to work with it.

#### 1. Google Colab vs. Jupyter Notebook
Before we turn to Google Colab, let's have a closer look at 
the main features of Google Colab and Jupyter Notebook.

| Syntax      | Description |
| ----------- | ----------- |
| Initiate online sessions to work with your team. | Doesn't allow instant team work. A researcher has to wait until another one finishes his part of the code and sends it for further editing.|
| Use Google computer power | Use the power of your computer only. |
| Most of the ML libraries are on-board. | You need to install the libraries on your machine first. | 
| Every line of code can be saved on Google Drive. | Sometimes, it is hard to get through various notebooks in different local folders. | 

Google Colab has some minor cons, too, as it cannot be
run offline. You can also lose your code if you close the 
environment without downloading the results.
Nevertheless, we see that it still has a lot of benefits over
Jupyter Notebook.

#### 2. First steps
Here we go! This is how we can write our first program in
Google Colab:

1. Sign in to your Google account.
2. Go to [Google Colab](https://colab.research.google.com/).
3. If you are a new user, you are going to see the 
   following page:
    ![](https://ucarecdn.com/f2d70213-9e1a-4b5b-a4f3-3a6a3e01f82e/)
4. You can skip this page and proceed to create your 
   own **Colab notebook**. To do it, press the *File* button
   in the upper-left corner and choose *New Notebook*.
5. If you have already visited Google Colab, you can
   choose one of the existing notebooks from the list.
   Have a look at the example below.
6. Choose the *New Notebook* button at the bottom of
   the page.
7. Hooray! You have created a new notebook!

#### 3. Interface
Let's have a look at the interface of your environment. As
you can see, it resembles the interface of Jupyter 
Notebook.

![](https://ucarecdn.com/5708a4ab-d3eb-4cab-bbd8-d95261e33311/)

1. At the top of the page, you can see the name of your 
   notebook. By default, it has the *"UntitledXX.ipynb"*
   name where *"XX"* is a number of your notebook.
2. The *File* button allows you to do the main
3. The *Connect* button connects you to Google servers.
   Once connected, you can start working with your 
   code.
4. The highlighted buttons at the top allow you to
   modify a cell - move it up or down, comment, or 
   delete it.
5. The *Play* button allows you to run your code. An
   error message will appear on the screen under the 
   cell in case something is wrong.
6. The *+ Code* and *+ Text* buttons can add one more 
   cell, a piece of code, or any text information. You
   can also do it pressing the buttons that can be 
   found near the *Connect* button.
7. The *Folder* button provides access to files that are
   used by the notebook.

![](https://ucarecdn.com/6e2d20e7-0de9-4ba6-9260-b3f589565112/)

By default, there are no files, but one folder. By pressing 
the button that is highlighted in the picture above, you
can upload your own datasets for further processing.

Now let's describe code examples in Colab.

#### 4. Programs in Colab
In this section, we will discuss several programs and 
show some features of Colab.

1. **The simplest example**. First of all, let's analyze an
   easy example. Imagine, we want to count the 
   average number of likes for three posts. You can see
   how similar it is to Jupyter Notebook.

    ![](https://ucarecdn.com/1e1f6b16-f9a4-4b31-8f2b-dcf31280acef/)

    We have created two cells. In the first one, we have
    defined three variables, in the second one we have
    calculated the average number of likes. After that,
    we can run each cell in the given order and get the 
    results shown in the picture above.
2. **Uploading a file**. Let's imagine we need to process a 
   text file named *names.txt*. We have put down the 
   names of our friends and relatives, one per line. We
   want to print their names, and we need to upload
   the file in advance for that. You can do it in two 
   different ways:
        1. Use the buttons described in the previous
           section.
        2. Use the following snippet.
            
            from google.colab import files
            uploaded = files.upload()

After that, you will see a button for uploading 
a file. You can press it and choose the file you
need.
        
![](https://ucarecdn.com/f31b03c0-d6ea-482d-a1ec-7f333e50c035/)

And then open it.

![](https://ucarecdn.com/54110b02-598c-48d6-a0e0-86f791777fe0/)

Now, we can carry out other operations and print all
the names.

3. **Downloading a file**. Sometimes you need to 
   download a file with data. Imagine, you have a CSV
   file with information on passengers. There are two
   ways to download it.

        1. *Press the folder* button on the left side,
           choose your file, press the button with three
           dots, and download your file.
        
        ![](https://ucarecdn.com/e3d8ed20-8815-43df-9232-2c158e78345f/)
        
        2. Use the following snippet to download the file.
        
            from google.colab import files
            files.download("passengers_flight_a3412.csv")


#### 5. Working with libraries
Libraries are vital for every Python developer. Google
Colab allows us to use various external libraries. Suppose,
we are going to work with a pre-installed library. Let's use
NumPy for this purpose.

![](https://ucarecdn.com/c936b4c8-c3aa-4cb8-881c-d2edc9a0f06d/)

The first cell is used for importing NumPy, the second
one allows us to create an array from the list. Of course,
NumPy is not the only installed library. You can import
other libraries like NTLK, Keras, Scipy, TensorFlow, etc.
The installed libraries can be displayed by inputting `pip`
`list`.

![](https://ucarecdn.com/535820dd-a0b6-4791-bcac-7fcaa7a34660/)

Use the following `pip` command to install a library:

    pip install ...

Let's try to install the `pymorphy2` library that is used for
morphological analysis of Russian words.

![](https://ucarecdn.com/f358f6dd-1691-418a-8595-2471dcc547be/)

The library is installed successfully. You can use if for
your own experiments. Unfortunately, the libraries you
install cannot be saved, so you have to install them on
your virtual machine eah time you start a new session in
Colab.

#### 6. Summary
So, let's summarize what we learned about Google Colab:
- You can run it in the cloud;
- You can work in Google Colab with your team;
- Most of the libraries for machine learning are
  already installed, so you can easily import them;
- You can upload your files to work with them in the 
  environment and download them afterward.

Of course, it is just the beginning. [Welcome to
Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb) page contains more information about this 
environment. But for now, let's work on solving some
practical tasks.
