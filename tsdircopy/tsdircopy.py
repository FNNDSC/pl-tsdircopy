#!/usr/bin/env python                                            
#
# tsdircopy ts ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp


Gstr_title = """
 _           _ _                           
| |         | (_)                          
| |_ ___  __| |_ _ __ ___ ___  _ __  _   _ 
| __/ __|/ _` | | '__/ __/ _ \| '_ \| | | |
| |_\__ \ (_| | | | | (_| (_) | |_) | |_| |
 \__|___/\__,_|_|_|  \___\___/| .__/ \__, |
                              | |     __/ |
                              |_|    |___/ 
"""

Gstr_synopsis = """

    NAME

       tsdircopy.py 

    SYNOPSIS

        python tsdircopy.py                                        
            [-h] [--help]                                               
            [--json]                                                   
            [--man]                                                   
            [--meta]                                                    
            [--savejson <DIR>]                                        
            [-v <level>] [--verbosity <level>]                         
            [--version]                                                
            <outputDir> 
            --dir <DIR>
            [--plugininstances <instances>]                            
            [-f <filter>] [--filter <filter>]                          

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u) -v $(pwd)/out:/outgoing \
                fnndsc/pl-tsdircopy tsdircopy /outgoing    

    DESCRIPTION

        `tsdircopy.py` is a ts app to efficiently copy one or more obj storage 
        directories.

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
        
        <outputDir> 
        Output directory.
        
        --dir <DIR> 
        Required, it's a string representing a comma-separated list of one or more 
        directories.
        
        [--plugininstances <instances>] 
        If specified, it's a string representing a comma-separated list of plugin 
        instance ids.
        
        [-f <filter>] [--filter <filter>]
        If specified, it's a string representing a comma-separated list of regular 
        expressions.
"""


class TsDirCopy(ChrisApp):
    """
    Copy the *contents* of one or more obj storage directories given by the --dir
    argument to a new directory specified by <options.outpudir>. This argument is a
    string containing one or more directories separated by comma.
    """
    PACKAGE                 = __package__
    TITLE                   = 'A ChRIS ts app to efficiently copy one or more obj storage directories'
    CATEGORY                = 'utility'
    TYPE                    = 'ts'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--dir',
                          dest='dir',
                          type=ChrisApp.unextpath,
                          optional=False,
                          help='directories to be copied')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        print('Dir: %s' % options.dir)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
