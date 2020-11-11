import sys
import argparse
import os
import subprocess

from workflow import Workflow, ICON_WEB, web
from workflow.notify import notify
from os.path import expanduser

def main(wf):

	# parse the python script's arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('--bookmark', dest='bookmark', nargs='?', default=None)
	parser.add_argument('query', nargs='?', default=None)
	args = parser.parse_args(wf.args)
	
	if args.bookmark:
		#Format /path/to/repo bookmarkName
		params = args.bookmark.split(" ")
		bookmarkName = params[-1]
		path = "".join(params[:-1])
		wf.settings[bookmarkName] = path
		notify('Git Branches Bookmark Saved','Bookmarked {} as {}'.format(path, bookmarkName))
		return 0
	
	query = args.query	

	params = (query.split(" "))
	repoPath = params[0]

	# Can supply a bookmark name instead of a path
	# (Bookmark must already be saved in settings)
	if wf.settings[repoPath]:
		repoPath = wf.settings[repoPath]

	filterStr = ''
	if len(params) > 1:
		filterStr = params[1]
		if repoPath[0] != '/':
			repoPath = '{}/{}'.format(expanduser('~'), repoPath)

		branchProcess = subprocess.check_output(["git", "stash"], cwd=repoPath)
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