import sys
import subprocess

from workflow import Workflow, ICON_WEB, web
from workflow.notify import notify

def main(wf):

	#fetch argument from Alfred
	if len(wf.args) > 0:
		branchData = wf.args[0]
		branchData = branchData.split(" ")
		branchName = branchData[0]
		repoPath = branchData[1]

		branchProcess = subprocess.check_output(["git", "checkout", branchName], cwd=repoPath)
		notify('Git Branch Checked Out',"Checked out branch {}".format(branchName))
		wf.send_feedback()

if __name__ == u"__main__":
	wf = Workflow()
	sys.exit(wf.run(main))