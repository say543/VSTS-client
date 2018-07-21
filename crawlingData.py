
import requests
from vsts.git.v4_1.models.git_query_commits_criteria import GitQueryCommitsCriteria
from vsts.vss_connection import VssConnection
from msrest.authentication import BasicAuthentication
import pprint

# https://docs.microsoft.com/en-us/vsts/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts

# https://github.com/Microsoft/vsts-python-api
# https://github.com/Microsoft/vsts-python-samples


# qqccxbr43abamk3zykmcvufwx2je7zfllhfs6cgt7q75bj6ma6fa

if __name__ == "__main__":
    #response = requests.post('https://msasg.visualstudio.com/Cortana/_apis/git/repositories/CoreScience/commitsbatch?api-version=4.1',  data = {}, headers={'Authorization': 'qqccxbr43abamk3zykmcvufwx2je7zfllhfs6cgt7q75bj6ma6fa'})
    #print (response)


    team_instance = 'https://msasg.visualstudio.com/'
    credentials = BasicAuthentication('', 'qqccxbr43abamk3zykmcvufwx2je7zfllhfs6cgt7q75bj6ma6fa')
    connection = VssConnection(base_url=team_instance, creds=credentials)
    core_client = connection.get_client('vsts.core.v4_0.core_client.CoreClient')


    git_client = connection.get_client("vsts.git.v4_1.git_client.GitClient")

    # https://docs.microsoft.com/en-us/rest/api/vsts/git/commits/get%20commits%20batch?view=vsts-rest-4.1#gitquerycommitscriteria
    search_criteria = GitQueryCommitsCriteria()
    # git_client
    # def get_commits_batch(self, search_criteria, repository_id, project=None, skip=None, top=None, include_statuses=None):
    # https://github.com/Microsoft/vsts-python-api/blob/40d4f5803a3f0552e628b8ac3e7f7c99d1953f01/vsts/vsts/git/v4_1/models/git_query_commits_criteria.py
    result = git_client.get_commits_batch(project='Cortana',search_criteria =search_criteria, repository_id='CoreScience')

    print (len(result))
    for gitcommitRef in result:
        #print(type(gitcommitRef))


        # for all conetent
        print (gitcommitRef.__dict__)

        #print(gitcommitRef.commit_id)
        #commit_id = gitcommitRef.commit_id
        #change = git_client.get_changes(commit_id, project='Cortana', repository_id='CoreScience')
        #print (change.newContent.content)

        #gitcommitRef
        #pprint.pprint(gitcommitRef.changeCounts.newContent.content)
        #pprint.pprint(gitcommitRef.changeCounts.newContent.content)

        #changes = gitcommitRef.changes
        #for change in changes:    
        #    pprint.pprint(change.newContent.content)
        #pprint.pprint(gitcommitRef.author)

    #print(result)

    '''
    team_projects = core_client.get_projects()


    for project in team_projects:
        pprint.pprint(project.__dict__)
    '''


    # https://github.com/Microsoft/vsts-python-samples/blob/master/src/samples/git.py

    #core_client
