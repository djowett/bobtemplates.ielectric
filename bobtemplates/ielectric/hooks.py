#
import os
import shutil

def delete_profile(configurator):
    deldir = os.path.join (configurator.target_directory, 
                           configurator.variables['package.namespace'],
                           configurator.variables['package.name'],
                           'profiles')
    if configurator.variables['genericsetup.profile']:
        print 'keeping ' + deldir
    else:
        print 'deleting ' + deldir
        shutil.rmtree(deldir)
        if os.path.exists(deldir):
            print "Couldn't remove " + deldir

