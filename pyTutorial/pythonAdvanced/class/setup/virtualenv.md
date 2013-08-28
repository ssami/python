Virtual Environments
====================
A virtual environment is a local Python environment isolated from the system-wide environment. They are often used to prevent package dependency conflicts.



virtualenv
----------
The term **virtualenv** can refer to the command `virtualenv`, used to create a virtual environment, or to the virutal environment itself.



virtualenvwrapper
-----------------
`virtualenvwrapper` is a set of extensions to the `virtualenv` tool. The extensions include wrappers for creating and deleting virtual environments and otherwise managing your development workflow, making it easier to work on more than one project at a time without introducing conflicts in their dependencies.

* see: [virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper)
* see: [virtualenvwrapper for windows](https://github.com/davidmarble/virtualenvwrapper-win)


    mkvirtualenv class
    New python executable in class/bin/python
    Installing distribute.............................................................................................................................................................................................done.
    Installing pip...............done.
    virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/class/bin/predeactivate
    virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/class/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/class/bin/preactivate
    virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/class/bin/postactivate
    virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/class/bin/get_env_details
    
    # A few packages are installed by default
    pip freeze
    argparse==1.2.1
    distribute==0.6.24
    wsgiref==0.1.2
   
Note that when the virtual environment is active, its name (in this case "class") is prepended to the shell prompt:

    # Ordinary shell prompt
    $ 
    # Virtual environment "class" is active
    (class)$ 


If later you have logged out, and want to activate this virtual environment, you can use the `workon` command:

    $ workon class
    (class)$

You can deactivate the virtual environment with the `deactivate` command:

    (class)$ deactivate
    # Back to normal shell prompt
    $ 



Location of Virtualenvs
-----------------------
By default, `virtualenvwrapper` stores your virtual environments in `~/.virtualenvs` (or `%USERPROFILE%\Envs`). 

   

Virtual Environments for Scripts
--------------------------------
There are several ways you can run scripts that rely on a virtualenv:

* Use Fabric's `prefix()` `context manager` when calling the script remotely:

        def task():
            with prefix('workon class'):
                run('uptime')
                run('uname -a')

* Have whatever is calling your script (`cron` etc) call `workon` first.
* Specify your virtualenv's Python interpreter directly in the script's bangline.  
* Use a bash script as a wrapper.  Ugly, but sometimes convenient.
