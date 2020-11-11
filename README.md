# alfred-gitBranches

Easy git branch switching workflow for Alfred

## Usage
#### To switch to a different branch:

1. Start the gitBranches workflow using the keyword `gb`  
2. Enter the path to your local repository  (or a repository bookmark - see below) followed by a search string
Example:
`gb /path/to/repo searchString`
	1. gitBranches will stash your local changes on your current branch (you can easily get them back with `git stash pop`
	2. gitBranches will fetch any new remote branch names and list all available branches for your repository. As you type your search string this will filter down to only branch names which match your search string (case insensitive)
	3. When you select a branch, git will checkout the selected branch in your repo. No terminal, or GUI required :) 

#### To bookmark a repository: 

1. Start the gitBranches bookmark workflow using the keyword `gbookmark`
2. Enter the path to the local repository you want to bookmark, followed by the bookmark name you want to use. **Note** bookmark names may not contain spaces.
Example:
`gbookmark /path/to/repo bookmarkName`
3. Press enter and the bookmark will be saved. You can now avoid typing lengthy paths when switching branches and use your bookmark name instead.
Example:
`gb bookmarkName searchString`

Icons made by [Freepik](https://www.flaticon.com/authors/freepik) from [Flaticon](https://www.flaticon.com)
