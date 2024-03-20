#################################################################################################################
#
# This is the top level makefile, which is intended to be able to process a common set of rules on all 
# sub-projects underneath this directory.  Currently, the common/standardized set of rules are as follows
# and supported by .make.defaults 
#
# setup: 
# clean: 
# build:
# test:
#
# When finally getting to a makefile that requires a rule implementation, for example to test the build,
# that makefile should override/implement the rule to meet its needs.  Such a rule may continue to recurse
# using "$(MAKE) <rule>-recurse", for example "$(MAKE) test-recurse". 
#
# Each rule is called recursively on sub-directories and if a similar inclusion is done in the sub-Makefiles,
# the rules will be applied/executed recursively in their sub-directories.
#
#################################################################################################################

# Get some common rules for the whole repo
include .make.defaults

########## ########## ########## ########## ########## ########## ########## ########## 
# Global rules that are generally to be implemented in the sub-directories and can
# be overridden there (the double colon on the rule makes the overridable). 

setup:: 
	@# Help: Recursively setup in all subdirs 
	$(MAKE) RULE=setup .recurse

clean:: 
	@# Help: Recursively clean in all subdirs 
	$(MAKE) RULE=clean .recurse

setup::
	@# Help: setup, Recursively test in all subdirs
	@$(MAKE) RULE=setup .recurse

build:: 
	@# Help: Recursively build in all subdirs 
	$(MAKE) RULE=build .recurse

test::  
	@# Help: Recursively test in in all subdirs 
	@$(MAKE) RULE=test .recurse


