# WeiToGo

WeiToGo is a repo for utilities written for weibo operations.

## delWei
delWei is a script that helps user to delete all their weibo posts. Mass Deletion made easy.

### Dependencies
selenium with a chrome browser driver executable.
See [here](https://selenium-python.readthedocs.io/) for guidance.

### Usage
1. Execute the script. 
`python delWei.py`

2. Login With Your Weibo credentials (the target account for deletion)

3. Navigate to "个人中心"

4. Type `OK` to `terminal`/`cmd`/`stdin`

5. Watch it do the magic. 

6. (Sometimes, exception are being caught due to UI syncing or pagination loading. The scripts catches exceptions and prompt user to type `OK`. After you see the page is laoded and confirm manually you can delete a post, type OK and keep going.)