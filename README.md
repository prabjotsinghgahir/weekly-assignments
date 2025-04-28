# Assignment1
This repository contains assignments based on AWS and Python.

Below is a short description of different files:
1. .github/workflows/workflow.yaml => This is a github workflow file. This file runs when a push is happened on dev branch or pull request on main branch.
2. deploy_scripts/stack_deploy.py => This file creates a cloudformation stack using templates/copy-object-stack.yaml file. If the stack is already present then it will update the stack(if any updates are there to perform).
3. templates/copy-object-stack.yaml => Cloudformation Template file.
4. main.py => This file contains cloudformation template parameter values and other variables. This file will call stack_deploy.py for creating or updating the stack.
5. upload.sh => This file zips the lambda function code and upload it in code bucket.
6. lambdas/copy_function.py => This is lambda function code. This copies a file from landing S3 bucket and paste it to destination bucket.
