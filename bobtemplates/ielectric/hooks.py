#
def delete_profile(configurator):
    if configurator.variables['genericsetup.profile']:
        # do something here
        print 'keeping'
    else:
        print 'deleting'
