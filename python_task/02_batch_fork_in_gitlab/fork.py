##
# This script is used for batch forking all projects under source groups to the target group
# To configure .env file before run this script
#
# Usage: $ python3 ./fork.py
#
import time 
# pip3 install python-gitlab==1.4
import gitlab
import random
import json
# Note: for debug
# import dump_tool
import os
# pip3 install python-dotenv
from dotenv import load_dotenv

load_dotenv()

groups = json.loads(os.getenv('groups'))
target_namespace = os.getenv('target_namespace')
target_namespace_id = os.getenv('target_namespace_id')
private_token = os.getenv('private_token')
gitlab_url = os.getenv('gitlab_url')

# Note: change gitlab web url here
gl = gitlab.Gitlab(gitlab_url,
                   private_token=private_token,
                   ssl_verify=True,
                   api_version='3')

if os.getenv('debug_mode') == 'true':
    gl.enable_debug()

for group in groups:
    projects = gl.groups.get(group).projects
    # dump_tool.dump_object(projects)

    successCount = 0
    failureCount = 0
    page = 1
    while page > 0:
        print(f"lookuping for page {page}")
        list = projects.list(all=False, page=page, per_page=20)
        if len(list) == 0:
            page = -1
        else:
            page += 1

        for proj in list:
            wait_time = random.randint(2, 5)
            print(f"sleeping {wait_time} seconds")
            time.sleep(wait_time)

            print(f"Forking {proj.name}")
            try:
                # Note: 某些gitlab网站，不接收namespace参数，这里改成namespace_id参数
                # Search ProjectFork in /usr/local/lib/python3.11/site-packages/gitlab, and change optionalCreateAttrs = ['namespace'] => optionalCreateAttrs = ['namespace_id']
                print(f"target_namespace: {target_namespace}, target_namespace_id: {target_namespace_id}")
                fork = proj.forks.create({'namespace': target_namespace, 'namespace_id': target_namespace_id})

                print(f"Forked to {fork.namespace['name']}/{fork.name}")
                successCount = successCount + 1
            except:
                print(f"Failed to fork {proj.name} to {target_namespace}")
                failureCount = failureCount + 1

    print(f"finish forking for group {group}, success: {successCount}, failure: {failureCount}")

print("All done!")
