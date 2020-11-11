import sys
import os
import subprocess

from workflow import Workflow, ICON_WEB, web
from os.path import expanduser

def main(wf):

	#fetch argument from Alfred
	if len(wf.args) > 0:
		query = wf.args[0]
	else:
		query = "Foobar" 

	params = (wf.args[0].split(" "))
	repoPath = params[0]
	filterStr = ''
	if len(params) > 1:
		filterStr = params[1]
		if repoPath[0] != '/':
			repoPath = '{}/{}'.format(expanduser('~'), repoPath)

		branchProcess = subprocess.check_output(["git", "fetch"], cwd=repoPath)
		branchProcess = subprocess.check_output(["git", "branch"], cwd=repoPath)
		branchProcess = branchProcess.decode("utf-8")
		branches = branchProcess.split('\n')
		for branch in branches:
			if len(branch) > 0 and (filterStr.lower() in branch.lower()):
				branchName = branch.split(' ')[-1]
				wf.add_item(title= branchName,
				subtitle= 'Switch to {}'.format(branchName),
				icon="icon.png",
				valid=True,
				arg="{} {}".format(branchName, repoPath)
				)

		# Send the results to Alfred as XML
		wf.send_feedback()


if __name__ == u"__main__":
	wf = Workflow()
	sys.exit(wf.run(main))