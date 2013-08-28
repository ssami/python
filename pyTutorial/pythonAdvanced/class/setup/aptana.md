Aptana Studio
=============

Aptana Studio is an IDE - integrated development environment - based on Eclipse.  It provides powerful tools for exploring, understanding, and refactoring your code.

Aptana's Python support was formerly a separate Eclipse plugin called *PyDev*.  PyDev was purchased by Aptana and folded into Aptana Studio. Aptana can be installed as a seperate download, or as an Eclipse plugin.  For convenience we will download the whole application.

* see: [Download Aptana](http://aptana.com/products/studio3/download)



Workspace
---------
When it starts up, Aptana will ask you what folder you want to use as a workspace. I don't like workspaces and tend to ignore it. A good default is `~/workspace`.



Installing Eclipse Plugins
--------------------------
Each Eclipse plugin has an *Update Site* URL, from which it can be installed.

To install a plugin in Eclipse, choose `Install New Software...` from the `Help` menu.  Click the `Add...` button to add a new plugin repository.  Put the plugin's *Update Site* URL in the `Location:` field.

Once you have added the plugin repository, check the box of the plugin you want to install.  Click `Next >`, then click thru until it is installed.  Normally Eclipse will want to restart itself after a new plugin has been installed.



Python Perspective
------------------

Eclipse refers to collections of windows (*views* in Eclipse terminology) and their arrangement on screen as a *perspective*.  There is a Python perspective available, pre-configured with the views one typically wants while working on Python code.

You can select the Python perspective by going to the *perspective menu* - it is in the upper right corner of the window, and looks like a grid with a plus sign. Click on it, select "Other...", and choose "PyDev Perspective" from the ensuing dialog.

You will now be in the Python perspective.


   
Working with Virtual Environments
---------------------------------
Unfortunately, Aptana is not aware of virtual environments by default.  This can be worked around by manually configuring Aptana to use the Python interpreter from the virtual environment.  We will configure the interpreter in the course of starting a new project below.



Starting a New Project
----------------------
Start a new project by clicking on the new project menu - it looks like a window with a plus sign - in the upper left corner of the window.  Click on the new project menu, and select "PyDev Project".

A new project dialog will appear.  Fill in the name you want for your project, then click on the blue "Please configure an interpreter" link.  

You will be taken to Eclipse's Python interpreter settings page.  

Click the "New..." button.  A select file dialog will open; go to your home folder.  Once there, right-click on the file list, and choose "Show Hidden Files" from the context menu.

Click thru to select the `python` executable at `~/.virtualenvs/class/bin/python`.

Click OK, and you will return to the Select Interpreter dialog.

Click "OK", and you will return to the PyDev Project dialog.  From the "Interpreter" popup menu, choose "class", the virtualenv we just configured.

Click "Finish" and you will have successfully created a new project! Your new project will now be visible in the Project Explorer view.
