# Linux Fundamentals

## Philisophy

-   Everything is a file
-   Small, single-purpose programs
-   Ability to chain programs together to perform complex tasks
-   Configuration data stored in a text file
    -   `/etc/passwd` stores all users registered on the system



## Components

-   Bootloader: code, guide booting process to start OS
-   OS Kernel: main component of the OS, manages the resources for I/O devices the system  at harware level.
-   Daemons: Background services, ensure key functions work
-   OS Shell
-   X-server/Graphics server: provides a graphical sub-system(server), run locally
-   Window manager: GUI: Graphical User Interface
-   Utilities

## Linux Architecture

-   Hardware: peripheral devices (CPU, GPU...)
-   Kernel: core, control CPU, allocate memory, access data
-   Shell: Command-line Interface (CLI)
-   System Utility

## File System Hierarchy

>
-   Tree like
-   Documented in the Filesystem Hierarchy Standard (FHS)

-   / : top level directory. After boot, all of the filesystems are mounted at standard mout points as subdirectories of the boot.
-   /bin : contains essential command binaries
-   /boot : consists of static boot loader, kernel executable, other files required to boot the Linux OS
-   /dev : Contains device files to facilitate access to every hardware device attached to the system
-   /etc : Local system configuration files (also Configuration files for installed applications may be installed here as well)
-   /home : Each user on the system has a subdirectory here for storage
-   /lib : Shared library files that are required for system boot !@#
-   /media : External removable media such as USB devices are mounted here.
-   /mnt : Temporary mount point for regular filesystems
-   /opt : Optional files such as 3rd-party tools
-   /root
-   /sbin : Contains executables used for system administration (binary system files)
-   /tmp : Store temporary files, generally cleared upon system boot and may be deleted at other times without any warnings.
-   /usr : Contains executables, libraries, man files, etc.
-   /var : variable data, such as log files, email in boxes, web application realted files, cron files,...





## Shell 

`apropos`: searches the descriptions for instance of a given keyword

## User Management

`useradd`

`userdel`

`usermod`: Modifies a user account

`add group`

`delgroup`

`passwd`: Change user password

## Package Management 

-   pkg downloading 
-   dependency resolution 
-   Std binary pkg format
-   Common installation and configutation locations
-   Additional system-related configuration and functionality 
-   Quality control 

### Manager

`dpkg` install, build,   remove, manage Debian packages

`apt` Advance Package Manager

`aptitude` Alternative to `apt`

`snap` install, configure, refresh, remove `snap` packages

`gem` pkg manager for Ruby 

`pip` pkg manager for Python 

`git`



## Execute multiple Comands

3 method.

-   semicolon (`;`) : ignoring previous  commands' results and errors
-   Double `ampersand` characters (`&&`) : Previous error, the next will stop
-   Pipes (`|`) : depend on previous correct, also previous processes' results





