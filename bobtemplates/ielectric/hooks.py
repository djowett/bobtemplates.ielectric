#
import os
import shutil

def delete_profile_stuff(configurator):
    package_dir = os.path.join (configurator.target_directory, 
                                configurator.variables['package.namespace'],
                                configurator.variables['package.name'])
    profiles_dir = os.path.join (package_dir,
                                 'profiles')
    extensions_dir = os.path.join (package_dir,
                                   'Extensions')
                            
    delete_dirtree(configurator, profiles_dir)
    delete_dirtree(configurator, extensions_dir)

def delete_dirtree(configurator, directory):
    if configurator.variables['genericsetup.profile']:
        print 'keeping ' + directory
    else:
        print 'deleting ' + directory
        shutil.rmtree(directory)
        if os.path.exists(directory):
            print "Couldn't remove " + directory

